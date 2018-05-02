import time

# Open File
devices_file = open('input.txt', 'rt')

# Read info one line at a time





name = devices_file.readline().strip()
last = devices_file.readline().strip()
field = devices_file.readline().strip()
role = devices_file.readline().strip()

# Print out info
print("--------DEVICE INFO NICELY FORMATTED-----------")
print("Name     Last     Field    Role")
print("----     ----     -----    ----")
print("{:9}{:9}{:9}{:9}".format(name, last, field, role))
print("-----------------------------------------------")

worker_info = name
worker_info = worker_info + "," + last
worker_info = worker_info + "," + field
worker_info = worker_info + "," + role

print("Writing Worker Info to file...")
time.sleep(3)

output_file = open("output.txt", "w")
output_file.write(worker_info)
output_file.close()

print("Complete")

readFile = open("output.txt", "r")
workerStats = readFile.readline().strip()
readFile.close()

print(workerStats)


#print("Name:  ",name)
#print("Last:  ",last)
#print("Field: ",field)
#print("Role:  ",role)







