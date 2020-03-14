class House:
  lastname = ""
  firstname = ""
  fullname = ""
  def __init__(self, lastname):
    self.lastname = lastname
  def setname(self, name):
    self.firstname = name
    self.fullname = self.firstname + self.lastname
  def travel(self, location):
    print("%s, %s여행을 가다." % (self.fullname, location))

def createHouse(lastname):
  return House(lastname)

if __name__ == "__main__":
  kim = House('kim')
  kim.setname('sungwoook')
  kim.travel('india')
