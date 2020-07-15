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
    dbsetup()
    for i in range(len(known_face_encodings)):
        db.execute("INSERT INTO encoding (name, '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127') VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", known_face_names[i],\
            known_face_encodings[i][0].item(),\
            known_face_encodings[i][1].item(),\
            known_face_encodings[i][2].item(),\
            known_face_encodings[i][3].item(),\
            known_face_encodings[i][4].item(),\
            known_face_encodings[i][5].item(),\
            known_face_encodings[i][6].item(),\
            known_face_encodings[i][7].item(),\
            known_face_encodings[i][8].item(),\
            known_face_encodings[i][9].item(),\
            known_face_encodings[i][10].item(),\
            known_face_encodings[i][11].item(),\
            known_face_encodings[i][12].item(),\
            known_face_encodings[i][13].item(),\
            known_face_encodings[i][14].item(),\
            known_face_encodings[i][15].item(),\
            known_face_encodings[i][16].item(),\
            known_face_encodings[i][17].item(),\
            known_face_encodings[i][18].item(),\
            known_face_encodings[i][19].item(),\
            known_face_encodings[i][20].item(),\
            known_face_encodings[i][21].item(),\
            known_face_encodings[i][22].item(),\
            known_face_encodings[i][23].item(),\
            known_face_encodings[i][24].item(),\
            known_face_encodings[i][25].item(),\
            known_face_encodings[i][26].item(),\
            known_face_encodings[i][27].item(),\
            known_face_encodings[i][28].item(),\
            known_face_encodings[i][29].item(),\
            known_face_encodings[i][30].item(),\
            known_face_encodings[i][31].item(),\
            known_face_encodings[i][32].item(),\
            known_face_encodings[i][33].item(),\
            known_face_encodings[i][34].item(),\
            known_face_encodings[i][35].item(),\
            known_face_encodings[i][36].item(),\
            known_face_encodings[i][37].item(),\
            known_face_encodings[i][38].item(),\
            known_face_encodings[i][39].item(),\
            known_face_encodings[i][40].item(),\
            known_face_encodings[i][41].item(),\
            known_face_encodings[i][42].item(),\
            known_face_encodings[i][43].item(),\
            known_face_encodings[i][44].item(),\
            known_face_encodings[i][45].item(),\
            known_face_encodings[i][46].item(),\
            known_face_encodings[i][47].item(),\
            known_face_encodings[i][48].item(),\
            known_face_encodings[i][49].item(),\
            known_face_encodings[i][50].item(),\
            known_face_encodings[i][51].item(),\
            known_face_encodings[i][52].item(),\
            known_face_encodings[i][53].item(),\
            known_face_encodings[i][54].item(),\
            known_face_encodings[i][55].item(),\
            known_face_encodings[i][56].item(),\
            known_face_encodings[i][57].item(),\
            known_face_encodings[i][58].item(),\
            known_face_encodings[i][59].item(),\
            known_face_encodings[i][60].item(),\
            known_face_encodings[i][61].item(),\
            known_face_encodings[i][62].item(),\
            known_face_encodings[i][63].item(),\
            known_face_encodings[i][64].item(),\
            known_face_encodings[i][65].item(),\
            known_face_encodings[i][66].item(),\
            known_face_encodings[i][67].item(),\
            known_face_encodings[i][68].item(),\
            known_face_encodings[i][69].item(),\
            known_face_encodings[i][70].item(),\
            known_face_encodings[i][71].item(),\
            known_face_encodings[i][72].item(),\
            known_face_encodings[i][73].item(),\
            known_face_encodings[i][74].item(),\
            known_face_encodings[i][75].item(),\
            known_face_encodings[i][76].item(),\
            known_face_encodings[i][77].item(),\
            known_face_encodings[i][78].item(),\
            known_face_encodings[i][79].item(),\
            known_face_encodings[i][80].item(),\
            known_face_encodings[i][81].item(),\
            known_face_encodings[i][82].item(),\
            known_face_encodings[i][83].item(),\
            known_face_encodings[i][84].item(),\
            known_face_encodings[i][85].item(),\
            known_face_encodings[i][86].item(),\
            known_face_encodings[i][87].item(),\
            known_face_encodings[i][88].item(),\
            known_face_encodings[i][89].item(),\
            known_face_encodings[i][90].item(),\
            known_face_encodings[i][91].item(),\
            known_face_encodings[i][92].item(),\
            known_face_encodings[i][93].item(),\
            known_face_encodings[i][94].item(),\
            known_face_encodings[i][95].item(),\
            known_face_encodings[i][96].item(),\
            known_face_encodings[i][97].item(),\
            known_face_encodings[i][98].item(),\
            known_face_encodings[i][99].item(),\
            known_face_encodings[i][100].item(),\
            known_face_encodings[i][101].item(),\
            known_face_encodings[i][102].item(),\
            known_face_encodings[i][103].item(),\
            known_face_encodings[i][104].item(),\
            known_face_encodings[i][105].item(),\
            known_face_encodings[i][106].item(),\
            known_face_encodings[i][107].item(),\
            known_face_encodings[i][108].item(),\
            known_face_encodings[i][109].item(),\
            known_face_encodings[i][110].item(),\
            known_face_encodings[i][111].item(),\
            known_face_encodings[i][112].item(),\
            known_face_encodings[i][113].item(),\
            known_face_encodings[i][114].item(),\
            known_face_encodings[i][115].item(),\
            known_face_encodings[i][116].item(),\
            known_face_encodings[i][117].item(),\
            known_face_encodings[i][118].item(),\
            known_face_encodings[i][119].item(),\
            known_face_encodings[i][120].item(),\
            known_face_encodings[i][121].item(),\
            known_face_encodings[i][122].item(),\
            known_face_encodings[i][123].item(),\
            known_face_encodings[i][124].item(),\
            known_face_encodings[i][125].item(),\
            known_face_encodings[i][126].item(),\
            known_face_encodings[i][127].item())
    
