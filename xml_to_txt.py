import os
import xml.etree.ElementTree as ET


def xml_to_txt(file_name):
    path = os.path.join('images\\test\\', file_name)
    tree = ET.parse(path)
    root = tree.getroot()
    #txt_name = path.split(".")[0] + '.txt'
    txt_name = file_name.split('.')[0] + '.txt'
    with open('PASCALVOC\\groundtruths\\' + txt_name, 'w') as txt_file:
        for member in root.findall('object'):
            txt_file.write(member[0].text + ' ' +
                           member[4][0].text + ' ' + member[4][1].text + ' ' +
                           member[4][2].text + ' ' + member[4][3].text + '\n')

def main():
    for f in os.listdir("images/test"):
        # Generate .txt files of groundtruth images - 2020.3.12 Joy
        if f.endswith(".xml"):
            xml_to_txt(f)
            
    print('Successfully converted xml to txt.')


#main()
