from tastypie import fields
from tastypie.resources import ModelResource

from .models import LogEntry, Process


class LogEntryResource(ModelResource):
    class Meta:
        queryset = LogEntry.objects.all()


class ProcessResource(ModelResource):
    logentries = fields.ToManyField(LogEntryResource, 'logentry_set', full=True)

    class Meta:
        queryset = Process.objects.all()
