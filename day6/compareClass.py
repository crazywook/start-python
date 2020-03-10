class Simple:
  pass

print(Simple() == Simple())
print('type', type(Simple()) is Simple)
print(isinstance(Simple(), Simple))
