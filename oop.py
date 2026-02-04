class Car:
  def __init__(self , model , year , color , for_sale):
    self.model = model
    self.year = year 
    self.color = color 
    self.for_sale = for_sale


  def drive(self):
      print(f"you drive the car {self.model} {self.color}")


  def stop(self):
      print("you stop the car ")




car1 = Car("BMW","2023","black",False)

car2 = Car("alentra","2026","red",True)


#print(car1.model)
#print(car1.year)
#print(car1.color)
#print(car1.for_sale)




#print(car2.model)
##print(car2.year)
#print(car2.color)
#print(car2.for_sale)

car1.drive()
 




