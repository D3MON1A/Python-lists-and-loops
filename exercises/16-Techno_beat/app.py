def lyrics_generator(List):
    dj=""
    count=0
    for each in List:
        if each==0:
            dj=dj+"Boom "
        else:
            dj=dj + "Drop the base "
            if each==1:
                count+=1
            if count==3:
                dj+="!!!Break the base!!! "
    return dj
# Your code go above, nothing to change after this line:
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))