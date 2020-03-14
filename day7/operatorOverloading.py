from House import House

class ExtendedHouse(House):
  def love(self, other):
    print("%s, %s 사랑에 빠졌네" % (self.fullname, other.fullname))
  def __add__(self, other):
    print("%s, %s 결혼했네" % (self.fullname, other.fullname))
  def fight(self, other):
    print("%s, %s 싸우네" % (self.fullname, other.fullname))
  def __sub__(self, other):
    print("%s, %s 이혼했네" % (self.fullname, other.fullname))

kim = ExtendedHouse("김")
kim.setname("성욱")
stone = ExtendedHouse("스톤")
stone.setname("엠마")

kim.love(stone)
kim + stone
kim - stone