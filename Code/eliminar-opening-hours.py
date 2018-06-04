import xml.etree.ElementTree as ET

tree = ET.parse('station_facilities_data.xml')
root=tree.getroot()



for parents in tree.findall("stations/station"):
   print(parents)
   j = parents.find(".//openingHours")
   parents.remove(j)

tree.write('StationFacilitiesNOH.xml')