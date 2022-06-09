def printPattern(targetNumber) :
  if (targetNumber <= 0) :
    print(targetNumber)
    return
 # Recursive Case
  print(targetNumber)
  printPattern(targetNumber - 5)
  print(targetNumber)
n = 10
printPattern(n)
