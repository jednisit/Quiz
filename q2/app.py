from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from werkzeug.middleware.proxy_fix import ProxyFix
import json
import readjson
from flask_basicauth import BasicAuth

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'admin'
app.config['BASIC_AUTH_PASSWORD'] = 'admin'
app.wsgi_app = ProxyFix(app.wsgi_app)
basic_auth = BasicAuth(app)
api = Api(app, version='1.0', title='FoodandCalories',
          description='For healt',
          )

ns = api.namespace('Food', description='For healt')

task_model = api.model('FoodData', {
    'Name': fields.String(readonly=True, description='Name of food'),
    'Kilocalories': fields.Integer(required=True, description='Calories of food'),
    'Alpha-Carotene':fields.Integer(required=True, description='Alpha-Caroteen of food'),
    'Beta-Carotene':fields.Integer(required=True, description='Beta-Caroteen of food'),
    'Carbohydrate':fields.Integer(required=True, description='Carbohydrate of food'),
    'Cholesterol':fields.Integer(required=True, description='Cholesterol of food'),
    'Choline':fields.Integer(required=True, description='Choline of food'),
    'Fiber':fields.Integer(required=True, description='Fiber of food'),
    'Lycopene':fields.Integer(required=True, description='Lycopene of food'),
    'Manganese':fields.Integer(required=True, description='Manganese of food'),
    'Protein':fields.Integer(required=True, description='Protein of food'),
    'Selenium':fields.Integer(required=True, description='Selenium of food'),
    'Sugar-Total':fields.Integer(required=True, description='Sugar-Total of food'),
    'Zinc':fields.Integer(required=True, description='Zinc of food'),
    'Vitamin-B12':fields.Integer(required=True, description='Vitamin-B12 of food'),
    'Vitamin-B6':fields.Integer(required=True, description='Vitamin-B6 of food'),
    'Vitamin-C':fields.Integer(required=True, description='Vitamin-C of food'),
    'Vitamin-E':fields.Integer(required=True, description='Vitamin-E of food'),
    'Vitamin-K':fields.Integer(required=True, description='Vitamin-K of food')
})

task_model2 = api.model('FoodDataCal', {
    'Name': fields.String(readonly=True, description='Name of food'),
    'Kilocalories': fields.Integer(required=True, description='Calories of food'),
})

task_model3 = api.model('BMR', {
    'Your BMR': fields.Integer(readonly=True, description='BMR')
})

task_model4 = api.model('Message', {
    'Message': fields.String(readonly=True, description='error Message')
})


data = readjson.read()

@ns.route('/<string:name>')
class Foodtracking(Resource):
    @ns.doc('list_tasks')
    @ns.marshal_list_with(task_model)
    def get(self,name):
        for t in data:
            if t['Name'].upper()==name.upper():
                return t
    
    @basic_auth.required
    @ns.marshal_list_with(task_model4)
    def put(self,name):
        data = api.payload
        check=readjson.up(name.upper(),data)
        task=[]
        if check == 200:
            task.append({"Message":"Update Complete"})
        elif check == 400:
            task.append({"Message":"NotFound"})
        return task

@ns.route('/<int:cal>')
class Caltracking(Resource):
    @ns.doc('list_tasks')
    @ns.marshal_list_with(task_model2)
    def get(self,cal):
        task=[]
        for t in data:
            if t['Kilocalories']<cal:
                task.append({'Name':t['Name'],'Kilocalories':t['Kilocalories']})
        return task

@ns.route('/BMR')
class TodoList(Resource):
    @ns.doc('list_tasks')
    @ns.expect(task_model3)
    @ns.marshal_with(task_model3, code=201)
    def post(self):
        weight = api.payload['weight']
        height = api.payload['height']
        age = api.payload['age']
        sum = (((10*weight)+(6.25*height))-5*age)+5
        task = [{'Your BMR':sum}]
        return task

@ns.route('/')
@ns.response(404, 'Todo not found')
class adminfun(Resource):
    @basic_auth.required
    @ns.doc('delete_task')
    @ns.response(204, 'Task deleted')
    @ns.marshal_list_with(task_model4)
    def delete(self):
        name = api.payload['Name']
        check = readjson.dele(name.upper())
        task=[]
        if check == 200:
            task.append({"Message":"Delete Complete"})
        elif check == 400:
            task.append({"Message":"NotFound"})
        return check

    @basic_auth.required
    @ns.response(204, 'Task add')
    @ns.marshal_list_with(task_model4)
    def post(self):
        check = readjson.add2(api.payload)
        task=[]
        if check == 200:
            task.append({"Message":"Add Complete"})
        elif check == 400:
            task.append({"Message":"NotFound"})
        
        return task
    

