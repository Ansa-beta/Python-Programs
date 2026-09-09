num = int(input("Enter a number: "))
temp=num
total=0
while num>0:
    digit=num%10
    total+=digit**len(str(num))
    num//=10
if total==temp:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

