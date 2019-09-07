from matchbox import models

# Camera collection keys
CAMERA_COLLECTION = 'Camera'
CAMERA_NAME = 'name'


class Camera(models.Model):

    name = models.TextField()
    machine_id_list = models.ListField(default=list())

    class Meta:
        collection_name = CAMERA_COLLECTION
