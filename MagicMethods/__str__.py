num=12
val = int.__str__(num)
print(val)
print(type(val))

class employee:
  def __init__(self):
    self.name='Swati'
    self.salary=10000
  def __str__(self):
    return 'name='+self.name+', salary=$'+str(self.salary)

e1 = employee()
print(e1)
