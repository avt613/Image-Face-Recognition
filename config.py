from cs50 import SQL
db = SQL('sqlite:///data/faces.db')

search = 'static/All/'
extentions = ['JPG', 'jpg', 'JPEG', 'jpeg', 'BMP', 'bmp', 'PNG', 'png']
tofinddir = 'static/pics/'
unknowndir = 'static/assets/img/'

datadir = 'data/'
knowndir = datadir + 'known/'
known_face_encodings_loc = datadir + 'known_face_encodings.txt'
known_face_names_loc = datadir + 'known_face_names.txt'
