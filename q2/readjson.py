import json


a_file = open("food_db.json","r")
k=a_file.read()
json_object = json.loads(k)

def read():
    return json_object

def up(name,data):
    a_file = open("food_db.json","w")
    for count,i in enumerate(json_object):
        if i["Name"].upper()==name:
            for update_item in list(data.keys()):
                if update_item not in list(i.keys()):
                    return 400
                
            json_object[count].update(data)
            json.dump(json_object,a_file)
            return 200

def dele(name):
    a_file = open("food_db.json","w")
    for count,i in enumerate(json_object):
        if i["Name"].upper()==name.upper():
            json_object.remove(i)
            json.dump(json_object, a_file)
            return 200
        return 400 


# def add(name,cal,alpha,beta,carbo,choles,cho,fib,lyco,manga,pro,sele,sug,zin,b12,b6,c,e,k):
#     a_file = open("food_db.json","w")
#     for count,i in enumerate(json_object):
#         json_object.append({
#     'Name': name,
#     'Kilocalories': cal,
#     'Alpha-Carotene': alpha,
#     'Beta-Carotene':beta,
#     'Carbohydrate':carbo,
#     'Cholesterol':choles,
#     'Choline':cho,
#     'Fiber':fib,
#     'Lycopene':lyco,
#     'Manganese':manga,
#     'Protein':pro,
#     'Selenium':sele,
#     'Sugar-Total':sug,
#     'Zinc':zin,
#     'Vitamin-B12':b12,
#     'Vitamin-B6':b6,
#     'Vitamin-C':c,
#     'Vitamin-E':e,
#     'Vitamin-K':k
# })
#         json.dump(json_object, a_file)
#         return ("x")

def add2(data):
    for count,i in enumerate(json_object):
        if [i.keys()]==[data.keys()]:
            return 400
        else:
            json_object.append(data)
            a_file = open("food_db.json","w")
            json.dump(json_object, a_file)
            return 200