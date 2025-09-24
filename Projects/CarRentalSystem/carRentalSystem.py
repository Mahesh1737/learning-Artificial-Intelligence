# Car database with brand -> car -> rent & deposit
cars = {
    "Toyota": {
        "Innova": {"rent": 1200, "deposit": 5000},
        "Fortuner": {"rent": 2500, "deposit": 8000, "discount": 10},  # 10% discount
    },
    "Hyundai": {
        "i20": {"rent": 800, "deposit": 3000},
        "Creta": {"rent": 1500, "deposit": 6000},
    },
    "Maruti": {
        "Swift": {"rent": 700, "deposit": 2500},
        "Baleno": {"rent": 900, "deposit": 3500},
    }
}

def show_brands():
    print("\nAvailable Brands:")
    for brand in cars:
        if cars[brand]:  # Only show brand if cars are available
            print("-", brand)

def show_cars(brand):
    print(f"\nCars in {brand}:")
    for model in cars[brand]:
        rent = cars[brand][model]["rent"]
        deposit = cars[brand][model]["deposit"]
        discount = cars[brand][model].get("discount", 0)
        discount_text = f" (Discount {discount}%)" if discount > 0 else ""
        print(f"{model} -> Rent: ₹{rent}/day, Deposit: ₹{deposit}{discount_text}")

def main():
    while any(cars.values()):  # Run until at least one car is left
        show_brands()
        brand = input("\nEnter brand you prefer: ")
        
        if brand in cars and cars[brand]:
            show_cars(brand)
            car = input("\nEnter car model: ")
            
            if car in cars[brand]:
                rent = cars[brand][car]["rent"]
                deposit = cars[brand][car]["deposit"]
                discount = cars[brand][car].get("discount", 0)
                
                days = int(input("Enter number of days: "))
                total = (rent * days) + deposit
                
                if discount > 0:
                    discount_amount = total * (discount / 100)
                    total -= discount_amount
                    print(f"\nSpecial Discount Applied: {discount}% off (-₹{discount_amount:.2f})")
                
                print(f"\nSelected Car: {car}")
                print(f"Rent per day: ₹{rent}, Deposit: ₹{deposit}")
                print(f"Total Price = (Rent × Days) + Deposit = ₹{rent} × {days} + {deposit} = ₹{total}")
                
                choice = input("Do you want to approve this bill? (yes/no): ")
                if choice.lower() == "yes":
                    print(f"\nBooking Confirmed for {car} ({days} days). Final Price = ₹{total}")
                    break
                else:
                    print(f"\n{car} removed temporarily. Let's choose another car.")
                    del cars[brand][car]  # Remove car temporarily
            else:
                print("Invalid car model.")
        else:
            print("Invalid brand or no cars left in this brand.")
    
    else:
        print("\nNo cars available for booking. Please try again later.")

if __name__ == "__main__":
    main()
