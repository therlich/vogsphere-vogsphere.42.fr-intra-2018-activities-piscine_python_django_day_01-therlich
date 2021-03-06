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

	import sys
	if len(sys.argv)!=2:
		return

	if sys.argv[1] not in states:
		print ("Unknown state")
		return
	else:
		print (capital_cities[states[sys.argv[1]]])



if __name__=="__main__":
	execute()