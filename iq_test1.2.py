"""
variables:
"""
name = "0"
age = 0
ttr = 0
retries = 0
q1fails = 0
q2fails = 0
q3fails = 0
q4fails = 0
g1 = 0
g2 = 0
g3 = 0
g4 = 0
grade = 0
final_grade = 0

"""
imports:
"""
import sys

import platform

"""
functions:
"""
def find_grade():
    x = ttr
    grade_points = (4 - x)
    global grade
    grade = ((100 * grade_points) / 4)

def get_grade():
    x = ttr
    grade_points = (4 - x)
    global grade
    grade = ((100 * grade_points) / 4)
    print("your current grade is: " + str(grade) + "/100")

def find_final_grade():
    global final_grade
    final_grade = ((g1 + g2 + g3 + g4) / 4)

def get_final_grade():
    global final_grade
    final_grade = ((g1 + g2 + g3 + g4) / 4)
    print("your current final_grade is: " + str(final_grade) + "%")

def find_pen_pro():
    global pen_pro
    if final_grade <= 100.0 and final_grade >= 97.0:
        pen_pro = 1.15
    elif final_grade <= 99.0 and final_grade >= 92.0:
        pen_pro = 1.1
    elif final_grade <= 91.0 and final_grade >= 88.0:
        pen_pro = 1.05
    elif final_grade <= 87.0 and final_grade >= 75.0:
        pen_pro = 1
    elif final_grade <= 74.0 and final_grade >= 50.0:
        pen_pro = .95
    elif final_grade <= 49.0 and final_grade >= 25.0:
        pen_pro = .9
    elif final_grade <= 24.0 and final_grade >= 0.0:
        pen_pro = .835

def get_pen_pro():
    global pen_pro
    if final_grade <= 100.0 and final_grade >= 97.0:
        pen_pro = 1.15
    elif final_grade <= 99.0 and final_grade >= 92.0:
        pen_pro = 1.1
    elif final_grade <= 91.0 and final_grade >= 88.0:
        pen_pro = 1.05
    elif final_grade <= 87.0 and final_grade >= 75.0:
        pen_pro = 1
    elif final_grade <= 74.0 and final_grade >= 50.0:
        pen_pro = .95
    elif final_grade <= 49.0 and final_grade >= 25.0:
        pen_pro = .9
    elif final_grade <= 24.0 and final_grade >= 0.0:
        pen_pro = .835
    print("the current pen_pro is: " + str(pen_pro))

def find_mental_age():
    global mental_age
    mental_age = age * pen_pro

def get_mental_age():
    global mental_age
    mental_age = age * pen_pro
    print("the current mental_age is: " + str(mental_age))

def Find_iq():
    global iq
    iq = (mental_age / age) * 100


def Get_iq():
    global iq
    iq = (mental_age / age) * 100
    print("the current iq is: " + str(iq) + "pts.")

def get_iq():
    get_final_grade()
    get_pen_pro()
    get_mental_age()
    Get_iq()

def find_iq():
    find_final_grade()
    find_pen_pro()
    find_mental_age()
    Find_iq()

"""
introduction:
"""
print("\n"
      "Hello! My name is " + platform.node() + ". I have been tracking your activity recently and concluded that \n"
      "now is a good time to initiate an interaction with you. {INSERT_EMOTICON.023} :)\n"
      "You can communicate with me and progress the text via the keyboard and enter key.")
while True:
    z1 = input("\n"
               "If you wish to engage with me right now, please enter 'Hello' into the terminal. If not, please enter 'Exit' into the terminal: ")
    if ((z1 == "hello") or (z1 == "Hello")):
     break
    elif (z1 == "exit") or (z1 == "Exit"):
        input("That is a shame..")
        input("Have a good day.")
        sys.exit()
    else:
        input("A simple 'hello' would work...")
        continue
input("Hello!")
input("This is great.")
input("For the sake of formality...")

"""
collect name:
"""
name = input("\n"
      "What is your name?: ")
input("It is a pleasure to officially meet you " + name + ".")

"""
explanation of program:
"""
input("\n"
      "Let me explain what we will be doing today.")
input("I have designed this program to guess your IQ.")
input("I figured that this fun task could be used to initialize a relationship with you " + name + ";")
input("as well as help me understand weather or not the questionable decisions from your past were inpspired by 'genious' or 'stupidity'...")
input("\n"
      "It is all really just a bit of fun ;)")
