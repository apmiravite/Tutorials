    def removeDuplicates(self,head):
        #Write your code here
        queue=[]
        if head==None:
            return
        p=head
        queue.append(p.data)
        p=p.next
        while p is not None:
            queue.append(p.data)
            p=p.next
        queue=list(dict.fromkeys(queue))
        for i in queue:
            print(i, end=" ")
