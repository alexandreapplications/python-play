phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

print('=' * 20)
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

print('=' * 20)
phonebook2 = {
    "John": 938477566,
    "Jack": 938377264,
    "Jill": 947662781
}
print(phonebook2)

print('=' * 20)
del phonebook2["John"]
print(phonebook2)
print("Removing %s" % phonebook2.pop("Jill"))
print(phonebook2)
