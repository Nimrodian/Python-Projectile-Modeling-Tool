# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 14:29:02 2017

@author: Joe
"""

#Projectile modelling game.

#This is where I have imported all of the necessary modules, sqlite3 for the database back end, where I will store the user's game scores. Numpy for my maths calculations. Matplotlib to plot the trajectory of all of my projectile calculations. Math also for my maths calculation (sqrt etc.) Random, to be pick a random set of variables for the projetiel game. And finally, time, to be able to time how long it takes for a user to enter a guess when playing the game.

import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import math
import random 
import time

score = 0
counter = 0
overall_time = 0
won = 0
game = 0

#This subroutine (menu) is here as the main menu, to welcome the user to the program, and show them the options available to them. This will be looped back to, every time a user enters an option.

def menu():
    print ("""
  ┌──────────────────────────────────────────────┐
  ┃  |P|r|o|j|e|c|t|i|l|e| |G|a|m|e              ┃
  └──────────────────────────────────────────────┘""")
    print(""" 
  ┌──────────────────────────────────────────────┐
  ┃  To play the game, enter 1                   ┃
  ┃  To enter a calculation on its own, enter 2  ┃
  ┃  To try a pre-set example, enter 3           ┃
  ┃  To display the high score board, enter 4    ┃
  ┃  To find a users score, enter 5              ┃
  ┃  To quit the program, enter 6                ┃
  └──────────────────────────────────────────────┘""")

#This subroutine is here to get the users main menu choice after the code has ran through the main menu above, and then returning their valid input. There is a try and except here to only allow values between 1 and 7 to be passed, and with an exception for value errors like entering a float.
    
def get_main_choice(menu_choice): 
    while True:
        try:
            choice = int(input("Please enter your main menu choice: "))
            if choice <=6 and choice >= 1:
                return choice
            else:
                print ("Error 1: you need to enter a valid menu choice.")
        except ValueError:
            print ("Error 2: you need to enter a valid menu choice.")

#This subroutine is here to get the users input when they have selected option 3 on the main menu, to try a projectile example on another planet. I have carried the list of valid planets in our solar system in the parameters of the subroutine; "planets". If the user enters a planet that is in the list of planets, it will return the choice to the main() subroutine. If not, it will loop back and ask again. The try and except here has an exception for a value error also. 

def examples(planets):
    print ("""\nTrajectory is all dependent on g, Gravity
