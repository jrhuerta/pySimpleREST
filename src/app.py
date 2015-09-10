#!/usr/bin/env python
__author__ = 'jrhuerta'

from flask import Flask
from flask_restful import Api

from entities import Post
from resource import create_parser

p = create_parser(Post)

app = Flask(__name__)
api = Api(app)


if __name__ == '__main__':
    app.run()
