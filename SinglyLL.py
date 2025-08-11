
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    head=None
one=Node(10)
two=Node(20)
three=Node(30)
four=Node(40)
five=Node("Anu")

head=one
one.next=two
two.next=three
three.next=four
four.next=five
five.next=None
print(head.next.data)
print(head.next.next.data)
print(head.next.next.next.data)
print(head.next.next.next.next.data)

temp=head
while temp!=None:
    print(temp.data)
    temp=temp.next
    
