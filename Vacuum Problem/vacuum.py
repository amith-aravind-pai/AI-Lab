class Vacuum:
  def __init__(self):
    self.position = 'A'
  def clean(self,roo):
    roo.isCleaned = True
    print("Cleaned room " + roo.name)

class Room:
  def __init__(self,name):
    self.name = name
    self.isCleaned = False
  def isClean(self):
    return self.isCleaned


def vac_clean(vac,roomA,roomB):
  while(True):
    if(roomA.isClean() and roomB.isClean()):
      print("All rooms are clean!")
      break
    if(vac.position == 'A'):
      if(roomA.isClean()):
        print("Moving to B ...")
        vac.position = 'B'
      else:
        vac.clean(roomA);
    if(vac.position == 'B'):
      if(roomB.isClean()):
        print("Moving to A ...")
        vac.position = 'A'
      else:
        vac.clean(roomB);

vac = Vacuum()
roomA = Room('A')
roomB = Room('B')
vac_clean(vac,roomA,roomB)


