from flask import Flask
from flask_restful import Api, Resource
import pandas as pd
import sqlite3
from Lab_2_methods import select_from_table, delete_from_table

app = Flask(__name__)
api = Api()

class Single_line_op(Resource):

    def get(self, table_name, line_id):
        return select_from_table('house_data.db',table_name).get(line_id)
    
    def delete(self, table_name, line_id):
        delete_from_table('house_data.db',table_name, line_id)


class Get_table(Resource):
    def get(self, table_name):
        return select_from_table('house_data.db',table_name) 

api.add_resource(Get_table, "/api/main/<string:table_name>/", endpoint="get_table")
api.add_resource(Single_line_op, "/api/main/<string:table_name>/<int:line_id>/", endpoint="single_line_op")


api.init_app(app)

if __name__ =="__main__":
    app.run(debug=True, port=3000, host="localhost")