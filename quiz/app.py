import json
import readJson

from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from werkzeug.middleware.proxy_fix import ProxyFix

from flask_basicauth import BasicAuth


app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = 'admin'
app.config['BASIC_AUTH_PASSWORD'] = 'admin'
basic_auth = BasicAuth(app)

app.wsgi_app = ProxyFix(app.wsgi_app)

api = Api(app, version='1.0', title='Quiz Food Provider',
          description='Food',
          )

ns = api.namespace('Food', description='Manage Food System')

task_model = api.model('Task', {
    'Name': fields.String(required=True, description='The task details')
})

@ns.route('/<string:afood>')
class infofood(Resource):
    @ns.doc('list_tasks')
    
    def get(self,afood):
        x = readJson.showitem()
        for i in x :
            if i['Name'].upper() == afood.upper():
                return i
 
@ns.route('/<int:bfood>')
class calfood(Resource):
    @ns.doc('list_tasks')
    
    def get(self,bfood):
        x = readJson.showitem()
        xfood = []
        for i in x :
            if i['Kilocalories'] < bfood:
                xfood.append({"name":i['Name'],"kilocalories":i['Kilocalories']})
        return xfood

@ns.route('/BMR')
class bmr(Resource):
    @ns.doc('list_tasks')
    
    def post(self):
        weight = api.payload["weight"]
        height = api.payload["height"]
        age = api.payload["age"]
        sum = (((10*weight)+(6.25*height))-(5*age)) + 5
        xbmr = [{"BMR": sum}]
        return xbmr

@ns.route('/')
class delete(Resource):
    @basic_auth.required
    @ns.doc('list_tasks')
    def delete(self):
        xdel = api.payload["Name"].upper()
        status = readJson.deleteitem(xdel)
        if status == 200:
            resultdelete = [{"data delete" : "DATA DELETED"}]
        else:
            resultdelete = [{"data delete" : "DELETE FAILED"}]
        return resultdelete

@ns.route('/')
class add(Resource):
    @basic_auth.required
    @ns.doc('list_tasks')
    def post(self):
        xadd = api.payload
        add = readJson.additem(xadd)
        if add == 200:
            resultadd = [{"data delete" : "DATA ADDED"}]
        else:
            resultadd = [{"data delete" : "ADD FAILED"}]
        return resultadd

@ns.route('/<string:foodnameupdate>')
class update(Resource):
    @basic_auth.required
    @ns.doc('list_tasks')
    def put(self):
        xname =  foodnameupdate.upper()
        xupdate = api.payload
        update = readJson.updateitem(xname,xupdate)
        if update == 200:
            resultupdate = [{"data delete" : "DATA UPDATED"}]
        else:
            resultupdate = [{"data delete" : "UPDATE FAILED"}]
        return resultupdate