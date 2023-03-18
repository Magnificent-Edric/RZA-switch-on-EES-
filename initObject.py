import classSources.classObject as classObject
import json

def createTR():
    trDict = {}
    with open("components/trData.json", "r") as my_file:
        tr_json = my_file.read()
    tr = json.loads(tr_json)
    for key in tr:
        trDict[key] = classObject.Transfomator(tr[key]['name'], 
                                               tr[key]['cVolt'], 
                                               tr[key]['number'],
                                               tr[key]['switch'])
    return trDict

def createLine():
    lineDict = {}
    with open("components/lineData.json", "r") as my_file:
        line_json = my_file.read()
    line = json.loads(line_json)
    for key in line:
        lineDict[key] = classObject.LineTransport(line[key]['name'], 
                                                  line[key]['cVolt'], 
                                                  line[key]['number'],
                                                  line[key]['switch'])
    return lineDict

def createBus():
    busDict = {}
    with open("components/busData.json", "r") as my_file:
        bus_json = my_file.read()
    bus = json.loads(bus_json)
    for key in bus:
        busDict[key] = classObject.Bus(bus[key]['name'], 
                                        bus[key]['cVolt'], 
                                        bus[key]['number'],
                                        bus[key]['switch'])
    return busDict

def createProtection():
    with open("components/protection.json", "r") as my_file:
        protection_json = my_file.read()
    return json.loads(protection_json)