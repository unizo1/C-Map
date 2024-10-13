import os
from dotenv import load_dotenv
from openai import OpenAI
from EventScraper import event_grabber

def EventAi(user_filter):
    load_dotenv("OAKEY.en")
    API_KEY = os.getenv("OAKEY")
    client = OpenAI(
        # This is the default and can be omitted
        api_key = API_KEY
    )

    events_string = event_grabber()
    #print(events_string)

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"""
                Given the following list of events read each one throughly, 
                Only show the top 3 events that match this criteria 
                User input is the most important thing to consider compare to the title and tags of events, 
                make assumptions based off the titles so that you are an expert at each topic example: if they like indoor don't do something thats ususally outdoor
                and jsonify the output: {user_filter}\n{events_string}""",
            }
        ],
        model="gpt-3.5-turbo",
    )
    return chat_completion.choices[0].message.content