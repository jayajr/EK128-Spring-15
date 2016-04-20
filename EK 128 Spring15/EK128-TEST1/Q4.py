names=["Noah", "Esther", "Jessica", "Diego", "Jerome", "Rachel", "Arslan",
  "Nicholas", "Benjamin", "Charles", "Benjamin", "William", "Abraham",
  "Ricardo", "Nicholas", "Daniel", "Adeeb", "Nathaniel", "David",
  "David", "Kenneth", "Tate", "Ricky", "Veronica", "Blake", "Sabrina",
  "Brian", "Baraa", "Jared", "Douglas", "Jeffrey", "Erostin", "Trent",
  "Nicholas", "Michaela", "Erin", "Anton", "Khai", "Simone", "Jasper",
  "Sami", "Illya", "Eric", "Bonnie", "Joseph", "Jack", "Barry",
  "Shuxian", "Chengjie"]

Dlengths = {}
y=0
div = 0
count = -1

for i in names:
    x = len(i)
    Dlengths[i] = x
    div += 1

num = sum(Dlengths.values())
avg = num/div

vals = Dlengths.values()
maxVal, minVal = max(vals), min(vals)
maxVals, minVals = [], []

for i,j in zip(Dlengths.keys(), Dlengths.values()):
  if j == maxVal:
    maxVals.append(i)
  if j == minVal:
    minVals.append(i)
  

out = (avg, maxVals, minVals)
print(out)
