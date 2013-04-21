from django.core.management.base import BaseCommand

from timelapse.models import LogEntry, Process


class Command(BaseCommand):
    args = 'path_to/log_file_name'

    def handle(self, *args, **options):
        filename = args[0]

        import xml
        import xml.etree.ElementTree as ET

        tree = ET.parse(filename)
        root = tree.getroot()

        for item in root.findall('Info'):
            try:
                if 'activated and initialized' in item.text and item.attrib['Process'].startswith('CONTROL'):
                    index = item.text.index('Array') + len('Array')
                    array = item.text[index:].split(' ')[0]
                    process = Process.objects.create(start=item.attrib['TimeStamp'], array=array)
                    LogEntry.objects.create(tag='Info', SourceObject=item.attrib['SourceObject'], TimeStamp=item.attrib['TimeStamp'], process=process)
                elif 'has successfully released a component with curl' in item.text and 'TotalPowerProcessor' in item.text:
                    index = item.text.index('Array') + len('Array')
                    array = item.text[index:].split("'")[0]
                    try:
                        process = Process.objects.get(array=array, end=None)
                        process.end = item.attrib['TimeStamp']
                        process.save()
                        LogEntry.objects.create(tag='Info', SourceObject=item.attrib['SourceObject'], TimeStamp=item.attrib['TimeStamp'], process=process)
                    except Process.DoesNotExist:
                        pass
            except IndexError:
                pass

        for item in root.findall('Error'):
            logentry = LogEntry.objects.create(tag='Error', SourceObject=item.attrib['SourceObject'], TimeStamp=item.attrib['TimeStamp'])
            if 'Array' in item.attrib['SourceObject']:
                try:
                    process = Process.objects.get(array=array, error=None)
                    process.error = item.attrib['TimeStamp']
                    process.save()
                    logentry.process = process
                    logentry.save()
                except Process.DoesNotExist:
                    pass
