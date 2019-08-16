from matchbox import models
from matchbox.queries.error import DocumentDoesNotExists

import gymnos_firestore.gyms as gyms
from google.cloud import firestore
from datetime import date

# Gym collection keys
from gymnos_firestore import usage

GYM_COLLECTION = 'Gyms'

# Machine collection keys
MACHINE_COLLECTION = 'Machines'
MACHINE_ID = 'MachineID'
MACHINE_NAME = 'Name'
MACHINE_LOC = 'Location'
MACHINE_LOC_TOPX = 'TopX'
MACHINE_LOC_LEFTY = 'LeftY'
MACHINE_LOC_BOTTOMX = 'BottomX'
MACHINE_LOC_RIGHTY = 'RightY'


class Machines(models.Model):
    machine_id = models.TextField(column_name='MachineID')
    name = models.TextField(column_name='Name')
    location = models.MapField(column_name='Location')
    open = models.BooleanField(column_name='Open', default=True)

    class Meta:
        collection_name = 'Machines'
