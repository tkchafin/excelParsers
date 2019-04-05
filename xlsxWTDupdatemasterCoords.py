#!/usr/bin/python

import sys
import re
import functools
import pandas as pd

"""
script looks through a provided field data sheet 
and tries to fill in utm coordinates in master data sheet 
format should be:
field data = field.ID
dnaex data = DNAex.ID
utms: utm_easting & utm_northing

no extra columns above headers

sorry this sucks so bad, was in a hurry and pissed at 
what a clusterfuck our database is
"""


def main():
	master=""
	data=""
	t=""
	
	if len(sys.argv) != 4:
		print("Exiting because .xlsx not provided")
		print("Usage:",sys.argv[0]," <master.xlsx> <field data.xlsx> <field/dna")
		sys.exit(1)
	if sys.argv[1]:
		master=sys.argv[1]
	else:
		print("Exiting because .xlsx not provided")
		print("Usage:",sys.argv[0]," <master.xlsx> <field data.xlsx> <field/dna")
		sys.exit(1)
	if sys.argv[2]:
		field=sys.argv[2]
	else:
		print("Exiting because .xlsx not provided")
		print("Usage:",sys.argv[0]," <master.xlsx> <field data.xlsx> <field/dna")
		sys.exit(1)
	if sys.argv[3]:
		t=sys.argv[3]
		if t not in ["field", "dna"]:
			print("Exiting because type not provided")
			print("Usage:",sys.argv[0]," <master.xlsx> <field data.xlsx> <field/dna")
			sys.exit(1)
	else:
		print("Exiting because type not provided")
		print("Usage:",sys.argv[0]," <master.xlsx> <field data.xlsx> <field/dna")
		sys.exit(1)

	master_df = pd.read_excel(master,sheet_name=0, dtype='str')
	field_df = pd.read_excel(field,sheet_name=0, dtype='str')
	#print(field_df)
	
	if (t == "field"):
		field_df = field_df[["field.ID", "utm_easting", "utm_northing"]]
		#print(field_df)
		field_df['field.ID'] = field_df['field.ID'].apply(remove_delims)
	elif (t == "dna"):
		field_df = field_df[["DNAex.ID", "utm_easting", "utm_northing"]]
		field_df['DNAex.ID'] = field_df['DNAex.ID'].apply(padSampleName)

	else:
		print("invalid type")
		sys.exit(1)
	
	d = makeDict(field_df, 0)
	
	updateMaster(master_df, d)
	#print(df)

def makeDict(from_df, col_key):
	d = {}
	index=int(col_key)
	for i,row in from_df.iterrows(): #yields tuples
		l = list(row)
		key = l[index]
		new_vals = l[:index] + l[index+1 :]
		d[key] = new_vals
	return(d)

def findCoords(d, row):
	#check if ID in dict
	if row['field.ID'] in d:
		row["utm_easting"] = d[row['field.ID']][0]
		row["utm_northing"] = d[row['field.ID']][1]
	elif "CWD"+str(row['field.ID']) in d:
		row["utm_easting"] = d["CWD"+str(row['field.ID'])][0]
		row["utm_northing"] = d["CWD"+str(row['field.ID'])][1]
	elif str(row['field.ID'].replace("CWD", "")) in d:
		row["utm_easting"] = d[str(row['field.ID'].replace("CWD", ""))][0]
		row["utm_northing"] = d[str(row['field.ID'].replace("CWD", ""))][1]
	elif row["DNAex.ID"] in d:
		row["utm_easting"] = d[row["DNAex.ID"]][0]
		row["utm_northing"] = d[row["DNAex.ID"]][1]
	return(row)

def updateMaster(m, d):
	fc = functools.partial(findCoords, d)
	m = m.apply(fc, axis=1)
	writer = pd.ExcelWriter('wtd_master.xlsx')
	m.to_excel(writer, 'Sheet1')
	writer.save()



#Makes sure we have padded zeros in DNA sample name
def padSampleName(samp):
	l = re.split('(N|P|U)', samp)
	if len(l[-1]) !=3:
		n = l[-1].zfill(3)
		l[-1] = n
	return("".join(l))

#Filter out unwanted rows
def filter_bad(l):
	if l[7] in ["nan", "", "None", "NaN"] or l[7] is None:
		return(False)
	elif l[8] in ["nan", "", "None", "NaN"] or l[8] is None:
		return(False)
	elif l[15] != "Whitetailed Deer":
		return(False)
	elif l[17] != "Y":
		return(False)
	else:
		return(True)

def new_name(row):
	samp = row[2] + row[3] + row[4]
	samp = samp.upper()
	samp = padSampleName(samp)
	return(samp)

def remove_delims(value):
	value = value.replace('-',"")
	value = value.replace('_',"")
	value = value.replace(',',"")
	return(value)

def printMaster(field_df):

	sub = field_df[['field.ID', 'spec.', 'loc', 'num']]
	
	sub.insert(1, 'DNAex.ID', 'NA')

	sub['DNAex.ID'] = sub.apply(new_name, axis=1)
	sub['field.ID'] = sub['field.ID'].apply(remove_delims)
	
	writer = pd.ExcelWriter('wtd_master.xlsx')
	sub2 = sub[["field.ID", "DNAex.ID"]]
	sub2.insert(2, "utm_easting", "")
	sub2.insert(3, "utm_northing", "")
	sub2.to_excel(writer, 'Sheet1')
	writer.save()




#Call main function
if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		sys.exit(1)
