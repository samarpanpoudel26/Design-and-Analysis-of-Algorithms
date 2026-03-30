class QuickFind:
  def __init__(self,n):
    self.id=list(range(n))
  def find(self,p):
    return self.id[p]
  def connected(self,p,q):
    return self.find(p)==self.find(q)
  def union(self,p,q):
    pid=self.find(p)
    qid=self.find(q)
    if pid==qid:
      return
    for i in range(len(self.id)):
      if self.id[i]==pid:
        self.id[i]=qid
        
class QuickUnion:
  def __init__(self,n):
    self.parent=list(range(n))
  def find(self,p):
    while p!=self.parent[p]:
      p=self.parent[p]
    return p 
  def connected(self,p,q):
    return self.find(p)==self.find(q)
  def union(self,p,q):
    rootP=self.find(p)
    rootQ=self.find(q)
    self.parent[rootP]=rootQ
    
class WeightedQuickUnion:
  def __init__(self,n):
    self.parent=list(range(n))
    self.size=[1]*n  #storing size
  def find(self,p):
    while p!=self.parent[p]:
      p=self.parent[p]
    return p 
  def connected(self,p,q):
    return self.find(p)==self.find(q)
  def union(self,p,q):
    rootP=self.find(p)
    rootQ=self.find(q)
    if rootP==rootQ:
      return
    if self.size[rootP]<self.size[rootQ]: #attaching small tree with larger one
      self.parent[rootP]=rootQ
      self.size[rootQ]+=self.size[rootP]
    else:
      self.parent[rootQ]=rootP
      self.size[rootP]+=self.size[rootQ]
class WeightedQuickUnionPathCompression:
  def __init__(self,n):
    self.parent=list(range(n))
    self.size=[1]*n  #storing size
  def find(self,p):
    if p!=self.parent[p]:
      self.parent[p]=self.find(self.parent[p])
    return self.parent[p]
  def connected(self,p,q):
    return self.find(p)==self.find(q)
  def union(self,p,q):
    rootP=self.find(p)
    rootQ=self.find(q)
    if rootQ==rootP:
      return
    if self.size[rootP]<self.size[rootQ]: #attaching small tree with larger one
      self.parent[rootP]=rootQ
      self.size[rootQ]+=self.size[rootP]
    else:
      self.parent[rootQ]=rootP
      self.size[rootP]+=self.size[rootQ]
      
if __name__ == "__main__":
    n = 10
    qf = QuickFind(n)
    qu = QuickUnion(n)
    wqu = WeightedQuickUnion(n)
    wqupc = WeightedQuickUnionPathCompression(n)

    # Example usage:
    qf.union(0, 1)
    qf.union(1, 2)
    print(qf.connected(0, 2))  # True

    qu.union(3, 4)
    qu.union(4, 5)
    print(qu.connected(3, 5))  # True

    wqu.union(6, 7)
    wqu.union(7, 8)
    print(wqu.connected(6, 8))  # True

    wqupc.union(9, 0)
    wqupc.union(0, 1)
    print(wqupc.connected(9, 1))  # True
    
    