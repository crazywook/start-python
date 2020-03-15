from functools import reduce

numbers = list(filter(lambda n:
  not (n % 3 and n % 5)
,range(1, 1000)))

result = 0
for n in list(numbers):
  result += n

print("result: %d" % result)

sum = reduce(lambda acc, curr: acc + curr,
  numbers)
print('lambda number %d' % sum)

sumReduce = reduce(
  lambda acc, curr: (
    acc if curr % 3 and curr % 5
      else acc + curr
  ), range(1, 1000))

print("sumReduce %d" % sumReduce)
