import os
import xml.etree.ElementTree as ET

mystr = "wcrs.com,southjordan-sugarhousestorage.com"
mylist = mystr.split(",")

cumulation = []

for i in mylist:
	os.system("theharvester -d %s -l 500 -b google -f out.html"%(i))

	with open('out.xml', 'rt') as f:
	    tree = ET.parse(f)
	
	node = tree.iter()

	hostname = "%s"%i
	emails = []
	
	for value in tree.iter('email'):
		concat = hostname
		names = value.text.split("@")[0].split(".")

		if len(names) == 2:
			concat = concat + "\t%s\t%s\t%s"%(value.text,names[0],names[1])
		else:
			concat = concat + "\t%s\t%s\t"%(value.text,names[0])
		emails.append(concat)

	if len(emails) == 0:
		cumulation.append(hostname)
	else:
		for x in emails:
			cumulation.append(x)
			print x

	os.system("rm -f out.*")
os.system("rm -f results.txt")
with open('results.txt', 'w+') as f:
	for x in cumulation:
		f.write(x)
		f.write("\n")
