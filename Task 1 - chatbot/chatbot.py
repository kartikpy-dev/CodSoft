from datetime import datetime
import random
import time

print("=" * 60)
print("WELCOME TO CODBOT")
print("=" * 60)

name = input("Enter your Name: ")
age = input("Enter your Age: ")
city = input("Enter your City: ")

print(f"\nWelcome {name}!")
print("Type 'help' to view commands.")
print("Type 'bye' to exit.\n")

start_time = time.time()
question_count = 0

history = open("chat_history.txt", "a", encoding="utf-8")
history.write("\n")
history.write("=" * 60)
history.write(f"\nSession Started: {datetime.now()}\n")
history.write("=" * 60 + "\n")

jokes = [
    "Why did the computer get cold? Because it left Windows open.",
    "Why do programmers like dark mode? Because light attracts bugs.",
    "Why was the computer tired? Too many tabs were open.",
    "Debugging is like being the detective in a crime movie where you are also the criminal.",
    "Why do Python programmers wear glasses? Because they can't C."
]

quotes = [
    "Believe in yourself.",
    "Success comes from consistency.",
    "Never stop learning.",
    "Dream big and work hard.",
    "Every expert was once a beginner."
]

ai = {
    "what is ai": "Artificial Intelligence is the simulation of human intelligence by machines.",
    "what is machine learning": "Machine Learning is a branch of AI where computers learn from data.",
    "what is deep learning": "Deep Learning is a subset of Machine Learning using neural networks.",
    "what is nlp": "NLP stands for Natural Language Processing.",
    "what is computer vision": "Computer Vision enables computers to understand images and videos.",
    "what is chatgpt": "ChatGPT is an AI chatbot developed by OpenAI.",
    "who made chatgpt": "ChatGPT was developed by OpenAI.",
    "uses of ai": "AI is used in healthcare, banking, education, robotics and transportation.",
    "advantages of ai": "AI improves speed, accuracy and automation.",
    "disadvantages of ai": "AI requires high-quality data and may replace repetitive jobs."
}

programming = {
    "what is python": "Python is a simple and powerful programming language.",
    "what is java": "Java is an object-oriented programming language.",
    "what is c": "C is a procedural programming language.",
    "what is html": "HTML is used to create web pages.",
    "what is css": "CSS is used to style web pages.",
    "what is javascript": "JavaScript adds interactivity to websites.",
    "what is sql": "SQL is used to manage databases.",
    "what is oop": "OOP stands for Object-Oriented Programming.",
    "what is github": "GitHub is a platform to host and manage code.",
    "what is git": "Git is a version control system."
}

