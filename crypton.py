import random
import sys

print("[[Crypton]]\nPasskey based random password generator")

# get alphabet data from the txt file
try:
	file = open("data.txt")
except:
	sys.exit("NO FILE FOUND (data.txt) IS MISSING")
alphabet = list(file.read())

# use a phrase/password as a seed
password = input("Please input a starting password\n> ")
password = list(password)

# count up seed based on position in the alphabet list hello = 7+4+11+11+14 = 47
startSeed = 0
for i in range(0, len(password)):
	try:
		startSeed += alphabet.index(password[i])
	except:
		print("[warn]: char: " + password[i] + " does not exsist in data.txt\n[resolution]: adding 22 to seed")
		startSeed += 22

# set seed
random.seed(startSeed)

# get configuration
length = int(input("desired length of your passwords:\n> "))
count = int(input("number of passwords desired:\n> "))

print("password(s): ")
for i in range(0, count):
	output = []
	for i in range(0, length):
		# outputs a random char and stitches them together to make a length password
		output.append(alphabet[random.randint(0, len(alphabet)-1)])
	print(''.join(output))

input("press enter to exit")
