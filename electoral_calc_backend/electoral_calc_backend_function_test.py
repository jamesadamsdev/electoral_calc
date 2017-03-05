from electoral_calc_backend import _dhondt

def main():
    
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


if __name__ == '__main__':
    main()
