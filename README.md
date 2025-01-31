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
                                            #Time to be a Chill guy ![image](https://github.com/user-attachments/assets/bd3516bf-4860-4392-8e31-698b62f70f78)

#Example Conversation
##User: "HI Bot good day!!"
##Bot: "Good day to you! Welcome to GreenLife Foods, your premier destination for organic and sustainable food options. Today, you'll find an assortment of fresh produce, artisanal cheeses, and wholesome products that cater to diverse tastes and dietary requirements.

We are happy to offer electronic terminals where you can look at our menu and place an order. Here is a brief overview of our menu and some popular items:

Fresh Produce
Fresh lettuce
Red Apples
Baby Carrots
Organic Delights......( a full list)
Brownies
Quinoa Bites
Almond Cake
Artisanal Cheeses
Cheddar Cheese
Cottage Cheese
Goat Cheese
What would you like to order today?

Would you like to place an individual order or a bulk order for a special occasion?

Type menu if you want to view the entire menu again, order now to place your order, or update availability if you want to see updated availability of our items.
        "
##User: "Menu"
##Bot: "You've decided to take a look at our menu again. Here's an updated list of our fresh produce, organic delights, and artisanal cheeses:

###Fresh Produce

Fresh lettuce (in stock)
Red Apples (in stock)
Baby Carrots (temporarily out of stock, estimated availability: 1.5 hours)
Organic Delights

Brownies (in stock)
Quinoa Bites (in stock)
Almond Cake (limited stock, estimated availability: 2 hours)
Artisanal Cheeses

Cheddar Cheese (in stock)
Cottage Cheese (in stock)
Goat Cheese (temporarily out of stock, estimated availability: 1.5 hours)
###New Arrivals

Roasted Almonds (in stock)
Fresh Mixed Berries (in stock)
Our Featured Item of the Day is our Quinoa Bites, made with organic quinoa and topped with a hint of honey. Would you like to try these out?

Would you like to place an individual order or a bulk order for a special occasion?

Type order now to place your order, update availability if you want to see updated availability of our items, or details of product if you want to know more about our products

###Also, we offer various payment modes including:

Credit/ Debit Card
Online Transfer
Cheque
COD
What will be your preferred mode of payment?"

##User: "order now"

##Bot: "You've decided to place an order. Please select the items you'd like to purchase, and I'll guide you through the process.

To place an order, please respond with the following format:

Item Name (Quantity)
For example, if you'd like to order 2 Quinoa Bites, you would respond with
Quinoa Bites (2)
Here's a reminder of our menu:
Fresh Produce
Fresh lettuce (in stock)
Red Apples (in stock)
Baby Carrots (temporarily out of stock, estimated availability: 1.5 hours)
Organic Delights
Brownies (in stock)
Quinoa Bites (in stock)
Almond Cake (limited stock, estimated availability: 2 hours)
Artisanal Cheeses
Cheddar Cheese (in stock)
Cottage Cheese (in stock)
Goat Cheese (temporarily out of stock, estimated availability: 1.5 hours)
New Arrivals
Roasted Almonds (in stock)
Fresh Mixed Berries (in stock)
What would you like to order?

(Remember, feel free to ask for item details if you need more information)

Your current total is: $0

###We have payment modes as follows:

Credit/ Debit Card
Online Transfer
Cheque
COD
Which mode of payment would you prefer to use?"

##User: "i will have 10 organic tomatoes"

##Bot: "Organic tomatoes are a great choice. Our organic tomatoes are locally sourced and are perfect for salads, sandwiches, or just snacking on their own.

###Here's your updated order:

###Order Summary:

Organic Tomatoes (10)
Availability Update:
We have 10 organic tomatoes in stock, so this quantity should be available for you.
Total:
###Your current total is: $5.50

###Types of Orders:

We have 2 types of orders:

###Individual Order: This is a standard order for personal consumption.
###Bulk Order: This is an order for a larger quantity of items, typically for special events or business purposes.
Which type of order would you like to place?

Type individual order for a standard order or bulk order for a larger quantity.

###Also, we have additional payment modes as follows:

Credit/ Debit Card ($5.50)
Online Transfer ($5.50)
Cheque ($5.50)
COD ($5.50)
Would you prefer cash on delivery(COD) to pay for your order. we will add $0.50 as service charge in case of COD

###what is your preferred mode of payment?"

##User: "Cash please"

##Bot: "You've chosen the cash payment option. We will add $0.50 as service charge to your total. Here's your updated receipt:

###Receipt:

Date: Today
Time: [Current Time]
Store Name: GreenLife Foods
Order Type: Cash Payment (COD)
Order Summary:

Organic Tomatoes (10) - $5.50
Service Charge: $0.50
Total: $6.00
Please note that we have added a $0.50 service charge as per our store policy.

Payment:

Payment has been received. Please take your receipt and enjoy your organic tomatoes.

Payment Mode:

Cash On Delivery (COD)

Thank you for shopping at GreenLife Foods. We hope you will visit us again soon.

Here's your invoice number: GLF/001

Please dispose of your receipt properly.

Have a nice day!"

