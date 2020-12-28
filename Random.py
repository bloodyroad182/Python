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

problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]


out_line1=""
out_line2=""
out_line3=""
out_line4=""
error_counter=0

if len(problems) > 5:
    print ("Error: Too many problems.")

else:
    
    for problem in problems:
        calculations = problem.split()
        # print(calculations)
        # print(type(calculations))
        num1 = int(calculations[0])
        num2 = int(calculations[-1])
        operation = calculations[1]

        
        max_width=0
     
        separator="    "
        
        #Check if both numbers are integers
        if ((type(num1) == int) and (type(num2) == int)):
            # print("num1 and num2 are integers")
            
            if len(calculations[0]) > 4 or len(calculations[-1]) > 4:
                print("Error: Numbers cannot be more than four digits.")
            else:
                
                if operation == "+" or operation == "-":
                
                    if operation == "+":
                        total = num1 + num2
                        # return total
                    elif operation == "-":
                        total = num1 - num2
                    
                    #arrange output
                    if num1 >= num2:
                        # print("if statment: num1 >= num2")
                        max_width = len(calculations[0]) + 2
                        line1_space_counter = max_width - len(calculations[0])
                        # print(max_width)
                        # print(line1_space_counter)
                        if out_line1 =="":
                            while line1_space_counter > 0:
                                out_line1 += " "
                                line1_space_counter -= 1
                            out_line1 += str(calculations[0])
                        else:
                            while line1_space_counter > 0:
                                out_line1 += " "
                                line1_space_counter -= 1
                            out_line1 += separator + str(calculations[0])
                        
                        if out_line2 == "":
                            out_line2 += operation
                            line2_space_counter = max_width - 1 - len(calculations[-1])
                            while line2_space_counter > 0:
                                out_line2 += " "
                                line2_space_counter -= 1
                            out_line2 +=  str(calculations[-1])
                        else:
                            out_line2 += separator + operation
                            line2_space_counter = max_width - 1 - len(calculations[-1])
                            while line2_space_counter > 0:
                                out_line2 += " "
                                line2_space_counter -= 1
                            out_line2 += str(calculations[-1])

                        if out_line3 == "":
                            line3_space_counter = 0
                            while line3_space_counter < max_width:
                                out_line3 += "-"
                                line3_space_counter += 1
                        else:
                            out_line3 += separator
                            line3_space_counter = 0
                            while line3_space_counter < max_width:
                                out_line3 += "-"
                                line3_space_counter += 1
                            
                        if out_line4 == "":
                            line4_space_counter = 0
                            line4_space_counter = max_width - len(str(total)) 
                            while line4_space_counter > 0:
                                out_line4 += " "
                                line4_space_counter -= 1
                            out_line4 += str(total)
                        else:
                            out_line4 += separator
                            line4_space_counter = max_width - len(str(total)) 
                            while line4_space_counter > 0:
                                out_line4 += " "
                                line4_space_counter -= 1
                            out_line4 += str(total)

                    
                    else: # num2 > num1
                        max_width = len(calculations[-1]) + 2
                        line1_space_counter = max_width - len(calculations[0])
                        # print(max_width)
                        # print(line1_space_counter)
                        if out_line1 =="":
                            while line1_space_counter > 0:
                                out_line1 += " "
                                line1_space_counter -= 1
                            out_line1 += str(calculations[0])
                        else:
                            while line1_space_counter > 0:
                                out_line1 += " "
                                line1_space_counter -= 1
                            out_line1 += separator + str(calculations[0])
                        
                        if out_line2 == "":
                            out_line2 += operation
                            line2_space_counter = max_width - 1 - len(calculations[-1])
                            while line2_space_counter > 0:
                                out_line2 += " "
                                line2_space_counter -= 1
                            out_line2 +=  str(calculations[-1])
                        else:
                            out_line2 += separator + operation
                            line2_space_counter = max_width - 1 - len(calculations[-1])
                            while line2_space_counter > 0:
                                out_line2 += " "
                                line2_space_counter -= 1
                            out_line2 += str(calculations[-1])

                        if out_line3 == "":
                            line3_space_counter = 0
                            while line3_space_counter < max_width:
                                out_line3 += "-"
                                line3_space_counter += 1
                        else:
                            out_line3 += separator
                            line3_space_counter = 0
                            while line3_space_counter < max_width:
                                out_line3 += "-"
                                line3_space_counter += 1

                        if out_line4 == "":
                            line4_space_counter = 0
                            line4_space_counter = max_width - len(str(total)) 
                            while line4_space_counter > 0:
                                out_line4 += " "
                                line4_space_counter -= 1
                            out_line4 += str(total)
                        else:
                            out_line4 += separator
                            line4_space_counter = max_width - len(str(total)) 
                            while line4_space_counter > 0:
                                out_line4 += " "
                                line4_space_counter -= 1
                            out_line4 += str(total)
                
                else:
                    print("Error: Operator must be '+' or '-'.")
        
        else:
            print("Error: Numbers must only contain digits.")
            break
out_total = out_line1 + "\n" + out_line2 + "\n" + out_line3 + "\n" + out_line4
print(out_total)



