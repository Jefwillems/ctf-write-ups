import xml.etree.ElementTree as ET

tree = ET.parse('./drawing.flag.svg')

flag = ''

for i in tree.getroot().findall('{http://www.w3.org/2000/svg}g/{http://www.w3.org/2000/svg}text/{http://www.w3.org/2000/svg}tspan'):
    flag += i.text.rstrip().replace(' ', '')

print(flag)