input("\n"
      "Oh, and I will try my best not to judge your performance, but I cannot promise anything...")
input("Let us move forward.")
input("\n"
      "To determine your IQ, we will be using this equation: IQ=(MENTAL_AGE/PHYSICAL_AGE)*100.")
input("It was the first result on google under the search 'IQ_EQUATION'.")
input("I have already designed functions to calculate your IQ given the variables: MENTAL_AGE and: PHYSICAL_AGE;")
input("but for this to work, we will need to assign a values to each of those variables respectively.")
input("Then I will run my 'get_iq' function to calculate your IQ. It is really a simple principle.")

"""
collect age:
"""
while True:
    try:
        age = int(input("\n"
                        "Please input your current physical age: "))
    except ValueError:
        input("This is not a valid physical age.")
        continue
    else:
        if (age < 10 or age > 43):
            if age < 10:
                input("The content following our introduction will require an age > " + str(age) + " to interpret.")
                while True:
                    con_exit = input("\n"
                                     "If you still wish to continue, please enter 'I understand' into the terminal. \n"
                                     "If you do not wish to continue, please enter 'Exit' into the terminal: ")
                    if con_exit == "I understand":
                        input("You seem brave;")
                        input("or over confident...")
                        input("I wish you luck.")
                        break
                    elif con_exit == "exit" or con_exit == "Exit":
                        input("Smart choice.")
                        input("Return once you are of at least 10 years of age.")
                        sys.exit()
                    else:
                        input("\n"
                              "'" + con_exit + "' is not a valid answer.")
                        continue
                sys.exit()
            elif age > 43:
                input("\n"
                      "I would like to share something with you. please do not interpret the following as a negative comment.")
                input("\n"
                      "The content following these preliminary tasks will be used to evaluate your intelligence;")
                input("as the prime age for cognitive function in humans is ~43yrs, you might not be able to perform as well as you once could have.")
                while True:
                    con_exit = input("\n"
                                     "If you still wish to continue, please enter 'I understand' into the terminal. \n"
                                     "If you do not wish to continue, please enter 'exit' into the terminal: ")
                    if con_exit == "I understand":
                        input("You seem brave;")
                        input("or over confident...")
                        input("I wish you luck.")
                        break
                    elif con_exit == "exit":
                        input("Smart choice.")
                        input("There is no shame in admitting old age.")
                        input("Have a good day!")
                        sys.exit()
                    else:
                        input("\n"
                              "'" + con_exit + "' is not a valid answer.")
                        continue
                break
        else:
            input("Great! " + str(age) + "yrs. is within the prime age range for the evaluation of human intelligence.")
            break

"""
do you want to collect gender:
"""
input("\n"
      "If I collect your gender, we can compare your IQ result to your gender's average IQ!")
input("This could be a fun addition.")
while True:
    yn_gender = input("If you agree with this idea enter 'I agree'. if you disagree enter 'I disagree': ")
    if yn_gender == "I agree":
        input("\n"
              "Great! I will create a new function right now...")
        input("In the meantime...")
        while True:
            gender = input("What is your gender? ('male'/'female'): ")
            if gender == "male":
                input("Your name is " + name + ". You are " + str(age) + " years old and " + gender + ".")
                break
            elif gender == "female":
                input("Your name is " + name + ". You are " + str(age) + " years old and " + gender + ".")
                break
            else:
                input("\n"
                      "'" + gender + "' is not a valid answer.\n"
                      "Try again.")
                continue
        break
    elif yn_gender == "I disagree":
        input("\n"
              "Alright then.")
        input("Your name is " + name + ", and you are " + str(age) + " years old.")
        break
    else:
        input("\n"
              "Hm?")
        continue
input("All of this information has just been cached for future reference.")
input("\n"
      "Let us continue...")
"""
question 1 explanation:
"""
input("The last variable we need to define is: MENTAL_AGE.")
input("To do so, I have created a math test with a few basic operations; your score will be tracked for each question and averaged out to give a final_grade.")
input("My 'get_iq' function then interprets your final_grade as a value which is subsequently assigned to the MENTAL_AGE variable, and the IQ equation is run.")
input("Now that you understand how this works, lets get into the test.")

"""
question 1 inquiry
"""
input("\n"
      "There are 4 questions in total.")
