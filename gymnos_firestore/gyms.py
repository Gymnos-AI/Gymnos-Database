from matchbox import models

# Gym collection keys
GYM_COLLECTION = 'Gyms'
GYM_ID = 'GymID'
GYM_NAME = 'Name'
GYM_LOCATION = 'Location'


class Gyms(models.Model):
    gym_id = models.TextField(column_name='GymID')
    name = models.TextField(column_name='Name')
    last_check_in = models.TimeStampField(column_name='Last_Check_In')
    location = models.TextField(column_name='Location')

    class Meta:
        collection_name = 'Gyms'
