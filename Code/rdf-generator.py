import rdflib
from rdflib import Graph, Literal, URIRef, Namespace, BNode
import xml.etree.ElementTree as ET

#Parseamos el fichero y sacamos root:

g=Graph()
tree = ET.parse('Tflfacilities.xml')
root=tree.getroot()



#Antes de comenzar con el código, vamos a definir el vocabulario que vamos a utilizar:

#Vocabulario propio de la estacion:
tflNamespace= Namespace("http://tfl.gov.uk/tfl#")
Name=tflNamespace.hasname
Adrress=tflNamespace.hasAdrress
Phone=tflNamespace.hasPhone
id_station=tflNamespace.hasID
type_station=tflNamespace.hasType

#vocabulario de linea:
lineNamespace= Namespace("http://tfl.gov.uk/tfl/line#")
Line=lineNamespace.hasLine
Linename=lineNamespace.hasname
Platform=lineNamespace.hasPlatform
Direction=lineNamespace.hasDirrection
Direction_towards=lineNamespace.hasDirrection_towards
Step_min=lineNamespace.hasStep_min
Step_max=lineNamespace.hasStep_max
Gap_min=lineNamespace.hasGap_min
Gap_max=lineNamespace.hasGap_max
Level_access_by_map=lineNamespace.hasLevel_access_by_map
Location_of_level_access=lineNamespace.hasLocation_of_level_access


#Vocabulario Naptans:

NPespace= Namespace("http://tfl.gov.uk/tfl/Naptans#")
NP=NPespace.hasNaptans
NPDescription=NPespace.hasDescription
NPId=NPespace.hasId


#Vocabulario Entrance:
Ent=Namespace("http://tfl.gov.uk/tfl/Accessibility_Entrance#")
Entrance=Ent.hasEntrance
Entname=Ent.hasname
EntranceToBookingHall=Ent.hasentranceToBookingHall

#Vocabulario Placemark:
Place_markmespace= Namespace("http://tfl.gov.uk/tfl/Place_mark#")
Mark=Place_markmespace.hasMark_place
PName=Place_markmespace.hasName
PDescripntion=Place_markmespace.hasDescription
PCoordinates=Place_markmespace.hasCoordinates
PUrs_Styles=Place_markmespace.hasURL_Style

BookingHallToPlatform=Namespace("http://tfl.gov.uk/tfl/Accessibility_Entrance/BookingHallToPlatform#")
BookEnt=BookingHallToPlatform.BookingHallToPlatform
PointName=BookingHallToPlatform.hasPointName
Heading=BookingHallToPlatform.hasHeading
PathDescription=BookingHallToPlatform.hasDescription

platformToTrain=Namespace("http://tfl.gov.uk/tfl/Accessibility_Entrance/platformToTrain#")
Totraint=platformToTrain.hasPlatformtotrain
TrainName=platformToTrain.hastrainName
PlatformToTrainSteps=platformToTrain.hasplatformToTrainSteps

zo=Namespace("http://tfl.gov.uk/tfl/Zones#")
zon=zo.hasZone
Zone=zo.hasnumber

selin = Namespace("http://tfl.gov.uk/tfl/selin#")
seline = selin.hasServingline
ServingLine = selin.hasname

#Vocabulario interchanges:

interamespace= Namespace("http://tfl.gov.uk/tfl/interchanges#")
Inter=interamespace.hasInterchanges
Airport=interamespace.hasAirport
Pier=interamespace.hasPier
Mainbus=interamespace.hasMainbus
Emirates_airlines=interamespace.hasEmirates_airlines
National_rail=interamespace.hasNational_rail
Tramlink=interamespace.hasTramlink


Acespace= Namespace("http://tfl.gov.uk/tfl/Accessibility#")
Ac=Acespace.hasAccessibility
Aditional_information=Acespace.hasAditional_information
BlueBadgeCarParkSpaces=Acespace.hasBlueBadgeCarParkSpaces
TaxiRanksOutsideStation=Acespace.hasTaxiRanksOutsideStation
AccessibilityType=Acespace.hasAccessibilityType


Lif=Namespace("http://tfl.gov.uk/Accessibility/lifts#")
Lift=Lif.hasLift
AccessViaLift=Lif.hasAccessViaLift
LimitedCapacityLift=Lif.hasLimitedCapacityLift

Toi = Namespace("http://tfl.gov.uk/Accessibility/Toilets#")
Toil = Toi.hastoilets
AccessibleToilet = Toi.hasAccessibleToilet
AccessibleToiletNote = Toi.hasAccessibleToiletNote

EspEN = Namespace("http://tfl.gov.uk/Accessibility/Especific_entrance#")
espe = EspEN.hasEntranceSpecific
SpecificEntranceRequired = EspEN.hasSpecificEntranceRequired
SpecificEntranceInstructions = EspEN.hasSpecificEntranceInstructions


