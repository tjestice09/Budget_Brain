def generate_reply(message: str) -> str:
    """
    Generates a reply for Budget Brain based on the user message.
    :param message: The user's message as a string.
    :return: A string containing Budget Brain's reply.
    """
    if "groceries" in message.lower():
        return "Budget Brain: The groceries should be about 15 percent of your budget..please budget wisely."
    elif "spend" in message.lower():
        return "Budget Brain: You spent $150 this week on groceries."
    elif "save" in message.lower():
        return "Budget Brain: You saved $200 this week..way to go!"
    else:
        return "Can you repeat that? I didn't understand your message."