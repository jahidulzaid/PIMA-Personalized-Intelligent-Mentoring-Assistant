def get_response(msg):
    msg = msg.lower()
    if "hello" in msg:
        return "Hi there! How can I assist you?"
    elif "bye" in msg:
        return "Goodbye! Have a great day."
    else:
        return "I'm not sure I understand. Can you rephrase?"
