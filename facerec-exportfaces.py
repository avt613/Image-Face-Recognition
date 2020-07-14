import face_recognition
from PIL import Image
import os
# Place to take images from
tododir = 'exportfaces/todo/'
# Place to save all the cut out faces
donedir = 'exportfaces/done/'
folder = os.listdir(tododir)
for image in folder:
    # Only load if it is a file
    if os.path.isdir(tododir + image) == False:
        print(tododir + image)
        imagename = os.path.splitext(image)[0]
        facenum = 0
 
        # Load an image with an unknown face
        unknown_image = face_recognition.load_image_file(tododir + image)

        # Find all the faces and face encodings in the unknown image
        face_locations = face_recognition.face_locations(unknown_image)
        face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

        # Loop through each face found in the unknown image
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            faces = Image.open(tododir + image)
            face = faces.crop(((left*.9), (top*.9), (right*1.1), (bottom*1.1)))
            face.save( '{0}{1}-{2}.JPG'.format(donedir, imagename, facenum))
            face.close()
            facenum += 1
