pwd = 'quiz/fileIO'
with open(pwd + '/sample1.txt', 'r') as f:
  numbers = f.readlines()

total = 0

for n in numbers:
  total += int(n)

average = total / len(numbers)

with open(pwd + '/result1.txt', 'w') as f:
  f.writelines([
    'total = %d \n' % total,
    'average = %0.2f \n' % average
  ])
