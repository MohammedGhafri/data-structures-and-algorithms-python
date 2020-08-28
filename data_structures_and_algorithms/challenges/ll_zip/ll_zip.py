from data_structures_and_algorithms.challenges.linked_list.linked_list import Node,LinkedList





def merge_list(list1,list2):
    if not list1:
        return list2
    elif not list2:
        return list1
    merged_list=LinkedList()

    current1=list1
    current1=current1.head
    # print(current1)
    current2=list2.head
    # print(current1.data)
    # print(current2.data)
    while current1 or current2:
        if current1:
            merged_list.append_data(current1.data)
            current1=current1.next
        if current2:
            merged_list.append_data(current2.data)
            current2=current2.next
    return merged_list







if __name__=='__main__':
    list1=LinkedList()
    list2=LinkedList()
    list1.append_data("1")
    list1.append_data("3")
    list1.append_data("5")
    list1.append_data("7")
    list2.append_data("2")
    list2.append_data("4")
    list2.append_data("6")
    list2.append_data("8")
    list2.append_data("9")
    list2.append_data("10")

    a=merge_list(list1,list2)
    print(a)
    # print(a)
    # print(a)
    # print(list1)


    # bird=LinkedList()
    # a=bird.append_data("Eagle")
    # # bird.append_data("Eagle")
    # bird.append_data("Dov")
    # bird.append_data("Hawk")
    # bird.append_data("Haaaaawk")
    # bird.insertBefore("Haaaaawk","before")
    # bird.insertAfter("gty",'newOne')
    # print(f""" "{bird}" """)
    # print(bird.count)
    # print(bird[5])
    # # bird.includes("awk")
    # bird.insert_btw("Hawk","Woody_Packer") # this for handle the error