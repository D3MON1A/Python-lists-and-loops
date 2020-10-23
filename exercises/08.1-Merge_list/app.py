chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    #Your code go here:
    newlist =[]
    for x in (list1):
          newlist.append(x)
    for y in (list2):
          newlist.append(y)
    return newlist
   
        
    
print(merge_list(chunk_one, chunk_two))
