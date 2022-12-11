def sign_value(list, value):
    list.append(value)

def delete_el(list, element):
    list.pop(element)

def show_list(list1, list2):
    print("---------------------LISTA---------------------")
    for x in range(len(list1)):
        print((x + 1), list1[x], "\t -", list2[x])