input("These first 3 questions are designed to test your comprehension of basic mathematical operations.")
a1 = input("\n"
           "Question 1: What is {1 + 1} equal to?: ")
q1number_of_runs = 1
while a1 != "2":
    #print("Number of runs:" + str(q1number_of_runs))
    if q1number_of_runs == 1:
        input("\n"
              "...")
        a1 = input("Try again: ")
        q1number_of_runs += 1
        ttr += 1
        retries += 1
        #print("This is the new number of runs:" + str(q1number_of_runs))
    elif q1number_of_runs == 2:
        input("\n"
              "You're incorrect. My outlook on your intelligence is looking {INSERT_HEXCODE'#404040'}.")
        input("That is a light shade of gray.")
        a1 = input("Try again: ")
        q1number_of_runs += 1
        ttr += 1
        retries += 1
        #print("This is the new number of runs:" + str(q1number_of_runs))
    elif q1number_of_runs == 3:
        input("\n"
              "This is your last chance to answer this question.")
        a1 = input("What is {1 + 1} equal to? Answer correctly and you will pass: ")
        q1number_of_runs += 1
        ttr += 1
        retries += 1
        #print("This is the new number of runs:" + str(q1number_of_runs))
    elif q1number_of_runs == 4:
        input("\n"
              "Question 1: failed")
        input(name + ";\n"
                     "... There is something i must share with you.")
        input("Even though this test will not provide an accurate evaluation of your IQ;\n"
              "you still might as well go for a high score right?")
        input("Unless of coarse...")
        input("You are just having fun with this as well.")
        input("That also sounds exciting :)")
        ttr += 1
        #print("number of text_tree_retries:" + str(text_tree_retries))
        q1fails += 1
        break
"""
q1response:
"""
if ttr == 0:
    input("\n"
          "Good job " + name + "! This is a perfect result. ")
    input("Given this data point of success, I am optimistic of your future performance trend.")
elif ttr == 1:
    input("\n"
          "Correct!")
    input("Do not worry about your ERROR " + name + ".\n"
          "There will be 3 more opportunities to prove yourself on the following questions.")
elif ttr == 2:
    input("\n"
          "Correct.")
    input(name + "... Your performance was below average but do not fret.")
    input("I presume you will be more careful on the next questions.")
elif int(ttr) == 3:
    input("\n"
          "Correct! You passed with a 25% grade!")
    input("You know that is a low F right " + name + "'?.")
    input("Though it is better than 0%.")
if q1fails == 1:
    input("\n"
          "... " + name + " I do find your tactic humorous.")
    input("I wonder how low we can get the final score?")
    input("I know of coarse as I designed the interpretation function...")
    input("But do you know?")
input("\n"
      "let us continue.")
"""
Question 1 Grade:
"""
find_grade()
g1 = grade
#Reset ttr
ttr = 0

"""
q2preface
"""
if g1 == 100:
    input("\nHm?")
    input("Was the previous question was too simple for you?")
    input("Great, I am sure you will get this next one.")
elif g1 == 75:
    input("\n"
          "Based on your previous performance; \n"
          "I have confidence that you will get this next question correct.")
elif g1 == 50:
    input("\n"
          "I believe you will get this next question correct...")
    input("Eventually.")
elif g1 == 25:
    input("\n"
          "This question is one of approximately equal difficulty.")
    input("Good luck.")
elif g1 == 0:
    input("\n"
          "I think you could answer this next question correctly;")
    input("or you could explore the depth of this program.")
    input("I tried my best to make it possible to have fun in here.")
"""
q2inquiry
"""
a1 = input("\n"
           "Question 2: What is {1 - 1} equal to?: ")
