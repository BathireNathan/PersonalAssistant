import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate('/home/bathirenathan/Downloads/personal-assistant-e59c7-0b71f1cea1d2.json')
firebase_admin.initialize_app(cred)
db = firestore.client()


def getUserAndSave():
    user = set()
    docs = db.collection("Notifications").stream()
    for doc in docs:
        dic_doc = doc.to_dict()
        print(f'docu :: {dic_doc}')
        user.add(dic_doc['user'])
    print(user)
    saveuser(user)

def saveuser(user):
    db.collection("UserInfo").document("users").set({u'distinctUser': list(user)}, merge=True)
