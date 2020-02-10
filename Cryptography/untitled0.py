
def ShiftRows(state):
	temp = ["",] *16
	
	for i in state:
		index = state.index(i)
		rem = index%4
		if rem == 0:
			temp[index] = state[index]
		elif rem == 1:
			calc = (index + 4)%16
			temp[index] = state[calc]
		elif rem == 2:
			calc = (index + 8)%16
			temp[index] = state[calc]
		elif rem == 3:
			calc = (index + 12)%16
			temp[index] = state[calc]
		
	for i in range(0, 16):
		state[i] = temp[i]
		
message = "Sixteen bits msg"

state = [i for i in message]

ShiftRows(state)

print(message[0:4])
print(message[4:8])
print(message[8:12])
print(message[12:16])
print("\n")
print(state[0:4])
print(state[4:8])
print(state[8:12])
print(state[12:16])