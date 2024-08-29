"""2.Write a Python program to implement for following.
(a) Create integer set from list and character set. Perform following functions on the 
same: update(), discard(), pop() and intersection()
(b ) Implement following string functions: replace(), count(), capitalize()."""
'''inte = list(range(1,11))
a = set(inte)

b = {'a' ,'b' ,'c' ,'d' ,'e'}

print(a)
print(b)

a.update([10,11])
b.update(['e','f'])

print(a)
print(b)

a.discard(11)
b.discard('f')

print(a)
print(b)

a.pop()
b.pop()

inter=a.intersection(b)
print(a)
print(b)

c = "charu"
d = "abcd"

print(c)
print(d)

c.replace('c','C')
print(c)
print(d)

print(c.count('a'))
print(d.count('a'))

print(c.capitalize(''))
print(d.capitalize())'''






'''3. Write a Python program to implement for following.
(a) Create a list of integers, mixed data types, duplicate data items and nested lists. 
# Create a list with integers, mixed data types, duplicate items, and nested lists
(b) Use nested indexing to display items from nested list.
# Nested indexing to display items from nested list
(c) Perform list methods: append(), insert() and remove(). 
# Perform list methods: append(), insert(), and remove()
# append() method



a = [1,'w','abc',1.2,[5,6,7]]
print(a)
b = a[4][1]
print(b)

a.append(8)
print(a)

a.insert(1,9)
print(a)

a.remove(9)
print(a)'''


'''4.
(a) Create a list of integers, mixed data types
(b) Show that lists are mutable
(c) Perform list methods: extend(), pop(), index(), count() and sort().

b =[2,1,4,6,5]
a = [1,'w','abc',1.2,[5,6,7]]
a[1]=2
print(a)
a.extend(a)
print(a)
print(a.index(1.2))
print(a.count('w'))
print(b.sort())







def is_armstrong_number(num):
    # Convert the number to a string to find its length
    num_str = str(num)
    # Calculate the power to which each digit should be raised
    power = len(num_str)
    # Calculate the sum of digits raised to the power
    sum_of_digits = sum(int(digit) ** power for digit in num_str)
    # Check if the sum of digits is equal to the original number
    return sum_of_digits == num

def is_palindrome(num):
    # Convert the number to a string and check if it's equal to its reverse
    return str(num) == str(num)[::-1]

if __name__ == "__main__":
    # Get input from the user
    number = int(input("Enter a number: "))
    
    # Check if the number is an Armstrong number
    if is_armstrong_number(number):
        print(number, "is an Armstrong number.")
    else:
        print(number, "is not an Armstrong number.")
    
    # Check if the number is a palindrome
    if is_palindrome(number):
        print(number, "is a palindrome.")
    else:
        print(number, "is not a palindrome.")











class MathOperation:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

if __name__ == "__main__":
    math_op = MathOperation()
    print(math_op.add(2, 3))       # Output: TypeError: add() missing 1 required positional argument: 'c'
    print(math_op.add(2, 3, 4))    # Output: 9

'''
'''

import tkinter as tk
from tkinter import messagebox

def credentials():
    password = pentry.get()
    username = uentry.get()

    if username =="username" and password == "password":
        messagebox.showinfo("success")
    else:
        messagebox.showerror("Error")
        

root = tk.Tk()
root.title = "Login"

ulabel= tk.Label(root,text = "username" )
ulabel.grid(row=0 ,column = 0,padx=10,pady=5,sticky = "e")
        
uentry = tk.Entry(root)
uentry.grid(row=0,column=1,padx=10,pady=5)


plabel= tk.Label(root,text = "password" )
plabel.grid(row=1 ,column = 0,padx=10,pady=5,sticky = "e")


pentry = tk.Entry(root)
pentry.grid(row=1,column=1,padx=10,pady=5)

lbutton = tk.Button(root,text="Login",command = credentials)
lbutton.grid(row=2 ,columnspan = 2,padx=10,pady=10)
root.mainloop()
