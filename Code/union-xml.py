import xml.etree.ElementTree as ET

tree2 = ET.parse('StationFacilitiesNOH.xml')
root2 = tree2.getroot()

tree1= ET.parse('StepFreeTubeNNone.xml')
root = tree1.getroot()

for parents2 in tree2.findall("stations"):
    root.append(parents2)


tree1.write('TFLfacilities.xml')




