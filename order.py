y={'John':40,'Alex':2,'Benny':32,'Danny':3}
l=list(y.items())
l.sort()
print("Ascending order is:",l)
l=list(y.items())
l.sort(reverse=True)
print("Descending order is:",l)
