from flask import Flask,request
import os
import random
import json
data = 'data/data.json'

app = Flask(__name__)
#############class and other defenitions#################

class employee:
    def __init__(self,id,name,city):
        self.empid = str(id)
        self.name = name
        self.city = city



##########################end#############################


@app.route("/greeting",methods=['GET'])
def greeting():
    return {'code':200,'content':'Hello World!'}

@app.route('/employee',methods=['POST'])
def add_emp():
    if os.path.exists(data):
        with open(data) as json_file:
            emp_collection = json.load(json_file)
    else:
        emp_collection = {}

    id = str(random.randrange(1000,5000))
    name = request.json.get("name")
    city = request.json.get("city")
    print(name,city)
    emp_collection[id] = employee(id,name,city).__dict__

    with open(data,"w") as outfile:
        json.dump(emp_collection,outfile)

    return {'code':200,'employeeId':emp_collection[id]["empid"]}

    print(emp_collection[id])

@app.route('/employee/<id>',methods=['GET','PUT','DELETE'])
def get_one(id):
    if os.path.exists(data):
            with open(data) as json_file:
                emp_collection = json.load(json_file)
    else:
        return{'code':401,'message':'there are no data'}
    
    if request.method == 'PUT':
        id = str(id)
        name = request.json.get("name")
        city = request.json.get("city")

        emp_collection[id] = employee(id,name,city).__dict__

        with open(data,"w") as outfile:
            json.dump(emp_collection,outfile)

        return {'code':201,'Content':emp_collection[id]}

    elif request.method == 'GET':
        id = str(id)
        try:
            emp = emp_collection[id]
            print(emp)
            return {'code':200,'Content':emp_collection[id]}
        except:
            print(id)
            for x in emp_collection:
                print(type(x))
            #print(emp_collection[id])
            return {'code':404,'message':"Employee with {} is not found".format(id)}
        
    else:
        id = str(id)
        try:
            emp = emp_collection[id]
            del emp_collection[id]
            return {'code':200,'Content':emp[id]}
        except:
            return {'code':404,'message':"Employee with {} is not found".format(id)}

@app.route('/employees/all',methods=['GET'])
def getall():
    if os.path.exists(data):
        with open(data) as jsonfile:
            emp_collection = json.load(jsonfile)
    else:
        return {'code':401,'message':'not avilable'}
    
    try:
        return {'code':200,'Content':emp_collection}
    except:
        return {'code':404,'message':"empty list"}




if __name__ == '__main__':
    app.run()

