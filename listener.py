import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('/home/bathirenathan/Downloads/personal-assistant-e59c7-0b71f1cea1d2.json')
firebase_admin.initialize_app(cred)
db = firestore.client()


def manage_tasks_collection():
    move_completed_tasks()
    prepareDashboardContent()


def move_completed_tasks():
    task_comp = db.collection('Tasks').where('status', '==', 'COMP').stream()
    for doc in task_comp:
        print(f'doc :{doc.reference} and {doc.to_dict()}')
        db.collection('CompletedTasks').add(doc.to_dict())
        doc.reference.delete()


def prepareDashboardContent():
     doc_ref = db.collection("Users").get()
     for doc in doc_ref:
         print(f'user  {doc.id}')
         task_dets_dash(doc.id)

def task_dets_dash(user):
    if user == "":
        return
    save_dash_data(user, "CompletedTasks", "Completed")
    save_dash_data(user, "Tasks", "Pending")
    time = get_start_and_end()
    docs = db.collection("Tasks").where(u'user', '==', user).stream()
    # where(u'plannedCompletionTime', '>=', time[0]).where(u'plannedCompletionTime', '<=', time[1]).
    i = 0
    for doc in docs:
        doct_dict = doc.to_dict()
        if(doct_dict['plannedCompletionTime'] >= time[0] and doct_dict['plannedCompletionTime'] <= time[1]):
            i += 1
    print(i)
    db.collection(user).document('TaskDashboard').set({u"Today Planned": i}, merge=True)

def save_dash_data(user, collectionName, key):
    i = 0
    docs = db.collection(collectionName).where('user', '==', user).stream()
    for doc in docs:
        print(doc)
        i += 1
    print(i)
    db.collection(user).document('TaskDashboard').set({key: i}, merge=True)


def get_start_and_end():
    tz = pytz.timezone('Asia/Kolkata')
    today = datetime.now(tz=tz)
    print(today)
    start = today.replace(hour=0, minute=0, second=0, microsecond=0)
    end = start + timedelta(1)
    start_time = start.timestamp() * 1000
    end_time = end.timestamp() * 1000
    return start_time, end_time