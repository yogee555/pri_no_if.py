# Prime number without using for loop

n=int(input("enter n value: "))   # Take the user input & store n value
count=0                           # count is 0
for i in range(2,n):              # range take 2 and n value
    if n%i==0:                    # n modulus i is 0
        count = count+1           # count is add 1 value
        break                     # add value is end/break
if count == 0:                    # prime number is execute print prime number
    print("prime number")
else:
    print("not prime number")     # Not prime number print this execution