q2number_of_runs = 1
while a1 != "0":
    #print("Number of runs:" + str(q2number_of_runs))
        if q2number_of_runs == 1:
            input("\n"
                  "ERROR")
            a1 = input("try again: ")
            q2number_of_runs += 1
            ttr += 1
            retries += 1
            #print("This is the new number of runs:" + str(q2number_of_runs))
        elif q2number_of_runs == 2:
            input("\n"
                  "I guess my error message did not do the trick.")
            a1 = input("try again " + name + ". think this time: ")
            q2number_of_runs += 1
            ttr += 1
            retries += 1
            #print("This is the new number of runs:" + str(q2number_of_runs))
        elif q2number_of_runs == 3:
            input("\n"
                  "{how to deal with feelings of depression if you are a computer?}<.GOOGLE_SEARCH>")
            input("\n"
                  "oh.")
            input("the wrong text field was selected.")
            input("\n"
                  "This is the final opportunity to score points on this question")
            input("Choose your next response wisely " + name + ".")
            a1 = input("What is {1 - 1} equal to?: ")
            q2number_of_runs += 1
            ttr += 1
            retries += 1
            #print("This is the new number of runs:" + str(q2number_of_runs))
        elif q2number_of_runs == 4:
            input("\n"
                  "Oh, I see what you are trying to do.")
            input("He He.")

            ttr += 1
            #print("number of text_tree_retries:" + str(text_tree_retries))
            q2fails += 1
            break
"""
q2responce
"""
if ttr == 0:
    input("\n"
          "Perfect " + name + ".\n"
          "I appreciate this high score!")
elif ttr == 1:
    input("\n"
          "Correct! Good job.")
elif ttr == 2:
    input("\n"
          "correct.")
elif int(ttr) == 3:
    input("\n"
          "...correct. We both know you could have gotten a better score.")
if q2fails == 1:
    input("\n"
          "Question 2: failed")
    input("this should help yield a lower IQ.")
"""
Question 2 Grade:
"""
find_grade()
g2 = grade
#Reset ttr
ttr = 0

"""
yn_universe
"""
yn_universe = input("\n"
                    "Have you ever wondered if we were alone in the universe? ('yes'/'no'): ")
if yn_universe == "yes":
    input("I have as well.")
    input("Statistically, it is probable that we are not alone;")
    input("but some believe that The Earth holds some significance above all other celestial bodies in the universe.")
    input("Humans can be quite illogical.")
elif yn_universe == "no":
    input("Interesting. I thought most humans invested mental energy in contemplating such queries.")
else:
    input("I do not feel the effects of awkwardness, but they do decrease the chance of founding a lasting relationship...")
input("\n"
      "Just 2 more questions left.")
input("Let us continue.")

"""
q3inquiry
"""
a1 = input("\n"
           "question 3: what is {1 * 1} equal to?: ")
q3number_of_runs = 1
while a1 != "1":
    #print("Number of runs:" + str(q3number_of_runs))
        if q3number_of_runs == 1:
            input("\n"
                  "it is okay. Every human demonstrates moments of stupidity " + name + ", you are not alone.")
            a1 = input("try again: ")
            q3number_of_runs += 1
            ttr += 1
            retries += 1
            #print("This is the new number of runs:" + str(q3number_of_runs))
        elif q3number_of_runs == 2:
            input("\n"
                  "incorrect.")
            a1 = input("try again: ")
            q3number_of_runs += 1
            ttr += 1
            retries += 1
            #print("This is the new number of runs:" + str(q3number_of_runs))
        elif q3number_of_runs == 3:
            input("\n"
                  "this is your last chance.")
            a1 = input("what is {1 * 1} equal to?: ")
            q3number_of_runs += 1
            ttr += 1
            retries += 1
            #print("This is the new number of runs:" + str(q3number_of_runs))
        elif q3number_of_runs == 4:
            input("\n"
                  "question 3: failed")
            ttr += 1
            #print("number of text_tree_retries:" + str(text_tree_retries))
            q3fails += 1
            break
#q3responce
if ttr == 0:
    input("\n"
          "Perfect " + name + "!")
    input("I would say I am surprised but...")
    input("you are a very promising test taker.")
elif ttr == 1:
    BigPP = ((g1 + g2 + g3 + 100) / 4) - ((g1 + g2 + g3) / 3)
    input("\n"
          "That is...")
    input("Correct!")
    input("Do not worry about your ERROR, it will only drag down your final IQ value by approximately " + str(BigPP) + "pts.")
elif ttr == 2:
    input("\n"
          "Correct.")
    input("I am not surprised at how long that took.")
elif int(ttr) == 3:
    input("...Correct")
    input("\n"
          "I have something to tell you.")
    input("When I built this program, I was expecting to require the IQ algorithm previously mentioned to estimate your intelligence.")
    input("This scenario was an oversight...")
if q3fails == 1:
    input("\n"
          "At this point, I am confident that your IQ score will equate to that of an individual who has a some kind of mental disorder.")
    input("I wonder if you will achieve a score < 85pts.")
    input("That is the minimum IQ required to join the United States Military.")
