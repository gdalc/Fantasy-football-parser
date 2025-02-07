# Auxiliary functions for role parsing

def getRole(strRole, role):
	out = []
	for i in range(len(strRole)):
		if role in strRole[i][1]:
			out.append(strRole[i])
	return out
	
def getRoles(data, roles):
	out = []
	for i in range(len(data)):
		for role in roles:
			if role in data[i][4] and not(data[i] in out):
				out.append(data[i])
	return out

def getPor(data):
	return [A for A in data if "Por" in A[4]]

def getDdDsDc(data):
	return [A for A in data if ("Dd" in A[4] or "Dc" in A[4] or "Ds" in A[4])]

def getEMC(data):
	return [A for A in data if ("E" in A[4] or "M" in A[4] or "C" in A[4]) and not ('Dd' in A[4] or 'Ds' in A[4] or 'Dc' in A[4] )]

def getWT(data):
	return [A for A in data if ("W" in A[4] or "T" in A[4]) and not ('M' in A[4] or 'C' in A[4] or 'E' in A[4] )]

def getAPc(data):
	return [A for A in data if ("Pc" in A[4] or "A" in A[4]) and not ('W' in A[4] or 'T' in A[4] or 'C' in A[4] )]
