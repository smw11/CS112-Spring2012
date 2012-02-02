#!/usr/bin/env python

print "Enter your name: "
name=raw_input()
print "Prissybot: Hello there, "+name+"."
name2=name+": "
text=raw_input(name2)
print "Prissybot: You mean, "+text+", sir!"
text2=raw_input(name2)
print "Prissybot: Well, I never have been so insulted in all my life."
text3=raw_input(name2)
print "Prissybot: I only understand English. Tell me about a bad experience you had. It will amuse me."
text4=raw_input(name2)
print "Prissybot: This one time, in band camp, "+text4+", and it was fun. Much more fun than what you said."
text5=raw_input(name2)
print "Prissybot: You, sir, need a good lesson in manners. Let's start with math. Please enter in a number."
n=raw_input(name+", enter your number: ")
n=float(n)
print "Prissybot: Good! Now another."
m=raw_input(name+", enter a second number: ")
m=float(m)
print "Prissybot: Now let me perform some basic functions."
print n,"+",m,"=",n+m
print n,"-",m,"=",n-m
print n,"*",m,"=",n*m
print n,"/",m,"=",n/m
text6=raw_input(name2)
print "Prissybot: Thanks. I thought it was also very "+text6+" as well."
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

