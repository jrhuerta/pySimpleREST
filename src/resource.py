__author__ = 'jrhuerta'

from flask_restful import Resource


class Collection(Resource):

    def get(self, **kwargs):
        pass

    def post(self, **kwargs):
        pass


class Scalar(Resource):

    def get(self, pk):
        pass

    def put(self, pk):
        pass

    def delete(self, pk):
        pass


#api.add_resource(TodoSimple, '/<string:todo_id>')