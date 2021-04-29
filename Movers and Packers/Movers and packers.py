"""
File: moving.py
Author: Dhruv Rajpurohit
Language: Python3
Description: The code performs the greedy functions to help in packing the items by using dataclass
"""



from dataclasses import dataclass

@dataclass
class box:
    name : str
    kind : str
    weightcapacity : float

@dataclass
class object:
    name : str
    weight : float

def items_list(file):
    """
    the function makes a sorted list of the objects with respect to their weight
    :param file: the file
    :return: the sorted list of object and box
    """
    file = open(filename)
    line_num = 1
    objects = []
    boxes = []
    for line in file:
        l = line.strip().split (" ")
        if (line_num == 1):
            for i in range(0, len(l)):
                boxes.append(box(str(i) ,"box", int(l[i])))
        else:
            objects.append(object(l[0], l[1]))
            objects.sort(key = lambda x: x.weight, reverse=True)
        line_num += 1
    return boxes, objects

def printfun(str,list1,list2):
    """
    prints the final output
    :param str: algorithm name
    :param list1: final list
    :param list2: left items
    :return:
    """
    boxes, objects = items_list(filename)
    print("Results from ",str)
    list1.sort(key = lambda x : x[0])
    if len(list2) == 0:
        print("All items successfully packed into boxes!")
        for i in list1:
            print("box",i[0]+1 ,"of weight capacity",boxes[i[0]].weightcapacity)
            print(i[1])
    else:
         print("Unable to pack all items!")
         for i in list1:
             print("box", str(i[0]+1) ,"of weight capacity",str(boxes[i[0]]).weightcapacity)
             print(i[1])
         for i in list2:
             print(i)


def greedy1(filename):
    """
    performs the first greedy task
    :param filename: the file
    :return: prints object
    """
    finalprint=[]
    f1 = open(filename)
    boxes, objects = items_list(filename)
    itemLeft = []
    for i in objects:
        max_weight = 0
        max_index = 0
        for index in range(len(boxes)):
            if max_weight < boxes[index].weightcapacity:
                max_weight = boxes[index].weightcapacity
                max_index = index
        if float(i.weight) <= max_weight:
            temp=[]
            boxes[max_index].weightcapacity -= float(i.weight)
            temp.append(max_index)
            temp.append(i)
            finalprint.append(temp)
            #boxes[max_index].kind.append(i)
        else:
            itemLeft.append(i)
    printfun('greedy1',finalprint,itemLeft)
    print("")

def greedy2(filename):
    """
    performs the second greedy task
    :param filename: the file
    :return: prints object
    """
    finalprint=[]
    f1 = open(filename)
    boxes, objects = items_list(filename)
    itemLeft = []
    for i in objects:
        obj_weight = float(i.weight)
        max_weight = 0
        max_index = 0
        #calc max val
        for index in range(len(boxes)):
            if max_weight < boxes[index].weightcapacity:
                max_weight = boxes[index].weightcapacity
                max_index = index
        closest = max_weight
        if(closest>=obj_weight):
            temp=[]
            jnew=0
            for j in boxes:
                if(j.weightcapacity>=obj_weight and j.weightcapacity<closest):
                    closest = j.weightcapacity
                    jnew=j
            boxes[jnew].weightcapacity -= obj_weight
            temp.append(max_index)
            temp.append(i)
            finalprint.append(temp)
        else:
            itemLeft.append(i)
        printfun('greedy2',finalprint,itemLeft)


def greedy3(filename):
    """
    performs the third greedy task
    :param filename: the file
    :return: prints object
    """
    finalprint=[]
    f1 = open(filename)
    boxes, objects = items_list(filename)
    itemLeft = []
    for j in objects:
        flag=False
        for i in boxes:
            if float(j.weight)<=i.weightcapacity:
                i.weightcapacity -= float(j.weight)
                temp=[]
                temp.append(i.name)
                temp.append(j)
                finalprint.append(temp)
                flag=True
                break
            else:
                continue
        if(flag):
            continue
        else:
            itemLeft.append(j)
        printfun('greedy3',finalprint,itemLeft)








filename = input("name of the file to open: ")
items_list(filename)
greedy1(filename)
greedy2(filename)
greedy3(filename)
