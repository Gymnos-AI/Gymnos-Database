from matchbox import models

# Usage collection keys
USAGE_COLLECTION = 'Usage'
USAGE_DATE = 'date'
USAGE_MACHINE_ID = 'machine_id'
USAGE_NAME = 'name'
USAGE_TIME_ARRAY = 'times'
USAGE_TOTAL_TIME = 'total_time'


class Usage(models.Model):

    date = models.TextField()
    machine_id = models.TextField()
    name = models.TextField()
    times = models.ListField(default=list())
    total_time = models.IntegerField(default=0)

    class Meta:
        collection_name = USAGE_COLLECTION
