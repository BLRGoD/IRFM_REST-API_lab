from flask import Flask
from flask_restful import Api, Resource, reqparse
import pandas as pd
import sqlite3
from Lab_2_methods import select_from_table, delete_from_table, insert_into_table

app = Flask(__name__)
api = Api()

class Single_line_op(Resource):

    def get(self, table_name, line_id):
        return select_from_table('house_data.db',table_name).get(line_id)
    
    def delete(self, table_name, line_id):
        delete_from_table('house_data.db',table_name, line_id)

    # def put(self, table_name, line_id):
        



class Table_op(Resource):
    def get(self, table_name):
        return select_from_table('house_data.db',table_name) 
    
    def post(self, table_name):
        parser = reqparse.RequestParser()
        parser.add_argument("id",type=int)
        parser.add_argument("date",type=str)
        parser.add_argument("price",type=int)
        parser.add_argument("yr_built",type=int)
        parser.add_argument("yr_renovated",type=int)
        parser.add_argument("sqft_living",type=int)
        parser.add_argument("condition",type=int)
        parser.add_argument("real_year",type=int)

        args = parser.parse_args()
        args_dict = vars(args)
        new_line = pd.DataFrame(args_dict,index=[0])
        
        insert_into_table('house_data.db', table_name, new_line)


api.add_resource(Table_op, "/api/main/<string:table_name>/", endpoint="get_table")
api.add_resource(Single_line_op, "/api/main/<string:table_name>/<int:line_id>/", endpoint="single_line_op")


api.init_app(app)

if __name__ =="__main__":
    app.run(debug=True, port=3000, host="localhost")