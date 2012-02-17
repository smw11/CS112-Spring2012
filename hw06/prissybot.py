#!/usr/bin/env python

#User inputs name to which prissybot refers to the user as their entered name
print "Enter your name: "
name=raw_input()
print "Prissybot: Hello there, "+name+"."

#Colon is added so user's name appears before he/she types
name2=name+": "

#Here the user can enter anything, preferably a greeting, to which prissybot adds 'sir'
text=raw_input(name2)
print "Prissybot: You mean, "+text+", sir!"

#Once again, user can enter anything, to which prissybot will be insulted
text=raw_input(name2)
print "Prissybot: Well, I never have been so insulted in all my life."

#Another user input, followed by prissybot asking a question
text=raw_input(name2)
print "Prissybot: I only understand English. Tell me about a bad experience you had. It will amuse me."

#User enters a bad experience, to which prissybot will respond with a similar statement
text=raw_input(name2)
print "Prissybot: This one time, in band camp, "+text+", and it was fun. Much more fun than what you said."

#At this point, user will most likely say something rude, to which prissybot will ask for numbers
text=raw_input(name2)
print "Prissybot: You, sir, need a good lesson in manners. Let's start with math. Please enter in a number."

#User gives a number and it is made an integer
firstnum=raw_input(name+", enter your number: ")
firstnum=float(firstnum)

#User gives a second number after a prompt
print "Prissybot: Good! Now another."
secondnum=raw_input(name+", enter a second number: ")
secondnum=float(secondnum)

#Prissybot adds, subtracts, multiplies, and divides the two numbers
print "Prissybot: Now let me perform some basic functions."
print firstnum,"+",secondnum,"=",firstnum+secondnum
print firstnum,"-",secondnum,"=",firstnum-secondnum
print firstnum,"*",secondnum,"=",firstnum*secondnum
print firstnum,"/",secondnum,"=",firstnum/secondnum

#User enters a final statement, to which prissybot will use the input in its final statements
text=raw_input(name2)
print "Prissybot: Thanks. I thought it was also very "+text+" as well."
print "Prissybot: See you later."

"""
prissybot.py

CS112 Homework 3:   PrissyBot

Prissy bot, the rude chat bot, is just mean!  It does not listen, asks obnoxious questions, and says anything it likes.
"""

# Step 1:
# -----------------------
# Program the following.
# 
#    $ python prissybot.py
#    Enter your name:  Paul
#   
#    PrissyBot: Hello there, Paul
#    Paul: hi bot
#    PrissyBot: You mean, "hi bot, sir!"
# 
# Make sure the user inputs their own name and responses.



# Step 2:
# -----------------------
# Keep adding to the conversation. Make sure that your program 
# includes the following:
# 
#  * get and use input from the user
#  * 3 math problems
#     * at least one should get numbers from the user
#  * at least 3 insults


# Advanced
# -------------------------
# Make sure your prissy bot uses string formatting throughout.  
# Also, create new programs for the following:
#  
#  1. draw some kind of ascii art based on user input
#  2. print a decimal/binary/hexidecimal conversion table 
#     * well formated and labeled
#     * reads 5 numbers from the input (all less than 256)
#  3. reduce a fraction
#     * read a numerator and denominator from the user
#     * ex.  6/4 = 1 2/4

