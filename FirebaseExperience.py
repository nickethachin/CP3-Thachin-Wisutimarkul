import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('cp3-thachin-w-firebase-adminsdk-k96d8-8b53fc6ae8.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://cp3-thachin-w.firebaseio.com/'
})


def PrintDict(data, tab = False, space = 0):
    tabs = ""
    if tab == True:
        tabs = " "*int(3*space)
    for i in data:
        if type(data[i]) is dict:
            print("%s%s" % (tabs, i))
            PrintDict(data[i], True, space+1)
        else:
            print("%s%s : %s" % (tabs, i, data[i]))


ref = db.reference('')
data = ref.get()
PrintDict(data)

'''users_ref = ref.child('Users')
users_ref.push({
    'Alan': {
        'age': '23',
        'email': 'alanisawesome@gmail.com',
        'tel': '123456'
    },
    'Grace': {
        'age': '21',
        'email': 'gracehop@gmail.com',
        'tel': '654321'
    }
})'''
