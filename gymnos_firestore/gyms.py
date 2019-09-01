import datetime

from matchbox import models

# Gym collection keys
GYM_COLLECTION = 'Gyms'
GYM_NAME = 'name'
GYM_LAST_CHECK_IN = 'last_check_in'
GYM_LOCATION = 'location'


class Gyms(models.Model):
    name = models.TextField()
    last_check_in = models.TimeStampField(default=datetime.datetime.utcnow())
    location = models.TextField()

    class Meta:
        collection_name = GYM_COLLECTION