facilities = Namespace("http://tfl.gov.uk/facilities#")
facilitie = facilities.hasFacilities
Ticket_Halls = facilities.Ticket_Halls
Lifts = facilities.Lifts
Escalators = facilities.Escalators
Gates = facilities.Gates
Toilets = facilities.Toilets
Photo_Booths = facilities.Photo_Booths
Cash_Machines = facilities.Cash_Machines
Payphones = facilities.Payphones
Car_park = facilities.Car_park
Vending_Machines = facilities.Vending_Machines
Help_Points = facilities.Help_Points
Bridge = facilities.Bridge
Waiting_Room = facilities.Waiting_Room
Other_Facilities = facilities.Other_Facilities



#Una vez definido el vocabulario vamos a generar el código respuesta:
#Estamos en ante una situación que tiene tres posibles casos:

## La estación este en ambos ficheros, en nuestro caso en un fichero de los que ha generado TFLfacilities.

##La estación solo estuviese en step-free.

##La estación solo estuviese en station facilities.

#Antes de empezar decidimos que solo pareceran esos nodos del grafo sobre los que se tengan datos.

###La estación está en ambos ficheros:

estaciones1=[]

for parents0 in tree.findall("stations/station"):

    name_station = parents0.find('.//name')
    n2 = name_station.text
    estaciones1.append(n2)



