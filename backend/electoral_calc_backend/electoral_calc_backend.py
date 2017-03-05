'''
Documentation, License etc.

@package electoral_calc_backend
'''

from flask import Flask, request, abort
from operator import itemgetter
from collections import Counter
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
    # The list of possible counting methods and associated python functions are in the methods.json file.
    # The logic will check the specified method in the request against the file to get the proper function.
    config_file = open("methods.json")
        
    config = json.loads(config_file.read())
    
    if request.method == 'GET':
        return """
Provide this json in request:
{
    "CountMethod": <one of """ + str(list(config.keys())).replace("[", "").replace("]","") + """>,
    "TotalVotes": <int>,
    "NumberOfSeats": <int>,
    ["Threshold":<int>,]
    "PartyVotes": 
    [
        {
            "PartyName":"<Party1>",
            "Votes": <int>
        },
        {
            "PartyName":"<Party2>",
            "Votes": <int>
        },
        ...
        {
            "PartyName":"<PartyN>",
            "Votes": <int>
        },
    ]
}

Response:
{
    "PartySeats": 
    [
        {
            "PartyName":"<Party1>",
            "Seats": <int>
        },
        {
            "PartyName":"<Party2>",
            "Seats": <int>
        },
        ...
        {
            "PartyName":"<PartyN>",
            "Seats": <int>
        }
    ]
    "UnassignedSeats": <int>
}
"""
    if request.method == 'POST':
        
        data = json.loads(request.data)
        
        _verify_calculate_data(data)
        
        # Threshold is optional, but to simplify calculation, set it to 0 if not in request
        if "Threshold" not in data.keys():
            data["Threshold"] = 0
        
        method = data["CountMethod"]
        
        if(method not in config.keys()):
            abort(403)
        
        return json.dumps(globals()[config[method]](data["TotalVotes"], data["NumberOfSeats"], data["Threshold"], data["PartyVotes"])), 200
        
    abort(404)  
    
 
def _verify_calculate_data(data):
    if "CountMethod" not in data.keys() or "TotalVotes" not in data.keys() or "NumberOfSeats" not in data.keys() or "PartyVotes" not in data.keys():
        abort(403)
    

def _dhondt(total_votes, number_of_seats, threshold, party_votes):
    
    vote_list = []

    for party in party_votes:
        party_name = party["PartyName"]
        votes = party["Votes"]
        
        # Ensure party got enough votes, according to the threshold
        if(votes > (threshold / 100) * total_votes):
            initial_divisor = 1
            
            for i in range(0, number_of_seats):
                vote_list.append({"PartyName": party_name, "DividedVotes": votes / (initial_divisor + i)})
    
    vote_list = sorted(vote_list, key=itemgetter('DividedVotes'), reverse=True)[:number_of_seats] 
    
    c = Counter([p["PartyName"] for p in vote_list])
    
    res = {"PartySeats":[],"UnassignedSeats":0}
    
    unassigned_seats = number_of_seats
    
    for party in party_votes:
        party_name = party["PartyName"]
        
        unassigned_seats -= c[party_name]
        
        res["PartySeats"].append({"PartyName": party_name, "Seats": c[party_name]})
        
    res["UnassignedSeats"] = unassigned_seats
    
    return res
                        

if __name__ == '__main__':
    APP.run()
