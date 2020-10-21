theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:
def wikiOrWoko(string):
    if (string == 0):
        print (str ("woko"))
    else:
        print(str ("wiki"))
    

new_list = list(map(wikiOrWoko,theBools))
print (new_list)