for i in estaciones1:

    for parents in tree.findall("./{ELRAD}Station"):
        Name_ = parents.find(".//{ELRAD}StationName")
        name_ = Name_.text

        if name_ == i:

            bag0 = rdflib.BNode()
            g.add((bag0, Name, Literal(name_)))

            for parents2 in parents.findall("./{ELRAD}Lines/{ELRAD}Line"):

                lineN = parents2.find(".//{ELRAD}LineName")
                if lineN is not None:
                    lineName = lineN.text
                else:
                    lineN = 'None'

                platform = parents2.find(".//{ELRAD}Platform")
                if platform is not None:
                    platform = platform.text

                direction = parents2.find(".//{ELRAD}Direction")
                if direction is not None:
                    direction = direction.text

                directionTowards = parents2.find(".//{ELRAD}DirectionTowards")
                if directionTowards is not None:
                    directionTowards = directionTowards.text

                stepMin = parents2.find(".//{ELRAD}StepMin")
                if stepMin is not None:
                    stepMin = stepMin.text

                stepMax = parents2.find(".//{ELRAD}StepMax")
                if stepMax is not None:
                    stepMax = stepMax.text

                gapMin = parents2.find(".//{ELRAD}GapMin")
                if gapMin is not None:
                    gapMin = gapMin.text

                gapMax = parents2.find(".//{ELRAD}GapMax")
                if gapMax is not None:
                    gapMax = gapMax.text

                levelAccessByManualRamp = parents2.find(".//{ELRAD}LevelAccessByManualRamp")
                if levelAccessByManualRamp is not None:
                    levelAccessByManualRamp = levelAccessByManualRamp.text

                locationOfLevelAccess = parents2.find(".//{ELRAD}LocationOfLevelAccess")
                if locationOfLevelAccess is not None:
                    locationOfLevelAccess = locationOfLevelAccess.text

                if lineN is not None:
                    bag1 = rdflib.BNode()
                    g.add((bag0, Line, bag1))
                    g.add((bag1, Linename, Literal(lineName)))

                    if platform is not None:
                        g.add((bag1, Platform, Literal(platform)))

                    if direction is not None:
                        g.add((bag1, Direction, Literal(direction)))

                    if directionTowards is not None:
                        g.add((bag1, Direction_towards, Literal(directionTowards)))

                    if stepMin is not None:
                        g.add((bag1, Step_min, Literal(stepMin)))

                    if stepMax is not None:
                        g.add((bag1, Step_max, Literal(stepMax)))

                    if gapMin is not None:
                        g.add((bag1, Gap_min, Literal(gapMin)))

                    if gapMax is not None:
                        g.add((bag1, Gap_max, Literal(gapMax)))

                    if levelAccessByManualRamp is not None:
                        g.add((bag1, Level_access_by_map, Literal(levelAccessByManualRamp)))

                    if locationOfLevelAccess is not None:
                        g.add((bag1, Location_of_level_access, Literal(locationOfLevelAccess)))

            for parents3 in parents.findall(".//{ELRAD}Naptans/{ELRAD}Naptan"):

                Description = parents3.find(".//{ELRAD}Description")
                if Description is not None:
                    Description = Description.text

                NaptanID = parents3.find(".//{ELRAD}NaptanID")
                if NaptanID is not None:
                    NaptanID = NaptanID.text

                if NaptanID and Description != None:
                    bag2 = rdflib.BNode()
                    g.add((bag0, NP, bag2))
                    if Description is not None:
                        g.add((bag2, NPDescription, Literal(Description)))
                    if NaptanID is not None:
                        g.add((bag2, NPId, Literal(NaptanID)))


            for parents4 in parents.findall(".//{ELRAD}AccessibleInterchanges"):

                airportInterchange = parents4.find(".//{ELRAD}AirportInterchange")
                if airportInterchange is not None:
                    airportInterchange = airportInterchange.text

                pierInterchange = parents4.find(".//{ELRAD}PierInterchange")
                if pierInterchange is not None:
                    pierInterchange = pierInterchange.text

                mainBusInterchange = parents4.find(".//{ELRAD}MainBusInterchange")
                if mainBusInterchange is not None:
                    mainBusInterchange = mainBusInterchange.text

                emiratesAirLineInterchange = parents4.find(".//{ELRAD}EmiratesAirLineInterchange")
                if emiratesAirLineInterchange is not None:
                    emiratesAirLineInterchange = emiratesAirLineInterchange.text

                tramlinkInterchange = parents4.find(".//{ELRAD}TramlinkInterchange")
                if tramlinkInterchange is not None:
                    tramlinkInterchange = tramlinkInterchange.text

                nationalRailInterchange = parents4.find(".//{ELRAD}NationalRailInterchange")
                if nationalRailInterchange is not None:
                    nationalRailInterchange = nationalRailInterchange.text

                bag3 = rdflib.BNode()
                g.add((bag0, Inter, bag3))

                if airportInterchange is not None:
                    g.add((bag3, Airport, Literal(airportInterchange)))

                if pierInterchange is not None:
                    g.add((bag3, Pier, Literal(pierInterchange)))

                if mainBusInterchange is not None:
                    g.add((bag3, Mainbus, Literal(mainBusInterchange)))

                if emiratesAirLineInterchange is not None:
                    g.add((bag3, Emirates_airlines, Literal(emiratesAirLineInterchange)))

                if tramlinkInterchange is not None:
                    g.add((bag3, National_rail, Literal(tramlinkInterchange)))

                if nationalRailInterchange is not None:
                    g.add((bag3, Tramlink, Literal(nationalRailInterchange)))

            for parents5 in parents.findall(".//{ELRAD}Accessibility"):

                additionalAccessibilityInformation = parents5.find(".//{ELRAD}AdditionalAccessibilityInformation")
                if additionalAccessibilityInformation is not None:
                    additionalAccessibilityInformation = additionalAccessibilityInformation.text

                blueBadgeCarParkSpaces = parents5.find(".//{ELRAD}BlueBadgeCarParkSpaces")
                if blueBadgeCarParkSpaces is not None:
                    blueBadgeCarParkSpaces = blueBadgeCarParkSpaces.text

                taxiRanksOutsideStation = parents5.find(".//{ELRAD}TaxiRanksOutsideStation")
                if taxiRanksOutsideStation is not None:
                    taxiRanksOutsideStation = taxiRanksOutsideStation.text

                accessibilityType = parents5.find(".//{ELRAD}AccessibilityType")
                if accessibilityType is not None:
                    accessibilityType = accessibilityType.text

                bag4 = rdflib.BNode()
                g.add((bag0, Ac, bag4))
                if additionalAccessibilityInformation is not None:
                    g.add((bag4, Aditional_information, Literal(additionalAccessibilityInformation)))
                if blueBadgeCarParkSpaces is not None:
                    g.add((bag4, BlueBadgeCarParkSpaces, Literal(blueBadgeCarParkSpaces)))
                if taxiRanksOutsideStation is not None:
                    g.add((bag4, TaxiRanksOutsideStation, Literal(taxiRanksOutsideStation)))
                if accessibilityType is not None:
                    g.add((bag4, AccessibilityType, Literal(accessibilityType)))

                accessViaLift = parents5.find(".//{ELRAD}AccessViaLift")
                if accessViaLift is not None:
                    accessViaLift = accessViaLift.text

                limitedCapacityLift = parents5.find(".//{ELRAD}LimitedCapacityLift")
                if limitedCapacityLift is not None:
                    limitedCapacityLift = limitedCapacityLift.text

                if accessViaLift is not None:
                    g.add((bag4, AccessViaLift, Literal(accessViaLift)))
                if limitedCapacityLift is not None:
                    g.add((bag4, LimitedCapacityLift, Literal(limitedCapacityLift)))

                accessibleToilet = parents5.find(".//{ELRAD}AccessibleToilet")
                if accessibleToilet is not None:
                    accessibleToilet = accessibleToilet.text

                accessibleToiletNote = parents5.find(".//{ELRAD}AccessibleToiletNote")
                if accessibleToiletNote is not None:
                    accessibleToiletNote = accessibleToiletNote.text

                if accessibleToilet is not None:
                    g.add((bag4, AccessibleToilet, Literal(accessibleToilet)))
                if accessibleToiletNote is not None:
                    g.add((bag4, AccessibleToiletNote, Literal(accessibleToiletNote)))

                specificEntranceRequired = parents5.find(".//{ELRAD}SpecificEntranceRequired")
                if specificEntranceRequired is not None:
                    specificEntranceRequired = specificEntranceRequired.text

                specificEntranceInstructions = parents5.find(".//{ELRAD}SpecificEntranceInstructions")
                if specificEntranceInstructions is not None:
                    specificEntranceInstructions = specificEntranceInstructions.text

                if specificEntranceRequired is not None:
                    g.add((bag4, SpecificEntranceRequired, Literal(specificEntranceRequired)))
                if specificEntranceInstructions is not None:
                    g.add((bag4, SpecificEntranceInstructions, Literal(specificEntranceInstructions)))

    for parents6 in tree.findall("stations/station"):
        Name_2 = parents6.find('.//name')
        name_2 = Name_2.text
        if name_2 == i:

            bag0 = rdflib.BNode()
            ad = parents6.find('.//address')
            address = ad.text
            if address is not None:
                g.add((bag0, Adrress, Literal(address)))


            ph = parents6.find('.//phone')
            phone = ph.text
            if phone is not None:
                g.add((bag0, Phone, Literal(phone)))

            t = parents6.attrib
            id = t['id']
            type = t['type']
            if id is not None:
                g.add((bag0, id_station, Literal(id)))

            if type is not None:
                g.add((bag0, type_station, Literal(type)))

            for parents7 in parents6.findall(".//entrances/entrance"):

                name_entrance = parents7.find(".//name")
                if name_entrance is not None:
                    name_entrance = name_entrance.text


                entranceToBookingHall = parents7.find(".//entranceToBookingHall")
                if entranceToBookingHall is not None:
                    entranceToBookingHall = entranceToBookingHall.text

                bag5 = rdflib.BNode()
                g.add((bag0, Entrance, bag5))
                g.add((bag5, Entname, Literal(name_entrance)))
                g.add((bag5, EntranceToBookingHall, Literal(entranceToBookingHall)))

                for parents8 in parents7.findall(".//bookingHallToPlatform"):

                    pointName = parents8.find(".//pointName")
                    if pointName is not None:
                        pointName = pointName.text

                    pathDescription = parents8.find(".//pathDescription")
                    if pathDescription is not None:
                        pathDescription = pathDescription.text

                    heading = parents8.find(".//heading")
                    if heading is not None:
                        heading = heading.text

                    bag6 = rdflib.BNode()
                    g.add((bag5, BookEnt, bag6))
                    g.add((bag6, PointName, Literal(pointName)))
                    g.add((bag6, PathDescription, Literal(pathDescription)))
                    g.add((bag6, Heading, Literal(heading)))


                for parents9 in parents7.findall(".//platformToTrain"):

                    trainName = parents9.find(".//trainName")
                    if trainName is not None:
                        trainName = trainName.text

                    platformToTrainSteps = parents9.find(".//platformToTrainSteps")
                    if platformToTrainSteps is not None:
                        platformToTrainSteps = platformToTrainSteps.text

                    bag7 = rdflib.BNode()
                    g.add((bag5, Totraint, bag7))
                    if trainName is not None:
                        g.add((bag7, TrainName, Literal(trainName)))
                    if platformToTrainSteps is not None:
                        g.add((bag7, PlatformToTrainSteps, Literal(platformToTrainSteps)))

            for parents10 in parents6.findall(".//Placemark"):

                name_makr = parents10.find(".//name")
                if name_makr is not None:
                    name_makr = name_makr.text

                descriptio = parents10.find(".//description")
                if descriptio is not None:
                    descriptio = descriptio.text

                coordinates = parents10.find(".//coordinates")
                if coordinates is not None:
                    coordinates = coordinates.text

                styleUrl = parents10.find(".//styleUrl")
                if styleUrl is not None:
                    styleUrl = styleUrl.text

                if name_makr and descriptio and coordinates and styleUrl != None:
                    bag8 = rdflib.BNode()
                    g.add((bag0, Mark, bag8))
                    if name_makr is not None:
                        g.add((bag8, PName, Literal(name_makr)))
                    if descriptio is not None:
                        g.add((bag8, PDescripntion, Literal(descriptio)))
                    if coordinates is not None:
                        g.add((bag8, PCoordinates, Literal(coordinates)))
                    if styleUrl is not None:
                        g.add((bag8, PUrs_Styles, Literal(styleUrl)))

            for parents11 in parents6.findall(".//facilities"):

                ticket= parents11.find(".//facility")
                if ticket is not None:
                    ticket=ticket.attrib['name']

                if ticket == "Ticket Halls":
                    ticket = parents11.text

                else:
                    ticket= None

                if ticket == "Help Points":
                    help_Points = parents11.text
                else:
                    help_Points = None

                if ticket == "Bridge":
                    bridge = parents11.text
                else:
                    bridge = None

                if  ticket == "Vending Machines":
                    vending_Machines = parents11.text
                else:
                    vending_Machines = None

                if ticket == "Car park":
                    car_park = parents11.text
                else:
                    car_park = None

                if ticket == "Payphones":
                    payphones = parents11.text
                else:
                    payphones = None


                if ticket == "Cash Machines":
                    cash_Machines = parents11.text
                else:
                    cash_Machines = None


                if ticket == "Photo Booths":
                    photo_Booths = parents11.text
                else:
                    photo_Booths = None


                if ticket == "Toilets":
                    toilets = parents11.text
                else:
                    toilets = None

                if ticket == "Gates":
                    gates = parents11.text
                else:
                    gates = None


                if ticket == "Lifts":
                    lifts = parents11.text
                else:
                    lifts = None

                if ticket == "Escalators":
                    escalators = parents11.text
                else:
                    escalators = None

                if ticket == "Other Facilities":
                    other_Facilities = parents11.text
                else:
                    other_Facilities = None


                if ticket == " Waiting Room":
                    waiting_Room = parents11.text
                else:
                    waiting_Room = None

                bag9 = rdflib.BNode()
                g.add((bag0, facilitie, bag9))
                if waiting_Room is not None:
                    g.add((bag9, Waiting_Room, Literal(waiting_Room)))
                if other_Facilities is not None:
                    g.add((bag9, Other_Facilities, Literal(other_Facilities)))
                if lifts is not None:
                    g.add((bag9, Lifts, Literal(lifts)))
                if escalators is not None:
                    g.add((bag9, Escalators, Literal(escalators)))
                if gates is not None:
                    g.add((bag9, Gates, Literal(gates)))
                if toilets is not None:
                    g.add((bag9, Toilets, Literal(toilets)))
                if photo_Booths is not None:
                    g.add((bag9, Photo_Booths, Literal(photo_Booths)))
                if cash_Machines is not None:
                    g.add((bag9, Cash_Machines, Literal(cash_Machines)))
                if payphones is not None:
                    g.add((bag9, Payphones, Literal(payphones)))
                if car_park is not None:
                    g.add((bag9, Car_park, Literal(car_park)))
                if vending_Machines is not None:
                    g.add((bag9, Vending_Machines, Literal(vending_Machines)))
                if bridge is not None:
                    g.add((bag9, Bridge, Literal(bridge)))
                if help_Points is not None:
                    g.add((bag9, Help_Points, Literal(help_Points)))

            for parents12 in parents6.findall(".//zones"):

                zone = parents12.find(".//zone")
                if zone is not None:
                    zone = zone.text

                if zone is not None:
                    bag10 = rdflib.BNode()
                    g.add((bag0, zon, bag10))
                    g.add((bag10, Zone, Literal(zone)))

            for parents13 in parents6.findall(".//servingLines"):

                servingLine = parents13.find(".//servingLine")
                if servingLine is not None:
                    servingLine = servingLine.text

                if servingLine is not None:
                    bag11 = rdflib.BNode()
                    g.add((bag0, seline, bag11))
                    g.add((bag11, ServingLine, Literal(servingLine)))


