# hotel management
# this program is to get the order from the customer in selecting hotel and their dish of choice
class Hotel:
    def __init__(self, menu, hotel):  # This is to assign the values of hotel and menu to self
        self.menu = menu
        self.hotel = hotel

    def order(self):  # here the method order uses the values of  the objects hotel and menu by using self
        while True:  # while condition is to rerun the program incase the customer enters wrong hotel or name of dish
            print(f"The available shops are: {self.hotel}")  # this is to show the customer the available hotels
            slctd_hotel = input("Enter your choice of hotel: ")  # their choice is stored in a variable for easy access
            if slctd_hotel.upper() in self.hotel:  # their choice of hotel is checked for any errors
                print(f"Your menu: {self.menu}")   # customer is shown the available dishes in the menu
                slctd_dish = input("Enter your dish: ")  # choice of customer stored as selected dish
                if slctd_dish.upper() in self.menu:  # their choice is checked for any errors
                    print(f"The hotel u have selected is {slctd_hotel} and the dish ordered by u is {slctd_dish}")
                    # showcase of customers order/ selection
                    payment = input("Enter your mode of payment(UPI, credit, cash): ")  # payment method is asked
                    if payment.upper() == "UPI":  # choice of customer to use UPI
                        print("Payment through UPI is successful")
                    elif payment.upper() == "CREDIT":  # choice of customer to use credit
                        print("Payment through credit is successful")
                    else:  # choice of customer to use cash
                        print("Cash is accepted on delivery")
                    print("Your order is on the way")
                    break  # loop is broken if there is no error in customer's selection/ choice

                else:  # else condition is to rerun the program due to an error
                    # in the absence of customer's selection in the list of dishes available
                    print("Your choice does not seem to be available!! Try again")

            else:  # else condition is to rerun the program due to an error
                # in the absence of customer's selection in the list of hotels available
                print("Your choice does not seem to be available!! Try again")


# customer is the object of the class Hotel which is assigned the parameters (menu and hotel)
customer = Hotel(["PIZZA","GARLIC BREAD","MILKSHAKE","BEVERAGES","CHOCO LAVA"],
                 ["DOMINOS","PIZZA HUT","OVEN STORY","OYALO"])
customer.order()  # customer is an object of the type order
