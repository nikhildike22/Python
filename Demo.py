from functools import reduce
num = [1,2,3,4,5,6,7,8]
num1 = [1,2,3,4]

is_even = lambda n : n % 2 == 0
double_it = lambda n : n * n
sum_it = lambda a,b: a+b

evens = list(filter(is_even,num))
doubles = list(map(double_it , evens))
sums = reduce(sum_it , evens)

print(evens)  
print(doubles)
print(sums)