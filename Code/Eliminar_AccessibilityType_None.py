import xml.etree.ElementTree as ET

doc = ET.parse("step_free_tube_data.xml")
raiz=doc.getroot()

for station in raiz.iter('{ELRAD}Station'):
    accesibility = station.find ('{ELRAD}Accessibility')
    acces_type = accesibility.find('{ELRAD}AccessibilityType')
    if acces_type.text == 'None':
        accesibility.remove(acces_type)


xmlnamespace = raiz.tag.split('{')[1].split('}')[0]
ET.register_namespace('',xmlnamespace)
doc.write('StepFreeTubeNNone.xml')