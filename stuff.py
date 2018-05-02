#Creates my list

#person_info = list() this is the same as the line below
person_info = []

file = open('info.txt', 'r')
file_line = file.readline().strip()
file.close()

print('The file I read is: ' + file_line)

person_info = file_line.split(',')

print(person_info)
