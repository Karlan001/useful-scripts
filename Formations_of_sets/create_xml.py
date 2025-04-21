import csv
from lxml import etree as ET
from typing import List
from os import path

STR_DOC = '<?xml version="1.0" encoding="UTF-8"?>'
DIRECTORY = 'for_upload/'
TEMPLATE = 'TEMPLATE.xml'

UNITS = 'едЗеленый_test.csv'
PACKS = 'наборЗеленый_test.csv'
FINAL_FILE = path.join(DIRECTORY, 'test0.xml')

tree = ET.ElementTree(file=TEMPLATE)
root = tree.getroot()


def write_org_info(org_name: str,
                   inn: str,
                   index: str,
                   kpp: str = None,
                   phone_num: str = None,
                   email: str = None):

    for elem in root.iter():
        if elem.tag == 'LP_info':
            elem.attrib['org_name'] = org_name
            elem.attrib['LP_TIN'] = inn
            if kpp is None:
                del elem.attrib['RRC']
            else:
                elem.attrib['RRC'] = kpp
        elif elem.tag == 'location_address':
            elem.attrib['text_address'] = index
        elif elem.tag == 'contacts':
            if phone_num is None:
                del elem.attrib['phone_number']
            else:
                elem.attrib['phone_number'] = phone_num
            if email is None:
                del elem.attrib['email']
            else:
                elem.attrib['email'] = email


def get_cis_pack():
    with open(PACKS) as pack_file:
        pack_reader = csv.reader(pack_file, delimiter=' ')
        for row in pack_reader:
            yield row[0]


with open(UNITS) as units_file:
    units_reader = csv.reader(units_file, delimiter=' ')
    pack = get_cis_pack()

    for row in units_reader:
        cis_main: List = []
        cis_main.extend(row)

        for elem in root.iter('Document'):
            pack_content = ET.SubElement(elem, 'pack_content')
            pack_code = ET.SubElement(pack_content, 'pack_code')
            pack_code.text = ET.CDATA(f'{next(pack)}')
            cis = ET.SubElement(pack_content, 'cis')
            cis2 = ET.SubElement(pack_content, 'cis')
            cis.text = ET.CDATA(f'{cis_main[0]}')
            cis2.text = ET.CDATA(f'{cis_main[1]}')

    new_tree = ET.ElementTree(root)
    with open(FINAL_FILE, 'wb') as f:
        write_org_info('123', '123', '123', kpp='12312')
        new_tree.write(f, encoding='utf-8', xml_declaration=True)
