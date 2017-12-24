import unittest
from electoral_calc_backend import _dhondt, _sainte_lague, _imperiali

class CalcTestFixture(unittest.TestCase):
    def test_dhondt(self): 
        
        dhondt_test_values = [[500, 200, 0, [
            {
                "PartyName":"GOP",
                "Votes": 200
                
            },
            {
                "PartyName":"Dem",
                "Votes": 200
                
            },
            {
                "PartyName":"Green",
                "Votes": 100
                
            }
        ], {'PartySeats': [{'PartyName': 'GOP', 'Seats': 80}, {'PartyName': 'Dem', 'Seats': 80}, {'PartyName': 'Green', 'Seats': 40}], 'UnassignedSeats': 0}],
                [230000, 8, 0, [
            {
                "PartyName":"A",
                "Votes": 100000
                
            },
            {
                "PartyName":"B",
                "Votes": 80000
                
            },
            {
                "PartyName":"C",
                "Votes": 30000
                
            },
            {
                "PartyName":"D",
                "Votes": 20000
                
            }
        ], {'PartySeats': [{'PartyName': 'A', 'Seats': 4}, {'PartyName': 'B', 'Seats': 3}, {'PartyName': 'C', 'Seats': 1}, {'PartyName': 'D', 'Seats': 0}], 'UnassignedSeats': 0}
],
                [230000, 8, 0, [
            {
                "PartyName":"A",
                "Votes": 100000
                
            },
            {
                "PartyName":"B",
                "Votes": 90000
                
            },
            {
                "PartyName":"C",
                "Votes": 20000
                
            },
            {
                "PartyName":"D",
                "Votes": 20000
                
            }
        ],{'PartySeats': [{'PartyName': 'A', 'Seats': 4}, {'PartyName': 'B', 'Seats': 4}, {'PartyName': 'C', 'Seats': 0}, {'PartyName': 'D', 'Seats': 0}], 'UnassignedSeats': 0}]]
        
        for value in dhondt_test_values :
            result = _dhondt(value[0], value[1], value[2], value[3])
            self.assertEqual(result, value[4])


    def test_sainte_lague(self): 
        
        sainte_lague_test_values = [[500, 200, 0, [
        {
        	"PartyName":"GOP",
        	"Votes": 200
        	
        },
        {
        	"PartyName":"Dem",
        	"Votes": 200
        	
        },
        {
        	"PartyName":"Green",
        	"Votes": 100
        	
        }
        ], {'PartySeats': [{'PartyName': 'GOP', 'Seats': 80}, {'PartyName': 'Dem', 'Seats': 80}, {'PartyName': 'Green', 'Seats': 40}], 'UnassignedSeats': 0}],
                [100000, 7, 0, [
        {
        	"PartyName":"A",
        	"Votes": 53000
        	
        },
        {
        	"PartyName":"B",
        	"Votes": 24000
        	
        },
        {
        	"PartyName":"C",
        	"Votes": 23000
        	
        }
    ], {'PartySeats': [{'PartyName': 'A', 'Seats': 3}, {'PartyName': 'B', 'Seats': 2}, {'PartyName': 'C', 'Seats': 2}], 'UnassignedSeats': 0}]]
        
        for value in sainte_lague_test_values :
            result = _sainte_lague(value[0], value[1], value[2], value[3])
            self.assertEqual(result, value[4])

    
    def test_imperiali(self): 
        
        imperiali_test_values = [[500, 200, 0, [
        {
        	"PartyName":"GOP",
        	"Votes": 200
        	
        },
        {
        	"PartyName":"Dem",
        	"Votes": 200
        	
        },
        {
        	"PartyName":"Green",
        	"Votes": 100
        	
        }
    ], {'PartySeats': [{'PartyName': 'GOP', 'Seats': 80}, {'PartyName': 'Dem', 'Seats': 80}, {'PartyName': 'Green', 'Seats': 40}], 'UnassignedSeats': 0}],
                [100000, 7, 0, [
        {
        	"PartyName":"A",
        	"Votes": 53000
        	
        },
        {
        	"PartyName":"B",
        	"Votes": 24000
        	
        },
        {
        	"PartyName":"C",
        	"Votes": 23000
        	
        }
    ], {'PartySeats': [{'PartyName': 'A', 'Seats': 5}, {'PartyName': 'B', 'Seats': 1}, {'PartyName': 'C', 'Seats': 1}], 'UnassignedSeats': 0}
]]
        
        for value in imperiali_test_values :
            result = _imperiali(value[0], value[1], value[2], value[3])
            self.assertEqual(result, value[4])


if __name__ == '__main__':
    unittest.main()
