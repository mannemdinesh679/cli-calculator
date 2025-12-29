a=int(input("Enter the first num: "))
b=int(input("Enter the second num: "))
choice=int(input("Enter the choice (+,-,*,/,%):"))
if choice==1:
	print(a+b)
elif choice==2:
	print(a-b)
elif choice==3:
	print(a*b)
elif choice==4:
	print(a/b)
elif choice==5:
	print(a%b)
else:
	print("Invalid choice")