import face_recognition
import os
knowndir = 'known/'
saveddir = 'known/learnt/'
# This is an example of running face recognition on a single image
# and drawing a box around each person that was identified.
known_face_encodings = []
known_face_names = []
folder = os.listdir(knowndir)
for image in folder:
    # Load a sample picture and learn how to recognize it.
    # Only load if it is a file
    if os.path.isdir(knowndir + image) == False:
        print(image)
        face_image = face_recognition.load_image_file(knowndir + image)
        face_face_encoding = face_recognition.face_encodings(face_image)[0]
        # Create arrays of known face encodings and their names
        known_face_encodings.append(face_face_encoding)
        name = os.path.splitext(image)[0]
        known_face_names.append(name)
        os.rename(knowndir + image, saveddir + image)
print('Learned encoding for', len(known_face_encodings), 'images.')

from db import *
dbadd(known_face_encodings, known_face_names)
