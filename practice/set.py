# Set
black = set([1, 2, 2, 5, 3])

print(black)
# Resault {1, 2, 3, 5}

#add
nasser = {"reloj", "recard", "blanco", "negro", "blanco"}

nasser.add("elemento")
print(set(nasser))


#update

nasser.update(["nassou", "big"])
print(nasser)

oufallah = {"nassedine", "white"}
final = nasser.union(oufallah)
print(final)