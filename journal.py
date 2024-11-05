import time
import sys

print("Hey! What are you thinking? \n")
text = input()

file = open("journal.txt", "a")
file.write("\n \n")
file.write(time.ctime())
file.write("\n")
file.write(text)
file.write("\n")

time.sleep(3)

sys.exit