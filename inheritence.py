class Animal:
  def __init__(self,name):
    self.name = name 
    self.is_alive = True

  def eat(self):
    print(f"{self.name} is eating")

  def sleep(self):
    print(f"{self.name} is sleeping")


class Dog(Animal):
  def speak(self):
    print('howhow')

class Cat(Animal):
  def speak(self):
    print('mewmew')

class Mouse(Animal):
  def speak(self):
    print("mousemouse")


dog1 = Dog("ric")
cat_1 = Cat("tomm")
mouse_1 = Mouse("jery")

print(dog1.name)
