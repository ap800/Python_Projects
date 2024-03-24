#A basic quiz game in Python

def new_game():
    guesses=[]
    correct_guess = 0
    question_number = 1
    for key in questions:
        print("---------------------")
        print(key)
        for i in options[question_number-1]:
            print(i)
        guess = input("Enter (A,B,C or D) : ")
        guess = guess.upper()
        guesses.append(guess)
        
        correct_guess += check_answer(questions.get(key),guess)
        question_number += 1
    
    display_score(correct_guess,guesses)


def check_answer(answer,guess):
    if answer==guess:
        print("The answer is correct!!!")
        return 1
    else:
        print("The answer is incorrect!!!")
        return 0
        
def display_score(correct_guess,guesses):
    print("RESULTS!!!")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i),end=" ")
    print()
    
    print("Guesses: ",end="")
    for i in guesses:
        print(i,end=" ")
    print()
    
    score = int(correct_guess/len(questions)*100)
    print("Your score is : "+str(score)+"%")
        
def play_again():
    
    response = input("Do you wnat to play again (Yes or No): ")
    response = response.upper()
    
    if response=="YES":
        return True
    else:
        return False

questions = {"Who created Python?: ":"A",
             "Who created Java?: ":"B",
             "Who created C#?: ":"B",
             "Who created JavaScript?: ":"D"
}

options = [["A. Guido Van Roussom", "B. Elon Musk", "C. Mark Zuckerburg", "D. Bill Gates"],
           ["A. Guido Van Roussom","B. James Gosling", "C. Dennis Ritchie", "D. Bill Gates"],
           ["A. Don Syme","B. Anders Heilberg","C. Elon Musk","D. Bjarne Stroustrup"],
           ["A. Tim Berners-Lee","B. Hakon Wium Lie","C. Anders Hejlsberg","D. Brendan Eich"]]

new_game()

while play_again():
    new_game()
    
print("You have exited the game!!!!")