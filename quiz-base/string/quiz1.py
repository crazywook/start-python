pin="881120-1068234"
splitted = pin.split("-")
yyyymmdd = splitted[0]
num = splitted[1]

print(yyyymmdd)
print(num)
genderNum =  num[0]

def decideGender(num):
  if genderNum == "1":
    print('male')
  elif genderNum == "2":
    print('female')

decideGender(genderNum)
