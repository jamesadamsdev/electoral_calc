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
    <<<Optional>>>"Threshold":<int>,
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
    """
    Here's how the D'Hondt method works: 
    for each party, take the number of votes, and create a list of numbers, starting with the original number,
    then that number divided by 2, then 3, all the way until it's divided by the number of available seats.
    For those n seats, find the highest n numbers throughout the parties' lists, giving that party a seat 
    if a number comes from their list.
    
    Since a couple other methods use similar systems, the actual implementation is in the _highest_averages function below.
    """
    return _highest_averages(total_votes, number_of_seats, threshold, party_votes, 1, 1)


def _sainte_lague(total_votes, number_of_seats, threshold, party_votes):
    """
    Similar to the D'Hondt method, but divides by 1, 3, 7... instead.
    """
    return _highest_averages(total_votes, number_of_seats, threshold, party_votes, 1, 2)

def _imperiali(total_votes, number_of_seats, threshold, party_votes):
    """
    Similar to the D'Hondt method, but divides by 2, 3, 4... instead.
    """
    return _highest_averages(total_votes, number_of_seats, threshold, party_votes, 2, 1)

# TODO: Figure out how to handle tied values
def _highest_averages(total_votes, number_of_seats, threshold, party_votes, initial_divisor, increment):
    """
    Runs the highest averages formula.
    
    Args:
    total_votes: How many votes were cast.
    number_of_seats: How many seats to be allocated.
    threshold: Parties that didn't get more than threshold % aren't counted.
    party votes: 
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
    initial_divisor: Start at this number when calculating each parties' divided vote list
    increment: Increment by this number each time when calculating each parties' divided vote list
    """
    
    # Create a list of { "PartyName":"<name>", "DividedVotes":votes }
    vote_list = []
    
    for party in party_votes:
        party_name = party["PartyName"]
        votes = party["Votes"]
        
        # Ensure party got enough votes, according to the threshold
        if(votes > (threshold / 100) * total_votes):
            
            for i in range(0, number_of_seats):
                vote_list.append({"PartyName": party_name, "DividedVotes": votes / (initial_divisor + (increment * i))})
    
    # Sort the divided vote list by DividedVotes descending and take the top number_of_seat elements
    vote_list = sorted(vote_list, key=itemgetter('DividedVotes'), reverse=True)[:number_of_seats] 
    
    # Generate the response by counting how many times each party is on the list of highest DividedVotes,
    # then adding UnassignedSeats, if any
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
