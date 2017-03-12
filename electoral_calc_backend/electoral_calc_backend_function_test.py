from electoral_calc_backend import _dhondt, _sainte_lague, _imperiali

def main():
    print("D'Hondt method tests")
    
    print(_dhondt(500, 200, 0, ([
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
    ])))
        
    # Taken from the wikipedia article on the D'Hondt method
    print(_dhondt(230000, 8, 0, ([
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
    ])))  
        
    print(_dhondt(230000, 8, 20, ([
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
        	"Votes": 30000
        	
        },
        {
        	"PartyName":"D",
        	"Votes": 10000
        	
        }
    ])))  
        
    print("Sainte-Laguë method tests")
    
    print(_sainte_lague(500, 200, 0, ([
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
    ])))
        
    print(_sainte_lague(100000, 7, 0, ([
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
    ])))
        
    print("Imperiali method tests")
    
    print(_imperiali(500, 200, 0, ([
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
    ])))
        
    print(_imperiali(100000, 7, 0, ([
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
    ])))
    


if __name__ == '__main__':
    main()
