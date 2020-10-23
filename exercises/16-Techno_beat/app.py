
def lyrics_generator(my_list):
  string = ""
  for x in range(len(my_list)):
    if my_list[x] == 0:
      string += "Boom "
    if my_list[x] == 1:
      string += "Drop the base "
      if my_list[x-1] == 1 and my_list[x-2] == 1 :
        string += "!!!Break the base!!!" 
  return string
# Your code go above, nothing to change after this line:
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))