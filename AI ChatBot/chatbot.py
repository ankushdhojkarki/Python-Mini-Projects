#NEED TO WORK ON THIS PROJECT
from openai import OpenAI

API_KEY = "your-api-key-here"  # Replace with your valid key

client = OpenAI(api_key=API_KEY)

messages = []


def completion(user_message):
    global messages
    messages.append({
        "role": "user",
        "content": user_message
    })

    chat_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )

    bot_message = chat_completion.choices[0].message.content
    messages.append({
        "role": "assistant",
        "content": bot_message
    })

    print(f"Chatbot: {bot_message}")


if __name__ == "__main__":
    print("ChatBot: Hi! I'm your AI assistant. How may I help you?\n")
    while True:
        user_input = input("You: ")
        completion(user_input)
