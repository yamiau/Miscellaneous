alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

input_string = input("Enter a string: ").upper()
shift_level = int(input("Shift value: "))
 
output_string = ""

for i in range(len(input_string)):
	character = input_string[i]
	if character not in alphabet:
		output_string += character
	else:
		actual_index = alphabet.find(character)
		shifted_index = (actual_index + shift_level) % 26
#		if shifted_index > len(input_string):
#		shifted_index -= 25
#		elif shifted_index < 0:
#		shifted_index += 26
		output_string += alphabet[shifted_index]

sign = "+" if shift_level > 0 else ""
print("Ciphered with a shift of ", sign, shift_level, ": ", output_string)