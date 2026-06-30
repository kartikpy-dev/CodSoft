print("====================================")
print("      Welcome to AI Chatbot")
print("====================================")

name = input("Enter your name: ")

print(f"\nHello, {name}!")
print("Type 'bye' anytime to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "hi" or user == "hello":
        print("Bot: Hello! Nice to meet you.")

    elif user == "how are you":
        print("Bot: I'm doing great. Thanks for asking!")

    elif user == "what is your name":
        print("Bot: My name is CodBot.")

    elif user == "what is ai":
        print("Bot: AI stands for Artificial Intelligence.")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")