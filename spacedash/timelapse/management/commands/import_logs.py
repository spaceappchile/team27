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
                    print 'INIT'
                    print item.attrib
                    print item.text
                    index = item.text.index('Array') + len('Array')
                    array = item.text[index:].split(' ')[0]
                    print array
                    Process.objects.create(start=item.attrib['TimeStamp'], array=array)
                elif 'has successfully released a component with curl' in item.text and 'TotalPowerProcessor' in item.text:
                    print 'TERM'
                    print item.attrib
                    print item.text
                    index = item.text.index('Array') + len('Array')
                    array = item.text[index:].split("'")[0]
                    print array
                    try:
                        process = Process.objects.get(array=array, end=None)
                        process.end = item.attrib['TimeStamp']
                        process.save()
                    except Process.DoesNotExist:
                        pass
            except IndexError:
                pass

        for item in root.findall('Error'):
            if 'Array' in item.attrib['SourceObject']:
                process = Process.objects.get(array=array, error=None)
                process.error = item.attrib['TimeStamp']
                process.save()