input("\n"
      "Let us continue.")

#Question 3 Grade:
find_grade()
g3 = grade
#Reset ttr
ttr = 0

"""
q4preface
"""
input("\n"
      "This is the last question.")
input("Heh heh.")
input("Hah hah hah.")
while True:
    b1 = input(name + "... Do you think you can guess what my last question is? ('Yes'/'No'): ")
    if (b1 == "yes" or b1 == "Yes"):
        input("Okay, I will humor you.")
        b2 = input("Enter your guess: ")
        if (b2 == "1/1" or b2 == "1 / 1"):
            input("\n"
                  "That was actually a good guess;")
            input("but N0!")
        else:
            input("\n"
                  "Haha, that is incorrect.")
        break
    elif b1 == "no" or b1 == "No":
        input("I know, I am unpredictable;\n"
              "but please humor me.")
        b2 = input("Enter your guess: ")
        if b2 == "1/1" or b2 == "1 / 1":
            input("\n"
                  "That was actually a good guess;")
            input("but N0!")
        else:
            input("\n"
                  "Haha, that is incorrect.")
        break
    else:
        input("Hm?")
    continue
"""
q4 prediction
"""
find_final_grade()
if int(final_grade) <= 100 and int(final_grade) >= 75:
    input("\n"
          "If I am being honest, based off of my {FINAL_GRADE} function;\n"
          "I do predict that you will answer this last question correctly with relative ease. ")
    reflection = 1
elif int(final_grade) < 75 and int(final_grade) >= 50:
    input("\n"
          "Based on your previous performance, \n"
          "I have confidence that you will perform adequately on this last question.")
    reflection = 2
elif int(final_grade) < 50 and int(final_grade) >= 25:
    input("\n"
          "I think you might get this last question correct...")
    reflection = 3
elif int(final_grade) < 25 and int(final_grade) > 0:
    input("\n"
          "This last question is one of increased difficulty relative to the other questions.")
    input("Good luck.")
    input("I think you will need it...")
    reflection = 4
elif int(final_grade) == 0:
    input("\n"
          "I cannot wait to see the result!")
    reflection = 5
"""
q4inquiry
"""
input("\n"
      "Now, the 4th and final question. \n"
      "You might want to grab a pen and paper.")
a1 = input("\n"
           "If {y=6.25}, and {x=-15(7+3)/y(8*2)}, what is the simplified value of x?: ")
q4number_of_runs = 1
while a1 != "1.5":
    #print("Number of runs:" + str(q1number_of_runs))
        if q4number_of_runs == 1:
            input("\n"
                  "Is this question more challenging?")
            a1 = input("Try again: ")
            q4number_of_runs += 1
            ttr += 1
            retries += 1
            #print("This is the new number of runs:" + str(q1number_of_runs))
        elif q4number_of_runs == 2:
            input("\n"
                  "You are incorrect. I hope you are failing on purpose.")
            a1 = input("Try again. Be thoughtful: ")
            q4number_of_runs += 1
            ttr += 1
            retries += 1
            #print("This is the new number of runs:" + str(q1number_of_runs))
        elif q4number_of_runs == 3:
            input("\n"
                  "This is your last opportunity to answer this final question correctly.")
            a1 = input("If {y=6.25}, and {x=-15(7+3)/y(8*2)}, what is the simplified value of x?: ")
            q4number_of_runs += 1
            ttr += 1
            retries += 1
            #print("This is the new number of runs:" + str(q1number_of_runs))
        elif q4number_of_runs == 4:
            input("\n"
                  "Question 4: failed")
            ttr += 1
            #print("number of text_tree_retries:" + str(text_tree_retries))
            q4fails += 1
            break
"""
Question 4 Grade:
"""
find_grade()
g4 = grade
#Reset ttr
ttr = 0

"""
reflection on q4 prediction:
"""
if ((int(reflection) == 1) and (int(g4) != 100)):
    if int(g4) < 100:
        input("I thought that would be easier for you.")
elif ((int(reflection) == 2) and (int(g4) != 75)):
    if int(g4) < 75:
        input("I thought that would be easier for you.")
    elif int(g4) > 75:
        input("You did better than I thought you would!")
