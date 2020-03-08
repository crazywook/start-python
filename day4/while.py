prompt = """
  1.Add
  2.Del
  4.Quit
Enter number: """

number = 0
while number != 4:
  print(prompt)
  number = int(input())
  print('choice', number)
