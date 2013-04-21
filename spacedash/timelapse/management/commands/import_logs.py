from django.core.management.base import BaseCommand

from timelapse.models import LogEntry


class Command(BaseCommand):
    args = 'path_to/log_file_name'

    def handle(self, *args, **options):
        filename = args[0]  # 'data/log2013-04-17T23:51:22.735--2013-04-17T23:57:27.505--AOS.xml_recortado'

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
                elif 'has successfully released a component with curl' in item.text and 'TotalPowerProcessor' in item.text:
                    print 'TERM'
                    print item.attrib
                    print item.text

                # print item.attrib
            except IndexError:
                pass
