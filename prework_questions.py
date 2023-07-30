#Question One

def hello_name():
    """function to greet user"""
    user_name = input('Enter username: ')
    print ('Hello, ' + user_name)

hello_name()

#Question Two

def first_odds():
    """Print odd numbers between 1 and 100"""
    for i in range(1,101,2):
        print(i)

first_odds()

#Question Three

list=[3,67,34,78,55,66]

def max_num_in_list(a_list):
    """Return the highest number in a list"""
    print(max(a_list))

max_num_in_list(list)

#Question Four

def is_leap_year(a_year):
    """check if a year is or was a leap year"""
    if a_year % 4 == 0:
        if a_year % 100 != 0 or a_year % 400 ==0:
            return True
    else:
       return False


print(is_leap_year(1998))
print(type(is_leap_year(1998)))

#Question Five
a_list = [1,2,3,4,3]

def is_consecutive(a_list):
    """determine if list items are consecutive"""
   
    for x in a_list[:-2]:
        if a_list[x] + 1 == a_list [x + 1]:
            continue
        else:
            return False
    return True
    
print(is_consecutive(a_list))