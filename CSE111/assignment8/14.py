class A:
  temp = 7
  def __init__(self):
    self.sum, self.y = 0, 0
    self.y = A.temp - 1
    self.sum = A.temp + 2
    A.temp -= 3
  def methodA(self, m, n):
    x = 4
    n[0] += 1
    self.y = self.y + m + A.temp
    A.temp += 2
    x = x + 3 + n[0]
    n[0] = self.sum + 2
    print(f"{x} {self.y} {self.sum}")
  def get_A_sum(self):
    return self.sum
  def update_A_y(self, val):
    self.y = val
class B(A):
  x = 2
  def __init__(self, b = None):
    super().__init__()
    self.sum = 2
    if b == None:  
      self.y = self.temp + 1    
      B.x = 4 + A.temp + self.x
      A.temp -= 2
    else:
      self.sum = self.sum + self.get_A_sum()
      B.x = b.x + self.x
  def methodB(self, m, n):
    y = [0]
    self.update_A_y(y[0] + self.y + m)
    B.x = self.y + 4 +  self.temp - n
    
    self.methodA(self.x, y)
    self.sum = self.x + y[0] + self.get_A_sum()
    print(f"{self.x} {y[0]} {self.sum}")
x = [32]
a1 = A()
b1 = B()
b2 = B(b1)
a1.methodA(2, x)
print(a1.y)
b2.methodB(2, 3)
a1.methodA(3, x)