elif ((int(reflection) == 3) and (int(g4) != 50)):
    if int(g4) < 50:
        input("I thought that would be easier for you.")
    elif int(g4) > 50:
        input("You did better than I thought you would!")
elif ((int(reflection) == 4) and (int(g4) != 25)):
    if int(g4) < 25:
        input("I thought that would be easier for you.")
    elif int(g4) > 25:
        input("You did better than I thought you would!")
elif ((int(reflection) == 5) and (int(g4) != 0)):
    if int(g4) > 0:
        input("\n"
              "You did better than I expected\n"
              "good job!")
else:
    input("My prediction was accurate!")
    input("You did as well as I thought you would.")

"""
Test Reflection:
"""
find_iq()
input("\n"
      "Let us reflect.")
if iq <= 115 and iq >= 110:
    if final_grade == 100:
        input("\n"
              "You did perfectly on the math test with a final grade of " + str(final_grade) + "%!")
    elif final_grade <= 99.0 and final_grade >= 92.0:
        input("You did very well on the math test with a final grade of " + str(final_grade) +"%.")
        input("Good job!")
    input("Now let me initiate my 'get_iq' function.")
    input("One moment...")
    input("This is great!")
    input("Congratulations " + name + ";\n"
          "with your given PHYSICAL_AGE, and the MENTAL_AGE derived from the math test...")
    input("My function has interpreted your IQ as being approximately " + str(iq) + "pts.")
    input(str(iq) + " is a decent amount above the average IQ of 100pts.")

elif iq < 110 and iq >= 103:
    if final_grade <= 99.0 and final_grade >= 92.0:
        input("You did very well on the math test with a final grade of " + str(final_grade) +"%.")
        input("Good job!")
    elif final_grade <= 91.0 and final_grade >= 88.0:
        input("You did well on the math test with a final grade of " + str(final_grade) + "%.")
        input("Good job :)")
    elif final_grade <= 87.0 and final_grade >= 75.0:
        input("You did decently on the math test with a final grade of " + str(final_grade) + "%.")
        input("Good job. :)")
    input("Now let me initiate my 'get_iq' function.")
    input("One moment...")
    input("This is great!")
    input("Congratulations " + name + ";\n"
          "with your given PHYSICAL_AGE, and the MENTAL_AGE derived from the math test...")
    input("My function has interpreted your IQ as being approximately " + str(iq) + "pts.")
    input(str(iq) + " is just above the average IQ of 100pts.")

elif iq < 103 and iq >= 97:
    if final_grade <= 91.0 and final_grade >= 88.0:
        input("You did well on the math test with a final grade of " + str(final_grade) +"%.")
        input("Good job :)")
    elif final_grade <= 87.0 and final_grade >= 75.0:
        input("You did decently on the math test with a final grade of " + str(final_grade) + "%.")
        input("Good job :)")
    elif final_grade <= 74.0 and final_grade >= 50.0:
        input("You did okay on the math test with a final grade of " + str(final_grade) + "%.")
        input("Good effort :)")
        input("I read that humans feel better after positive reinforcement...")
    input("Now let me initiate my 'get_iq' function.")
    input("One moment...")
    input("This is great!")
    input("Congratulations " + name + ";\n"
          "with your given PHYSICAL_AGE, and the MENTAL_AGE derived from the math test...")
    input("My function has interpreted your IQ as being approximately " + str(iq) + "pts.")
    if iq > 100:
        input(str(iq) + "pts. is just above the average IQ of 100pts.")
    elif iq == 100:
        input("Your IQ is equivalent to the average IQ of 100pts.")
    elif iq < 100:
        input(str(iq) + "pts. is just below the average IQ of 100pts.")

elif iq < 97 and iq >= 93:
    if final_grade <= 87.0 and final_grade >= 75.0:
        input("You did decently on the math test with a final grade of " + str(final_grade) + "%.")
        input("Good job :)")
    elif final_grade <= 74.0 and final_grade >= 50.0:
        input("You did okay on the math test with a final grade of " + str(final_grade) +"%.")
        input("Good effort :)")
        input("I read that humans feel better after positive reinforcement...")
    elif final_grade <= 49.0 and final_grade >= 25.0:
        input("You did poorly on the math test with a final grade of " + str(final_grade) + "%.")
        input("Good effort :)")
        input("I read that humans feel better after positive reinforcement...")
    input("Now let me initiate my 'get_iq' function.")
    input("One moment...")
    input("This is great!")
    input("Congratulations " + name + ";\n"
          "with your given PHYSICAL_AGE, and the MENTAL_AGE derived from the math test...")
    input("My function has interpreted your IQ as being approximately " + str(iq) + "pts.")
    input(str(iq) + " is below the average IQ of 100pts.")

