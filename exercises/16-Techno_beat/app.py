
def lyrics_generator(ones_and_zeros_list):
  the_song = ""
  for x in range(len(the_song)):
    if the_song[x] == 0:
      x += 'Boom '
    elif the_song[x] == 1:
      x += 'Drop the base '
      if the_song[x-1] == 1 and the_song[x-2] == 1:
        x += '!!!Break the base!!! '
  return x
# Your code go above, nothing to change after this line:
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))