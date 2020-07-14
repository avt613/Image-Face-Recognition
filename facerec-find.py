import face_recognition
import numpy as np
import os
from PIL import Image, ImageDraw
tofinddir = 'tofind/'
unknowndir = 'known/unknown/'
imagename = "IMG_2559.JPG"
imagetoname = tofinddir + imagename
# define an empty list
known_face_encodings = []
known_face_names = []

# open file and read the content in a list
with open('known_face_encodings.txt', 'r') as filehandle:
    text = filehandle.read()
    known_face_encodings = [[float(j) for j in i.strip().strip('[').split()] for i in text.split(']')[:-1]]
with open('known_face_names.txt', 'r') as filehandle:
    for line in filehandle:
        # remove linebreak which is the last character of the string
        currentPlace = line[:-1]
        # add item to the list
        known_face_names.append(currentPlace)

folder = os.listdir(tofinddir)
for image in folder:
    imagetoname = tofinddir + image
    # Load a sample picture and learn how to recognize it.
    # Only load if it is a file
    if os.path.isdir(imagetoname) == False:
        # Load an image with an unknown face
        unknown_image = face_recognition.load_image_file(imagetoname)
        # Find all the faces and face encodings in the unknown image
        face_locations = face_recognition.face_locations(unknown_image)
        face_encodings = face_recognition.face_encodings(unknown_image, face_locations)
        # Convert the image to a PIL-format image so that we can draw on top of it with the Pillow library
        # See http://pillow.readthedocs.io/ for more about PIL/Pillow
        pil_image = Image.fromarray(unknown_image)
        faces = Image.open(imagetoname)
        # Create a Pillow ImageDraw Draw instance to draw with
        draw = ImageDraw.Draw(pil_image)
        facenum = 0
        # Loop through each face found in the unknown image
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.55)
            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            else:
                name = "Unknown"
                extrawidth = 0.2*(right - left)
                extraheight = 0.2*(bottom - top)
                face = faces.crop(((left - extrawidth), (top - extraheight), (right + extrawidth), (bottom + extraheight)))
                face.save('{0}face{1}.JPG'.format(unknowndir, facenum))
                face.close()
                facenum += 1
            # Draw a box around the face using the Pillow module
            draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

            # Draw a label with a name below the face
            text_width, text_height = draw.textsize(name)
            draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
            draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))
            print(name)
        # Display the resulting image
        #pil_image.save('{0}-named.JPG'.format(imagetoname))
        #Image.open('{0}-named.JPG'.format(imagetoname)).show()
        pil_image.show()
        input("Press Enter to continue...")
# Remove the drawing library from memory as per the Pillow docs
del draw
