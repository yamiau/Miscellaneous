import matplotlib.pyplot as plt

def die_type(key):
	switch = {
	      0: "BiZe", 	#Billion/Zero
	      1: "Thre", 	#Three Only
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
matrix_title = []
matrix_counter = -1

for first in range(len(dice)):
	for second in range(first + 1, len(dice)):
		results.append([])
		matrix_title.append("%s vs %s" % (die_type(first), die_type(second)))
		matrix_counter += 1
		for i in range(len(dice[0])):
			results[matrix_counter].append([])
			for j in range(len(dice[0])):
				if ( (dice[first])[i] > (dice[second])[j] ):
					(results[matrix_counter])[i].append(1)
				elif ( (dice[first])[i] < (dice[second])[j] ):
					(results[matrix_counter])[i].append(-1)
				else:
					(results[matrix_counter])[i].append(0)

def die_color(key):
	switch = {
	    "BiZe" : "brown",
	    "Thre" : "yellowgreen",
	    "FoZe" : "coral",
	    "FiOn" : "skyblue",
	    "SiTw" : "gold",
	    "Draw" : "gray"
       }
	return switch[key]

'''for matrix in range(len(results)):
	print(matrix_title[matrix])
	for row in results[matrix]:
		print(row)'''


counter = -1

for first in range(len(dice)):
	for second in range(first + 1, len(dice)):
		counter += 1
		first_score = 0
		second_score = 0
		draw_score = 0
		for matrix in results[counter]:
			for i in matrix:
				if i == 1:
					first_score += 1
				elif i == -1:
					second_score += 1
				else:
					draw_score += 1
								
		labels = (die_type(first), die_type(second), "Draw")
		legend_labels = (die_type(first) + " " +  str(dice[first]), 
			     die_type(second) + " " + str(dice[second]), 
			     "Draw")
		sizes = [first_score, second_score, draw_score]
		color_set = (die_color(die_type(first)), die_color(die_type(second)), die_color("Draw"),)		
		
		fig1, ax1 = plt.subplots()
		ax1.pie(sizes, colors = color_set, labels = labels, autopct = "%0.3f%%")
		ax1.axis("equal")
		ax1.set_title(matrix_title[counter])
		
		plt.legend(legend_labels, loc = "best", prop = {"size" : 8})	
		plt.savefig("Pie Charts/%s.png" % matrix_title[counter])
		
	