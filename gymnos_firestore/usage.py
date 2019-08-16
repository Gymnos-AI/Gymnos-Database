from matchbox import models

# Usage collection keys
USAGE_COLLECTION = 'Usage'
USAGE_DATE = 'Date'
USAGE_TIME_ARRAY = 'Times'
USAGE_TOTAL_TIME = 'TotalTime'


class Usage(models.Model):
    date = models.TextField(column_name='Date')
    machine_id = models.TextField(column_name='MachineID')
    name = models.TextField(column_name='Name')
    times = models.ListField(column_name='Times', default=list())
    total_time = models.IntegerField(column_name='TotalTime', default=0)

    class Meta:
        collection_name = 'Usage'
