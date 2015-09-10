__author__ = 'jrhuerta'

import arrow
from functools import partial
from flask_restful import Resource, reqparse
from sqlalchemy import Integer, Float, Unicode, DateTime, Boolean
from sqlalchemy.inspection import inspect

__all__ = ['create_parser']


_safe_caster = lambda t, v: t(v) if v is not None else None

_default_map = {
    map_type: partial(_safe_caster, mapped_type)
    for map_type, mapped_type in [
        (Integer, int),
        (Float, float),
        (Unicode, unicode),
        (DateTime, lambda x: arrow.get(x).datetime),
        (Boolean, bool)
    ]
}


def _default_type_mapper(type_):
    if type_ not in _default_map:
        raise TypeError('No type map found for %s' % type_)
    return _default_map.get(type_)


def create_parser(entity, type_mapper=None):
    type_mapper = type_mapper or _default_type_mapper

    meta = inspect(entity)
    if not meta:
        raise RuntimeError('%s does not correspond to a inspected type.')

    parser = reqparse.RequestParser()
    for attribute in meta.attrs:
        column = getattr(meta.columns, attribute.key)
        parser.add_argument(attribute.key,
                            type=type_mapper(column.type.__class__),
                            required=False)
    return parser


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