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

	state_to_city={}
	for state in states:
		state_to_city[(state.strip()).lower()]=(capital_cities[states[state]].strip()).lower()

	city_to_state={}
	for state in state_to_city:
		city_to_state[(state_to_city[state].strip()).lower()]=(state.strip()).lower()

	state_conversion={}
	for state in states:
		state_conversion[(state.strip()).lower()]=state

	city_conversion={}
	for item in capital_cities:
		city_conversion[(capital_cities[item].strip()).lower()]=capital_cities[item]

	import sys

	if len(sys.argv)==1:
		return

	string_list=(sys.argv[1]).split(',')

	new_list=[]

	for item in string_list:
		item=(item.strip()).lower()
		if item!="":
			new_list.append(item)


	for item in new_list:
		if item in city_to_state:
			result=state_conversion[city_to_state[item]]
			print ("{} is the capital of {}".format(city_conversion[item],result))

		elif item in state_to_city:
			result=city_conversion[state_to_city[item]]
			print ("{} is the capital of {}".format(result,state_conversion[item]))

		else:
			print ("{} is neither a capital city nor a state".format(item))





if __name__=="__main__":
	execute()