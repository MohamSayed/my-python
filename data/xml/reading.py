import xml.etree.ElementTree as ET
tree = ET.parse('test.xml')
root = tree.getroot()
print(root.tag)
print(" Attibutes:", root.attrib)
for child in root:
    print(child.tag, child.attrib)

print([elem.tag for elem in root.iter()])
print(ET.tostring(root, encoding='utf8').decode('utf8'))
