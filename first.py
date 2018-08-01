from pip._vendor.distlib.compat import raw_input

ministry = "The Ministry of Silly Walks"

print (len(ministry))
print (ministry.upper())

#  last letter
print (ministry[-1])


print("Spam"+ " and " +"eggs")

"""If you'd like to print a variable that is an integer, 
you can "pad" it with zeros using %02d. 
The 0 means "pad with zeros", the 2 means to pad to 2 characters wide, 
and the d means the number is a signed integer (can be positive or negative).
"""

day = 6
print ("03 - %s - 2019" % (day))
# 03 - 6 - 2019
print ("03 - %02d - 2019" % (day))
# 03 - 06 - 2019

# input from user
#name = raw_input("What is your name? ")

# getting sysdate
from datetime import datetime

now= datetime.now()
print ("now is =>  " + str(now))
print(now.strftime('%B'))
current_year = now.year
current_month = now.month
current_day = now.day
print ("formatted date is =>  "+  ('%02d/%02d/%04d' % (now.day , now.month , now.year)))

print  ('%02d/%02d/%04d %02d:%02d:%04d' % (now.month , now.day , now.year , now.hour, now.minute, now.second))

STORY = "This morning _ woke up feeling _. 'It is going to be a _ day!' Outside, a bunch of _s were protesting to keep _ in stores. They began to _ to the rhythm of the _, which made all the _s very _. Concerned, _ texted _, who flew _ to _ and dropped _ in a puddle of frozen _. _ woke up in the year _, in a world where _s ruled the world."

print('starting !!!!')
name = raw_input('Enter a name : ')
adj1 = raw_input('Enter an adj1 : ')
adj2 = raw_input('Enter an adj2 : ')
adj3 = raw_input('Enter an adj3 : ')



