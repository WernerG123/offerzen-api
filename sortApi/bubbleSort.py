class Sorter:
    

    def flattenArray(array):
        flat_list = []

        for element in array:
            if type(element) is list:
                for item in element:
                    flat_list.append(item)
            else:
                flat_list.append(element)

        print(flat_list)
        temp_list = []
        for element in flat_list:
            if str(element).isdigit():
                temp_list.append(int(element))
        print("THIS IS THE CONVERTED LIST")
        print(temp_list)
        return temp_list
        
    def sort(nlist):
        print(nlist)
        nlist = Sorter.flattenArray(nlist)
        print(nlist)
        for passnum in range(len(nlist)-1,0,-1):
            for i in range(passnum):
                if nlist[i]>nlist[i+1]:
                    temp = nlist[i]
                    nlist[i] = nlist[i+1]
                    nlist[i+1] = temp
        return nlist

