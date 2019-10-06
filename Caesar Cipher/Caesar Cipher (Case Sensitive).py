alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

input_string = input("Enter a string: ")
shift_level = int(input("Shift value: "))
 
output_string = ""

for i in range(len(input_string)):
	character = input_string[i]
			
	if character in alphabet_lower:
		actual_index = alphabet_lower.find(character)
		shifted_index = (actual_index + shift_level) % 26
		output_string += alphabet_lower[shifted_index]
	elif character in alphabet_upper:
		actual_index = alphabet_upper.find(character)
		shifted_index = (actual_index + shift_level) % 26
		output_string += alphabet_upper[shifted_index]
	else:
		output_string += character
	
sign = "+" if shift_level > 0 else ""
print("Ciphered with a shift of ", sign, shift_level, ": ", output_string)