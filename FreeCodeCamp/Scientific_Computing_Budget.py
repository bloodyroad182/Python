#https://repl.it/@mspx4qn1pg/boilerplate-budget-app#README.md

class Category:
        
    def __init__ (self, category):
        self.category = category
        self.ledger = []
        
    def __str__(self):
        output=""
        out_max_width=30
        out_description_max_width=23
        category_title_space=""
        i=0
        while i < (out_max_width - len(self.category)) / 2 :
            category_title_space += "*"
            i += 1
        output += category_title_space + self.category + category_title_space + "\n"
        c = 0
        balance = 0
        while c < len(self.ledger):
            amount = self.ledger[c].split(":")
            descriptions = self.ledger[c+1].split(":")
            description = descriptions[1]
            if len(description) > out_description_max_width:
                output += description[:23]
                space_c = out_max_width - (23 + len(str(amount[1])))
                while space_c > 0:
                    space_c -= 1
                    output += " "
            else:
                output += description
                space_c = out_max_width - (len(description) + len(str(amount[1])))
                while space_c > 0:
                    space_c -= 1
                    output += " "
            output += str(amount[1]) + "\n"            
            balance += float(amount[1])
            # print (self.ledger[c+1])
            c += 2
            # output += description + str(amount[1]) + "\n"
        output += "Total: " + str(balance)
        return output
    
    def deposit (self, amount, description=""):
        self.amount = "{:.2f}".format(amount)
        self.description = description
        self.ledger += ["amount:" + self.amount, "description:" + self.description]
    
    def withdraw(self, amount, description=""):
        if self.check_funds(float(amount)):
            self.amount = "{:.2f}".format(amount)
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
        Transfer_Amount = float(amount)
        Transfer_source = "Transfer to " + dest_category.category
        Transfer_destination = "Transfer from " + self.category
        if self.check_funds(Transfer_Amount):
            self.withdraw(Transfer_Amount,Transfer_source)
            dest_category.deposit(Transfer_Amount,Transfer_destination)
            return True
        else:
            return False
    # return "default return"


def create_spend_chart(categories):
    spend_by_categories=[]
    spend_by_categories_in_perc=[]
    total_category_spent=0
    grand_total_spent=0
    for category in categories:
        c=0
        while c < len(category.ledger):
            amount = category.ledger[c].split(":")
            if float(amount[1]) < 0:
                total_category_spent += float(amount[1])                
            else:
                pass
            c += 2
            # print(category.category)
            # print(str(amount[1]))
        spend_by_categories.append(category.category)
        spend_by_categories.append(total_category_spent)
    
    #calculate grand_total_spent accross all categories
    c=0
    while c < len(spend_by_categories):
        grand_total_spent += spend_by_categories[c+1]
        c += 2
    # print("Grand total spent: " + str(grand_total_spent))

    #Calculate percentage spent by categories
    c=0
    cat_perc=0
    while c < len(spend_by_categories):
        cat_perc = (spend_by_categories[c+1] * 100) / grand_total_spent
        cat_perc = int((cat_perc)/10) * 10
        spend_by_categories[c+1] = cat_perc
        # print(cat_perc)
        c += 2

    output="Percentage spent by category\n"
    out_bar = 100
    out_bar_scale = 10
    out_bar_cat_perc_t ="o  "
    out_bar_cat_perc_f ="   "
    out_bar_cat_name = "     "
    while out_bar >= 0:
        if len(str(out_bar)) == 3:
            output += str(out_bar) + "| "
            c=0
            while c < len(spend_by_categories):
                if spend_by_categories[c+1] >= out_bar:
                    output += out_bar_cat_perc_t
                else:
                    output += out_bar_cat_perc_f
                c += 2
            output += "\n"
        elif len(str(out_bar)) == 2:
            output += " " + str(out_bar) + "| "
            c=0
            while c < len(spend_by_categories):
                if spend_by_categories[c+1] >= out_bar:
                    output += out_bar_cat_perc_t
                else:
                    output += out_bar_cat_perc_f
                c += 2
            output += "\n"
        else:
            output += "  " + str(out_bar) + "| "
            c=0
            while c < len(spend_by_categories):
                if spend_by_categories[c+1] >= out_bar:
                    output += out_bar_cat_perc_t
                else:
                    output += out_bar_cat_perc_f
                c += 2
            output += "\n"
        out_bar -= out_bar_scale
    # print(spend_by_categories)
    #Generate total "-" under the bar chart
    c = (len(spend_by_categories)/2) * 3 + 1
    output += "    "
    while c > 0:
        output += "-"
        c -= 1
    output += "\n"
    
    #Generate category names under the bar chart
    c=0
    largest_category_name=0
    while c < len(spend_by_categories)-1:
        if len(spend_by_categories[c]) > largest_category_name:
            largest_category_name = len(spend_by_categories[c])
        else:
            pass
        c += 2
    # print ("largest cat length = " + str(largest_category_name))
    # output += "largest cat length = " 
    i=0
    while i < largest_category_name:
        c=0
        output += "     "
        while c < len(spend_by_categories)-1:
            if len(spend_by_categories[c]) <= largest_category_name:
                if i < len(spend_by_categories[c]):
                    output += spend_by_categories[c][i] + "  "
                else:
                    output += "   "
            c += 2
        output += "\n"
        i += 1

    return output
        

#Test Code
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
# print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

# print(food)
# print(clothing)

print(create_spend_chart([food, clothing, auto]))
# print("EOF")
