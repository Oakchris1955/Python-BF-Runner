#set some variables
point = 0

#begin by initialising a list with 30000 items, all ints set to 0
cells = [0 for i in range(30000)]

#set the filename to read
filename = 'main.bf'

#get the file contents
with open(filename) as bf_file:
	bf_string = bf_file.read()

#run the BF file
def run(code):
	#define some variables
	global point
	i = 0
	while True:
		#if nothing to read, quit
		if i >= len(code):
			quit()
		#get the current character
		char = code[i]
		#if moved past the cells, raise an error
		if point < 0 or point > len(cells)-1:
			raise MemoryError('Moved past the cells')
		#if overflowed cell, set to zero
		elif cells[point] < 0 or cells[point] > 255:
			cells[point] = 0
		#else, execute the program
		elif char == '>':
			point +=1
		elif char == '<':
			point -=1
		elif char == '+':
			cells[point] += 1
		elif char == '-':
			cells[point] -= 1
		elif char == '.':
			print(chr(cells[point]), end='')
		elif char == ',':
			cells[point] = ord(input(f'Input for cell {point}: ')[0])
		#if ']' found, set i to previous '['
		elif char == ']':
			beggining_of_loop = len(code)-code[::-1].find('[')-1
			if cells[point] != 0:
				i = beggining_of_loop

		#increase i by one to get to next character
		i+=1

#run the program
run(bf_string)
