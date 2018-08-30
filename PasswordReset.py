

import getpass
import sys
import telnetlib

HOST = "x.x.x.x"

tn = telnetlib.Telnet(HOST, timeout = 10)


#AD Authentication Credentials 
tn.read_until("login: ".encode('ascii'))

user = input("Enter your remote account: ")

tn.write(b'user + b"\n")


tn.read_until(b"Password: ")

 password = input("Enter your remote account password: ")

tn.write(b'password + b"\r\n")

op = tn.read_until(b"number:   ", timeout = 5)

print (op)

#opp = tn.read_until(b"com")
#p=tn.read_until(":\x1b[0m ".encode('ascii'))



#print(opp)

#Unidata Authentication Credentials
#Hardcode with set reset account or ask users to enter their user/badge number

tn.write(b'xxxxxx' + b"\r\n") 

tn.write(b'xxxxxx' + b"\r\n") 

opop = tn.read_until(b"ncwicn", timeout = 2) #fake read until timeout. Using this to avoid ansi escape characters

print (opop)


tn.write(b'sm' + b"\r\n") #Must enter SM to reach security maintenance screen

opop = tn.read_until(b"ncwicn", timeout = 2)

print (opop) #Script Location Check


user2reset = input('Enter 6 digit ID of user you would like to reset:' + " ")
tn.write(user2reset.encode('ascii') + b"\r\n")

opop = tn.read_until(b"ncwicn", timeout = 2)

print (opop) #Script Location Check

tn.write(b'R' + b"\r\n")

opop = tn.read_until(b"ncwicn", timeout = 2)

print (opop) #Script Location Check


tn.write(b'OK' + b"\r\n")

opop = tn.read_until(b"ncwicn", timeout = 2)

print (opop) #Script Location Check

tn.write(b"\r\n")

opop = tn.read_until(b"ncwicn", timeout = 2)

print (opop) #Script Location Check


tn.write(b"\r\n")

opop = tn.read_until(b"ncwicn", timeout = 2) 

print (opop) #Script Location Check


tn.write(b'T' + b"\r\n")

opop = tn.read_until(b"ncwicn", timeout = 1)

print (opop) #Script Location Check

print ('You have successfully reset: ' + user2reset)

 

tn.write(b'QUIT' + b"\r\n")



tn.close