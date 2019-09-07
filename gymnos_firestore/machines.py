from gymnos_firestore import camera
from matchbox import models

# Machine collection keys
MACHINE_COLLECTION = 'Machines'
MACHINE_LOC = 'location'
MACHINE_LOC_TOPX = 'top_x'
MACHINE_LOC_LEFTY = 'left_y'
MACHINE_LOC_BOTTOMX = 'bottom_x'
MACHINE_LOC_RIGHTY = 'right_y'
MACHINE_NAME = 'name'
MACHINE_OPEN = 'open'


class Machines(models.Model):

    camera = models.ReferenceField(ref_model=camera.Camera)
    location = models.MapField()
    name = models.TextField()
    open = models.BooleanField(default=True)

    class Meta:
        collection_name = MACHINE_COLLECTION
