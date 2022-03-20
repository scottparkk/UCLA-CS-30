def remove(n,l):
    if l == []:
        return []
    else:
        head = l[0]
        tail = l[1:]
        if head == n:
            return remove(n,tail)
        else:
            return [head] + remove(n,tail)

def countDistinct(l):
    if l == []:
        return 0
    else:
        head = l[0]
        tail = l[1:]
        return 1 + countDistinct(remove(head,tail))
    
def isSorted(l):
    if len(l) == 1:
        return True
    else:
        head = l[0]
        head2 = l[1]
        tail = l[1:]
        if head <= head2:
            return isSorted(tail)
        else:
            return False

def insert(n,l):
    if l == []:
        return [n]
    else:
        head = l[0]
        tail = l[1:]
        if n <= head:
            return [n] + [head] + tail
        else:
            return [head] + insert(n,tail)

def merge(l1,l2):
    if l1 == []:
        return l2
    elif l2 == []:
        return l1
    else:
        head1 = l1[0]
        head2 = l2[0]
        tail1 = l1[1:]
        tail2 = l2[1:]
        if head1 <= head2:
            return [head1] + merge(tail1,l2)
        else:
            return [head2] + merge(l1, tail2)
    
