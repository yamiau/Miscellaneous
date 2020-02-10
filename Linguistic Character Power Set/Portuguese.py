pp = ['a', 'á', 'à', 'â', 'ã', 'b', 'c', 'd']

portuguese_characters = ['a', 'á', 'à', 'â', 'ã', 'b', 'c', 'd', 'e', 'é', 'ê', 'f', 'g',
			    'h', 'i', 'í', 'j', 'k', 'l ', 'm', 'n', 'o', 'ó', 'ô', 'õ', 'p', 
			    'q', 'r', 's', 't', 'u', 'ú', 'v', 'w', 'x', 'y', 'z', ',', ';', '.', 
			    '!', '?', '"', ' ']

def powerset(l):
	result = [[]]
	for c in l:
		new_subset = [subset + [c] for subset in result]
		result.extend(new_subset)
	return result

print(powerset(pp))
