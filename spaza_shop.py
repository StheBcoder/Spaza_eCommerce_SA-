# Spaza shop eCommerce Portfolio Project 
# Owner : Sthembile Buthelezi / Location : South Africa 

products = {
    "Bread": 18.00,
    "Milk": 22.50,
    "Eggs (dozen)": 45.00, 
    " Maize Meal 5kg": 89.99,
    "Airtime R30": 30.00
}


cart = []

stock = {
    "Bread": 20,
    "Milk": 15,
    "Eggs (dozen)": 10,
    "Maize Meal 5kg": 8,
    "Airtime R30": 50
}

def show_products(): 
    print("\n--- Welcome to Spaza eCommerce ---")
    for item, price in products.items():
        print(f"{item} - R{price}") 


def add_to_cart(): 
    show_products()   
    choice = input("\nWhat do you want to buy? Type name: ") 
    if choice in products:
        cart.append(choice) 
        print(f"Added {choice} to cart!")
    else: 
        print("Item not found! ")


def checkout():
    if not cart:
        print("cart is empty! ") 
        return
    total = sum(products[item] for item in cart)
    print("\n--- Your Receipt ---") 
    for item in cart:
        print(f"{item} - R{products[item]}") 
    print(f"Total: R{total:.2f}")  
    print("Thank You! Order has been placed. ")


# Main App 
while True:   
    print("\n1. View Products\n2. Add to Cart\n3. Checkout\n4. Exit")
    option = input("Choose: ") 
    if option == "1":   
        show_products()
    elif option == "2": 
        add_to_cart() 
    elif option == "3": 
        checkout()
    elif option == "4": 
        print("Shop closed. See you Tommorrow!")
        break                        