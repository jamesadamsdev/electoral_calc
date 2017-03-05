'''
Documentation, License etc.

@package electoral_calc_backend
'''

from flask import Flask, request, abort
import json, logging
APP = Flask(__name__)


@APP.route('/ping')
def hello_world():
    """
    A simple ping endpoint
    Returns:
    A short message and 200
    """
    return "Hello world", 200


@APP.route('/calculate', methods=['GET', 'POST'])
def calculate():
    config_file = open("methods.json")
        
    config = json.loads(config_file.read())
    
    if request.method == 'GET':
        return """
Provide this json in request:
{
    "CountMethod": <one of """ + str(list(config.keys())) + """>,
    "TotalVotes": <int>,
    "NumberOfSeats": <int>,
    "PartyVotes": 
    [
        {"<Party1>": <int>},
        {"<Party2>": <int>},
        ...
        {"<PartyN>": <int>}
    ]
}
"""
    if request.method == 'POST':
        
        data = json.loads(request.data)
        
        _verify_calculate_data(data)
        
        method = data["CountMethod"]
        
        if(method not in config.keys()):
            abort(403)
        
        return globals()[config[method]](data["TotalVotes"], data["NumberOfSeats"], data["PartyVotes"]), 200
        
    abort(404)  
    
 
def _verify_calculate_data(data):
    if "CountMethod" not in data.keys() or "TotalVotes" not in data.keys() or "NumberOfSeats" not in data.keys() or "PartyVotes" not in data.keys():
        abort(403)
    

def _dhondt(total_votes, number_of_seats, party_votes):
    return "hi"
                        

if __name__ == '__main__':
    APP.run()
