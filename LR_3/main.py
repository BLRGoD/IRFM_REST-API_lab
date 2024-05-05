from flask import Flask
from flask_restful import Api, Resource, reqparse
import pandas as pd
import sqlite3
from Lab_2_methods import select_from_table, delete_from_table, insert_into_table, houses_sold_sum

app = Flask(__name__)
api = Api()

class Single_line_op(Resource):

    def get(self, table_name, line_id):
        return select_from_table('house_data.db',table_name).get(line_id)
    
    def delete(self, table_name, line_id):
        delete_from_table('house_data.db',table_name, line_id)
    


class Table_op(Resource):
    def get(self, table_name):
        return select_from_table('house_data.db',table_name) 
    
    def post(self, table_name):
        parser = reqparse.RequestParser()
        parser.add_argument("id",type=int)
        parser.add_argument("date",type=str)
        parser.add_argument("price",type=float)
        parser.add_argument("yr_built",type=int)
        parser.add_argument("yr_renovated",type=int)
        parser.add_argument("sqft_living",type=int)
        parser.add_argument("condition",type=int)
        parser.add_argument("real_year",type=int)
        args = parser.parse_args()
        new_line = pd.DataFrame(args,index=[0])
        insert_into_table('house_data.db', table_name, new_line)

class Task_F_class(Resource):
    def get(self, table_name, year, month):
        return houses_sold_sum('house_data.db',table_name, year, month)     


api.add_resource(Table_op, "/api/main/<string:table_name>/", endpoint="get_table")
api.add_resource(Single_line_op, "/api/main/<string:table_name>/<int:line_id>/", endpoint="single_line_op")
api.add_resource(Task_F_class, "/api/main/<string:table_name>/<int:year>/<int:month>/", endpoint="task_F_class")

api.init_app(app)

if __name__ =="__main__":
    app.run(debug=True, port=3000, host="localhost")