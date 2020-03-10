from numpy.random import randint

filename = "text original.txt"
file_in = open(filename).read()

words = file_in.split(" ")

blanks = int(input("There are %d words in this text.\nHow many blanks to be generated?\n" %len(words)))

punctuation = open("punctuation.txt").read()
brackets = open("brackets.txt").read()
print(words)

def check_format(word):
	if "\n" in word:
		word = word.split("\n")
		return blankLine(word)
	elif word[0] in punctuation:
		return blankFirst(word)
	elif word[-1] in punctuation:
		return blankLast(word)
	elif word[0] in brackets and word[-1] in brackets:
		return blankBracketed(word, 0)
	elif word[0] in brackets:
		return blankBracketed(word, 1)
	elif word[-1] in brackets:
		return blankBracketed(word, 2)
	elif "'" in word:
		word = word.split("'")
		return blankContracted(word, "'")
	elif "-" in word:
		word = word.split("-")
		return blankContracted(word, "-")
	else:
		return blank(word)

def blankLine(word):
	blanked_word = word[0] + "\n"
	for i in range(0, len(word[1])):
		blanked_word += "__"
	return blanked_word

def blankFirst(word):
	blanked_word = word[0]
	for i in range(1, len(word)):
		blanked_word += "__"
	return blanked_word

def blankLast(word):
	blanked_word = ""
	for i in range(0, len(word) -1):
		blanked_word += "__"
	blanked_word += word[-1]
	return blanked_word

def blankBracketed(word, setting):
	if setting == 0:
		blanked_word = word[0]
		for i in range(1, len(word) -1):
			blanked_word += "__"
		blanked_word += word[-1]
	elif setting == 1:
		blanked_word = word[0]
		for i in range(1, len(word)):
			blanked_word += "__"
	elif setting == 1:
		blanked_word = word[0]
		for i in range(0, len(word) -1):
			blanked_word += "__"
		blanked_word += word[-1]	
	return blanked_word

def blankContracted(word, sign):
	blanked_word = word[0] + sign
	for i in range(len(word[1])):
		blanked_word += "__"
	
	return blanked_word

def blank(word):
	blanked_word = ""
	for i in range(len(word)):
		blanked_word += "__"
	return blanked_word

blanked = []
for i in range(0, blanks):
	position = randint(len(words))
	if position not in blanked:
		blanked.append(position)
		words[position] = check_format(words[position])

print(words)

filename_out = "text blanked.txt" 
file_out = open(filename_out, "w")
for word in words:
	file_out.write(word + " ")
file_out.close()

file_check = open(filename_out).read()
final_words = file_check.split(" ")
print(len(final_words))