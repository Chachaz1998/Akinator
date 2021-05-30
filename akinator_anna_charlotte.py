#import openpyxl and panda to run the program and read the excel-file
import openpyxl
import pandas as pd

#Read the excel-file with all the information about the famous people and the questions 
df = pd.read_excel("Excel_Liste_buchstaben.xlsx")

#Read the columns headings
list_of_questions = df.columns


#Read the columns index
df.index = ('Johnny Depp', 'Brad Pitt', 'Meryl Streep', 'Tom Cruise', 'Till Schweiger', 'Matthias Schweighöfer', 'Marlon Brando', 'Marilyn Monroe', 'Justin Bieber', 'Elvis Presley', 'Billie Eilish', 'Madonna', 'Britney Spears', 'Taylor Swift', 'Stress', 'Helene Fischer', 'Cleopatra', 'Napoleon', 'Picasso', 'Christoph Kolumbus', "Jeanne d'Arc", 'Leonardo da Vini', 'Wolfgang Amadeus Mozart', 'Christiano Ronaldo', 'Roger Federer', 'Tiger Woods', 'Serena Williams', 'Beat Feuz', 'Harry Potter', 'Hulk', 'Spider Man', 'Schlumpf', 'Angela Merkel', 'Donald Trump', 'Barack Obama', 'Wladimir Putin', 'Alain Berset', 'John F. Kennedy', 'Queen Elisabeth', 'Rapunzel', 'Schneewittchen', 'Aschenputtel', 'Rotkäppchen', 'Nemo', 'Simba', 'Biene Maya', 'Barbie', 'Alberto Giaccometti', 'Heidi Klum', 'Thomas Gottschalk', 'Greta Thunberg')

#Store all possible names in list_of_names
list_of_names = df.index

#Import one name from "Excel_Liste_buchstaben.xlsx" randomly and store in who_am_I
import random

who_am_I = random.choice(list_of_names)
res = who_am_I

#Set user's score to 50
score = 50

#Ask: "Ask your first question: " so user can enter his first question
user_question = input("Ask your first question: ")

#When user's input is not in heading of Excel-List
while user_question not in df.columns:
    if user_question in list_of_names:
        #If the user enters the name of a famous person and the name is the same as the randomly picked one he wins the game. The game stops here. The program asks if he/she wants to play again.
        if user_question == who_am_I:
            play_again = input ("Well done, you found it. You have " + str(score) + " points. Do you wanna play again? (Yes/No): ")
            #If user wants to play again, another name is picked randomly and sotred in who_am_I again. Also the score is set to 50. The user can then ask his/her first question of the new round.
            if play_again == "Yes":
                score = 50
                who_am_I = random.choice(list_of_names)
                res = who_am_I
                user_question = input ("Ask your first question: ")
                continue
            #If user doesn't want to play again, the game ends here.
            else:
                print("That's a shame.")
                break
        #If the user enters the name of a wrong person the score decreases by 10 and the user has to ask another question.
        else:
            score -=10
            #If the user's score is less than 0, he/she loses the game. The program asks if he/she wants to play again.
            if score <= 0:
                play_again = input ("Game over. You've lost too many points. You were " + who_am_I +". Do you wanna play again? (Yes/No):")
                ##break
                ##play_again = input ("Do you wanna play again? (Yes/No): ")
                #If user wants to play again, another name is picked randomly and sotred in who_am_I again. Also the score is set to 50. The user can then ask his/her first question of the new round.
                if play_again == "Yes":
                    score = 50
                    who_am_I = random.choice(list_of_names)
                    res = who_am_I
                    user_question = input ("Ask your first question: ")
                    continue
                #If user doesn't want to play again, the game ends here.
                else:
                    print("That's a shame.")
                    break
            #When the user has enough points, the game continues and the user can ask more quetions.
            else:
                user_question = input ("Wrong person. You just lost 10 points. You now have " + str(score) + " points. Ask another question or guess again: ")
    #If the name/question from user's input can't be found in index or heading of Excel-List.
    elif user_question not in df.columns:
        #If the lenght from user's input is more than 5 characters long, it's not a question from the possible questions to ask since these are maximal four characters long. 
        if len(user_question) >= 5:
            #The score decreases by 10 points because the program recognizes that the user has guessed a name.
            score -=10
            #If the user's score is less than 0, he/she loses the game. The program asks if he/she wants to play again.
            if score <= 0:
                play_again = input ("Game over. You've lost too many points. You were " + who_am_I +". Do you wanna play again? (Yes/No):")
                ##break
                ##play_again = input ("Do you wanna play again? (Yes/No): ")
                #If user wants to play again, another name is picked randomly and sotred in who_am_I again. Also the score is set to 50. The user can then ask his/her first question of the new round.
                if play_again == "Yes":
                    score = 50
                    who_am_I = random.choice(list_of_names)
                    res = who_am_I
                    user_question = input ("Ask your first question: ")
                    continue
                #If user doesn't want to play again, the game ends here.
                else:
                    print("That's a shame.")
                    break
            #When the user has enough points, the game continues and the user can ask more quetions.
            else:
                user_question = input ("Wrong person. You just lost 10 points. You now have " + str(score) + " points. Ask another question or guess again: ")
        else:
            user_question = input("This question can't be answered. Try another one. Ask a question or guess who you are: ") 
            continue

