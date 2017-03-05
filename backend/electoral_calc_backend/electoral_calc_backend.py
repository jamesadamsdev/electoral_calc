'''
Documentation, License etc.

@package electoral_calc_backend
'''

import flask
APP = flask.Flask(__name__)

@APP.route('/ping')
def hello_world():
    return "Hello world"

if __name__ == '__main__':
    APP.run()
