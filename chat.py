#!/usr/bin/env python3
from hugchat import hugchat
from hugchat.login import Login

chatbot = hugchat.ChatBot(cookie_path=f"token.json")  # login using token
id = chatbot.new_conversation()
chatbot.change_conversation(id)

# print(chatbot.chat("Hi"))# Create a new conversation
# id = chatbot.new_conversation()
# chatbot.change_conversation(id)# Get conversation list
# conversation_list = chatbot.get_conversation_list()print(chatbot.chat("How old is the founder of the company Space X?"))

print("[[ Welcome to AI. Let's talk! ]]")
print("'q' or 'quit' to exit")
print("'c' or 'change' to change conversation")
print("'n' or 'new' to start a new conversation")

while True:
    user_input = input("> ")
    if user_input.lower() == "":
        pass
    elif user_input.lower() in ["q", "quit"]:
        break
    elif user_input.lower() in ["c", "change"]:
        print("Choose a conversation to switch to:")
        print(chatbot.get_conversation_list())
    elif user_input.lower() in ["n", "new"]:
        print("Clean slate!")
        id = chatbot.new_conversation()
        chatbot.change_conversation(id)
    else:
        print(chatbot.chat(user_input))
