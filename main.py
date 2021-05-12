'''
Task 1

Write a function called oops that explicitly raises an IndexError exception when called. Then write another function that calls oops inside a try/except state­ment to catch the error. What happens if you change oops to raise KeyError instead of IndexError?

'''
def oops(i):
    try:
        int(i)
        return(f'There is not element with index {i}')
    except:
        raise KeyError
        return(f'There is not element with key {i}')

def elem_l(list, i):
    try:

        return list[int(i)]
    except IndexError:
        return oops(i)
    except:
        return 'index must be int'
def elem_d(dict, k):
    try:
        return dict[k]
    except KeyError:
        return oops(k)
print(elem_l((input('put list ')).split(), input("put index ")))
print('now please put keys and items to it to try next function and the end print *')
user={}
key=input('Key:')
item = input('Item:')
while key!='*' and item!='*':
    user.update({key:item})
    key=input('Key:')
    item = input('Item:')
print(elem_d(user,input('put key ')))
'''
Task 2

Write a function that takes in two numbers from the user via input(), call the numbers a and b, and then returns the value of squared a divided by b, construct a try-except block which raises an exception if the two values given by the input function were not numbers, and if value b was zero (cannot divide by zero).  
 '''


def calc():
    while True:
        try:
            a = int(input('Put number a '))
            b = int(input('Put number b '))
            return a**2/b
        except ValueError:
            print('you can put only int! try again')
        except ZeroDivisionError:
            print('b cant be nul')
        except:
            print('something wrong. try again')
print('answer:', calc())
