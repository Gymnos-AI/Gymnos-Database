import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account to connect to the databse
cred = credentials.Certificate('./serviceAccount.json')
firebase_admin.initialize_app(cred)
db = firestore.client()


def create_gym(gym_name, location):
    """
    This function will create a gym in the database

    :return: gymid - AutoID of gym that you created
    """
    if get_gym(gym_name, location) < 1:
        new_gym_ref = db.collection(u'gyms').document()
        gym_id = new_gym_ref.id
        doc_data = {
            u'GymId': gym_id,
            u'Name': gym_name,
            u'Location': location
        }
        db.collection(u'gyms').document(gym_id).set(doc_data)

        return gym_id
    else:
        return "This Gym has already been created"


def get_gym(gym_name, location):
    """
    Retrieve all instances of a gym
    """
    users_ref = db.collection(u'gyms').where(u'Name', u'==', gym_name).where(u'Location', u'==', location)
    docs = users_ref.get()

    gyms_retrieved = 0
    for doc in docs:
        gyms_retrieved += 1
        print(u'{} => {}'.format(doc.id, doc.to_dict()))

    return gyms_retrieved


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