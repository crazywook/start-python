class Calculator:

  def __init__(self):
    self.__value = 0

  def adder(self, n):
    self.__value += n
    return self.__value

  def subtractor(self, n):
    self.__value -= n
    return self.__value

  def getValue(self):
    return self.__value

calculator = Calculator()
calculator2 = Calculator()

print(calculator.adder(9))
print(calculator2.adder(3))
print(calculator.subtractor(2))
print(calculator2.subtractor(1))

print('v1: ', calculator.getValue())
print('v2: ', calculator2.getValue())

class A:
  def show(self):
    print('AA')

A.show('')