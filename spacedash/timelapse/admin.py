from django.contrib import admin

from timelapse.models import LogEntry, Process


class LogEntryAdmin(admin.ModelAdmin):
        list_display = ['id', 'StackId', 'StackLevel', 'SourceObject', 'File', 'Thread' ,'Process' ,'TimeStamp' ,'Host' ,'Audience' ,'Context', 'Routine', 'Line', 'LogId', 'tag']


class ProcessAdmin(admin.ModelAdmin):
        list_display = ['id', 'start', 'error', 'end', 'array']


admin.site.register(LogEntry, LogEntryAdmin)
admin.site.register(Process, ProcessAdmin)
