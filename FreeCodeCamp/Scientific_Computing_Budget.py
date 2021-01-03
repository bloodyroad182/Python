#https://repl.it/@mspx4qn1pg/boilerplate-budget-app#README.md

class Category:    
    def __init__ (self, category):
        self.category = category
        self.ledger = []
        
    def __str__(self):
        output=""
        out_max_width=30
        out_description_max_width=23
        category_title=""
        i=0
        while i < (out_max_width - len(self.category)) / 2 :
            category_title += "*"
            i += 1
        output += category_title + self.category + category_title + "\n"
        
        c = 0
        balance = 0
        while c < len(self.ledger):
            amount = self.ledger[c].split(":")
            descriptions = self.ledger[c+1].split(":")
            description = descriptions[1]
            balance += float(amount[1])
            # print (self.ledger[c+1])
            c += 2
            output += description + str(balance) + "\n"
        return output
    
    def deposit (self, amount, description=""):
        self.amount = str(amount)
        self.description = description
        self.ledger += ["amount:" + self.amount, "description:" + self.description]
    
    def withdraw(self, amount, description=""):
        if self.check_funds(float(amount)):  
            self.amount = str(amount)
            self.description = description        
            self.ledger += ["amount:-" + self.amount, "description:" + self.description]
            return True
        else:
            False

    def get_balance(self):
        # Retrieve all items in ledger
        c = 0
        balance = 0
        while c < len(self.ledger):
            amount = self.ledger[c].split(":")
            balance += float(amount[1])
            # print (self.ledger[c+1])
            c += 2
        return balance
        # print (len(self.ledger))

    def check_funds(self, checkfund):
        # Retrieve all items in ledger
        if self.get_balance() > checkfund:
            return True
        else:
            False

    def transfer(self, amount, dest_category):
        Transfer_Amount = float(self.amount)
        Transfer_source = "Transfer from " + self.category
        Transfer_destination = "Transfer to " + dest_category.category
        if self.check_funds(Transfer_Amount):
            self.withdraw(Transfer_Amount,Transfer_source)
            self.deposit(Transfer_Amount,Transfer_destination)
            return True
        else:
            return False
    # return "default return"


# def create_spend_chart(categories):

#Test Code
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

# print(create_spend_chart([food, clothing, auto]))

