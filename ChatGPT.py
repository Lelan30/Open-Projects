import openai
from apikey import APIKEY

# Set apikey for the service
openai = APIKEY

# Lets chat
output = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    # Everything is stored in this messages array
    # 2 keys: role and content(text)
    # system(overall context), user(Anything you are saying), assistant(the feedback)
    messeges=[{"role":"user", "content": "Can you give me a breakfast recommendation "
                                         "that is high in protein and delicious"}]
)

# Print out the chat
print(output)
      #['choices'][0]['message']['content'])

# Get APIKEY
# inside of apikey.py files
# platform.openai.com
