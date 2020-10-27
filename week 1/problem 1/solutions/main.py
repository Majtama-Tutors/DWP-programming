# let's make a class for the user

class User():
    def __init__(self):
        self.shopping_cart = []
        self.donuts = [
            {
                "name": "red",
                "price": 5.55
            },
            {
                "name": "green",
                "price": 2.25
            },
            {
                "name": "orange",
                "price":3.36
            },
            {
                "name": "purple",
                "price": 4.77
            },
            {
                "name": "white",
                "price": 3.23
            },
            {
                "name": "brown",
                "price": 4.44
            },
            {
                "name": "yellow",
                "price": 3.00
            }
        ]

    def run(self):
        print("----- JIMS DONUT SHOP -----")
        print("Welcome to Jims Donut Shop!")
        print("Enter the number beside the command name to run that command")
        self.main_menu()
    
    def main_menu(self):
        print("Enter the number beside the command name to run that command")
        print("----- COMMANDS -----")
        print("[1] Start shopping!")
        print("[2] Checkout")
        print("")
        print("Enter the command number: ")
        res = int(input())

        if res == 1:
            self.item_prompt()
        elif res == 2:
            self.checkout()
        else:
            print("Sorry your input was invalid!")
            self.main_menu()
        

    def add_item(self, item):
        self.shopping_cart.append(item)
        print("Added item: " + item["name"])
        print("Would you like to add another item? Y/N")
        res = input()

        if res.upper() == "Y":
            self.item_prompt()
        else:
            self.main_menu()
    
    def item_prompt(self):
        print("")
        print("Here are the items and their prices!")

        for i in range(len(self.donuts)):
            donut = self.donuts[i]
            print("[" + str(i + 1) + "] " + donut["name"] + " = $" + str(donut["price"]))

        print("")
        print("Enter the number beside the item to add that item to your shopping cart")
        res = int(input())

        try:
            self.add_item(self.donuts[res - 1])
        except IndexError:
            print("Sorry this item doesn't exist!")
            print("Do you want to go back to adding items? Y/N")
            res = input()

            if res.upper() == "Y":
                self.item_prompt()
            else:
                print("Thanks for coming to Jims Donut Shop!")

    def checkout(self):
        total = 0
        print("Checking out...")
        for item in self.shopping_cart:
            print("Item name: " + item["name"] + " " + str(item["price"]))
            total += item["price"]

        print("Total = " + str(total))
        grand = round(total * 1.13, 2)
        print("HST = " + str(grand))
        print("Grand Total = " + str(grand))
    

if __name__ == "__main__":
    user = User()
    user.run()