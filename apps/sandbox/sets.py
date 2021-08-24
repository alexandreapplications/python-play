# Sets are lists with no duplicate entries. Let's say you want to collect a list of words used in a paragraph:

print(set("my name is Eric and Eric is my name".split()))
a = set(["Jake", "John", "Eric"])
print(a)
b = set(["John", "Jill"])
print(b)
print(a.intersection(b))
print(b.intersection(a))

print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

print(a.union(b))
