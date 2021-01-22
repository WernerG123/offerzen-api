def bubbleSort(nlist):
    print(nlist)
    nlist = flattenArray(nlist)
    print(nlist)
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp
    return nlist

def flattenArray(array):
    flat_list = []

    for element in array:
        if type(element) is list:
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)

    int_flat_list = [s for s in flat_list if s.isdigit()]
    return int_flat_list


# nlist = [14,46,43,[27,57],41,45,21,70]
# # nlist = flattenArray(nlist)
# # bubbleSort(nlist)
# print(bubbleSort(nlist))

# # return nlist