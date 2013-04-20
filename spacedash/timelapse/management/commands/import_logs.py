from django.core.management.base import BaseCommand

from timelapse.models import LogEntry


class Command(BaseCommand):
    args = 'path_to/log_file_name'

    def handle(self, *args, **options):
        print args[0]

        filename = args[0]  # 'data/log2013-04-17T23:51:22.735--2013-04-17T23:57:27.505--AOS.xml_recortado'

        import xml
        import xml.etree.ElementTree as ET

        tree = ET.parse(filename)
        root = tree.getroot()

        for item in root:
            if item.tag != 'Header':
                print item.tag, item.attrib
                d = item.attrib
                d['tag'] = item.tag
                LogEntry.objects.create(**d)
