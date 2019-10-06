from xlsxwriter import Workbook

def die_type(key):
	switch = {
	      0: "BiZe", 	#Billion/Zero
	      1: "Three", 	#Three Only
	      2: "FoZe", 	#Four/Zero
	      3: "FiOn", 	#Five/One
	      4: "SiTw" 	#Six/Two
       }
	return switch[key]                       

die0 = [0, 0, 0, 0, 0, 10**9]
die1 = [3,] * 6
die2 = [0, 0, 4, 4, 4, 4]
die3 = [1, 1, 1, 5, 5, 5]
die4 = [2, 2, 2, 2, 6, 6]

dice = [die0, die1, die2, die3, die4]

results = []
matrix_counter = -1

for first in range(len(dice)):
	for second in range(first + 1, len(dice)):
		results.append([])
		matrix_counter += 1
		for i in range(len(dice[0])):
			results[matrix_counter].append([])
			for j in range(len(dice[0])):
				if ( (dice[first])[i] > (dice[second])[j] ):
					(results[matrix_counter])[i].append(die_type(first))
				else:
					(results[matrix_counter])[i].append(die_type(second))

for matrix in range(len(results)):
	