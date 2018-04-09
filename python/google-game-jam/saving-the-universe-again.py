def swap(i, j, sec):
  l = list(sec)
  x = l[i]
  l[i] = l[j]
  l[j] = x
  sec = "".join(l)
  return (sec)

def finish(str):
  char = False
  i = 0
  while (i < len(str)):
    if (str[i] == 'C'):
        char = True
    if (char and str[i] == 'S'):
        return (False)
    i += 1
  return (True)

def compute_score(sec):
    score = 0
    charge = 1
    for i in range(len(sec)):
        if (sec[i] == 'C'):
            charge += charge
        else:
            score += charge
    return (score)

def compute(mini, sec):
    nbSteps = 0
    i = len(sec) - 2
    while (not(finish(sec)) and i >= 0):
        if (compute_score(sec) <= mini):
            return (nbSteps)
        if (sec[i] == 'C' and sec[i + 1] == 'S'):
            nbSteps += 1
            sec = swap(i, i + 1, sec)
            i = len(sec) - 1
        i -= 1
    if (compute_score(sec) <= mini):
        return (nbSteps)
    else:
        return ('IMPOSSIBLE')


nbInputs = int(input())

for i in range(nbInputs):
  inputs = input().split(' ')
  mini = inputs[0]
  sec = inputs[1]
  print("Case #{}: {}".format(i + 1, compute(int(mini), sec)))
