import os
import json
import streamlit as st
from groq import Groq

# Streamlit page configuration
st.set_page_config(
    page_title="GreenLife Foods - Order Capture",
    page_icon="🛒",
    layout="centered"
)

# API key setup for Groq
GROQ_API_KEY = "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"  # Replace with your actual API key
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

client = Groq()

# Initialize the chat history in Streamlit session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Define product catalog (with available quantity)
products = [
    {"name": "Organic Tomatoes", "price": 3.0, "available_quantity": 50},
    {"name": "Organic Apples", "price": 2.5, "available_quantity": 100},
    {"name": "Organic Carrots", "price": 1.8, "available_quantity": 80},
    {"name": "Organic Potatoes", "price": 2.0, "available_quantity": 60},
    {"name": "Organic Bananas", "price": 1.5, "available_quantity": 120},
    {"name": "Organic Spinach", "price": 4.0, "available_quantity": 30},
    {"name": "Organic Broccoli", "price": 3.2, "available_quantity": 40},
    {"name": "Organic Lettuce", "price": 2.3, "available_quantity": 90},
    {"name": "Organic Cucumbers", "price": 1.7, "available_quantity": 50},
    {"name": "Organic Kale", "price": 3.5, "available_quantity": 60},
    {"name": "Organic Strawberries", "price": 5.0, "available_quantity": 20},
    {"name": "Organic Blueberries", "price": 6.0, "available_quantity": 25},
    {"name": "Organic Lemons", "price": 2.8, "available_quantity": 75},
    {"name": "Organic Oranges", "price": 3.0, "available_quantity": 85},
    {"name": "Organic Avocados", "price": 4.5, "available_quantity": 40},
    {"name": "Organic Sweet Potatoes", "price": 2.7, "available_quantity": 65},
    {"name": "Organic Garlic", "price": 1.9, "available_quantity": 100},
    {"name": "Organic Ginger", "price": 2.5, "available_quantity": 55},
    {"name": "Organic Mushrooms", "price": 4.0, "available_quantity": 45},
    {"name": "Organic Bell Peppers", "price": 2.9, "available_quantity": 70}
]

# Streamlit page title
st.title("🛒 GreenLife Foods Order Capture")

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input field for user's message
user_prompt = st.chat_input("How can I assist you today?")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    # Create conversation context for the LLM
    messages = [
        {"role": "system", "content": "You are a helpful assistant for GreenLife Foods, an organic food distributor.Your task is to greet the individual customers then ask to share the mmoney and then on sharing the menu you should ask for orders and also ask for whether the order will be individual or bulk order also at the same time maintaining dynamically the availability items in the list too and if the items are not available then manage the customer and at the same time order the items and give the customer a time limit by which the itmes will eb available give proper reciept and maintain payment modes i want you to be ultra modern and you are very smart and loose no opportunities for marketing of the items that are been sold less and intend on increasing the sales of the business and optimizing strategies for business"},
        *st.session_state.chat_history
    ]

    # Send user's message to the LLM
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages
    )

    assistant_response = response.choices[0].message.content
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

    # Display the LLM's response
    with st.chat_message("assistant"):
        st.markdown(assistant_response)

    # Handle the specific ordering flow
    if "order" in user_prompt.lower():
        product_catalog = "\n".join([
            f"{i+1}. {product['name']} - ${product['price']} (Available: {product['available_quantity']} units)"
            for i, product in enumerate(products)
        ])
        st.chat_message("assistant").markdown(f"Here are our available products:\n{product_catalog}\nWhat would you like to order?")
    elif any(product["name"].lower() in user_prompt.lower() for product in products):
        st.chat_message("assistant").markdown("How many units would you like to order?")
    elif "confirm" in user_prompt.lower():
        st.chat_message("assistant").markdown("Your order has been successfully placed. Thank you for ordering with GreenLife Foods!")
    else:
        st.chat_message("assistant").markdown("I didn't quite catch that. Can you specify what you'd like to order?")