#When user's input is in heading of Excel-List
else:   
    while user_question in df.columns:
        answer_question = df[user_question][who_am_I]
        #If user_question can be answered with yes user can ask another question
        if answer_question == "Yes": 
            print("You're right. You can ask your next question or guess who you are.")
            user_question = input ("Ask a question or guess: ")

            while user_question not in df.columns:
                if user_question in list_of_names:
                    #If user enters the name of a famous person and the name is the same as the randomly picked one he wins the game. The program asks, if he/she wants to play again.
                    if user_question == who_am_I:
                        play_again = input ("Well done, you found it. You have " + str(score) + " points. Do you wanna play again? (Yes/No):")
                        #If user wants to play again, another name is picked randomly and sotred in who_am_I again. Also the score is set to 50. The user can then ask his/her first question of the new round.
                        if play_again == "Yes":
                            score = 50
                            who_am_I = random.choice(list_of_names)
                            res = who_am_I
                            user_question = input ("Ask your first question: ")
                            continue
                        #If user doesn't want to play again, the game ends here.
                        else:
                            print("That's a shame.")
                            break
                    #If user enters the name of a wrong person the score decreases by 10 and the user has to ask another question.
                    else:
                        score -= 10
                        #If the user's score is less than 0, he/she loses the game. The program asks if he/she wants to play again.
                        if score <= 0:
                            play_again = input ("Game over. You've lost too many points. You were " + who_am_I +". Do you wanna play again? (Yes/No):")
                            ##break
                            ##play_again = input ("Do you wanna play again? (Yes/No): ")
                            #If user wants to play again, another name is picked randomly and sotred in who_am_I again. Also the score is set to 50. The user can then ask his/her first question of the new round.
                            if play_again == "Yes":
                                score = 50
                                who_am_I = random.choice(list_of_names)
                                res = who_am_I
                                user_question = input ("Ask your first question: ")
                                continue
                            #If user doesn't want to play again, the game ends here.
                            else:
                                print("That's a shame.")
                                break
                        else:
                            user_question = input ("Wrong person. You just lost 10 points. You now have " + str(score) + " points. Ask another question or guess again: ")
                #If the name/question from user's input can't be found in index or heading of Excel-List the user has to enter another question
                elif user_question not in df.columns:
                    #If the lenght from user's input is more than 5 characters long, it's not a question from the possible questions to ask since these are maximal four characters long.
                    if len(user_question) >= 5:
                        #The score decreases by 10
                        score -=10
                        #If the user's score is less than 0, he/she loses the game. The program asks if he/she wants to play again.
                        if score <= 0:
                            play_again = input ("Game over. You've lost too many points. You were " + who_am_I +". Do you wanna play again? (Yes/No):")
                            ##break
                            ##play_again = input ("Do you wanna play again? (Yes/No): ")
                            #If user wants to play again, another name is picked randomly and sotred in who_am_I again. Also the score is set to 50. The user can then ask his/her first question of the new round.
                            if play_again == "Yes":
                                score = 50
                                who_am_I = random.choice(list_of_names)
                                res = who_am_I
                                user_question = input ("Ask your first question: ")
                                continue
                            #If user doesn't want to play again, the game ends here.
                            else:
                                print("That's a shame.")
                                break
                        else:
                            user_question = input ("Wrong person. You just lost 10 points. You now have " + str(score) + " points. Ask another question or guess again: ")
                    else:
                        user_question = input("This question can't be answered. Try another one. Ask a question or guess who you are: ") 
                        continue
        #If user_question is answered with no score decreases by 5 points and user can ask another question
        elif answer_question == "No":
            score -= 5
            #If the user's score is less than 0, he/she loses the game. The program asks if he/she wants to play again.
            if score <= 0:
                play_again = input ("Game over. You've lost too many points. You were " + who_am_I +". Do you wanna play again? (Yes/No):")
                ##break
                ##play_again = input ("Do you wanna play again? (Yes/No): ")
                #If user wants to play again, another name is picked randomly and sotred in who_am_I again. Also the score is set to 50. The user can then ask his/her first question of the new round.
                if play_again == "Yes":
                    score = 50
                    who_am_I = random.choice(list_of_names)
                    res = who_am_I
                    user_question = input ("Ask your first question: ")
                    continue
                #If user doesn't want to play again, the game ends here.
                else:
                    print("That's a shame.")
                    break
            else:
                print("Sorry, you're wrong. You just lost 5 points. You now have " + str (score) + " points. You can ask your next question or guess who you are.")
                user_question = input ("Ask a question or guess: ")  

            while user_question not in df.columns:
                if user_question in list_of_names:
                    #If user enters the name of a famous person and the name is the same as the randomly picked one he wins the game. The program asks, if user wants to play again.
                    if user_question == who_am_I:
                        play_again = input ("Well done, you found it. You have " + str(score) + " points. Do you wanna play again? (Yes/No):")
                        #If user wants to play again, another name is picked randomly and sotred in who_am_I again. Also the score is set to 50. The user can then ask his/her first question of the new round.
                        if play_again == "Yes":
                            score = 50
                            who_am_I = random.choice(list_of_names)
                            res = who_am_I
                            user_question = input ("Ask your first question: ")
                            continue
                        #If user doesn't want to play again, the game ends here.
                        else:
                            print("That's a shame.")
                            break
                    #If user enters the name of a wrong person the score decreases by 10 and the user has to ask another question.
                    else:
                        score -= 10
                        #If the user's score is less than 0, he/she loses the game. The program asks if he/she wants to play again.
                        if score <= 0:
                            play_again = input ("Game over. You've lost too many points. You were " + who_am_I +". Do you wanna play again? (Yes/No):")
                            ##break
                            ##play_again = input ("Do you wanna play again? (Yes/No): ")
                            #If user wants to play again, another name is picked randomly and sotred in who_am_I again. Also the score is set to 50. The user can then ask his/her first question of the new round.
                            if play_again == "Yes":
                                score = 50
                                who_am_I = random.choice(list_of_names)
                                res = who_am_I
                                user_question = input ("Ask your first question: ")
                                continue
                            #If user doesn't want to play again, the game ends here.
                            else:
                                print("That's a shame.")
                                break
                        else:
                            user_question = input ("Wrong person. You just lost 10 points. You now have " + str(score) + " points. Ask another question or guess again: ")
                #If the name/question from user's input can't be found in index or heading of Excel-List the user has to enter another question
                elif user_question not in df.columns:
                    #If the lenght from user's input is more than 5 characters long, it's not a question from the possible questions to ask since these are maximal four characters long.
                    if len(user_question) >= 5:
                        #The score decreases by 10 beceause it's a wrong name.
                        score -=10
                        #If the user's score is less than 0, he/she loses the game. The program asks if he/she wants to play again.
                        if score <= 0:
                            play_again = input ("Game over. You've lost too many points. You were " + who_am_I +". Do you wanna play again? (Yes/No):")
                            ##break
                            ##play_again = input ("Do you wanna play again? (Yes/No): ")
                            #If user wants to play again, another name is picked randomly and sotred in who_am_I again. Also the score is set to 50. The user can then ask his/her first question of the new round.
                            if play_again == "Yes":
                                score = 50
                                who_am_I = random.choice(list_of_names)
                                res = who_am_I
                                user_question = input ("Ask your first question: ")
                                continue
                            #If user doesn't want to play again, the game ends here.
                            else:
                                print("That's a shame.")
                                break
                        else:
                            user_question = input ("Wrong person. You just lost 10 points. You now have " + str(score) + " points. Ask another question or guess again: ")
                    else:
                        user_question = input("This question can't be answered. Try another one. Ask a question or guess who you are: ") 
                        continue
        #If the name/question from user's input is not defined the user has to enter another question
        elif answer_question == "Not defined":
            user_question = input ("This question can't be answered. Try another one. Ask a question or guess who you are: ")
            
            while user_question not in df.columns:
                if user_question in list_of_names:
                    #If user enters the name of a famous person and the name is the same as the randomly picked one he wins the game. The program asks, if he/she wants to play again.
                    if user_question == who_am_I:
                        play_again = input ("Well done, you found it. You have " + str(score) + " points. Do you wanna play again? (Yes/No):")
                        #If user wants to play again, another name is picked randomly and sotred in who_am_I again. Also the score is set to 50. The user can then ask his/her first question of the new round.
                        if play_again == "Yes":
                            score = 50
                            who_am_I = random.choice(list_of_names)
                            res = who_am_I
                            user_question = input ("Ask your first question: ")
                            continue
                        #If user doesn't want to play again, the game ends here.
                        else:
                            print("That's a shame.")
                            break
                    #If user enters the name of a wrong person the score decreases by 10 and the user has to ask another question.
                    else:
                        score -= 10
                        #If the user's score is less than 0, he/she loses the game. The program asks if he/she wants to play again.
                        if score <= 0:
                            play_again = input ("Game over. You've lost too many points. You were " + who_am_I +". Do you wanna play again? (Yes/No):")
                            ##break
                            ##play_again = input ("Do you wanna play again? (Yes/No): ")
                            #If user wants to play again, another name is picked randomly and sotred in who_am_I again. Also the score is set to 50. The user can then ask his/her first question of the new round.
                            if play_again == "Yes":
                                score = 50
                                who_am_I = random.choice(list_of_names)
                                res = who_am_I
                                user_question = input ("Ask your first question: ")
                                continue
                            #If user doesn't want to play again, the game ends here.
                            else:
                                print("That's a shame.")
                                break
                        else:
                            user_question = input ("Wrong person. You just lost 10 points. You now have " + str(score) + " points. Ask another question or guess again: ")
                #If the name/question from user's input can't be found in index or heading of Excel-List the user has to enter another question
                elif user_question not in df.columns:
                    #If the lenght from user's input is more than 5 characters long, it's not a question from the possible questions to ask since these are maximal four characters long.
                    if len(user_question) >= 5:
                        #The score decreases by 10 because it was the wrong name.
                        score -=10
                        #If the user's score is less than 0, he/she loses the game. The program asks if he/she wants to play again.
                        if score <= 0:
                            play_again = input ("Game over. You've lost too many points. You were " + who_am_I +". Do you wanna play again? (Yes/No):")
                            ##break
                            ##play_again = input ("Do you wanna play again? (Yes/No): ")
                            #If user wants to play again, another name is picked randomly and sotred in who_am_I again. Also the score is set to 50. The user can then ask his/her first question of the new round.
                            if play_again == "Yes":
                                score = 50
                                who_am_I = random.choice(list_of_names)
                                res = who_am_I
                                user_question = input ("Ask your first question: ")
                                continue
                            #If user doesn't want to play again, the game ends here.
                            else:
                                print("That's a shame.")
                                break
                        else:
                            user_question = input ("Wrong person. You just lost 10 points. You now have " + str(score) + " points. Ask another question or guess again: ")
                    else:
                        user_question = input("This question can't be answered. Try another one. Ask a question or guess who you are: ") 
                        continue