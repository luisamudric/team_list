#import libraries
from random import sample
import math

def team_list(): #function called team_list
    while True: #while loop 
        try: #error handling

            print("Provide a list of names. Separate them by using space and press Enter. To leave, type 'leave'.")
            #first thing that prints to the user

            names = input("Enter a list of names: "); #asks the user to input a list of names

            if names == 'leave': 
                break
            #if user types in leave, the programme stops running

            list_number = int(input("Enter the number of lists you want: ")); #asks the user to input how many teams they want the names split into
            if list_number == 'leave': 
                break

            names_split = names.split() #setting a variable called names_split; .split splits a string into a list

            teams = int(len(names.split())/list_number) #variable teams; calucates size of 1 team to a whole number

            list_number2 = int(len(names_split)) #variable list_number2; how many names in 1 list

            number = 1 #variable number set to 1

            names_left = len(names.split())%list_number #variable names_left; calculates how many names are left
            if names_left == 0: 
                print("No one got left behind!")
            #if the number of names entered is an even number (0), "No one got left behind!" gets printed

            elif names_left == 1: 
                print("only " + str(names_left) + " name got left behind.")

            else:                                                                        #if the number of names entered in an uneven number, how many were left gets printed
                print("only " + str(names_left) + " names got left behind.")


            while list_number2 > 0 and list_number > 0: #while loop

                random_teams = sample(names_split, teams) #variable random_teams takes a sample from names_split (x axis) and teams (y axis)

                for i in random_teams: #for every element in random_teams
                    names_split.remove(i) #removes those elements

                list_number2 -= teams #variable list_number2 takes away how many names are in variable teams

                list_number -= 1 #continue

                print("Team " + str(number) + ": " + (", ".join(random_teams))) #names printed into randomized teams

                number = number + 1 #adds 1 

                if list_number == 0: #the names of those that didn't make it into a team
                    print("Name/s left behind: " + str(names_split))
            break
        
        except:
            print("error")
            break



team_list() #call to function team_list
