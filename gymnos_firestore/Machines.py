import gymnos_firestore.Gyms as gyms
from google.cloud import firestore
from datetime import date

# Gym collection keys
GYM_COLLECTION = u'Gyms'

# Machine collection keys
MACHINE_COLLECTION = u'Machines'
MACHINE_ID = u'MachineID'
MACHINE_NAME = u'Name'
MACHINE_LOC = u'Location'
MACHINE_LOC_TOPX = u'TopX'
MACHINE_LOC_LEFTY = u'LeftY'
MACHINE_LOC_BOTTOMX = u'BottomX'
MACHINE_LOC_RIGHTY = u'RightY'

# Usage collection keys
USAGE_COLLECTION = u'Usage'
USAGE_DATE = u"Date"
USAGE_TIME_ARRAY = u"Times"
USAGE_TOTAL_TIME = u"TotalTime"


def create_machine(db, gym_id, machine_json):
    """
    Creates a machine using the specified json file
    """
    gym_ref = gyms.get_gym_by_id(db, gym_id)
    machine_name = machine_json[MACHINE_NAME]
    exists, machine_id = machine_exists(gym_ref, machine_name)
    if not exists:
        new_machine_ref = gym_ref.collection(MACHINE_COLLECTION).document()
        doc_id = new_machine_ref.id
        machine_json[MACHINE_ID] = doc_id

        new_machine_ref.set(machine_json)
        print("Machine created successfully")

        return True, doc_id
    else:
        print("Machine already exists, returning Machine ID")
        return False, machine_id


def machine_exists(gym_ref, machine_name):
    """
    Checks to see if a machine exists

    :return: : True if that machine is already in database
    """
    query_ref = gym_ref.collection(MACHINE_COLLECTION).where(u'Name', u'==', machine_name).limit(1)
    docs = query_ref.get()

    machines = []
    for doc in docs:
        machines.append(doc)

    if len(machines) > 0:
        machine_id = machines[0].reference.id
        return True, machine_id
    else:
        return False, None


def insert_machine_time(db, gym_id, machine_name, machine_id, start, end):
    """
    Inserts a row of machine usage

    :param db: Reference to the database instance
    :param gym_id: Document ID of gym
    :param machine_id: Machine ID
    :param start: Start of machine usage in Unix time
    :param end: End of machine usage in Unix time
    """
    gym_ref = gyms.get_gym_by_id(db, gym_id)
    usage_ref = gym_ref.collection(USAGE_COLLECTION)

    # Check if usage for this day has already started
    today = date.today().strftime("%Y/%m/%d")
    todays_doc = usage_ref.where(MACHINE_ID, u'==', machine_id).where(USAGE_DATE, u'==', today).limit(1)
    machine_time = u'{}#{}'.format(start, end)
    time_used = end - start
    try:
        doc_ref = next(todays_doc.get()).reference
        doc_ref.update({
            USAGE_TOTAL_TIME: firestore.Increment(time_used),
            USAGE_TIME_ARRAY: firestore.ArrayUnion([machine_time])})
    except StopIteration:
        print("No doc found, creating new date")
        data = {
            MACHINE_NAME: machine_name,
            MACHINE_ID: machine_id,
            USAGE_DATE: today,
            USAGE_TIME_ARRAY: [],
            USAGE_TOTAL_TIME: 0
        }

        doc_ref = usage_ref.document()
        # Create new entry
        doc_ref.set(data)
        # Insert machine time
        doc_ref.update({
            USAGE_TOTAL_TIME: firestore.Increment(time_used),
            USAGE_TIME_ARRAY: firestore.ArrayUnion([machine_time])})


def update_machine_location(db, gym_id, machine_id, new_location):
    """
    Updates the location of a machine
    """
    machine_ref = db.collection(GYM_COLLECTION).document(gym_id).collection(MACHINE_COLLECTION).document(machine_id)
    machine_ref.update({MACHINE_LOC: new_location})

    print("Machine location updated")
