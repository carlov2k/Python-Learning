
#PEXPECT DOESNT WORK

import pexpect


print("Enter the IP address:")
ip_address = input()

print("Enter the username:")
username = input()

print("Enter the password:")
password = input()


print(ip_address)
print(username)
print(password)

print("\n" + "--------------------------------------------------")
print("---Attempting connection via telnet to:",ip_address)

#Create the pexpect session
session = winpexpect.spawn('tel' + ip_adress, timeout=20)
result = session.expect(['Username:', winpexpect.TIMEOUT])

