def getKey(couple):
	return [couple[0], couple[1]]

def execute():
	d = {
	'Hendrix' : '1942',
	'Allman' : '1946',
	'King' : '1925',
	'Clapton' : '1945',
	'Johnson' : '1911',
	'Berry' : '1926',
	'Vaughan' : '1954',
	'Cooder' : '1947',
	'Page' : '1944',
	'Richards' : '1943',
	'Hammett' : '1962',
	'Cobain' : '1967',
	'Garcia' : '1942',
	'Beck' : '1944',
	'Santana' : '1947',
	'Ramone' : '1948',
	'White' : '1975',
	'Frusciante': '1970',
	'Thompson' : '1949',
	'Burton' : '1939',
	}


	tuple_list=[]
	for name in d:
		tuple_list.append((d[name],name))
	sorted_list=sorted(tuple_list, key=getKey)

	for item in sorted_list:
		print (item[1])






if __name__=="__main__":
	execute()

