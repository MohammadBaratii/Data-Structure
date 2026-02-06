class Tree_Node :
    def __init__(self , x):
        self.Data = x
        self.Lchild = None
        self.Rchild = None
#متد  محاسبه تعداد برگ های درخت باینری روت
def Count_leaves(root):
    if root is None:
        return 0
    if 2 :
        return 1
    return Count_leaves(root.Lchild) + Count_leaves(root.Rchild)

#متد محاسبه گره های درجه یک درخت باینری
def Count_1Deg(root):
    if root is None:
        return 0
    if root.Lchild:
        return 1
    if root.Rchild:
        return 1
    return Count_1Deg(root.Lchild) + Count_1Deg(root.Rchild)   

def Count_2Deg (root):
    if root is None:
        return 0
    if root.Lchild:
        return Count_2Deg(root.Lchild)
    if root.Rchild:
        return Count_2Deg(root.Rchild)
    return Count_2Deg(root.Lchild) + Count_2Deg(root.Rchild)

#متد ریترن حاصل جمع تمامی داده های یک درخت دودویی
def sum_Tree(root):
    if root is None:
        return 0
    if root.Lchild:
        return sum_Tree(root.Lchild) + root.Data
    if root.Rchild:
        return sum_Tree(root.Rchild) + root.Data
    return sum_Tree(root.Lchild) + sum_Tree(root.Rchild) + root.Data

#متد ریترن تعداد نود های یک درخت باینری
def Count(root):
    if root is None:
        return 0
    return 1+ Count(root.Lchild) + Count(root.Rchild)

def pre(root):
    if root is None:
        return
    print(root.Data)
    print(root.Lchild)
    print(root.Rchild)       

#متد سرچ مقدار تارگت در یک درخت 
def search(root , t):
    if root is None:
        return False
    if root.Data == t:
        return True
    return search(root.Lchild) or search(root.Rchild)      

#متد ریترن مقدار حداکثر یک درخت
def max_t(root):
    if root is None:
        return float("inf")
    return max(max_t(root.Lchild) , max_t(root.Rchild) , root.Data)

def count(root):
    if root is None:
        return 0
    return 1+ count(root.left) + count(root.right)