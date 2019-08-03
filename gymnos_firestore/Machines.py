import gymnos_firestore.Gyms as gyms
from google.cloud import firestore
from datetime import date

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


def create_machine(db, gym_id, machine_json):
    """
    Creates a machine using the specified json file
    """
    gym_ref = gyms.get_gym_by_id(db, gym_id)
    machine_name = machine_json[MACHINE_NAME]
    if not machine_exists(db, gym_ref, machine_name):
        new_machine_ref = gym_ref.collection(MACHINE_COLLECTION).document()
        doc_id = new_machine_ref.id
        machine_json[MACHINE_ID] = doc_id

        new_machine_ref.set(machine_json)
        print("Machine created successfully")

        return doc_id
    else:
        print("This Machine has already been created")

def machine_exists(db, gym_ref, machine_name):
    """
    Checks to see if a machine exists

    :return: : True if that machine is already in database
    """
    query_ref = gym_ref.collection(MACHINE_COLLECTION).where(u'Name', u'==', machine_name)
    docs = query_ref.get()

    machines = []
    for doc in docs:
        machines.append(doc)

    if len(machines) > 0:
        return True
    else:
        return False


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
    try:
        doc_ref = next(todays_doc.get()).reference
        doc_ref.update({u'Times': firestore.ArrayUnion([machine_time])})
    except StopIteration:
        print("No doc found, creating new date")
        data = {
            MACHINE_NAME: machine_name,
            MACHINE_ID: machine_id,
            USAGE_DATE: today,
            USAGE_TIME_ARRAY: []
        }

        doc_ref = usage_ref.document()
        # Create new entry
        doc_ref.set(data)
        # Insert machine time
        doc_ref.update({u'Times': firestore.ArrayUnion([machine_time])})
