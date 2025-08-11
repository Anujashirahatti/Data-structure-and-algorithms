
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLL:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def insertAtBegin(self,newdata):
        if self.head==None:
            newNode=Node(newdata)
            self.head=newNode
        else:
            newNode=Node(newdata)
            newNode.next=self.head
            self.head=newNode
    def display(self):
        if self.head==None:
            print("Empty list")
        else:
            temp=self.head
            while temp!=None:
                print(temp.data,end="->")
                temp=temp.next
                
    def insertAtEnd(self,newdata):
        if self.head==None:
            newNode=Node(newdata)
            self.tail=newNode
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            newNode=Node(newdata)
            temp.next=newNode
            
    def counting(self):
        count=0
        if self.head==None:
            print(count)
        else:
            temp=self.head
            while temp!=None:
                count+=1
                temp=temp.next
            print(count)
            
    def deleteAtBegin(self):
        if self.head==None:
            return
        else:
            temp=self.head
            self.head=temp.next
            temp.next=None
            
    def deleteAtEnd(self):
        if self.head==None:
            return
        else:
            temp=self.head
            while temp.next.next!=None:
                temp=temp.next
            temp.next=None
            
    def searchNode(self,target):
        if self.head==None:
            print("Empty")
        else:
            temp=self.head
            found=False
            while temp!=None:
                if temp.data==target:
                    found=True
                    break
                else:
                    temp=temp.next
            if found!=False:
                print("Element Found")
            else:
                print("Element is not Found")
                
            
obj=SLL()
obj.insertAtBegin(100)
obj.insertAtBegin(200)
obj.insertAtBegin(300)
obj.insertAtBegin(400)
obj.insertAtBegin(500)

obj.insertAtEnd("pallu")
obj.insertAtEnd("Raju")
obj.insertAtEnd("Teju")

obj.searchNode("pallu")
obj.counting()

obj.deleteAtBegin()
obj.deleteAtBegin()
obj.deleteAtEnd()
obj.display()











            
            
            
