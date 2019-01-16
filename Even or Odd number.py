def isEven(n):
      if n%2==0:
            return True
      else:
            return False
n=int(input("Enter no :"))
even=isEven(n)
if even:
      print(n,"is even")
else:
      print(n,"is odd")
