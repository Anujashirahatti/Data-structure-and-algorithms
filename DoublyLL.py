
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
    head=None
    tail=None
one=Node(10)
two=Node(20)
three=Node(30)
four=Node(40)

head=one
tail=four

one.next=two
two.prev=one

two.next=three
three.prev=two

three.next=four
four.prev=three
four.next=None
# print(head.next.next.data)
# print(head.next.next.next.data)
# print(head.next.next.next.next.data)

temp=head
while temp!=None:
    print(temp.data)
    temp=temp.next
    
temp=tail
while temp!=None:
    print(temp.data)
    temp=temp.prev
    
