#!/usr/bin/env python3
import os
import sys

virtualenv_dir = "/home/shiva/tmpexpdir/aigen/.env/"

# Setting up the environment variables
os.environ["PYTHONPATH"] = f":{virtualenv_dir}/lib/python3.12/site-packages:"
os.environ["LD_LIBRARY_PATH"] = f"{virtualenv_dir}/lib/"

sys.path.insert(0, virtualenv_dir + "/lib/python3.12/site-packages")

import argparse
import json

try:
    from hugchat import hugchat
except Exception:
    import hugchat


arg_parser = argparse.ArgumentParser(
    description="See https://github.com/Soulter/hugging-chat-api"
)

arg_parser.add_argument("cookies", help="JSON string or cookies files path")
arg_parser.add_argument(
    "-p",
    "--prompt",
    default="Prompt: ",
    help='Prompt indicator, a space is ensured at the end, defaults to ">>>> "',
)

parsed_args = arg_parser.parse_args()

try:
    cookies_dict = json.loads(parsed_args.cookies)
except ValueError:
    cookies_dict = None

if cookies_dict:
    chatbot = hugchat.ChatBot(cookies=cookies_dict)
else:
    chatbot = hugchat.ChatBot(cookie_path=parsed_args.cookies)

prompt_indicator = parsed_args.prompt
if prompt_indicator[-1] != " ":
    prompt_indicator += " "


while True:
    try:
        prompt = input(prompt_indicator)
        if prompt != "":
            print(chatbot.chat(prompt))
    except EOFError:
        break
