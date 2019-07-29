import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account to connect to the databse
cred = credentials.Certificate('./serviceAccount.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

def get_gym(gym):
    """
    Retrieve all instances of a gym
    """
    users_ref = db.collection(u'gyms').where(u'Name', u'==', gym)
    docs = users_ref.stream()

    print("Retrieve all Golds Gyms")
    for doc in docs:
        print(u'{} => {}'.format(doc.id, doc.to_dict()))


def get_gym_by_location(gym, location):
    """
    Retrieve all Golds Gyms in the SW
    """
    users_ref = db.collection(u'gyms').where(u'Name', u'==', gym).where(u'Location', u'==', location)
    docs = users_ref.stream()

    print("Retrieve all Golds Gyms in the SW")
    for doc in docs:
        print(u'{} => {}'.format(doc.id, doc.to_dict()))


def get_machines_from_gym():
    """
    Retrieve all Machines for the Golds Gyms in the SW
    """
    users_ref = db.collection(u'gyms').where(u'Name', u'==', "Golds").where(u'Location', u'==', u"N").limit(1)
    gym_doc = next(users_ref.stream())

    print("Retrieve all machines in the SW Golds Gyms")
    print("GymId: {}".format(gym_doc.id))
    users_ref = db.collection(u'gyms').document(gym_doc.id).collection("Machines")
    machine_docs = users_ref.stream()
    for doc in machine_docs:
        temp = doc.to_dict()
        print("{}: {}".format(temp["Name"], temp["MachineId"]))