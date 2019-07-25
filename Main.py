import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('./serviceAccount.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

doc_ref = db.collection('users').document('Next')
doc_ref.set({
    'first': 'Ada',
    'last': 'Lovelfsdace',
    'born': 1815
})