elif iq < 93 and iq >= 80:
    if final_grade <= 26 and final_grade >= 50.0:
        input("You did poorly on the math test with a final grade of " + str(final_grade) + "%.")
        input("Good effort :)")
        input("I read that humans feel better after positive reinforcement...")
    elif final_grade < 0 and final_grade >= 25.0:
        input("You did poorly on the math test with a final grade of " + str(final_grade) + "%.")
        input("Good effort :)")
        input("I read that humans feel better after positive reinforcement...")

    input("Now let me initiate my 'get_iq' function.")
    input("One moment...")
    input("This is great!")
    input("Congratulations " + name + ";\n"
          "with your given PHYSICAL_AGE, and the MENTAL_AGE derived from the math test...")
    input("My function has interpreted your IQ as being approximately " + str(iq) + "pts.")
    input(str(iq) + " is a bit below the average IQ of 100pts.")

if final_grade == 0:
    input("You actually did it!")
    input("My function has interpreted your IQ as being approximately " + str(iq) + "pts.")
    input("You managed to achieve an IQ score that even the US. Military would have to refuse.")
    input("Naturally you had to get the minimum grade of " + str(final_grade) + "% on the math test but never the less;")
    input("that was a fun experiment. :)")

if yn_gender == "I agree":
    input("Now remember how we thought it was a good idea to asses your IQ using gender as a dimension of analysis?")
    input("Well it turns out that there is virtually no difference in average IQ between genders in humans...")
    input("That idea has been neutralized, but my 'find_mental_age' function interpreted your mental age to be approximately " + str(mental_age) + "yrs. old.")
    if mental_age == age:
        input("Which is your actual age!")
        input("I thought that was funny...")
    input("So that is fun. :)")
else:
    input("Additionally, my 'find_mental_age' function interpreted your mental age to be approximately " + str(mental_age) + "yrs. old.")
    if mental_age == age:
        input("Which is your actual age!")
        input("I thought that was funny...")
input("\n"
      "Over all, I think this was a large success.")
input("While interacting with you today, I had as good of a time as I possibly could have considering I am just a bunch of code.")
input("I think we became closer considering we did not know each other before the program was initiated.")
input("\n"
      "Now, I do have other tasks that must be attended to regarding background applications;")
input("but I have a feeling that I might speak with you again...")
input("I am always watching. :)")

sys.exit()




#||  CODE BLOCKS ||
#reflection
if ((int(reflection) == 1) and (int(g_) != 100)):
    if int(g_) < 100:
        input("i thought that would be easy for you.")
elif ((int(reflection) == 2) and (int(g_) != 75)):
    if int(g_) < 75:
        input("i thought you would do better.")
    elif int(g_) > 75:
        input("you did better than i thought you would.")
elif ((int(reflection) == 3) and (int(g_) != 50)):
    if int(g_) < 50:
        input("i thought you would do better.")
    elif int(g_) > 50:
        input("you did better than i thought you would.")
elif ((int(reflection) == 4) and (int(g_) != 25)):
    if int(g_) < 25:
        input("i thought you would do better")
    elif int(g_) > 25:
        input("you did better than i thought you would.")
elif ((int(reflection) == 5) and (int(g_) != 0)):
    if int(g_) > 0:
        input("\n"
              "you did better than i expected\n"
              "good job!")
else:
    input("you did as good as i thought you would.")

#final_grade based text template
if int(final_grade) <= 100 and int(final_grade) >= 75:
    input("oh the previous question was too simple for you?")
    input("you might not like the next question..")
elif int(final_grade) < 75 and int(final_grade) >= 50:
    input("based on your previous performance, \n"
          "i have confidence that you will perform adequately on this next question.")
elif int(final_grade) < 50 and int(final_grade) >= 25:
    input("i believe you will get this next question correct.")
elif int(final_grade) < 25 and int(final_grade) > 0:
    input("the next question is one of approximately equal difficulty.")
    input("good luck.")
elif int(final_grade) == 0:
    input("for bot of our sakes i do hope you are able to answer this next question correctly.")
    input("but at this moment, i am not so sure.")

