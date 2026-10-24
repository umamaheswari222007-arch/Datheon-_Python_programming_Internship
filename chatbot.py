import re

# Customer support information
business_hours = "Monday to Saturday, 9 AM to 6 PM"

product_faqs = {
    "price": "Our product prices depend on the product you choose.",
    "delivery": "Delivery usually takes 3 to 5 business days.",
    "return": "Products can be returned within 7 days of delivery.",
    "payment": "We accept online payments and cash on delivery."
}

# Chatbot response dictionary
responses = {
    "greeting": "Hello! Welcome to our customer support.",
    "thanks": "You're welcome! Happy to help.",
    "goodbye": "Thank you for contacting us. Goodbye!",
    "help": "You can ask me about business hours, products, delivery, returns, or payment."
}


# Function to identify user intent
def identify_intent(user_input):

    text = user_input.lower().strip()

    # Greeting detection
    if re.search(r"\b(hi|hello|hey|good morning|good evening)\b", text):
        return "greeting"

    # Business hours detection
    elif re.search(r"\b(hours|timing|open|close|working hours)\b", text):
        return "hours"

    # Product price detection
    elif re.search(r"\b(price|cost|amount|rate)\b", text):
        return "price"

    # Delivery detection
    elif re.search(r"\b(delivery|shipping|deliver)\b", text):
        return "delivery"

    # Return policy detection
    elif re.search(r"\b(return|refund|exchange)\b", text):
        return "return"

    # Payment detection
    elif re.search(r"\b(payment|pay|cash|card)\b", text):
        return "payment"

    # Thank you detection
    elif re.search(r"\b(thanks|thank you)\b", text):
        return "thanks"

    # Help detection
    elif re.search(r"\b(help|support)\b", text):
        return "help"

    # Exit detection
    elif re.search(r"\b(bye|exit|quit)\b", text):
        return "goodbye"

    # Unknown query
    else:
        return "unknown"


# Function to generate chatbot responses
def get_response(intent):

    if intent == "greeting":
        return responses["greeting"]

    elif intent == "hours":
        return f"Our business hours are {business_hours}."

    elif intent in product_faqs:
        return product_faqs[intent]

    elif intent == "thanks":
        return responses["thanks"]

    elif intent == "help":
        return responses["help"]

    elif intent == "goodbye":
        return responses["goodbye"]

    else:
        return "Sorry, I didn't understand that. Please ask about our products, delivery, payment, or business hours."


# Main chatbot function
def chatbot():

    print("=" * 45)
    print("       CUSTOMER SUPPORT CHATBOT")
    print("=" * 45)

    print("Bot: Hello! Welcome to our customer support.")
    print("Bot: Type 'help' to see what I can answer.")
    print("Bot: Type 'bye', 'exit', or 'quit' to end the chat.")

    while True:

        user_input = input("\nYou: ").strip()

        if not user_input:
            print("Bot: Please enter a question.")
            continue

        intent = identify_intent(user_input)

        response = get_response(intent)

        print("Bot:", response)

        if intent == "goodbye":
            break


# Run the chatbot
if __name__ == "__main__":
    chatbot() 