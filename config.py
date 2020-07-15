search = 'static/All/'
extentions = ['JPG', 'jpg', 'JPEG', 'jpeg', 'BMP', 'bmp', 'PNG', 'png']
tofinddir = 'static/pics/'
unknowndir = 'static/assets/img/'

datadir = 'data/'
knowndir = datadir + 'known/'

# To add
# from config import *
# dbadd(known_face_encodings, known_face_names)
#
# To get
# from config import *
# res = dbget()
# known_face_encodings = res[0]
# known_face_names = res[1]

from cs50 import SQL
db = SQL('sqlite:///data/faces.db')

def dbadd(known_face_encodings, known_face_names):
    for i in range(len(known_face_encodings)):
        # Create a string of 128 numbers from 0 to 127
        # '0','1','2','3','4' ...
        queryColumns = ",".join(["'" + str(x) + "'" for x in range(128)])
        # Create a string of 129 question marks
        # ?,?,?,? ...
        queryPlaceholders = ",".join(["?" for x in range(129)])
        # Combine the query column names and the placeholders string to one single query string
        queryString = "INSERT INTO encoding (name, " + queryColumns + ") VALUES (" + queryPlaceholders + ")"
        # Now we create and fill the values tuple
        queryValues = (known_face_names[i],);
        # Loop from 0 to 127 (128 iterations in total)
        for j in range(128):
            queryValues = queryValues + (known_face_encodings[i][j].item(),)
        
        # Spread queryValues tuple and apply it to separate function arguments
        db.execute(queryString, *queryValues)

def dbget():
    saved_encodings = []
    saved_names = []
    query = db.execute("SELECT * FROM encoding ORDER BY id DESC")
    for i in range(len(query)):
        saved_names.append(query[i]['name'])
        saved_encodings.append([])
        
        # Loop from 0 to 127 (128 iterations in total)
        for j in range(128):
            saved_encodings[i].append(query[i][str(j)])
            
    #print(saved_encodings)
    #print(saved_names)
    return saved_encodings, saved_names