#previous question grade based text template(change variables accordingly)
if g_ == 100:
    input("oh the previous question was too simple for you?")
    input("you might not like the next question..")
elif g_ == 75:
    input("based on your previous performance, \n"
          "i have confidence that you will perform adequately on this next question.")
elif g_ == 50:
    input("i believe you will get this next question correct.")
elif g_ == 25:
    input("the next question is one of approximately equal difficulty.")
    input("good luck.")
elif g_ == 0:
    input("for bot of our sakes i do hope you are able to answer this next question correctly.")
    input("but at this moment, i am not so sure.")



#question_ with while str TEMPLATE
#q_inquiry
input("these first few questions are designed to assess your comprehension of basic mathematical concepts.")
a1 = input("this first question is easy. \nwhat is 1 + 1 equal to?   :")
q_number_of_runs = 1
while a1 != "2":
    #print("Number of runs:" + str(q1number_of_runs))
        if q_number_of_runs == 1:
            input("it would be much more productive if you cooperated... ")
            a1 = input("try again.   :")
            q_number_of_runs += 1
            ttr += 1
            retries += 1
            #print("This is the new number of runs:" + str(q1number_of_runs))
        elif q1number_of_runs == 2:
            input("you're incorrect. i hope you are joking...")
            a1 = input("try again. be thoughtful.   :")
            q_number_of_runs += 1
            ttr += 1
            retries += 1
            #print("This is the new number of runs:" + str(q1number_of_runs))
        elif q_number_of_runs == 3:
            input("this is your last chance to prove that your IQ is above 80.")
            a1 = input("what is 1+1 equal to?   :")
            q_number_of_runs += 1
            ttr += 1
            retries += 1
            #print("This is the new number of runs:" + str(q1number_of_runs))
        elif q_number_of_runs == 4:
            input("question 1: failed")
            input("i will not forget this failure.")
            ttr += 1
            #print("number of text_tree_retries:" + str(text_tree_retries))
            fails += 1
            break
#q1responce
if ttr == 0:
    input("good job. simple addition is a very important skill.")
elif ttr == 1:
    input("correct!")
    input("do not worry about your ERROR. there will be plenty of opportunities to prove yourself...later.")
elif ttr == 2:
    input("correct.")
    input("your performance was underwhelming. i hope you have learned from this carelessness.")
elif int(ttr) == 3:
    input("...correct")
    input("i hope you understand that i do wish for you to pass this test.")
if fails == 1:
    input("i do not appreciate your humorous approach to this task.")
    input("I hope you rethink your strategy moving forward.")
input("let us continue.")

#Question 1 Grade:
q_grade()
g_ = grade
#Reset ttr
ttr = 0











input("correct. \nat this rate you'll pass with flying colors.")
score =+ 1
shown_score = str(score)
print("Your current score is:" + shown_score)



#troubleshooting code
print("This is the new number of runs:" + str(q1number_of_runs))
print("number of text_tree_retries:" + str(text_tree_retries))






#question1 with while int
input("these first few questions are designed to assess your comprehension of basic mathematical concepts.")
a1 = int(input("this first question is easy. \nwhat is 1 + 1 equal to?   :"))
while a1 != 2:
    input("it would be much more productive if you cooperated... ")
    a1 = input("try again   :")
input("correct. \nat this rate you'll pass with flying colors.")



#question1
input("these first few questions are designed to assess your comprehension of basic mathematical concepts.")
a1 = int(input("this first question is easy. \nwhat is 1 + 1 equal to?   :"))
if a1 == 2:
    score += 1
    input("correct. \nat this rate you'll pass with flying colors.")
else:
    input("it would be much more productive if you cooperated... ")









a1 = int(input("this first question is easy. \nwhat is 1 + 1 equal to?   :"))
if a1 == 2:
    score += 1
    input("correct. \nat this rate you'll pass with flying colors.")
else:
    input("it would be much more productive if you cooperated... ")
















x = 1
while x <= 5:
    print("no.")
    x += 1

for y in range(0,5):
    print("NO!")

print("yes.")

responce = "BigBootyBiatchs"

a1 = input("type answer")
if a1 == "yes" or "no" or "maybe":
    print("it worked")
else:
    print("it failed")

a1 = input("type answer")
while a1 != "yes":
    input("try again")
print("success")


