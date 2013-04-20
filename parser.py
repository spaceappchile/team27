# parser to test xml file

import xml
import xml.etree.ElementTree as ET

filename = 'data/log2013-04-17T23:51:22.735--2013-04-17T23:57:27.505--AOS.xml_recortado'

tree = ET.parse(filename)
root = tree.getroot()

for errortag in root.findall('Error'):
    print errortag.tag, errortag.attrib
