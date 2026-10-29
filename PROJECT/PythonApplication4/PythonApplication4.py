#n = int(input("Enter dlina:"))
#user_list = []
#i = 0
#while i < n:
#    string = ("enter lement#" +str(i + 1) + ": ")
#    user_list.append(input(string))
#    i+=1
#print(user_list)




#n = int(input("enter dlina:"))
#user_list = []
#i = 0
#while i<n:
#    string = "Enter element#" +str(i + 1) + ": "
#    user_list.append(input(string))
#    i += 1
#
#print(user_list)


#word = "itproger, hfyjfy"
#print(word.count("!"))
#0print(word.capitalize())


#print(word.find("p"))
#sgrgr = word.split(", ")
#for i in range(len(sgrgr)):
#    sgrgr[i] = sgrgr[i].capitalize()
#result = "!!".join(sgrgr)
#print(result)


#word = "Football"

#print(word[0:6:2])


#lis = [6, 4 , "Stroka", True, 6.5]
#from tkinter import LAST


#country = {"code": "UA", "name":"Ukranian", "population":40}
#country = dict(code="UA", name="Ukranian")
#print(country["name"])
#print(country)

#print(country.items())
#for el, val in country.items():
#    print(el," - ", val)

#print(country.get("name"))
#country.clear()
#country.pop("name")
#country["code"] = "none"
#print(country.i


#person = {
#    "user_1": {
#        "first_name":"John",
#        "last_name":"Marley",
#        "age":45,
#        "adress":"kiev",
#        "grades":{"math":12, "physics": 3}
#        },
#    "user_2": {
#        
#        }
#    }
#
#print(person["user_1"]["grades"])

#Artem = {
#    
#    "user_artem":{
#        "age":12,
#        "iq":52, 
#        "address": ("kiev"),
#        "grades": {"math": 2, "english": 4}
#}}
    
#print(Artem["user_artem"]["iq"])




##Timur = {
#    "opisanie Timura":{
#        "age": 12,
#        
#        "name2": ("dayn"),
#        "address":("kiev"),
#        "grades":{"math":2, "english":3, "science":2},
#        "iq":"iq timura:52"
#        }}
#print(Timur["opisanie Timura"]["iq"])





#nikita = {
#    "opisanie nikiti":{
#"iq":12,
#        "age":13,
#        "grades":{"math":10, "himia":2},
#        "address":("kiev")
#        }}
#
#print(nikita["opisanie nikiti"]["iq"])

#n = int(input("dlina lista:"))
#user_list = []
#i = 0
#while i<n:
#    string = "Enter element#"+ str(i + 1)+ ": "
#    user_list.append(input(string))
#    i+=1
#print(user_list)

#data = set("Hello")

#data = {5, 9, 4, 5}

#data.add(32)

#nums = [5,6,2,5]
#gonums = set(nums)
#new_data = frozenset([5, 3, 7, 5])

#print(new_data)




#def test_func(word):
#    print("word", end="")
#    print("!")



#test_func("HI")


#def summa(a, b):
#    res = a + b
#    return res

#res = summa(5, 7)
#print(res)
#print(summa("H", "i"))






#func = lambda x, y: x * y
#print(func(5,8))



import itertools

password = "teo132259123"
chars = "abcdefghijklmnopqrstuvwxyz0123456789"

for length in range(1, 15):  # длина пароля от 1 до 14
    for combo in itertools.product(chars, repeat=length):
        guess = ''.join(combo)
        if guess == password:
            print("Пароль найден:", guess)
            break
