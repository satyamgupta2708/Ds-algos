#Creation of linked lists:

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None 

class linked_list:
    def __init__(self):
        self.headval = None

    
# addition of new node at the begining of the linked list 

    def atbegining(self, newdata):
        NewNode = Node(newdata)

        NewNode.nextval = self.headval
        self.headval = NewNode

# addition of the new node at the end of the linked list : 
    def at_end (self, newdata):
        NewNode = Node(newdata)
        
        lastnode  = self.headval
        

        if lastnode is not None :
            while(lastnode.nextval):
                lastnode = lastnode.nextval
            lastnode.nextval = NewNode
        else:
            self.headval = NewNode
 # printing the list : 
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval




list = linked_list()
list.headval = Node('mon')

e2 = Node('tue')
e3 = Node('wed')

list.headval.nextval = e2
e2.nextval = e3

# list.listprint()

list.atbegining('sun')

list.at_end('thru')

list.listprint()