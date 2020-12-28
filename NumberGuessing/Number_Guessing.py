# import random
# def random_num(v1, v2):
#     return random.randint(v1,v2)

import re
passwd = "securepasswd"
# print(len(passwd))
for i in passwd:
    print (i)
    print(bool(re.match(i,"[a-z]") and True))
        

# def verify_password(passwd):
#     for i in passwd
#         print(i)

# attempt_list=[]
# print(random_num(1,100))