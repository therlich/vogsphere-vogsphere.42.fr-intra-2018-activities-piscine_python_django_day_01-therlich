def execute():
	states = {
	"Oregon" : "OR",
	"Alabama" : "AL",
	"New Jersey": "NJ",
	"Colorado" : "CO"
	}
	capital_cities = {
	"OR": "Salem",
	"AL": "Montgomery",
	"NJ": "Trenton",
	"CO": "Denver"
	}

	reverse_states={}
	for state in states:
		reverse_states[states[state]]=state

	reverse_capital_cities={}
	for city in capital_cities:
		reverse_capital_cities[capital_cities[city]]=city


	import sys
	if len(sys.argv)!=2:
		return

	if sys.argv[1] not in reverse_capital_cities:
		print ("Unknown capital city")
		return
	else:
		print (reverse_states[reverse_capital_cities[sys.argv[1]]])



if __name__=="__main__":
	execute()