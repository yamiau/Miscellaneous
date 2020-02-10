import matplotlib.pyplot as plt

filename = "C:\\Users\\Yami\\Desktop\\test.txt" 
file_in = open(filename).read()

discrete_characters = []

for char in file_in:
	if char not in discrete_characters:
		discrete_characters.append(char)
		
		
print(discrete_characters)

counting_characters = []

for char in discrete_characters:
	sub = [char, 0]
	counting_characters.append(sub)			

	
for char in file_in:
	for sub in counting_characters:
		if char == sub[0]:
			sub[1] += 1
		
print(counting_characters)

vowels = ['a', 'á', 'à', 'â', 'ã', 'e', 'é', 'ê', 'i', 'í', 'o', 'ó', 'ô', 'õ','u', 'ú']
consonants = ['b', 'c', 'ç', 'd', 'f', 'g', 'h', 'j', 'k', 'l ', 'm', 
		'n', 'p', 'q', 'r', 's', 't','v', 'w', 'x', 'y', 'z']
punctuation = [ ',', ';', ':', '.', '!', '?', '"',]

character_type ={"Vowels" : 0,"Consonants" : 0, "Punctuation" : 0, "Others" : 0}

for sub in counting_characters:
	if sub[0].lower() in vowels or sub[0].upper() in vowels:
		character_type["Vowels"] += sub[1]
	elif sub[0].lower() in consonants or sub[0].upper() in consonants:
		character_type["Consonants"] += sub[1]
	elif sub[0] in punctuation:
		character_type["Punctuation"] += sub[1]
	else:
		character_type["Others"] += sub[1]
		
print(character_type)

chart_labels = [k for k in character_type]
chart_sizes = [character_type[v] for v in character_type]
chart_colors = ['yellow', 'cyan', 'magenta', 'gray']
chart_explode = (0, 0, 0, 0)

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct

plt.pie(chart_sizes, labels=chart_labels, colors=chart_colors, autopct=make_autopct(chart_sizes))	

donut_core = plt.Circle((0, 0), 0.75, color='white', fc='white', linewidth=1.25)
fig = plt.gcf()
fig.gca().add_artist(donut_core)

plt.axis('equal')
plt.show()
		
		
		
		