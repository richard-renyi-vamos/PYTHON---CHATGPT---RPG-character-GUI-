import tkinter as tk
from tkinter import scrolledtext
import pyttsx3
import openai

# OpenAI API Key
openai.api_key = 'your-api-key'

# Function to send the message to GPT and get a response
def generate_response():
    user_input = user_input_box.get()
    user_input_box.delete(0, tk.END)  # Clear the input box

    # Send input to GPT for response
    response = get_gpt_response(user_input)

    # Display user input and response in conversation history
    conversation_history.config(state=tk.NORMAL)
    conversation_history.insert(tk.END, "You: " + user_input + "\n")
    conversation_history.insert(tk.END, "Character: " + response + "\n\n")
    conversation_history.config(state=tk.DISABLED)

    # Convert response to speech
    speak(response)

# Function to get a response from GPT
def get_gpt_response(prompt):
    personality_prompt = f"You are a brave and kind RPG character. Respond to the user as if you are in a medieval fantasy setting.\nUser: {prompt}\nCharacter:"
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=personality_prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text.strip()

# Function to convert text to speech
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Initialize Tkinter window
window = tk.Tk()
window.title("RPG Character Chat")

# Create a scrolled text widget for conversation history
conversation_history = scrolledtext.ScrolledText(window, wrap=tk.WORD, state=tk.DISABLED)
conversation_history.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Create an input box for the user to type messages
user_input_box = tk.Entry(window, width=80)
user_input_box.grid(row=1, column=0, padx=10, pady=10)

# Create a send button
send_button = tk.Button(window, text="Send", command=generate_response)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Start the Tkinter event loop
window.mainloop()
