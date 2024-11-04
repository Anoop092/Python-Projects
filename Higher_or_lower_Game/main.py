# Find the who has more followers
import random 
import sys
from data import data
from Art import logo,vs

game_data = data
game_over = False
score = 0

def get_question():
    return random.choice(game_data)

def question_exists(question,questions):
    if len(questions) > 0 and question["name"] == questions[0]["name"]:
        return True
    return False
questions = [get_question() for _ in range(0,2)]
def set_user_answer(user_input):
    if user_input == 'A':
        return 0
    elif user_input == "B":
        return 1
    return -1
def check(user_answer,correct_answer):
    if user_answer == correct_answer:
        return True
    return False
def get_correct_answer(questions):
    "This Function returns index of dictonary with maximum followers"
    if questions[0]['follower_count'] > questions[1]['follower_count']:
        return 0
    return 1

    
print(logo)
while not game_over:
    print(f"Compare A: {questions[0]['name']} ,{questions[0]['description']} from {questions[0]['country']}, {questions[0]['follower_count']}")
    print(vs)
    print(f"Compare B: {questions[1]['name']} ,{questions[1]['description']} from {questions[1]['country']},  {questions[1]['follower_count']}")
    user_input = input("Who has more followers? type 'A' or 'B': ").upper()
    user_answer = set_user_answer(user_input)
    correct_answer = get_correct_answer(questions)
    if check(user_answer,correct_answer):
        score += 1
        questions.pop(0)
        new_question = get_question()
        while question_exists(new_question,questions):
            new_question = get_question()
        questions.append(new_question)

    else:
        print(f"Sorry, that's  wrong. Your Final Score is: {score}")
        break
    print(f"You're right! your current score is : {score}")
    


    








