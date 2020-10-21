people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
def deletePerson(person_name):
    #Your code go here:
    newlist:[]
    for name in people:
        if name != person_name:
            newlist.append(name)
    return newlist
    
print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))