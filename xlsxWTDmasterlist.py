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
		print("Usage:",sys.argv[0]," <wtd_field_data.xlsx> <list.tsv>")
		sys.exit(1)
	if sys.argv[2]:
		dna_list=sys.argv[2]
	else:
		print("Exiting because .tsv not provided")
		print("Usage:",sys.argv[0]," <wtd_field_data.xlsx> <list.tsv>")
		sys.exit(1)

	if field_data == "" or dna_list == "":
		print("ain't nobody got time for that")
		sys.exit(1)
	field_df = pd.read_excel(field_data,sheet_name=0)
	dna_df = pd.read_csv(dna_list, sep='\t')

	printMaster(field_df, dna_df)
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
	l = samp.rsplit('P',1)
	if len(l) == 2:
		n = l[1].zfill(3)
		return(l[0]+"P"+n)
	else:
		l2 = samp.rsplit('N',1)
		if len(l2) == 2:
			n = l2[1].zfill(3)
			return(l2[0]+"N"+n)
		else:
			return(samp)

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

def printMaster(field_df, dna_df):

	l = field_df.columns.get_values().tolist()
	l.insert(2, "DNAex")
	l.insert(3, "conc.")

	new_list = list()
	dna_dict = makeDict(dna_df, 1)
	for index,row in field_df.iterrows():
		new_row = list(row)
		name=str(row[1])
		if name in ["nan", "", "NaN"]:
			continue
		if "CWD" not in name: #Skip older samples not in CWD naming scheme
			continue
		dna_name = ""
		dna_conc = ""
		if str(row[1]) in dna_dict: #check if CWD number is in dna_list
			dna_name = dna_dict[name][0]
			dna_conc = dna_dict[name][1]
			dna_name = padSampleName(dna_name)
			#print(dna_name)
		new_row.insert(2, dna_name)
		new_row.insert(3, dna_conc)
		#print(new_row)
		if len(new_row) != len(l):
			print("something fucked up")
		else:
			#Returns True if good row
			if filter_bad(new_row):
				new_list.append(new_row)

	new = pd.DataFrame(new_list, columns=l)
	writer = pd.ExcelWriter('out.xlsx')
	new.to_excel(writer, 'Sheet1')
	writer.save()



#Call main function
if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		sys.exit(1)
