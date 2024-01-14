class Employee:
  def __init__(self):
    print("__init__ magic method is called")
    self.name = 'Satya'
    print(self.name)
  def __new__(cls):
    print("__new__ magic method is called")
    inst = object.__new__(cls)
    return inst

emp = Employee()
