#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
   
   
               
          
def firstbatting():
   global Gameover
   print("Go for your first batting")
   runs = 0
   AIruns = 0
   
   while not Gameover:
       user = int(input("You may do batting:"))
       AI = random.randit(1,6)
       print("AI bowling:" , AI)
       runs += user
       print("current runs of user is:", runs)
       
       if user == AI:
           print("user is out")
           print("AI's turn for batiing")
           print("AI needs",(runs +1), "to win the match")
       
       while True:
           user = int(input("you may do bowling:"))
           AI = random.randint(1,6)
           print("AI batting:", AI)
           AIruns += AI
           print("current runs of AI is:", AIruns)
           
           if AIruns > runs:
               print("current runs of AI is:",AIruns)
               
           if AIruns > runs:
               print("AI won the match \n BETTER LUCK NEXT TIME")
               Gameover = True
               break
               
           elif user == AI:
               print("Sucessfully taken the wicket of AI")
               print("You have won the match by",(runs - AIruns),"runs")
               Gameover = True
               break
           
           
def firstbowling():
   global Gameover
   print("Go for yor first bowling")
   runs =0
   AIruns =0 
   
   while not Gameover:
       user = int(input("you may do bowling"))
       AI = random.randint(1,6)
       print("AI batiing:",AI)
       AIruns += AI
       print("current runs of AI is:",AIruns)
       
       if user == AI:
           print("AI is out")
           print("user's turn for batting")
           print("user needs",(AIruns +1),"to win the match")
           
           while True:
               user = int(input("You may do batting"))
               AI= random.randint(1,6)
               print("AI bowling:",AI)
               runs +=user
               print("Current runs of user is:",runs)
               
               if runs > AIruns:
                   print("User won the match ")
                   GameOver = True
                   break
                   
               elif user == AI:
                   print("AI successfully taken the wicket of user")
                   print("AI have won the match by",(AIruns - runs),"runs")
                   GameOver = True
                   break
                 
               
print("WELCOME TO HANDCRICKET")
name=input('enter your name')
toss=input("choose odd or even")
user=int(input('choose a number between 1-6:'))

if user > 6 or user < 0:
   print("invalid input")
else:
   AI=random.randint(1,6)
   print('input of AI:',AI)
   Gameover= False
   if toss.lower()==("even"):
       if (user+AI) % 2 == 0:
           print('You have won the toss\n Batting or Bowling')
           tossinput == input("choose BAT or BALL:")
           if tossinput == "BAT":
               firstbatting()
           elif tossinput =="BAT":              
               firstbowling()
           else:
               print("invalid input")
       
       else:
           print('AI has won the toss')
           AIinput = random.choice(["BAT!", "BALL!"])
           if AIinput == 'BAT!':
               print("AI is batting first")
               firstbowling()
           elif AIinput == 'BALL!':
               print("AI is bowling first")
               firstbatting()
   elif toss.lower() == "odd":
       if (user + AI ) % 2 ==0:
           print("You have won the \nchoose Batting or Bowling")
                
           tossinput = input("choose BAT or BALL:").upper()
           
       
           if tossinput == "BAT":
               firstbatting()
           elif tossinput =="BALL":
               firstbowling()
           else:
               print("Invalid input")
   else:
       print("AI has won the toss")
   AIinput = random.choice(["BAT" , "BALL"])
   if AIinput =="BAT":
       print("AI is batting first")
       firstbowling()
   elif AIinput == "BALL":
       print("AI is bowling first")
       firstbating()
       


# In[ ]:




