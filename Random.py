# class PartyAnimal:
#     x = 0
#     def party(self):
#         self.x = self.x + 2
#         print(self.x)

# an = PartyAnimal()
# an.party()
# an.party()

# URL: https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/object-lifecycle
# class PartyAnimal:
#     x = 0
#     name = ''
#     def __init__(self, nam):
#         self.name = nam
#         print(self.name,'constructed')
#     def party(self):
#         self.x = self.x + 1
#         print(self.name,'party count',self.x)

# q = PartyAnimal('Quincy')
# m = PartyAnimal('Miya')

# q.party()
# m.party()
# q.party()
# q.party()


# price = 810
# def mc_pricecalculator(price):
#     tax=8.88/100
#     mc_cc_discount=5/100
#     PriceWithDisc=(price+price*tax)-(price*mc_cc_discount)
#     print ("The total cost of the item with the 5% discount is: " + str(PriceWithDisc)) 
# mc_pricecalculator(price)

# def arithmetic_arranger(problems):
#   var_a = problems.split(",")
#   if len(var_a > 5):
#     print ("Error: Too many problems.")
#   else:
#     for problem in problems:
#         print (problem)
    
#     # return arranged_problems


# print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "45 + 43", "123 + 49"]))