##La estación se encuentra en solo en station-facilities:

for parents20 in tree.findall("./{ELRAD}Station"):
    Name_3 = parents20.find(".//{ELRAD}StationName")
    name_3 = Name_3.text

    if name_3 not in estaciones1:

        bag20 = rdflib.BNode()
        g.add((bag20, Name, Literal(name_3)))

        for parents21 in parents20.findall("./{ELRAD}Lines/{ELRAD}Line"):

            lineN = parents21.find(".//{ELRAD}LineName")
            if lineN is not None:
                lineName = lineN.text
            else:
                lineN = 'None'

            platform = parents21.find(".//{ELRAD}Platform")
            if platform is not None:
                platform = platform.text

            direction = parents21.find(".//{ELRAD}Direction")
            if direction is not None:
                direction = direction.text

            directionTowards = parents21.find(".//{ELRAD}DirectionTowards")
            if directionTowards is not None:
                directionTowards = directionTowards.text

            stepMin = parents21.find(".//{ELRAD}StepMin")
            if stepMin is not None:
                stepMin = stepMin.text

            stepMax = parents21.find(".//{ELRAD}StepMax")
            if stepMax is not None:
                stepMax = stepMax.text

            gapMin = parents21.find(".//{ELRAD}GapMin")
            if gapMin is not None:
                gapMin = gapMin.text

            gapMax = parents21.find(".//{ELRAD}GapMax")
            if gapMax is not None:
                gapMax = gapMax.text

            levelAccessByManualRamp = parents21.find(".//{ELRAD}LevelAccessByManualRamp")
            if levelAccessByManualRamp is not None:
                levelAccessByManualRamp = levelAccessByManualRamp.text

            locationOfLevelAccess = parents21.find(".//{ELRAD}LocationOfLevelAccess")
            if locationOfLevelAccess is not None:
                locationOfLevelAccess = locationOfLevelAccess.text

            if lineN is not None:
                bag21 = rdflib.BNode()
                g.add((bag20, Line, bag21))
                g.add((bag21, Linename, Literal(lineName)))

                if platform is not None:
                    g.add((bag21, Platform, Literal(platform)))
                if direction is not None:
                    g.add((bag21, Direction, Literal(direction)))
                if directionTowards is not None:
                    g.add((bag21, Direction_towards, Literal(directionTowards)))
                if stepMin is not None:
                    g.add((bag21, Step_min, Literal(stepMin)))
                if stepMax is not None:
                    g.add((bag21, Step_max, Literal(stepMax)))
                if gapMin is not None:
                    g.add((bag21, Gap_min, Literal(gapMin)))
                if gapMax is not None:
                     g.add((bag21, Gap_max, Literal(gapMax)))
                if levelAccessByManualRamp is not None:
                    g.add((bag21, Level_access_by_map, Literal(levelAccessByManualRamp)))
                if locationOfLevelAccess is not None:
                     g.add((bag21, Location_of_level_access, Literal(locationOfLevelAccess)))

        for parents22 in parents20.findall(".//{ELRAD}Naptans/{ELRAD}Naptan"):

            Description = parents22.find(".//{ELRAD}Description")
            if Description is not None:
                Description = Description.text

            NaptanID = parents22.find(".//{ELRAD}NaptanID")
            if NaptanID is not None:
                NaptanID = NaptanID.text

            if NaptanID and Description != None:
                bag22 = rdflib.BNode()
                g.add((bag20, NP, bag22))
                if Description is not None:
                    g.add((bag22, NPDescription, Literal(Description)))

                if NaptanID is not None:
                    g.add((bag22, NPId, Literal(NaptanID)))


        for parents23 in parents20.findall(".//{ELRAD}AccessibleInterchanges"):

            airportInterchange = parents23.find(".//{ELRAD}AirportInterchange")
            if airportInterchange is not None:
                airportInterchange = airportInterchange.text

            pierInterchange = parents23.find(".//{ELRAD}PierInterchange")
            if pierInterchange is not None:
                pierInterchange = pierInterchange.text

            mainBusInterchange = parents23.find(".//{ELRAD}MainBusInterchange")
            if mainBusInterchange is not None:
                mainBusInterchange = mainBusInterchange.text

            emiratesAirLineInterchange = parents23.find(".//{ELRAD}EmiratesAirLineInterchange")
            if emiratesAirLineInterchange is not None:
                emiratesAirLineInterchange = emiratesAirLineInterchange.text

            tramlinkInterchange = parents23.find(".//{ELRAD}TramlinkInterchange")
            if tramlinkInterchange is not None:
                tramlinkInterchange = tramlinkInterchange.text

            nationalRailInterchange = parents23.find(".//{ELRAD}NationalRailInterchange")
            if nationalRailInterchange is not None:
                nationalRailInterchange = nationalRailInterchange.text

            if airportInterchange and pierInterchange and mainBusInterchange and emiratesAirLineInterchange and tramlinkInterchange and nationalRailInterchange !=None:
                bag23 = rdflib.BNode()
                g.add((bag20, Inter, bag23))
                if airportInterchange is not None:
                    g.add((bag23, Airport, Literal(airportInterchange)))
                    print('airportInterchange')
                    print(airportInterchange)
                if pierInterchange is not None:
                    g.add((bag23, Pier, Literal(pierInterchange)))
                if mainBusInterchange is not None:
                    g.add((bag23, Mainbus, Literal(mainBusInterchange)))
                if emiratesAirLineInterchange is not None:
                    g.add((bag23, Emirates_airlines, Literal(emiratesAirLineInterchange)))

                if tramlinkInterchange is not None:
                    g.add((bag23, National_rail, Literal(tramlinkInterchange)))

                if nationalRailInterchange is not None:
                    g.add((bag23, Tramlink, Literal(nationalRailInterchange)))

        for parents24 in parents20.findall(".//{ELRAD}Accessibility"):

            additionalAccessibilityInformation = parents24.find(".//{ELRAD}AdditionalAccessibilityInformation")
            if additionalAccessibilityInformation is not None:
                additionalAccessibilityInformation = additionalAccessibilityInformation.text

            blueBadgeCarParkSpaces = parents24.find(".//{ELRAD}BlueBadgeCarParkSpaces")
            if blueBadgeCarParkSpaces is not None:
                blueBadgeCarParkSpaces = blueBadgeCarParkSpaces.text

            taxiRanksOutsideStation = parents24.find(".//{ELRAD}TaxiRanksOutsideStation")
            if taxiRanksOutsideStation is not None:
                taxiRanksOutsideStation = taxiRanksOutsideStation.text

            accessibilityType = parents24.find(".//{ELRAD}AccessibilityType")
            if accessibilityType is not None:
                accessibilityType = accessibilityType.text

                bag24 = rdflib.BNode()
                g.add((bag20, Ac, bag24))
                if additionalAccessibilityInformation is not None:
                    g.add((bag24, Aditional_information, Literal(additionalAccessibilityInformation)))

                if blueBadgeCarParkSpaces is not None:
                    g.add((bag24, BlueBadgeCarParkSpaces, Literal(blueBadgeCarParkSpaces)))

                if taxiRanksOutsideStation is not None:
                    g.add((bag24, TaxiRanksOutsideStation, Literal(taxiRanksOutsideStation)))

                if accessibilityType is not None:
                    g.add((bag24, AccessibilityType, Literal(accessibilityType)))

            accessViaLift = parents24.find(".//{ELRAD}AccessViaLift")
            if accessViaLift is not None:
                accessViaLift = accessViaLift.text

            limitedCapacityLift = parents24.find(".//{ELRAD}LimitedCapacityLift")
            if limitedCapacityLift is not None:
                limitedCapacityLift = limitedCapacityLift.text

            if accessViaLift is not None:
                  g.add((bag24, AccessViaLift, Literal(accessViaLift)))

            if limitedCapacityLift is not None:
                g.add((bag24, LimitedCapacityLift, Literal(limitedCapacityLift)))

            accessibleToilet = parents24.find(".//{ELRAD}AccessibleToilet")
            if accessibleToilet is not None:
                accessibleToilet = accessibleToilet.text

            accessibleToiletNote = parents24.find(".//{ELRAD}AccessibleToiletNote")
            if accessibleToiletNote is not None:
                accessibleToiletNote = accessibleToiletNote.text

            if accessibleToilet is not None:
                g.add((bag24, AccessibleToilet, Literal(accessibleToilet)))

            if accessibleToiletNote is not None:
                g.add((bag24, AccessibleToiletNote, Literal(accessibleToiletNote)))

            specificEntranceRequired = parents24.find(".//{ELRAD}SpecificEntranceRequired")
            if specificEntranceRequired is not None:
                specificEntranceRequired = specificEntranceRequired.text

            specificEntranceInstructions = parents24.find(".//{ELRAD}SpecificEntranceInstructions")
            if specificEntranceInstructions is not None:
                specificEntranceInstructions = specificEntranceInstructions.text

            if specificEntranceRequired is not None:
                g.add((bag24, SpecificEntranceRequired, Literal(specificEntranceRequired)))

            if specificEntranceInstructions is not None:
                g.add((bag24, SpecificEntranceInstructions, Literal(specificEntranceInstructions)))