while True:

    user = input(f"{name}: ").lower().strip()

    question_count += 1

    history.write(f"{name}: {user}\n")

    if user in ["hi", "hello", "hey"]:

        reply = "Hello! How can I help you today?"

    elif user == "good morning":

        reply = "Good Morning! Have a wonderful day."

    elif user == "good afternoon":

        reply = "Good Afternoon!"

    elif user == "good evening":

        reply = "Good Evening!"

    elif user == "how are you":

        reply = "I am doing great. Thank you for asking."

    elif user == "who are you":

        reply = "I am CodBot, a Rule-Based Chatbot."

    elif user == "my name":

        reply = f"Your name is {name}."

    elif user == "my age":

        reply = f"Your age is {age}."

    elif user == "my city":

        reply = f"You are from {city}."

    elif user in ai:

        reply = ai[user]

    elif user in programming:

        reply = programming[user]

    elif user == "time":

        reply = datetime.now().strftime("%I:%M:%S %p")

    elif user == "date":

        reply = datetime.now().strftime("%d-%m-%Y")

    elif user == "day":

        reply = datetime.now().strftime("%A")

    elif user == "month":

        reply = datetime.now().strftime("%B")

    elif user == "year":

        reply = datetime.now().strftime("%Y")

    elif "+" in user or "-" in user or "*" in user or "/" in user:

        try:
            reply = f"Answer = {eval(user)}"
        except:
            reply = "Invalid mathematical expression."

    elif user == "joke":

        reply = random.choice(jokes)

    elif user == "another joke":

        reply = random.choice(jokes)

    elif user == "quote":

        reply = random.choice(quotes)

    elif user == "motivate me":

        reply = random.choice(quotes)

    elif user == "flip coin":

        reply = random.choice(["Heads", "Tails"])

    elif user == "roll dice":

        reply = f"You rolled {random.randint(1,6)}"

    elif user == "random number":

        reply = str(random.randint(1,100))

    elif user == "i am happy":

        reply = "That's wonderful! Keep smiling."

    elif user == "i am sad":

        reply = "I'm sorry to hear that. Tomorrow will be better."

    elif user == "i am bored":

        reply = "Maybe try reading a book or learning Python."

    elif user == "i am tired":

        reply = "Take some rest and drink some water."

    elif user == "thank you":

        reply = "You're welcome."

    elif user == "thanks":

        reply = "Happy to help."

    elif user == "sorry":

        reply = "No problem."

    elif user == "good":

        reply = "Glad to hear that."

    elif user == "bad":

        reply = "I hope everything gets better soon."

    elif user == "nice":

        reply = "Thank you."

    elif user == "awesome":

        reply = "Indeed!"

    elif user == "what is bca":

        reply = "BCA stands for Bachelor of Computer Applications."

    elif user == "what is mca":

        reply = "MCA stands for Master of Computer Applications."

    elif user == "what is internship":

        reply = "An internship provides practical work experience."

    elif user == "why learn python":

        reply = "Python is easy to learn and widely used in AI, automation and web development."

    elif user == "what is codsoft":

        reply = "CodSoft offers internships to help students gain practical skills."

    elif user == "weather":

        reply = "Sorry, I cannot provide live weather information."

    elif user == "news":

        reply = "Sorry, I cannot provide live news updates."

    elif user == "help":

        reply = """
==================== HELP ====================

Greetings
---------
hi
hello
hey
good morning
good afternoon
good evening

Personal
--------
my name
my age
my city

AI
--
what is ai
what is machine learning
what is deep learning
what is nlp
what is computer vision
what is chatgpt
who made chatgpt
uses of ai
advantages of ai
disadvantages of ai

Programming
-----------
what is python
what is java
what is c
what is html
what is css
what is javascript
what is sql
what is oop
what is github
what is git

Utilities
---------
date
time
day
month
year

Calculator
----------
Examples:
2+2
50-10
12*5
100/4

Fun
---
joke
another joke
quote
motivate me
flip coin
roll dice
random number

Conversation
------------
i am happy
i am sad
i am bored
i am tired
thank you
thanks
good
bad
nice
awesome

College
-------
what is bca
what is mca
what is internship
why learn python
what is codsoft

Games
-----
guess game
rock paper scissors
quiz

Exit
----
bye

==============================================
"""
    elif user == "guess game":

        print("\nGuess a number between 1 and 10")

        number = random.randint(1, 10)

        while True:

            guess = input("Enter your guess: ")

            try:
                guess = int(guess)

                if guess == number:

                    reply = "Congratulations! You guessed the correct number."
                    break

                elif guess < number:

                    print("Bot: Too Low!")

                else:

                    print("Bot: Too High!")

            except:

                print("Bot: Please enter a valid number.")

    elif user == "rock paper scissors":

        choices = ["rock", "paper", "scissors"]

        computer = random.choice(choices)

        player = input("Choose Rock, Paper or Scissors: ").lower()

        if player not in choices:

            reply = "Invalid choice."

        elif player == computer:

            reply = f"Draw! We both selected {computer}."

        elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissors" and computer == "paper"):

            reply = f"You Win! Computer selected {computer}."

        else:

            reply = f"You Lose! Computer selected {computer}."

    elif user == "quiz":

        score = 0

        print("\n========== AI QUIZ ==========\n")

        answer = input("1. What does AI stand for? ")

        if answer.lower() == "artificial intelligence":
            score += 1

        answer = input("2. Which language is popular for AI? ")

        if answer.lower() == "python":
            score += 1

        answer = input("3. GitHub is mainly used for? ")

        if "code" in answer.lower():
            score += 1

        answer = input("4. HTML is used to create? ")

        if "web" in answer.lower():
            score += 1

        answer = input("5. CSS is mainly used for? ")

        if "style" in answer.lower():
            score += 1

        reply = f"Quiz Completed! Your Score is {score}/5."

    elif user == "about":

        reply = """
====================================================
CODBOT - RULE BASED CHATBOT

Developer : Kartik

Project : CodSoft Artificial Intelligence Internship

Language : Python

Version : 1.0

This chatbot responds using predefined rules
implemented with if-elif-else statements.

====================================================
"""

    elif user == "creator":

        reply = "This chatbot was developed by Kartik."

    elif user == "version":

        reply = "Current Version: 1.0"

    elif user == "commands":

        reply = "Type 'help' to view all available commands."

    elif user == "clear":

        print("\n" * 40)
        reply = "Screen Cleared."

    elif user == "fun fact":

        facts = [

            "Python was created by Guido van Rossum.",

            "The first programmer was Ada Lovelace.",

            "Git was created by Linus Torvalds.",

            "Artificial Intelligence is used in self-driving cars.",

            "Computers understand only binary numbers."

        ]

        reply = random.choice(facts)

    elif user in ["bye", "exit", "quit"]:

        session_time = round(time.time() - start_time, 2)

        print("\n=======================================")
        print("          SESSION SUMMARY")
        print("=======================================")
        print("Name :", name)
        print("Age :", age)
        print("City :", city)
        print("Questions Asked :", question_count)
        print("Session Time :", session_time, "seconds")
        print("=======================================")

        reply = "Goodbye! Thank you for using CodBot."

        print("\nBot:", reply)

        history.write(f"Bot: {reply}\n")
        history.write(f"Questions Asked : {question_count}\n")
        history.write(f"Session Time : {session_time} seconds\n")
        history.write("=" * 60 + "\n")

        history.close()

        break

    else:

        reply = "Sorry! I don't understand that command. Type 'help' to see all available commands."

    print("\nBot:", reply)

    history.write(f"Bot: {reply}\n")















    