    def insert(self,head,data): 
    #Complete this method
        temporary=Node(data)
        if head is None:
            head=temporary
            return head
        current=head
        while current.next is not None:
            current=current.next
        current.next=temporary
        return head
