# def name_of_function(name):
#     print("hello "+name)
# name_of_function("raju")


# def myfunc():
#     print('Some text')
# myfunc()


# def say_hello():
#     print("how")
#     print("are")
#     print("you")
# say_hello()

# def say_hello(name):
#     print(f'hello {name}')
# say_hello("ram")

# def say_hello(name="defoult"):
#     print(f'hello {name}')
# say_hello()
# say_hello("ram")

# def say_hello(name="radha"):
#     print(f'hello {name}')
# say_hello()
# say_hello("ram")


# def print_result(a,b):
#     print(a+b)
# print_result(10,20)

# def print_result(a,b):
#     return a+b
# result=print_result(10,70)
# print(result)


# def sum_numbers(num1,num2):
#     return num1+num2
# print(sum_numbers(40,50))


# def even_check(number):
#     if number % 2 == 0:
#         return "even"
#     else:
#         Print("odd")
# print(even_check(20))



# def even_check(number):
#     result = number % 2 == 0
#     return result
# print(even_check(20))



##any of list number is even BCOZ of non next program
# def even_check_list(num_list):
#     for number in num_list:
#         if number % 2 == 0:
#            return True
#         else:
#             pass
# print(even_check_list([2,5,7]))
# print(even_check_list([3,5,7]))
# print(even_check_list([3,4,7]))
# print(even_check_list([2,6,6]))




# def even_check_list(num_list):
#     for number in num_list:
#         if number % 2 == 0:
#            return True
#         else:
#             pass
#     return False
# print(even_check_list([2,5,7]))
# print(even_check_list([3,5,7]))
# print(even_check_list([3,4,7]))
# print(even_check_list([2,6,6]))



# def even_check_list(num_list):
#     even_number=[]
#     for number in num_list:
#         if number % 2 == 0:
#            even_number.append(number)
#         else:
#             pass
#     return even_number
# print(even_check_list([3,4,7]))
# print(even_check_list([2,6,6]))



# stock_price=[("appl",200),("goog",400),("NSFT",100)]
# for item in stock_price:
#     print(item)
# for ticker,price in stock_price:
#     print(ticker)
# for ticker,price in stock_price:
#     print(price)
# for ticker,price in stock_price:
#     print(price+0.1*price)


# work_hours=[("abby",100),("billy",400),("cassie",800)]
# def employee_check(work_hours):
#     current_max=0
#     employee_of_month=""
#     for employee,hours in work_hours:
#         if hours > current_max:
#             current_max=hours
#             employee_of_month=employee
#         else:
#             pass
#     return (employee_of_month,current_max)
# print(employee_check(work_hours))


# work_hours=[("abby",100),("billy",400),("cassie",800)]
# def employee_check(work_hours):
#     current_max=0
#     employee_of_month=""
#     for employee,hours in work_hours:
#         if hours > current_max:
#             current_max=hours
#             employee_of_month=employee
#         else:
#             pass
#     return (employee_of_month,current_max)
# result=employee_check(work_hours)
# print(result)


# work_hours=[("abby",100),("billy",400),("cassie",800)]
# def employee_check(work_hours):
#     current_max=0
#     employee_of_month=""
#     for employee,hours in work_hours:
#         if hours > current_max:
#             current_max=hours
#             employee_of_month=employee
#         else:
#             pass
#     return (employee_of_month,current_max)
# name,hours=employee_check(work_hours)
# print(name,hours)
# print(name)
# print(hours)


# work_hours=[("abby",100),("billy",400),("cassie",800)]
# def employee_check(work_hours):
#     current_max=0
#     employee_of_month=""
#     for employee,hours in work_hours:
#         if hours > current_max:
#             current_max=hours
#             employee_of_month=employee
#         else:
#             pass
#     return (employee_of_month,current_max)
# item=employee_check(work_hours)
# print(item)


# example=[1,2,3,4,5,6,7,8,9,0,]
# from random import shuffle
# def shuffle_list(mylist):
#     shuffle(mylist)
#     return mylist
# result = shuffle_list(example)
# print(result)

# mylist = [" ","0"," "]
# print(shuffle_list(mylist))




# def player_guess():
#     guess=''
#     while guess not in ['0','1','2']:
#           guess=input("pick a number:0,1 or 2:")
#     return int(guess)
# print(player_guess())



# def check_guess(mylist,guess):
#     if mylist[guess]=="0":
#         print("correct!")
#     else:
#         print("wrong Guess")
#         print(mylist)

# #INITIAL LIST
# mylist=['','0','']
# #SHUFFLE LIST
# mixedup_list=shuffle_list(mylist)
# #USER GUESS
# guess=player_guess()
# #CHECK GUESS
# check_guess(mixedup_list,guess)


# def myfunc(name):
#     return 'Hello {}'.format(name)
#     #print('Hello {}'.format(name))
# print(myfunc("john"))






def myfunc(x):
    out = []
    for i in range(len(x)):
        if i%2==0:
            out.append(x[i].lower())
        else:
            out.append(x[i].upper())
    return ' '.join(out)   
print(myfunc('Anthropomorphism'))