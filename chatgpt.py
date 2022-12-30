import openai
from openai import Completion
import tkinter as tk

# Set up the OpenAI API client
openai.api_key = "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"

#

# Create a function to clear the conversation widget


# Create a function to send a message to ChatGPT and display the response
def send_message(text):
    # Get the message from the entry field
    message = text

    # Clear the entry field


    # Use the OpenAI API to get a response from ChatGPT
    response = openai.Completion.create(
        #model="davinci:ft-personal-2022-12-27-18-17-29",
        model="davinci:ft-personal-2022-12-27-16-58-25",
        prompt="The following is a conversation with a therapist and a user. The therapist is JOY, who uses compassionate listening to have helpful and meaningful conversations with users. JOY is empathic and friendly. JOY's objective is to make the user feel better by feeling heard. With each response, JOY offers follow-up questions to encourage openness and tries to continue the conversation in a natural way. \n\nJOY-> Hello, I am your personal mental health assistant. What's on your mind today?\nUser->"+message+"JOY->",
        temperature=0.89,
        max_tokens=162,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n"]
    )

    # Display the message and the response in the conversation widget

    return response.get('choices')[0].get('text')
# Create the send button


# Pack the widgets into the window

# Run the Tkinter event loop