and since it varies, planet to planet here you can see by how much...""")
    while True:
        try:
            planet = str(input("Please enter a planet in our solar system to try: ")).lower()
            if planet in planets:
                return planet
            else:
                print ("\nError 1: Sorry you need to enter a valid planet.")
        except ValueError:
            print ("\nError 2: Sorry you need to enter a valid planet.")

#This subroutine is here to run through the calculations once the user has entered "3" on the main menu, and then entered a valid planet in the subroutine above. The calculations use physics algorithms and formulas to translate a velocity of 28 metres per second and an angle of 60 degrees into the x and y coordinates needed to plot a graph using matplotlib. You can see all of these calculations in the processing section of my write up for this projectile modeling tool. This subroutine utilizes complex mathematical algorithms.

def planet_calculation(g):
    print("\nThis is for a projectile being fired with an\nInitial velocity of 28m/s, and from an angle of 60 degrees")
    print (g)
    v = 28 
    angle = (60)/180.0*np.pi 
    plt.figure()
    time_max = ((2 * v) * np.sin(angle)) / g
    time = time_max*np.linspace(0,1,100)[:,None] 
    x = ((v * time) * np.cos(angle))
    y = ((v * time) * np.sin(angle)) - ((0.5 * g) * (time ** 2))
    plt.plot(x,y, linewidth = 2.5) 
    plt.ylim([0,200])
    plt.xlim([0,200])
    plt.show()   

#This subroutine is here to get the users option, after they select option 2 on the main menu, for if they want to fire the projectile from a height or from the origin (no height) and then return the value to main().

def height_or_not():
    while True:
        try:
            choice = str(input("Do you want to fire from a height or from level ground?\n Enter 'h' or 'o':"))
            if choice == "h" or choice == "o":
                return choice
            else:
                print ("Error 1: you need to enter a valid option.")
        except ValueError:
            print ("Error 2: you need to enter a valid option.")

#This subroutine is to run through calculations and plot the trajectory when the user enters 2 on the main menu and selects "o" for from the origin. The user is prompted to enter two variables, speed and angle, with appropriate error handling that will only accept inputs between set limits, and will not accept value errors. The calculations use physics algorithms and formulas to translate a velocity and angle into the x and y coordinates needed to plot a graph using matplotlib. You can see all of these calculations in the processing section of my write up for this projectile modeling tool. This subroutine utilizes complex mathematical algorithms.

def origin_calculation():
    print ("\nWhen firing a projectile from the origin\nWe need the angle and velocity it is being fired at\n To calculate it's trajectory...")
    while True:
        try:
            angle_0 = float(input("Please enter the angle you want it to be fired at\n(Between 1 and 90) : "))
            abs(angle_0)
            if angle_0 <= 90 and angle_0 >= 1:
                angle_0 = (angle_0)/180.0*np.pi
                break
            else:
                print ("\nError 1: you need to enter a valid number.")
        except ValueError:
            print ("\nError 2: you need to enter a valid number.")
    while True:
        try:
            speed = float(input("Please enter the initial velocity you want it be fired at\nIn meters per second (Between 0 and 1000) : "))
            if speed <= 1000 and speed >= 0:
                break
            else:
                print ("\nError 1: you need to enter a valid number.")
        except ValueError:
            print ("\Error 2: you need to enter a valid number.")
    g = 9.81
    plt.figure()
    time_max = ((2 * speed) * np.sin(angle_0)) / g
    time_1 = time_max*np.linspace(0,1,100)[:,None]
    x_values = ((speed * time_1) * np.cos(angle_0))
    y_values = ((speed * time_1) * np.sin(angle_0)) - ((0.5 * g) * (time_1 ** 2)) 
    distance_x = (speed * np.cos(angle_0))*time_max 
    plt.plot(x_values,y_values, linewidth = 1.5)
    plt.ylim([0,1000])
    plt.xlim([0,1000])
    plt.show()   
    print ("\nThe Range of this projectile will be, "+str(distance_x)+" metres!")

#This subroutine is to run through calculations and plot the trajectory when the user enters 2 on the main menu and selects "h" for from a height. The user is prompted to enter three variables, speed and angle and height, with appropriate error handling that will only accept inputs between set limits, and will not accept value errors. The calculations use physics algorithms and formulas to translate a velocity, angle and height into the x and y coordinates needed to plot a graph using matplotlib. You can see all of these calculations in the processing section of my write up for this projectile modeling tool. This subroutine utilizes complex mathematical algorithms.
    
def height_calculation():      
    print ("\nWhen firing a projectile from a height\nWe need the angle, velocity and the height\nIt is being fired from to calculate it's trajectory...") 
    while True:
        try:
            angle_0 = float(input("\nPlease enter the angle you want it to be fired at\n(Between 0 and 90) : "))
            abs(angle_0)
            if angle_0 <= 90 and angle_0 >= 0:
                angle_0 = (angle_0)/180.0*np.pi
                break
            else:
                print ("\nError 1: you need to enter a valid number.")
        except ValueError:
            print ("\nError 2: you need to enter a valid number.")
    while True:
        try:
            height = float(input("\nPlease enter the starting height for the projectile to be fired at\n(Between 0 and 1000) : "))
            abs(height)
            if height <= 1000 and height >= 0:
                break
            else:
                print ("\nError 1: you need to enter a valid number.")
        except:
            print ("\nError 2: you need to enter a valid number.")
    while True:
        try:
            speed = float(input("\nPlease enter the initial velocity you want it to be fired at\nIn metres per second (Between 0 and 1000) : "))
            abs(speed)
            if speed <= 1000 and speed >= 0:
                break
            else:
                print ("\nError 1: you need to enter a valid number.")
        except ValueError:
            print ("\nError 2: you need to enter a valid number.")
    g = 9.81
    plt.figure()
    velocity = (speed) * np.sin(angle_0)
    time_height = (velocity / g)
    height_0 = (velocity * time_height) - (0.5 * g * (time_height ** 2))
    h_max = height_0 + height
    print (h_max)
    good_time = (h_max / 2)/g
    time = good_time*np.linspace(0,1,100)[:,None]
    x_values = ((speed * time) * np.cos(angle_0))
    y_values = ((speed * time) * np.sin(angle_0)) - ((0.5 * g) * (time ** 2)) 
    calc_1 = speed * np.sin(angle_0)
    calc_2 = math.sqrt((speed ** 2 *(0.5-(0.5*np.cos(2 * angle_0)))) + (2 * g * height))    
    distance_x = (speed * np.cos(angle_0)*((calc_1 + calc_2)) / g)     
    plt.plot(x_values,[i+(height) for i in y_values], linewidth = 1.5)
    plt.ylim([0,1000])
    plt.xlim([0,1000])
    plt.show()
    print ("\nThe Range of this projectile will be, "+str(distance_x)+" metres!")    
    for x, y in zip(y_values, x_values):
        if x == 0 or y == 0:
            print(x, y)
    return       

#This subroutine is the main aspect of my program, the projectile range guessing game. The code will randomly produce three sets of variables, for angle, speed and height, and the user will be timed, when guessing the range of the projectile that is shown to them. The limits on where they can gain a point are made by multiplying the real range of the random projectile and setting limits based on the difficulty; 1 (easy) within 75% - 125%, 2 (medium) within 85% - 115% and 3 (hard) within 95% - 105%. Once the user has guessed the counter is incremented, and if they are on their third try and have got all three correct then they are added to the appropriate high score board. The calculations use physics algorithms and formulas to translate a velocity, angle and height into the x and y coordinates needed to plot a graph using matplotlib. You can see all of these calculations in the processing section of my write up for this projectile modeling tool. This subroutine utilizes complex mathematical algorithms.

def go_game(difficulty):
    global overall_time
    global score 
    global counter
    global won
    global game
    speed = float(random.randint(20,100))
    angle = float(random.randint(5,85))
    height = float(random.randint(1,500))    
    print ("\nThe speed is "+str(speed),"m/s")
    print ("\nThe angle is "+str(angle),"m/s")
    print ("\nThe height is "+str(height),"m/s") 
    angle = (angle)/180.0*np.pi
    g = 9.81
    plt.figure()
    velocity = (speed) * np.sin(angle)
    time_height = (velocity / g)
    height_0 = (velocity * time_height) - (0.5 * g * (time_height ** 2))
    h_max = height_0 + height
    good_time = (h_max / 2)/g
    time_1 = good_time*np.linspace(0,1,100)[:,None]
    x_values = ((speed * time_1) * np.cos(angle))
    y_values = ((speed * time_1) * np.sin(angle)) - ((0.5 * g) * (time_1 ** 2)) 
    calc_1 = speed * np.sin(angle)
    calc_2 = math.sqrt((speed ** 2 *(0.5-(0.5*np.cos(2 * angle)))) + (2 * g * height))    
    distance_x = (speed * np.cos(angle)*((calc_1 + calc_2)) / g)     
    if difficulty == 1:
        lower_limit = 0.75 * (distance_x)
        higher_limit = 1.25 * (distance_x)
    if difficulty == 2:
        lower_limit = 0.85 *(distance_x)
        higher_limit = 1.15 * (distance_x)
    if difficulty == 3:
        lower_limit = 0.95 * (distance_x)
        higher_limit = 1.05 * (distance_x)
    while True:
        try:
            start = time.time()
            guess = float(input("\nPlease enter your guess:"))
            end = time.time()            
            break
        except ValueError:
            print("\nError 2: you need to enter a valid number.")
    plt.plot(x_values,[i+(height) for i in y_values], linewidth = 1.5)
    plt.ylim([0,1000])
    plt.xlim([0,1000])
    plt.show()
    overall_time = overall_time + (end-start)
    print (overall_time)
    print ("\nThe Range of this projectile will be, "+str(distance_x)+" metres!")
    if guess >= lower_limit and guess <= higher_limit:
        print ("\nWell done you guessed close enough to get a point!")
        score = score + 1
        counter = counter + 1
        if counter == 3:
            if score == 3:
                print ("\nYou have won!")
                print ("To view the high score leader, select 4 on the main menu!")                
                game = 1
                won = 1
                return game
                return overall_time
            else:
                print ("\nSorry you only got "+str(score))
                print ("\nGAME OVER. You have lost, try again from the main menu")               
                game = 1 
                return game
                return overall_time
    else:
        print("\nSorry you didn't get close enough for a point.")
        counter = counter + 1
        if counter == 3:
                print ("\nSorry you only got "+str(score))
                print ("\nGAME OVER. You have lost, try again from the main menu")
                game = 1
                return game
                return overall_time

#This subroutine gets the users input for what difficulty they want to use for the game after they have entered 1 on the main menu. With error handling that only accepts inputs between 0 and 4, and declines inputs with value errors. This subroutine then returns the users selected difficulty to the main() block of code.
    
def get_diff():
    print ("""\nThis game will present 3 sets of random projectile variables
    that you will have to guess the range of. And getting
    3 out of 3 correct will make you a winner, your time 
    will be recorded, and if it is lower than other previous
    times, you will be made highest scorer. 
    
    But first you must select your difficulty setting (1-3).
    1 being easy, 3 being hard.""")
    while True:
        try:
            difficulty = int(input("\nDifficulty setting: "))
            if difficulty <=3 and difficulty >=1:
                return difficulty
            else:
                print("\nError 1: you need to enter a valid difficulty.")
        except ValueError:
            print ("\nError 2: you need to enter a valid difficulty.")

#This subroutine is here to add a users name and score to the database of winners. Carrying two parameters; the user's time (score) and the difficulty the user played the game with. This section of code asks for the users username, with it only being accepted if it isn't blank or being caught by a value error. The SQLite3 functions add the user's score and the time to the corresponding table withing the high score database. Using useful SQL functions.

def high_scores(overall_time, difficulty):
    current_score = float(overall_time)
    while True:
        try:
            player_name = str(input("\nPlease enter your name to go next to your score: "))
            if player_name == (""):
                print ("\nError 1: you need to enter a valid name.")
            else:
                False
        except ValueError:
            print ("\nError 2: you need to enter a valid name.")
        break
    con = sqlite3.connect("highscore.db")
    cur = con.cursor()
    cur.execute("INSERT INTO scores VALUES (?, ?)", (player_name, current_score))
    con.commit()

#This subroutine is here to perform a merge sort on the list of scores collected from the database back end. It will be called upon when the user selects option 4 on the main menu, which is to display the high score board. Since the scores, when stored in the database are unsorted this block of code will sort them so they can be returned to main() and be displayed alongside their usernames. A merge-sort is an efficient, sorting algorithm. It works by dividing the list into multiple sublists until you only have lists with single elements (which are sorted), then merge each sublist, comparing the values to each one, and repeat until you have a full list like you did at the beginning, but sorted in order. This block of code uses three different types of "A" bracket programming techniques; A merge sort, a recursive algorithm, and multiple list operations.
    
def merge_sort(scores):
    if len(scores)>1:
        split = len(scores)//2
        left = scores[:split]
        right = scores[split:]
        merge_sort(left)
        merge_sort(right)
        x=0
        y=0
        z=0
        while x < len(left) and y < len(right):
            if left[x] < right[y]:
                scores[z]=left[x]
                x=x+1
            else:
                scores[z]=right[y]
                y=y+1
            z=z+1
        while x < len(left):
            scores[z]=left[x]
            x=x+1
            z=z+1
        while y < len(right):
            scores[z]=right[y]
            y=y+1
            z=z+1

#This subroutine is here to create the database using the SQLite3 commands. This code will create a database file, with three tables in, scores, scores2, and scores3. All with two columns, user and score. The reason this is in a try and except is because when the program try's to run the code that creates the database with the tables, and it fails (because it already exists) it will return and carry on with the program. In the case it doesn't exist yet, it will run the creation code and the database will be initialised in the same directory as the Projectile modeling tool.

def create_database():
    while True:
        try:
            con = sqlite3.connect("highscore.db")
            cur = con.cursor()
            cur.execute("CREATE TABLE scores (user, score)")
            cur.execute("CREATE TABLE scores2 (user, score)")
            cur.execute("CREATE TABLE scores3 (user, score)")
            con.commit()
            con.close()
            return
        except:
            pass
        return con

#This subroutine is here to navigate the menu and all of its options. The global variables at the start are there for the go_game() subroutine, and the planets dictionary is there to store the gravity constants on each planet to be used on option 3 on the main menu. While the menu option the user enters is not 6 (quit) the main() subroutine will run through the IF statements for when each menu option is selected. If menu option 1 is selected get_diff() is called, to get the difficulty, then go_game() is called to run through the game aspect. If menu option 2 is selected, height_or_not() is called, and depending on the user's input, either origin_calculation() or height_calculation() is called. If menu option 3 is called, planets() is called to get the users choice for a planet, then planet_calculation() is called to run through the projectile trajectory calculations and plot the trajectory. If option 4 is selected by the user on the main menu, the scores from each difficulty table will be taken from the database, then ran through a merge sort (merge_sort called) and finally searched against their user names and the high score leader board displayed. If the user then selects 5 on the main menu to search for a specific name, they are asked for a name (with appropriate value error handling) and then the database is searched for that name and the corresponding score (if it exists) is displayed.

def main():               
    global counter
    global score
    global game
    global overall_time 
    global won
    planets = {"mercury":3.76, "venus": 9.04, "earth":9.8, "mars":3.77, "jupiter":23.6, "saturn":10.06, "uranus": 8.87, "neptune":11.23, "moon": 1.6}            
    menu_choice = 0
    while not menu_choice == 6:
        menu()
        menu_choice = get_main_choice(menu_choice)
        if menu_choice == 1:
            difficulty = get_diff()
            game = 0
            score = 0
            counter = 0  
            overall_time = 0
            won = 0
            while not game == 1:
                go_game(difficulty)
            if won == 1:
                high_scores(overall_time, difficulty)
        if menu_choice == 2:
            choice = height_or_not()
            if choice == "o":
                origin_calculation()
            else:
                height_calculation()
        if menu_choice == 3:
            planet = examples(planets)
            g = planets[planet]
            planet_calculation(g)
        if menu_choice == 4:
            con = sqlite3.connect("highscore.db")
            cur = con.cursor()
            cur.execute("SELECT score FROM scores")
            scores = list(cur.fetchall())
            merge_sort(scores)
            print ("\nHigh Score leader-board for difficulty setting 1:")
            print("")
            for x in scores:
                    y = cur.execute("SELECT * FROM scores WHERE score=?", (x))
                    y = str(cur.fetchone())
                    print (y)
            cur.execute("SELECT score FROM scores2")
            scores = list(cur.fetchall())
            merge_sort(scores)
            con = sqlite3.connect("highscore.db")
            cur = con.cursor()
            print ("\nHigh Score leader-board for difficulty setting 2:")
            print("")
            for x in scores:
                    y = cur.execute("SELECT * FROM scores2 WHERE score=?", (x))
                    y = str(cur.fetchone())
                    print (y)
            cur.execute("SELECT score FROM scores3")
            scores = list(cur.fetchall())
            merge_sort(scores)
            con = sqlite3.connect("highscore.db")
            cur = con.cursor()
            print ("\nHigh Score leader-board for difficulty setting 3:")
            print("")
            for x in scores:
                    y = cur.execute("SELECT * FROM scores3 WHERE score=?", (x))
                    y = str(cur.fetchone())
                    print (y)
        if menu_choice == 5:
            con = sqlite3.connect("highscore.db")
            cur = con.cursor()
            player_name = str(input("Please enter the user you want to know the score of: "))
            cur.execute("SELECT * FROM scores WHERE user=?", (player_name,))
            if str(cur.fetchone()) == "None":
                print ("\nSorry, no record for this user for difficulty 1.")
            else:
                cur.execute("SELECT * FROM scores WHERE user=?", (player_name,))
                print("")
                print ((player_name), "'s record for difficulty 1: "+str(cur.fetchone()))
            cur.execute("SELECT * FROM scores2 WHERE user=?", (player_name,))
            if str(cur.fetchone()) == "None":
                print ("\nSorry, no record for this user for difficulty 2.")
            else:
                cur.execute("SELECT * FROM scores2 WHERE user=?", (player_name,))
                print("")
                print ((player_name), "'s record for difficulty 2: "+str(cur.fetchone()))
            cur.execute("SELECT * FROM scores3 WHERE user=?", (player_name,))
            if str(cur.fetchone()) == "None":
                print ("\nSorry, no record for this user for difficulty 3.")
            else:
                cur.execute("SELECT * FROM scores3 WHERE user=?", (player_name,))
                print("")
                print ((player_name), "'s record for difficulty 3: "+str(cur.fetchone()))

#This is here to run the main block of code and make sure that the main() subroutine is always looped back to. It also includes the subroutine that creates the database "create_database()".

if __name__=="__main__":
    create_database()
    main()
