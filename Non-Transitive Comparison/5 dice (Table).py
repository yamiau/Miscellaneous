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
					(results[matrix_counter])[i].append(die_type(first))
				elif ( (dice[first])[i] < (dice[second])[j] ):
					(results[matrix_counter])[i].append(die_type(second))
				else:
					(results[matrix_counter])[i].append("Draw")

def die_color(key):
	switch = {
	    "BiZe" : "brown",
	    "Thre" : "green",
	    "FoZe" : "magenta",
	    "FiOn" : "blue",
	    "SiTw" : "yellow",
	    "Draw" : "gray"
       }
	return switch[key]

for matrix in range(len(results)):
	print(matrix_title[matrix])
	for row in results[matrix]:
		print(row)
		
fig = plt.figure()
ax = fig.add_subplot(111)
row_labels = die0 
col_labels = die1
table_vals = [list for list in results[0]]
print(table_vals)

the_table = plt.table(cellText=table_vals,
			 colWidths = [0.05] * 6,
			 rowLabels = row_labels, 
			 colLabels = col_labels, 
			 loc = 'center')

the_table.auto_set_font_size(False)
the_table.set_fontsize(24)
the_table.scale(4, 4)

plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.tick_params(axis='y', which='both', right=False, left=False, labelleft=False)
for pos in ['right','top','bottom','left']:
    plt.gca().spines[pos].set_visible(False)
plt.savefig('%s Table.png' % matrix_title[0], bbox_inches='tight', pad_inches=0.05)