##La estación se encuentra solo en step-free:

estaciones2=[]

for parents30 in tree.findall("./{ELRAD}Station"):
    Name_4 = parents30.find(".//{ELRAD}StationName")
    name_4 = Name_4.text
    estaciones2.append(name_4)


for parents31 in tree.findall("stations/station"):
   Name_5 = parents31.find('.//name')
   name_5 = Name_5.text
   if name_5 not in estaciones2:

       bag30 = rdflib.BNode()

       ad = parents31.find('.//address')
       address = ad.text
       if address is not None:
           g.add((bag30, Adrress, Literal(address)))
           g.add((bag30, Name, Literal(name_5)))

       ph = parents31.find('.//phone')
       phone = ph.text
       if phone is not None:
           g.add((bag30, Phone, Literal(phone)))

       t = parents31.attrib
       id = t['id']
       type = t['type']
       if id is not None:
           g.add((bag30, id_station, Literal(id)))

       if type is not None:
           g.add((bag30, type_station, Literal(type)))

       for parents32 in parents31.findall(".//entrances/entrance"):

           name_entrance = parents32.find(".//name")
           if name_entrance is not None:
               name_entrance = name_entrance.text

           entranceToBookingHall = parents32.find(".//entranceToBookingHall")
           if entranceToBookingHall is not None:
               entranceToBookingHall = entranceToBookingHall.text

           bag31 = rdflib.BNode()
           g.add((bag30, Entrance, bag31))
           g.add((bag31, Entname, Literal(name_entrance)))
           g.add((bag31, EntranceToBookingHall, Literal(entranceToBookingHall)))

           for parents33 in parents32.findall(".//bookingHallToPlatform"):

               pointName = parents33.find(".//pointName")
               if pointName is not None:
                   pointName = pointName.text

               pathDescription = parents33.find(".//pathDescription")
               if pathDescription is not None:
                   pathDescription = pathDescription.text

               heading = parents33.find(".//pathDescription")
               if heading is not None:
                   heading = heading.text

               bag32 = rdflib.BNode()
               g.add((bag31, BookEnt, bag32))
               g.add((bag32, PointName, Literal(pointName)))
               g.add((bag32, PathDescription, Literal(pathDescription)))
               g.add((bag32, Heading, Literal(heading)))



           for parents34 in parents33.findall(".//platformToTrain"):

               trainName = parents34.find(".//trainName")
               if trainName is not None:
                   trainName = trainName.text

               platformToTrainSteps = parents34.find(".//platformToTrainSteps")
               if platformToTrainSteps is not None:
                   platformToTrainSteps = platformToTrainSteps.text

               bag33 = rdflib.BNode()
               g.add((bag31, Totraint, bag33))
               if trainName is not None:
                   g.add((bag33, TrainName, Literal(trainName)))
               if platformToTrainSteps is not None:
                   g.add((bag33, PlatformToTrainSteps, Literal(platformToTrainSteps)))

       for parents35 in parents31.findall(".//Placemark"):

           name_makr = parents35.find(".//name")
           if name_makr is not None:
               name_makr = name_makr.text

           descriptio = parents35.find(".//description")
           if descriptio is not None:
               descriptio = descriptio.text

           coordinates = parents35.find(".//coordinates")
           if coordinates is not None:
               coordinates = coordinates.text

           styleUrl = parents35.find(".//styleUrl")
           if styleUrl is not None:
               styleUrl = styleUrl.text

           if name_makr and descriptio and coordinates and styleUrl != None:
               bag34 = rdflib.BNode()
               g.add((bag30, Mark, bag34))
               if name_makr is not None:
                   g.add((bag34, PName, Literal(name_makr)))
               if descriptio is not None:
                   g.add((bag34, PDescripntion, Literal(descriptio)))
               if coordinates is not None:
                   g.add((bag34, PCoordinates, Literal(coordinates)))
               if styleUrl is not None:
                   g.add((bag34, PUrs_Styles, Literal(styleUrl)))

       for parents36 in parents31.findall(".//facilities"):

           ticket = parents36.find(".//facility")
           if ticket is not None:
               ticket = ticket.attrib['name']

           if ticket == "Ticket Halls":
               ticket = parents11.text

           else:
               ticket = None

           if ticket == "Help Points":
               help_Points = parents11.text
           else:
               help_Points = None

           if ticket == "Bridge":
               bridge = parents11.text
           else:
               bridge = None

           if ticket == "Vending Machines":
               vending_Machines = parents11.text
           else:
               vending_Machines = None

           if ticket == "Car park":
               car_park = parents11.text
           else:
               car_park = None

           if ticket == "Payphones":
               payphones = parents11.text
           else:
               payphones = None

           if ticket == "Cash Machines":
               cash_Machines = parents11.text
           else:
               cash_Machines = None

           if ticket == "Photo Booths":
               photo_Booths = parents11.text
           else:
               photo_Booths = None

           if ticket == "Toilets":
               toilets = parents11.text
           else:
               toilets = None

           if ticket == "Gates":
               gates = parents11.text
           else:
               gates = None

           if ticket == "Lifts":
               lifts = parents11.text
           else:
               lifts = None

           if ticket == "Escalators":
               escalators = parents11.text
           else:
               escalators = None

           if ticket == "Other Facilities":
               other_Facilities = parents11.text
           else:
               other_Facilities = None

           if ticket == " Waiting Room":
               waiting_Room = parents11.text
           else:
               waiting_Room = None


           bag35 = rdflib.BNode()
           g.add((bag30, facilitie, bag35))
           if waiting_Room is not None:
               g.add((bag35, Waiting_Room, Literal(waiting_Room)))
           if other_Facilities is not None:
               g.add((bag35, Other_Facilities, Literal(other_Facilities)))
           if lifts is not None:
               g.add((bag35, Lifts, Literal(lifts)))
           if escalators is not None:
               g.add((bag35, Escalators, Literal(escalators)))
           if gates is not None:
               g.add((bag35, Gates, Literal(gates)))
           if toilets is not None:
               g.add((bag35, Toilets, Literal(toilets)))
           if photo_Booths is not None:
               g.add((bag35, Photo_Booths, Literal(photo_Booths)))
           if cash_Machines is not None:
               g.add((bag35, Cash_Machines, Literal(cash_Machines)))
           if payphones is not None:
               g.add((bag35, Payphones, Literal(payphones)))
           if car_park is not None:
               g.add((bag35, Car_park, Literal(car_park)))
           if vending_Machines is not None:
               g.add((bag35, Vending_Machines, Literal(vending_Machines)))
           if bridge is not None:
               g.add((bag35, Bridge, Literal(bridge)))
           if help_Points is not None:
               g.add((bag35, Help_Points, Literal(help_Points)))

       for parents37 in parents31.findall(".//zones"):

           zone = parents37.find(".//zone")
           if zone is not None:
               zone = zone.text

           if zone is not None:
               bag36 = rdflib.BNode()
               g.add((bag30, zon, bag36))
               g.add((bag36, Zone, Literal(zone)))

       for parents38 in parents31.findall(".//servingLines"):

           servingLine = parents38.find(".//servingLine")
           if servingLine is not None:
               servingLine = servingLine.text

           if servingLine is not None:
               bag37 = rdflib.BNode()
               g.add((bag30, seline, bag37))
               g.add((bag37, ServingLine, Literal(servingLine)))

g.serialize(destination ="rdf.xml", format = "xml")