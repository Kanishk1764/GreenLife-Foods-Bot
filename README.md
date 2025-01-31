# GreenLife Foods Order Capture Chatbot

## Overview
GreenLife Foods provides an intuitive chatbot for distributors and retailers to place orders for organic food products. The chatbot enables users to browse products, check availability, and place orders with ease.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/GreenLife-Foods-Bot.git
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Add your **Groq API Key** to the `GROQ_API_KEY` variable in the code.

## Running the App
Start the Streamlit app:
```bash
streamlit run app.py
```
                                            #Time to be a Chill guy ![ChillGuy Logo]((https://lookhuman.com/products/473609-chill-guy-die-cut-stickers))


# GreenLife Foods - Customer Interaction Bot

Welcome to **GreenLife Foods**! This bot is designed to help you browse our organic food offerings and place orders seamlessly.

## Example User Interaction

Here’s a step-by-step example conversation where the bot assists a user in placing an order:

### **User: "HI Bot good day!!"**
**Bot:**  
Good day to you! Welcome to GreenLife Foods, your premier destination for organic and sustainable food options. Today, you'll find an assortment of fresh produce, artisanal cheeses, and wholesome products that cater to diverse tastes and dietary requirements.

We are happy to offer electronic terminals where you can look at our menu and place an order. Here is a brief overview of our menu and some popular items:

- **Fresh Produce**
  - Fresh lettuce
  - Red Apples
  - Baby Carrots
- **Organic Delights**
  - Brownies
  - Quinoa Bites
  - Almond Cake
- **Artisanal Cheeses**
  - Cheddar Cheese
  - Cottage Cheese
  - Goat Cheese

Would you like to place an individual order or a bulk order for a special occasion?

---

### **User: "Menu"**
**Bot:**  
You've decided to take a look at our menu again. Here's an updated list of our fresh produce, organic delights, and artisanal cheeses:

#### Fresh Produce
- Fresh lettuce (in stock)
- Red Apples (in stock)
- Baby Carrots (temporarily out of stock, estimated availability: 1.5 hours)

#### Organic Delights
- Brownies (in stock)
- Quinoa Bites (in stock)
- Almond Cake (limited stock, estimated availability: 2 hours)

#### Artisanal Cheeses
- Cheddar Cheese (in stock)
- Cottage Cheese (in stock)
- Goat Cheese (temporarily out of stock, estimated availability: 1.5 hours)

#### New Arrivals
- Roasted Almonds (in stock)
- Fresh Mixed Berries (in stock)

Our Featured Item of the Day is our **Quinoa Bites**, made with organic quinoa and topped with a hint of honey. Would you like to try these out?

---

### **User: "order now"**
**Bot:**  
You've decided to place an order. Please select the items you'd like to purchase, and I'll guide you through the process.

To place an order, please respond with the following format:
- Item Name (Quantity)

For example, if you'd like to order 2 Quinoa Bites, you would respond with:
- `Quinoa Bites (2)`

### Current Menu:
- **Fresh Produce**
  - Fresh lettuce (in stock)
  - Red Apples (in stock)
  - Baby Carrots (temporarily out of stock, estimated availability: 1.5 hours)
- **Organic Delights**
  - Brownies (in stock)
  - Quinoa Bites (in stock)
  - Almond Cake (limited stock, estimated availability: 2 hours)
- **Artisanal Cheeses**
  - Cheddar Cheese (in stock)
  - Cottage Cheese (in stock)
  - Goat Cheese (temporarily out of stock, estimated availability: 1.5 hours)
- **New Arrivals**
  - Roasted Almonds (in stock)
  - Fresh Mixed Berries (in stock)

Would you like to proceed with an individual order or a bulk order?

---

### **User: "i will have 10 organic tomatoes"**
**Bot:**  
Organic tomatoes are a great choice! Our organic tomatoes are locally sourced and perfect for salads, sandwiches, or just snacking.

### Order Summary:
- Organic Tomatoes (10)  
**Total**: $5.50

What type of order would you like to place?
- **Individual Order** (Standard order for personal use)
- **Bulk Order** (For larger quantities)

---

### **User: "Cash please"**
**Bot:**  
You've chosen the cash payment option. Here's your updated receipt:

### **Receipt:**
- **Date**: Today
- **Time**: [Current Time]
- **Order Summary:**
  - Organic Tomatoes (10) - $5.50
  - Service Charge: $0.50
  - **Total**: $6.00
- **Payment Mode**: Cash On Delivery (COD)

Thank you for shopping at GreenLife Foods. We hope you will visit us again soon.

**Invoice Number**: GLF/001

---

## How It Works

This bot interface is designed for seamless customer interactions, allowing users to browse, select, and purchase organic food items from the store's catalog. The flow follows a simple conversation model where the bot offers choices, processes orders, and presents payment options in a user-friendly manner.

## Features
- **Product Selection**: Users can choose from fresh produce, organic delights, and artisanal cheeses.
- **Order Placement**: Users can specify the quantity and choose between individual or bulk orders.
- **Payment Options**: Multiple payment methods available, including COD (Cash on Delivery), Credit/Debit Cards, and Online Transfers.
- **Real-time Updates**: The bot provides real-time availability updates for stock.


