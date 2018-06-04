import requests

#Parametros de conexion al API
parameters = {"app_id": ", "app_key": ""}

#Obtenemos los datos de station-facilities
response = requests.get("http://data.tfl.gov.uk/tfl/syndication/feeds/stations-facilities.xml",params=parameters)
with open("station_facilities_data.xml", mode='wb') as localfile:
    localfile.write(response.content)

#Obtenemos los datos de Step free tube guide
response = requests.get ("https://tfl.gov.uk/tfl/syndication/feeds/step-free-tube-guide.xml")
with open("step_free_tube_data.xml", mode='wb') as localfile:
    localfile.write(response.content)
