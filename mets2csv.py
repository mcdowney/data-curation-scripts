import os
import csv
import xml.etree.ElementTree as ET
import io

path = 'gamble_xml'



def get_item_metadata(fname):
    for item in root.findall('./dmdSec/mdWrap/xmlData'):
        metadata = {}
        #spatial = []
        #type = []
        for child in item:
            element = child.tag.split("}")[1]
            if element not in metadata:
                metadata[element] = child.text
            else:
                element_values = []
                element_values.append(child.text)
                element_values.append(metadata[element])
                metadata[element] = element_values
        return metadata


collection_md = []
for filename in os.listdir(path):
    if not filename.endswith('.xml'): continue
    fullname = os.path.join(path, filename)
    tree = ET.parse(fullname)
    root = tree.getroot()
    for dmdSec in root.findall('dmdSec'):
        record = {}
        record_id = dmdSec.get('ID')
        record_md = get_item_metadata(filename)
        record[record_id] = record_md
    collection_md.append(record)

print(collection_md)


fields = ['ID', 'alternative', 'dcmitype', 'date', 'series', 'subject', 'source_collection', 'title', 'type', 'spatial', 'creator', 'roll_number', 'isVersionOf', 'description', 'hasVersion', 'abstract']
with io.open('gamble.csv', 'w', encoding='utf-8') as gamble:
    fieldnames = fields
    writer = csv.DictWriter(gamble, dialect=csv.excel, fieldnames = fields)
    writer.writeheader()

    for record in collection_md:
        for c_id, c_info in record.items():
            row = {'ID': c_id}
            row.update(c_info)
            writer.writerow(row)
    gamble.close()
