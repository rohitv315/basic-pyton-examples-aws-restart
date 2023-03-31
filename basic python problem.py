A=int(input("A= "))
B=int(input("B= "))

def find_greater(A,B):
    
    if A>B:
        print(A," is greater")
    else:
        print(B," is greater")
find_greater(A,B)


    
num = int(input("Enter a number:"))
if (num%2)==0:
    print(num," is even")
else:
    print(num," is odd")





inputn = int(input("Enter a number: "))

if inputn > 1:
  for i in range(2,inputn):
      if (inputn % i) == 0:
          print(inputn,"is not a prime number.")
          
          break
  else:
      print(inputn,"is a prime number.")

else:
  print(inputn,"is not a prime number.")


num = int(input("Enter a number:"))
factorial = 1

if num < 0:
  print("Sorry , factorial does not exit for negative no.")
elif num == 0:
  print("The factorial of 0 is 1")
else:
 for i in range (1,num + 1):
            factorial = factorial*i
 print("the factorial of ",num,"is",factorial)

#Python program to swap two variables



x = input('Enter value of x: ')
y = input('Enter value of y: ')


temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))

 
number = int(input("Please Enter any Number: "))
i = 1

print("The List of Natural Numbers from 1 to {0} are".format(number)) 

while ( i <= number):
    print (i, end = '  ')
    i = i + 1


num = int(input("Display multiplication table of? "))
for i in range(1, 11):
  print(num, 'x', i, '=', num*i)



list = [1, 3, 5, 7, 9]
for i in list:
    print(i)
