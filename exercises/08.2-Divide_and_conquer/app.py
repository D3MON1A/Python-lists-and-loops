list_of_numbers = [4,	80,	85,	59,	37,25,	5,	64,	66,	81,20,	64,	41,	22,	76,76,	55,	96,	2,	68]


#Your code here:
def merge_two_list(int):
    odd=[]
    even=[]
    for int in list_of_numbers:
        if int %2==0:
            even.append (int)
        else:
            odd.append (int)
    newlist=[]
    newlist.append(odd)
    newlist.append(even)
    return newlist


print(merge_two_list(list_of_numbers))

