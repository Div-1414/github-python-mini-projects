menu = {
    "Pizza": 120,
    "Burger": 80,
    "Pasta": 100,
    "Coffee": 60,
    "Sandwich": 70,
    "French Fries": 90,
    "Cold Drink": 40,
    "Ice Cream": 50,
    "Salad": 60,
    "Soup": 75,
    "Noodles": 110,
    "Manchurian": 130,
    "Thali": 200,
    "Paneer Tikka": 180,
    "Chapati": 15,
    "Rice": 100,
    "Dal": 90,
    "Paratha": 40
}
oder={}
def show_menu():
    print("Today's Menu⬇️")
    for key,value in menu.items():
        print(f"{key}:{value}")

def take_oder():
    while True:
        item=input("Enter the food name you want to order (enter 'Done' when you have finished ordering). : ")
        if item=="Done":
           print(" ")
           print("Your entered order:-")
           print("-------------------------------------")
           for key,value in oder.items():
               print(f"{key}:{value}")
           print("------------------------------------")   
           a=input("If you want to confirm oder then enter 'Confirm' or if you want to reoder then enter 'Reoder' : ").capitalize()
           print("-"*50)
           if a=="Confirm":
               print("Oder confirmed🫡")
               break
           else:
               print("-"*50)
               print("Re-enter your oder:- ")
               oder.clear()
               continue
             
                  
        elif item in menu:
            q=int(input(f"Enter the Quantity of {item} : "))
            oder[item]=oder.get(item,0)+q
        else:
            print("❌ Item Not Avilabel")    
    
def genrate_bill(name):
   
        print("Javiya's Resturant")
        print("******************************")
        print("Your Bill:--")
        print(f"Customber Name: {name}")
        print("-------------------------------")
        total=0
        for item,q in oder.items():
            prices=menu.get(item)*q
            total+=prices
            print(f" {item}*{q}={prices}")
        gst=total*0.05
        grandtotal=total+gst
        print("--------------------------")
        print(f"Subtotal = {total}")
        print(f"5% Gst   = {gst}")
        print(f"Total Bill = {grandtotal}")
        print("----------------------------")
        print("Thank you🙏")
        print("Visit Again😁")


            
        
             
print("🙏Welcome to the Automated Ordering System of our Restaurant.🙏")
name=input("Enter Your Name: ")




while True:
    print("-"*50)
    print("1. Menu")
    print("2. Oder")
    print("3.Genrate bill")
    print("-"*50)
    try :
        b=int(input("Enter your choise "))
    except ValueError:
        print("Only enter avilabel options")
        continue    
    match(b):
        case(1):
            show_menu()
        case(2):
            take_oder()
        case(3):
            if oder:
                genrate_bill(name)
                break
            else:
                print("☠️Oder Not placed")
                continue
              
              
            
        case _:
            print("Invalid Coise!")
            continue            

    

