all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]


def newNames(names):
    return names [0]=="R"
        
resulting_names = list(filter(newNames, all_names))

print(resulting_names)




