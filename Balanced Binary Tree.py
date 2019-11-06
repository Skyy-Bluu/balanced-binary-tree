class Node:
    def __init__(self, value = None):
        self.left  = None
        self.right = None
        self.value = value


list = [3,9,20,'null','null',15,7]
#root = Node(list[0])
list1 = []
counter = 0
for i in range(0 ,len(list)):
    print("i ",i)
    # if i == 1:
    #     root.left = Node(list[i])
    #     root.right = Node(list[i+1])
    if i == 0:
        list1.insert(i,Node(list[i]))
        print('list1: before ', list1[i].value)
    if list1[i].value != 'null':
        if (i*2)+1 <= len(list)-1 :
            #list1.insert(i+1, Node(list[(i*2)+1]))
            print('number going in the node left', list[(i*2)+1])
            list1.append(Node(list[(i*2)+1]))
            print('[O]number being put on the left', list1[(i*2)+1].value)
            list1[i].left = list1[(i*2)+1]
            print(list1[i].value, 'has this on the left ', list1[(i*2)+1].value)
        if (i*2)+2 <= len(list)-1:
            #list1.insert(i+2, Node(list[(i*2)+2]))
            print('number going in the node right', list[(i * 2) + 2])
            list1.append(Node(list[(i * 2) + 2]))
            print('[O]number being put on the right', list1[(i*2)+2].value)
            list1[i].right = list1[(i*2)+2]
            print(list1[i].value, 'has this on the right', list1[(i*2) + 2].value)
        for i in list1:
            print('list1: after ', i.value)

def BalancedBinaryTree(root:Node):


        if root.left is None or root.right is None:
            return
        else:



# for i in list1:
#     print(i.value)
# print(len(list1))

print('pls ', list1[0].right.left.value)