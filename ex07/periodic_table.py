def execute():

	table_info=open("ex07/periodic_table.txt", "r")

	lignes=(table_info.read()).split("\n")
	lignes.remove('')


	lignes_separees=[]
	for line in lignes:
		lignes_separees.append(line.split(","))

	rawinfo=[]
	for element in lignes_separees:
		name=element[0].partition(" ")[0]
		position=element[0].partition(":")[2]
		number=element[1].partition(":")[2]
		small=(element[2].partition(":")[2]).strip()
		molar=element[3].partition(":")[2]
		electrons=element[4].partition(":")[2]
		rawinfo.append([name, position, number, small, molar, electrons])

	rawinfo.insert(56,["Lanthanides","","57-71","","",""])
	rawinfo.insert(74,["Actinides","","89-103","","",""])

	print("<table>")
	print("<tr>")
	print("		<td style='border: 1px solid black; padding:10px'>")
	print("			<h4>{}</h4>".format(rawinfo[0][0]))
	print("			<ul>")
	print("				<li>No {}</li>".format(rawinfo[0][2]))
	print("				<li>{}</li>".format(rawinfo[0][3]))
	print("				<li>Masse molaire : {}</li>".format(rawinfo[0][4]))
	print("				<li>Electrons : {}</li>".format(rawinfo[0][5]))
	print("			</ul>")
	print("		</td>")
	for i in range(16):
		print("		<td>")
		print("		</td>")
	print("		<td style='border: 1px solid black; padding:10px'>")
	print("			<h4>{}</h4>".format(rawinfo[1][0]))
	print("			<ul>")
	print("				<li>No {}</li>".format(rawinfo[1][2]))
	print("				<li>{}</li>".format(rawinfo[1][3]))
	print("				<li>Masse molaire : {}</li>".format(rawinfo[1][4]))
	print("				<li>Electrons : {}</li>".format(rawinfo[1][5]))
	print("			</ul>")
	print("		</td>")
	print("</tr>")

	print("<tr>")
	for i in range(2,4):
		print("		<td style='border: 1px solid black; padding:10px'>")
		print("			<h4>{}</h4>".format(rawinfo[i][0]))
		print("			<ul>")
		print("				<li>No {}</li>".format(rawinfo[i][2]))
		print("				<li>{}</li>".format(rawinfo[i][3]))
		print("				<li>Masse molaire : {}</li>".format(rawinfo[i][4]))
		print("				<li>Electrons : {}</li>".format(rawinfo[i][5]))
		print("			</ul>")
		print("		</td>")
	for i in range(10):
		print("		<td>")
		print("		</td>")
	for i in range(4,10):
		print("		<td style='border: 1px solid black; padding:10px'>")
		print("			<h4>{}</h4>".format(rawinfo[i][0]))
		print("			<ul>")
		print("				<li>No {}</li>".format(rawinfo[i][2]))
		print("				<li>{}</li>".format(rawinfo[i][3]))
		print("				<li>Masse molaire : {}</li>".format(rawinfo[i][4]))
		print("				<li>Electrons : {}</li>".format(rawinfo[i][5]))
		print("			</ul>")
		print("		</td>")
	print("</tr>")

	("<tr>")
	for i in range(10,12):
		print("		<td style='border: 1px solid black; padding:10px'>")
		print("			<h4>{}</h4>".format(rawinfo[i][0]))
		print("			<ul>")
		print("				<li>No {}</li>".format(rawinfo[i][2]))
		print("				<li>{}</li>".format(rawinfo[i][3]))
		print("				<li>Masse molaire : {}</li>".format(rawinfo[i][4]))
		print("				<li>Electrons : {}</li>".format(rawinfo[i][5]))
		print("			</ul>")
		print("</td>")
	for i in range(10):
		print("		<td>")
		print("		</td>")
	for i in range(12,18):
		print("		<td style='border: 1px solid black; padding:10px'>")
		print("			<h4>{}</h4>".format(rawinfo[i][0]))
		print("			<ul>")
		print("				<li>No {}</li>".format(rawinfo[i][2]))
		print("				<li>{}</li>".format(rawinfo[i][3]))
		print("				<li>Masse molaire : {}</li>".format(rawinfo[i][4]))
		print("				<li>Electrons : {}</li>".format(rawinfo[i][5]))
		print("			</ul>")
		print("		</td>")
	print("</tr>")

	for k in range(4):
		print("<tr>")
		for i in range(18+k*18,36+k*18):
			print("		<td style='border: 1px solid black; padding:10px'>")
			print("			<h4>{}</h4>".format(rawinfo[i][0]))
			print("			<ul>")
			print("				<li>No {}</li>".format(rawinfo[i][2]))
			print("				<li>{}</li>".format(rawinfo[i][3]))
			print("				<li>Masse molaire : {}</li>".format(rawinfo[i][4]))
			print("				<li>Electrons : {}</li>".format(rawinfo[i][5]))
			print("			</ul>")
			print("		</td>")
		print("</tr>")

	print("</table>")





if __name__=="__main__":
	execute()
