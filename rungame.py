import os
for level in os.listdir("lockedgame-levels"):
  path = os.path.join("lockedgame-levels", level)
  if os.path.isfile(path):
    print("===",level,"===")
    print(open(path).read())

