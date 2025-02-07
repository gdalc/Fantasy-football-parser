import pandas as pd
import os
import shutil
import argparse

from roles import *

FILENAME = "2024.csv"


def importList(fname):
	data=pd.read_csv(fname, header=None)
	data=data.values.tolist()
	return data


def toFile(data, csvname):
	fpout = open(csvname + '.csv', "w")
	#print("gf")
	for A in data:
		data_str = ""
		for i in range(len(A)-1):
			data_str = data_str + str(A[i]) + ","
		fpout.write(data_str + str(A[-1]) + "\r\n")
	fpout.close()

if __name__=="__main__":
	parser = argparse.ArgumentParser("role_parser")
	parser.add_argument("filename", help="The filename of the list file, with its extension (.csv).", type=str)
	args = parser.parse_args()
	FILENAME = args.filename
	print(args)
	print("Generatore liste\n")
	
	try:
		data = importList(FILENAME)
		print("-Lists loaded")
		strRole = []

		os.mkdir(os.getcwd() + '/listev2')
		os.chdir(os.getcwd() + '/listev2')
		print("-Temp directory created")
		print("-Generation lists by roles")
		
		toFile(getPor(data), 'Por')
		print("--Por OK")
		toFile(getDdDsDc(data), 'Dif')
		print("--Dif OK")
		toFile(getEMC(data), 'Cen')
		print("--Cen OK")
		toFile(getWT(data), 'Treq')
		print("--Treq OK")
		toFile(getAPc(data), 'Att')
		print("--Att OK")
		
		print("-Verifica in corso")
		count = 0
		for fname in os.listdir(os.getcwd()):
			if fname.endswith(".csv"):
				count = count + sum(1 for line in open(fname))
		if count == len(data):
			print("-Check passed")
		else:
			print("Check failed")
			print("count=", count, ", data=", len(data))
		os.chdir(os.getcwd() + '/../')
		shutil.make_archive('listev2', 'zip', 'listev2')
		print("-Zip created")
		shutil.rmtree(os.getcwd() + '/listev2')
		print("-Temp directory deleted")
		
	except:
		print("Generic ERROR")
	print("\n\nBuona asta")


