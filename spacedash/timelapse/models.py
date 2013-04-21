from django.db import models


class LogEntry(models.Model):
    StackId = models.TextField()
    StackLevel = models.TextField()
    SourceObject = models.TextField()
    File = models.TextField()
    Thread = models.TextField()
    Process = models.TextField()
    TimeStamp = models.DateTimeField()
    Host = models.TextField()
    Audience = models.TextField()
    Context = models.TextField()
    Routine = models.TextField()
    Line = models.TextField()
    LogId = models.TextField()
    tag = models.TextField()
    process = models.ForeignKey('Process', null=True)


class Process(models.Model):
    start = models.DateTimeField()
    error = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)
    array = models.TextField()