def dbget():
    saved_encodings = []
    saved_names = []
    query = db.execute("SELECT * FROM encoding ORDER BY id DESC")
    for i in range(len(query)):
        saved_names.append(query[i]['name'])
        saved_encodings.append([])
        saved_encodings[i].append(query[i]['0'])
        saved_encodings[i].append(query[i]['1'])
        saved_encodings[i].append(query[i]['2'])
        saved_encodings[i].append(query[i]['3'])
        saved_encodings[i].append(query[i]['4'])
        saved_encodings[i].append(query[i]['5'])
        saved_encodings[i].append(query[i]['6'])
        saved_encodings[i].append(query[i]['7'])
        saved_encodings[i].append(query[i]['8'])
        saved_encodings[i].append(query[i]['9'])
        saved_encodings[i].append(query[i]['10'])
        saved_encodings[i].append(query[i]['11'])
        saved_encodings[i].append(query[i]['12'])
        saved_encodings[i].append(query[i]['13'])
        saved_encodings[i].append(query[i]['14'])
        saved_encodings[i].append(query[i]['15'])
        saved_encodings[i].append(query[i]['16'])
        saved_encodings[i].append(query[i]['17'])
        saved_encodings[i].append(query[i]['18'])
        saved_encodings[i].append(query[i]['19'])
        saved_encodings[i].append(query[i]['20'])
        saved_encodings[i].append(query[i]['21'])
        saved_encodings[i].append(query[i]['22'])
        saved_encodings[i].append(query[i]['23'])
        saved_encodings[i].append(query[i]['24'])
        saved_encodings[i].append(query[i]['25'])
        saved_encodings[i].append(query[i]['26'])
        saved_encodings[i].append(query[i]['27'])
        saved_encodings[i].append(query[i]['28'])
        saved_encodings[i].append(query[i]['29'])
        saved_encodings[i].append(query[i]['30'])
        saved_encodings[i].append(query[i]['31'])
        saved_encodings[i].append(query[i]['32'])
        saved_encodings[i].append(query[i]['33'])
        saved_encodings[i].append(query[i]['34'])
        saved_encodings[i].append(query[i]['35'])
        saved_encodings[i].append(query[i]['36'])
        saved_encodings[i].append(query[i]['37'])
        saved_encodings[i].append(query[i]['38'])
        saved_encodings[i].append(query[i]['39'])
        saved_encodings[i].append(query[i]['40'])
        saved_encodings[i].append(query[i]['41'])
        saved_encodings[i].append(query[i]['42'])
        saved_encodings[i].append(query[i]['43'])
        saved_encodings[i].append(query[i]['44'])
        saved_encodings[i].append(query[i]['45'])
        saved_encodings[i].append(query[i]['46'])
        saved_encodings[i].append(query[i]['47'])
        saved_encodings[i].append(query[i]['48'])
        saved_encodings[i].append(query[i]['49'])
        saved_encodings[i].append(query[i]['50'])
        saved_encodings[i].append(query[i]['51'])
        saved_encodings[i].append(query[i]['52'])
        saved_encodings[i].append(query[i]['53'])
        saved_encodings[i].append(query[i]['54'])
        saved_encodings[i].append(query[i]['55'])
        saved_encodings[i].append(query[i]['56'])
        saved_encodings[i].append(query[i]['57'])
        saved_encodings[i].append(query[i]['58'])
        saved_encodings[i].append(query[i]['59'])
        saved_encodings[i].append(query[i]['60'])
        saved_encodings[i].append(query[i]['61'])
        saved_encodings[i].append(query[i]['62'])
        saved_encodings[i].append(query[i]['63'])
        saved_encodings[i].append(query[i]['64'])
        saved_encodings[i].append(query[i]['65'])
        saved_encodings[i].append(query[i]['66'])
        saved_encodings[i].append(query[i]['67'])
        saved_encodings[i].append(query[i]['68'])
        saved_encodings[i].append(query[i]['69'])
        saved_encodings[i].append(query[i]['70'])
        saved_encodings[i].append(query[i]['71'])
        saved_encodings[i].append(query[i]['72'])
        saved_encodings[i].append(query[i]['73'])
        saved_encodings[i].append(query[i]['74'])
        saved_encodings[i].append(query[i]['75'])
        saved_encodings[i].append(query[i]['76'])
        saved_encodings[i].append(query[i]['77'])
        saved_encodings[i].append(query[i]['78'])
        saved_encodings[i].append(query[i]['79'])
        saved_encodings[i].append(query[i]['80'])
        saved_encodings[i].append(query[i]['81'])
        saved_encodings[i].append(query[i]['82'])
        saved_encodings[i].append(query[i]['83'])
        saved_encodings[i].append(query[i]['84'])
        saved_encodings[i].append(query[i]['85'])
        saved_encodings[i].append(query[i]['86'])
        saved_encodings[i].append(query[i]['87'])
        saved_encodings[i].append(query[i]['88'])
        saved_encodings[i].append(query[i]['89'])
        saved_encodings[i].append(query[i]['90'])
        saved_encodings[i].append(query[i]['91'])
        saved_encodings[i].append(query[i]['92'])
        saved_encodings[i].append(query[i]['93'])
        saved_encodings[i].append(query[i]['94'])
        saved_encodings[i].append(query[i]['95'])
        saved_encodings[i].append(query[i]['96'])
        saved_encodings[i].append(query[i]['97'])
        saved_encodings[i].append(query[i]['98'])
        saved_encodings[i].append(query[i]['99'])
        saved_encodings[i].append(query[i]['100'])
        saved_encodings[i].append(query[i]['101'])
        saved_encodings[i].append(query[i]['102'])
        saved_encodings[i].append(query[i]['103'])
        saved_encodings[i].append(query[i]['104'])
        saved_encodings[i].append(query[i]['105'])
        saved_encodings[i].append(query[i]['106'])
        saved_encodings[i].append(query[i]['107'])
        saved_encodings[i].append(query[i]['108'])
        saved_encodings[i].append(query[i]['109'])
        saved_encodings[i].append(query[i]['110'])
        saved_encodings[i].append(query[i]['111'])
        saved_encodings[i].append(query[i]['112'])
        saved_encodings[i].append(query[i]['113'])
        saved_encodings[i].append(query[i]['114'])
        saved_encodings[i].append(query[i]['115'])
        saved_encodings[i].append(query[i]['116'])
        saved_encodings[i].append(query[i]['117'])
        saved_encodings[i].append(query[i]['118'])
        saved_encodings[i].append(query[i]['119'])
        saved_encodings[i].append(query[i]['120'])
        saved_encodings[i].append(query[i]['121'])
        saved_encodings[i].append(query[i]['122'])
        saved_encodings[i].append(query[i]['123'])
        saved_encodings[i].append(query[i]['124'])
        saved_encodings[i].append(query[i]['125'])
        saved_encodings[i].append(query[i]['126'])
        saved_encodings[i].append(query[i]['127'])
    #print(saved_encodings)
    #print(saved_names)
    return saved_encodings, saved_names

