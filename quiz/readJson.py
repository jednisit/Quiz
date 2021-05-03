import json

open_file = open("food_db.json", "r")
read_file = open_file.read()
json_object = json.loads(read_file)




def showitem():
    return json_object

def deleteitem(foodnamefordel):
    open_file = open("food_db.json", "w")
    for recieve in enumerate(json_object):
        if recieve['Name'].upper() == foodnamefordel.upper():
            json_object.remove(recieve)
            json.dump(json_object,open_file)
            return 200
    return 500

#def additem(foodnameforadd):
#    open_file = open("food_db.json", "w")
#    for address,recieve in enumerate(json_object):
#       if [recieve.keys()] == [foodnameforadd.keys()]:
#           return 400
#       else:
#           json_object.append(foodnameforadd)
#           json.dump(json_object,open_file)
#           return 200

def additem(foodnameforadd):
    open_file = open("food_db.json", "w")
    json_object.append(foodnameforadd)
    json.dump(json_object,open_file)
    return 200
    
def updateitem(checkfood,foodnameforupdate):
    open_file = open("food_db.json", "w")
    for count,i in enumerate(json_object):
        if i["Name"].upper() == checkfood.upper():
            json_object[count].update(foodnameforupdate)
            json.dump(json_object,open_file)
            return 200
    return 400
