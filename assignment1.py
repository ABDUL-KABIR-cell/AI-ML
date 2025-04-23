def quiz():
    print('''LET THE QUIZ BEGIN!
     You'll be asked five random questions,
     Every question answered correctly awards a mark.
     Let see how many marks you can accumulate.
     Goodluck! ''')
    score = 0
    #Question 1
    president = input("1. What gender is the president of Nigeria? ").lower()
    if president == "male":
        print("True")
        score += 1
    else:
        print("False")
    #Question 2
    ikeja = input("2. What is the Capital of Lagos State? " ).lower()
    if ikeja == "ikeja":
        print("True")
        score += 1
    else:
        print("False")
    #Question 3
    states = input("3. How many states do we have in Nigeria? ")
    if states == "36":
        print("True")
        score += 1
    else:
        print("False")
    #Question 4
    week = input("4. What day begins a week? ").lower()
    if week == "sunday":
        print("True")
        score += 1
    else:
        print("False")
    #Question 5
    blood = input("5. What colour is the human blood? ").lower()
    if blood == "red":
        print("True")
        score += 1
        print(f"Your total score is {score}")
        
    else:
        print("False")
        print(f"Your Final Score is {score}")
        
def main():
    while True:
        quiz()
        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

    
main()