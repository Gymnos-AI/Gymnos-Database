
# Gym collection keys
GYM_COLLECTION = u'Gyms'
GYM_ID = u'GymID'
GYM_NAME = u'Name'
GYM_LOCATION = u'Location'


def create_gym(db, gym_name, location):
    """
    This function will create a gym in the database

    :return: gymid - AutoID of gym that you created
    """
    if not gym_exists(db, gym_name, location):
        new_gym_ref = db.collection(GYM_COLLECTION).document()
        gym_id = new_gym_ref.id
        doc_data = {
            u'GymId': gym_id,
            u'Name': gym_name,
            u'Location': location
        }
        new_gym_ref.set(doc_data)
        print("Gym created successfully")

        return gym_id
    else:
        return "This Gym has already been created"


def gym_exists(db, gym_name, location):
    """
    Checks to see if a gym exists

    :return: : True is that gym is already in database
    """
    users_ref = db.collection(GYM_COLLECTION).where(u'Name', u'==', gym_name).where(u'Location', u'==', location)
    docs = users_ref.get()

    gyms = []
    for doc in docs:
        gyms.append(doc)

    if len(gyms) > 0:
        return True
    else:
        return False


def get_gym_snapshot(db, gym_name, location):
    """
    Returns a snapshot of a gym
    """
    users_ref = db.collection(GYM_COLLECTION).where(u'Name', u'==', gym_name).where(u'Location', u'==', location).limit(1)
    doc = next(users_ref.get())

    return doc


def get_gym_by_id(db, gym_id):
    """
    Returns a snapshot of a gym by it's ID
    """
    users_ref = db.collection(GYM_COLLECTION).document(gym_id)

    return users_ref
