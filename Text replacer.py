filepath = input("Insert the path to your text file (\): ")
file_in = open(filepath).read()

all_terms = file_in.split(" ")
term = input("Insert the term you want to replace: ")
newTerm =  input("Insert the new term to replace it: ")

caseOn = 9
while not (caseOn == 0 or caseOn == 1):
	caseOn = int(input("Turn case sensitiveness on? 0 = NO, 1 = YES :" ))