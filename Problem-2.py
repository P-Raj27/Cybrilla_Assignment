list1 = []

list1 = [int(item) for item in input("Enter the list items : ").split()]

flag = False
for i in range(len(list1)-1):
  x = set()
  for k in range(i+1, len(list1)):
    summ = -(list1[i]+list1[k])
    if summ in x:
      print(summ, list1[i], list1[k])
      flag = True
    else:
      x.add(list1[k])
if flag == False:
  print("not found")
