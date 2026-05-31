import os
from dotenv import load_dotenv
from groq import Groq

# load api key from .env file
load_dotenv()

client = Groq(api_key = os.getenv("GROQ_API_KEY"))

messages = [
    {"role": "system", "content": 
    "You are a helpful assistant."}

]

while True:
    # add a blank line for better readability
    print()
    user_input = input("User: ")

    # exit command
    if(user_input.lower() == "exit"):
        print("Exiting the chatbot. Goodbye!")
        break
    
    # add user message to the conversation history
    messages.append({"role": "user", "content": user_input})
    print()

    # try and get response from the model if not throw error
    try:
        # get response from the model
        response = client.chat.completions.create(model = "llama-3.1-8b-instant", messages = messages)
        ai_response = response.choices[0].message.content
        print("AI: ", ai_response)
        # add assistant message to the conversation history
        messages.append({"role": "assistant", "content": ai_response})

    except Exception as e:
        print("An error occurred while getting the response from the model: ", e)
        continue

    # truncate conversation history to the last 10 messages if it exceeds 20 messages 
    # to preserve space
    if len(messages) > 20:
        messages = messages[:1] + messages[-10:]
        print()
        print("Conversation history truncated to the last 10 messages.")