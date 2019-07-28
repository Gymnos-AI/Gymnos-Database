import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account to connect to the databse
cred = credentials.Certificate('./serviceAccount.json')
firebase_admin.initialize_app(cred)
db = firestore.client()


"""
Retrieve all Golds Gyms
"""
users_ref = db.collection(u'gyms').where(u'Name', u'==', "Golds")
docs = users_ref.stream()

print("Retrieve all Golds Gyms")
for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))

"""
Retrieve all Golds Gyms in the SW
"""
users_ref = db.collection(u'gyms').where(u'Name', u'==', "Golds").where(u'Location', u'==', "SW")
docs = users_ref.stream()

print("Retrieve all Golds Gyms in the SW")
for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))

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