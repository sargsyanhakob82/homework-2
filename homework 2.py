#CLASS_2_1 Home
 class Python:
     def __init__(self,name):
         self.name = name
         self.dict_1 = dict_1
     def foo(self):
         dict_1 = {}
         x = 0
         for i in self.name:
             dict_1[self.name[x]] = 1
             x += 1
         print(dict_1)
     def remover(self):
         empty = {}
         for f, k in self.dict_1.items():
             if k not in empty.values():
                 empty[f] = k
         print(empty)

     def check(self)
         for o in self.dict_1:
             new_dict = {}
             if dict_1.values(0)>dict_1.values(1)

 dict_1 = {"One": 1, "Two": 1, "Tree": 2, "For": 2}
 text = Python("python")
 text.foo()

 text.remover()





# CLASS_2_2 Home
 class Cicle:

     def __init__(self,r):
         self.r = r

     def area_maker(self):
         area = self.r*self.r*3.14
         print(f"S ={area}")

     def perimetr_maker(self):
         perimetr = 2*self.r*3.14
         print(perimetr)

 area_1 = Cicle(5)
 area_1.area_maker()
 area_1.perimetr_maker()


class Human:
    def __init__(self, name , surname, age, weight, height):
        self.name = name
        self.surname = surname
        self.age = age
        self.height = height
        self.weight = weight
    def check_1(self):
        print("You will be 100 before" , 100-self.age+2022 , "ages ")

    def check_2(self):
        print("Your optimal weght is ",50 + (0.91 * self.height-152.4))

    def check_3(self):
        print(f"Greetings to you {self.surname} {self.name}")

human_1 = Human("John", "Smith" , 17, 60, 172)
human_1.check_1()
human_1.check_2()
human_1.check_3()