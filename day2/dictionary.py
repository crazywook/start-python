지민 = '지민'

hobby = {
  '성욱': 'basketball',
  '태연': 'volleyball',
  '지은': 'pingpong',
  지민: 'soccer',
  '지민': 'cricket'
}
print(hobby.get('혜리')) # return None
print(hobby.get('혜리', 'breath')) # return default value 'breath'
hobbyKeys = hobby.keys()
for k in hobbyKeys:
  print(k)
values = hobby.values()
print(values)
items = hobby.items()
print(items)
for item in items:
  print(item[1])