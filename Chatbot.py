def chatbot():
    print("Chatbot: Hello! How can I help you today? (Type 'exit' to quit)")

    while True:
        user_input = input("You: ").lower()

        if user_input in ['hi', 'hello']:
            print("Chatbot: Hi there! How can I assist you?")
        elif "your name" in user_input:
            print("Chatbot: I'm a Rule-Based Chatbot created by Tamanna!")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but I'm functioning as expected!")
        elif "bye" in user_input:
            print("Chatbot: Goodbye! Have a nice day")
            break
        elif user_input == "exit":
            print("Chatbot: Exiting... Bye!")
            break
        else:
            print("Chatbot: Sorry, I didn't understand that.")

# Run the chatbot
chatbot()
