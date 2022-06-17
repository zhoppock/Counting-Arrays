totalCount = 10
people = 0
dep = 0
counts = [0,0,0,0,0,0]
while people < totalCount:
  dep = int(input("How many dependents? "))
  if dep > 5 or dep < 0:
    print("Error")
  counts[dep] = counts[dep] + 1
  people += 1
  print(counts)
print("\nPeople with 0 dependents: " + str(counts[0]))
print("People with 1 dependent:  " + str(counts[1]))
print("People with 2 dependents: " + str(counts[2]))
print("People with 3 dependents: " + str(counts[3]))
print("People with 4 dependents: " + str(counts[4]))
print("People with 5 dependents: " + str(counts[5]))