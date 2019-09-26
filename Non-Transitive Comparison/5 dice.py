from xlsxwriter import Workbook
import random

def die_type(key):
	switch = {
	      0: "BiZe", 	#Billion/Zero
	      1: "Three", 	#Three Only
	      2: "FoZe", 	#Four/Zero
	      3: "FiOn", 	#Five/One
	      4: "SiTw" 	#Six/Two
       }
	return switch[key]                       

die0 = [0, 0, 0, 0, 0, 10**10]
die1 = [3,] * 6
die2 = [0, 0, 4, 4, 4, 4]
die3 = [1, 1, 1, 5, 5, 5]
die4 = [2, 2, 2, 2, 6, 6]

dice = [die0, die1, die2, die3, die4]

workbook = Workbook('Dice_comparison_results.xlsx')

for first in range(len(dice)):
	for second in range(first + 1, len(dice)):
		counter = 0
		comparison = [0, 0, 0]
		title = str(die_type(first)) + " vs " + str(die_type(second))
		
		worksheet = workbook.add_worksheet(title)
		
		worksheet.write(counter, 0, "%s res" % die_type(first))
		worksheet.write(1, 0, str(dice[first]))
		worksheet.set_column(0, 0, len(str(dice[first])) )
		
		worksheet.write(counter, 1, "%s res" % die_type(second))
		worksheet.write(1, 1, str(dice[second]))
		worksheet.set_column(1, 1, len(str(dice[second])) )
		
		worksheet.write(counter, 2, "Results")
		
		while counter < 1000:			
			counter += 1
			
			first_res = (dice[first])[random.randint(0, 5)]
			worksheet.write(counter + 1, 0, first_res)
			
			second_res = (dice[second])[random.randint(0, 5)]
			worksheet.write(counter +1 , 1, second_res)
			
			if ( (first_res - second_res) > 0 ):
				comparison[0] += 1
			elif ( (first_res - second_res) < 0):
				comparison[1] += 1
			else:
				comparison[2] += 1
				
		
		worksheet.write(1, 2, str(comparison))
		worksheet.set_column(2, 2, len(str(comparison)) )

workbook.close()
