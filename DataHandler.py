import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('/home/admin1/Documents/personal-assistant-e59c7-2ad21b6afa8b.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

def getAllTasks():
    users_ref = db.collection('Tasks')
    docs = users_ref.stream()
    for doc in docs:
        print(f'{doc.id} => {doc.to_dict()}')


getAllTasks();
