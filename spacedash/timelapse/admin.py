from django.contrib import admin

from timelapse.models import LogEntry


class LogEntryAdmin(admin.ModelAdmin):
        list_display = ['id', 'StackId', 'StackLevel', 'SourceObject', 'File', 'Thread' ,'Process' ,'TimeStamp' ,'Host' ,'Audience' ,'Context', 'Routine', 'Line', 'LogId', 'tag']


admin.site.register(LogEntry, LogEntryAdmin)
