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
    gyms = get_gym(gym_name, location)
    if len(gyms) < 1:
        new_gym_ref = db.collection(u'gyms').document()
        gym_id = new_gym_ref.id
        doc_data = {
            u'GymId': gym_id,
            u'Name': gym_name,
            u'Location': location
        }
        db.collection(u'gyms').document(gym_id).set(doc_data)
        print("Gym created successfully")

        return gym_id
    else:
        return "This Gym has already been created"


def get_gym(gym_name, location):
    """
    Retrieve all instances of a gym and return it as a list of
    dictionaries

    :return: gyms: List of dictionaries of each gym found
    """
    users_ref = db.collection(u'gyms').where(u'Name', u'==', gym_name).where(u'Location', u'==', location)
    docs = users_ref.get()

    gyms = []
    for doc in docs:
        gyms.append(doc.to_dict)

    return gyms
