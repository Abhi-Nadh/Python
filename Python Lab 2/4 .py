import collections
str1 = input("Enter a string: ")
d = collections.defaultdict(int)
for c in str1:
    d[c] += 1

for c in sorted(d, key=d.get, reverse=True):
  if d[c] > 1:
      print(c,"-",d[c])
      