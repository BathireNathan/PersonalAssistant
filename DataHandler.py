import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('/home/bathirenathan/Downloads/personal-assistant-e59c7-0b71f1cea1d2.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

def getAllTasks():
    users_ref = db.collection('Tasks')
    docs = users_ref.stream()
    for doc in docs:
        print(f'{doc.id} => {doc.to_dict()}')

def updatePackage():
    config = db.collection("Configurations").document("PackageToNameMap")
    doc = config.get()
    if doc.exists:
        pack_to_name = doc.to_dict()
        print(f'Document data: {pack_to_name}')
        for key, value in pack_to_name.items():
            print(f'{key}  && {value}')
            update_notification(key, value)


def update_notification(key, value):
    print(key)
    notif = db.collection("Notifications").where('packageName', '==', key).stream()
    for doc in notif:
        print(f'{doc.id} =>')
        db.collection("Notifications").document(doc.id).set({u'packageName': value}, merge=True)


updatePackage();
