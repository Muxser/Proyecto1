def comprobador(r, div, num, x):
  listdiv = []
  listnum = []
  while div:
    listdiv.append(div%10)
    div //= 10
  while num:
    listnum.append(num%10)
    num //= 10
  for i in range(10):
    if i == 0 and len(listdiv) == 4:
      x -= 1
    if listnum.count(i):
      x -= listnum.count(i)
    if listdiv.count(i):
      x -= listdiv.count(i)
    if x < 0:
      return False
    x = r
  return True

t = int(input())
while t > 0:
  t -= 1
  c, r = input().split()
  c = int(c)
  r = int(r)
  for div in range(int(10000/c), int(100000/c)):
    if div < 999:
      continue
    num = div * c
    if comprobador(r, div, num, r):
      print(str(num) + "/" + str(div) + "=" + str(c))
  print()