
# Responses Help Users Interact With The AI Chatbot

from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "sup",):
        return "Hey, How's it going?"

    if user_message in ("fine,how are you", "how are you",):
        return "Hey, Im fine thanks"

    if user_message in ("who are you", "who is this",):
        return "I am Jamil's AI Assistant!"

    if user_message in ("give him a message", "tell him this",):
        return "What do you want to say to Jamil?"

    if user_message in ("what are you doing now?", "are you busy?",):
        return "I am just relaxing. Jamil is busy at the moment.!"

    if user_message in ("time", "time?",):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)

    return "I don't understand you, Sorry!"
