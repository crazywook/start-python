from House import House

class HouseV2(House):
  def travel(self, location, duration):
    print("%s, %s여행 %d일 가다." % (self.fullname, location, duration))

juliet = HouseV2("김")
juliet.setname("줄리엣")
juliet.travel("독도", 3)
