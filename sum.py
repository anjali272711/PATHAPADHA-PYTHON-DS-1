# WAP to print the sum of even and odd numbers in the range of 20 to 30

even_sum=0
odd_sum=0

start = 20
end = 31

while start < end:
  if(start%2 == 0):
    even_sum+=start
  else:
    odd_sum+=start
  start+= 1
print("Sum of even numbers between 20 to 30 is :",even_sum)
print("Sum of odd numbers between 20 to 30 is :",odd_sum)
