f = open("./day5/test.txt", 'w')
f.write('test file\n')
f.write('test file2\n')

if f.readable():
  print('read file')
  f.read()

f.close()

f = open("./day5/test.txt", 'r')

if f.readable():
  print('read file')
  line = f.read()
  # print('line', ''.join(line))
  print('line', line)

f.close()

f = open("./day5/test.txt", 'a')
f.write('test file3\n')
f.close()

with open("./day5/test.txt", 'r') as f:
  if f.readable():
    print('read file')
    line = f.read()
    print(line)
    print('isClosed in with', f.closed)

print('isClosed', f.closed)
if not (f.closed):
  f.close()
