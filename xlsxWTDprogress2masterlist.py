#!/usr/bin/python

import sys
import re
import pandas as pd

def main():
	field_data=""
	dna_list=""
	if sys.argv[1]:
		field_data=sys.argv[1]
	else:
		print("Exiting because .xlsx not provided")
		print("Usage:",sys.argv[0]," <wtd_progress_overview.xlsx>")
		sys.exit(1)

	field_df = pd.read_excel(field_data,sheet_name=0, skiprows=1, dtype='str')

	printMaster(field_df)
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
	sub2.insert(4, "sex", "")
	sub2.insert(5, "age", "")
	sub2.to_excel(writer, 'Sheet1')
	writer.save()




#Call main function
if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		sys.exit(1)
