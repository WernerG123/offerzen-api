class Sorter:    

    def flattenArray(array):
        flat_list = []

        for element in array:
            if type(element) is list:
                for item in element:
                    flat_list.append(item)
            else:
                flat_list.append(element)   
        
        temp_list = []
        print(flat_list)
        for element in flat_list:

            if str(element).isdigit():
                temp_list.append(int(element))

        if Sorter.recursFlatList(temp_list) == 1:
            self.flattenArray(temp_list)
        else:
            return temp_list
        
    def recursFlatList(flat_list):
        listCount = 0
        for element in flat_list:
            if type(element) is list:
                listCount += 1
        if listCount == 0:
            return 0
        else:
            return 1

    def sort(nlist):
        nlist=list(nlist)
        if len(nlist) > 9999:
            raise ValueError("Length of list is too long!")
        else:
            nlist = Sorter.flattenArray(nlist)

            for passnum in range(len(nlist)-1,0,-1):
                for i in range(passnum):
                    if nlist[i]>nlist[i+1]:
                        temp = nlist[i]
                        nlist[i] = nlist[i+1]
                        nlist[i+1] = temp
            print(nlist)
            return nlist

