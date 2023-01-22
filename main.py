# For when school, or admin blocks websites such as ChatGPT.
# by @dhananjay007 on replit
import openai
import subprocess
from colorama import Fore, Style
import pwinput
import json


def askquestion(question, engine):
  completion = openai.Completion.create(
    engine=model_engine,
    prompt=question,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
  )

  response = completion.choices[0].text
  print(response + '\n')


if __name__ == "__main__":
  print(Fore.GREEN + 'Made by @dhananjay007 on Replit \n' + Style.RESET_ALL)

  print(
    'I know, this is a turnoff but sadly, you cannot use ChatGPT without an API key.'
  )

  print(
    '\nWhy do I need this? We cannot use a private API key due to rate limits and privacy. You can find your api key at: '
    + Fore.BLUE + 'https://beta.openai.com/account/api-keys' + Style.RESET_ALL)

  print(
    '\nBut, there is a solution! If you go to this replit: ' + Fore.BLUE +
    'https://replit.com/@MrTechy11/Emulated-Google-Chrome' + Style.RESET_ALL +
    ' and enter the link above, you can login to your account and find or create your API Key. For any issues you can check'
  )
  key = pwinput.pwinput(prompt='\nEnter API Key: ', mask='*')
  openai.api_key = key

  print("""
  GPT-3 Models:
  \ttext-davinci-003 (default, reccommended.)
  \ttext-curie-001
  \ttext-babbage-001	
  \ttext-ada-001	
  """)
  model_engine = input('Select engine: ')
  if not model_engine:
    model_engine = 'text-davinci-003'

  while True:
    print(
      Fore.BLUE +
      '\nOptions: \n\t1: Enter MLI (for multi line inputs) \n\t2: Ask Question'
      + Style.RESET_ALL)

    option = int(input('Enter Option: '))

    question = None
    if option == 1:
      subprocess.call(['sh', './nano.sh'])

      print(
        Fore.GREEN +
        'Use [nano] to identify the file you just edited. (example: Rewrite the following in a more formal way: [nano]'
        + Style.RESET_ALL)
      question = input('Enter Question: ')

      with open("./lines.txt", "r") as c:
        contents = c.read()
      question = question.replace('[nano]', contents)
    elif option == 2:
      question = input('Enter Question: ')
    else:
      print(Fore.RED + 'Invalid Option' + Style.RESET_ALL)

    if question:
      askquestion(question, model_engine)
