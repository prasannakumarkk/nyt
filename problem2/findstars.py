import sys
class Point:
  def __init__(self, x, y, z):
    self.x, self.y, self.z = float(x), float(y), float(z)

  def __str__(self):
    return "({}, {}, {})".format(self.x, self.y, self.z)

  def __repr__(self):
    return "({}, {}, {})".format(self.x, self.y, self.z)

  def distance(self, q):
      return ((self.x - q.x) **2
              + (self.y - q.y) **2
              + (self.z - q.z) ** 2
              )**(1/2.0)

import fileinput
i=0
earthPoint = Point(0,0,0)
resultList = []
# for line in fileinput.input():
# with open('C:\\Users\\pkk8199\\Downloads\\hygdata_v3.csv') as db:
for line in fileinput.input():
    if i < 1:
        i+=1
        continue
    rec = line.split(",")
    starPoint = Point(rec[17], rec[18], rec[19])
    distFromEarth = starPoint.distance(earthPoint)
    # print(rec[0], distFromEarth, starPoint)
    resultList.append((starPoint,distFromEarth))

print(*sorted(resultList, key=lambda x : x[1])[:int(sys.argv[1])], sep="\n")



# findstars service : Data can be loaded into Spark RDD and can be queried
#                      on real time by passing arbitary point


