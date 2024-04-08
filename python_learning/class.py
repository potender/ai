# class Cat():
#
#     def __init__(self,name):
#         self.name = name
#
#     def jump(self):
#         print(self.name + " is jumping")
#
#
# my_cat = Cat("haha")
# print(my_cat.name)
# my_cat.jump()


import my_numpy as np
class Car():
    """模拟汽车"""
    def __init__(self, brand, model, year):
        """初始化汽车属性"""
        self.brand = brand      #汽车的品牌
        self.model = model      #汽车的型号
        self.year = year        #汽车的出厂年份
        self.mileage = 0        #汽车总里程初始化为零

    def print_main_information(self):
        """打印主要信息"""
        print("品牌：{}    型号：{}   出场年份：{}".format(self.brand, self.model, self.year))

    def print_mileage(self):
        """打印总里程"""
        print("行车总里程：{}公里".format(self.mileage))

    def set_mileage(self,distance):
        """设置总里程数"""
        if distance > 0:
            self.mileage = distance
        else:
            print("里程数不能为负")

    def increase_mileage(self, distance):
        """增加里程数"""
        if distance > 0:
            self.mileage += distance
        else:
            print("里程数不能为负")


# class Battery():
#     """模拟电池"""
#     def __init__(self, battery_size = 70):
#







class ElectricCar(Car):
    """电动车类"""

    def __init__(self, brand, model, year, battery_size):
        """初始化电动车的属性"""
        super().__init__(brand, model, year)            #继承父类的属性
        self.battery_size = battery_size                #电池容量
        self.electric_rest = battery_size               #电池剩余电量
        self.electric_distance_rate = 5                 #电量距离转化比
        self.distance_range = self.electric_rest * self.electric_distance_rate    #可行驶距离

    def print_main_information(self):
        print("品牌：{}    型号：{}       出场年份：{}     续航里程：{}公里".format(self.brand, self.model, self.year, self.distance_range))

    def print_rest_electric(self):
        """输出剩余电量"""
        print("当前剩余电量为：{}".format(self.electric_rest))

    def set_rest_electric(self, electric):
        """设置剩余电量,重新计算可行驶里程"""
        if electric >= 0:
            self.electric_rest = electric
            self.distance_range = self.electric_rest * self.electric_distance_rate
        else:
            print("电量不能为负")

    def print_remainder_range(self):
        """输出剩余可行使的里程"""
        print("当前电量还可以继续驾驶{}公里".format(self.distance_range))



my_electric_car = ElectricCar("NextWeek", "FF91", 2046, 5000)
my_electric_car.print_main_information()





# my_new_car = Car("Audi","A6",2016)
# print(my_new_car.brand)
# my_new_car.print_main_information()

#修改属性
# my_new_car.mileage = 1200
# print(my_new_car.mileage)
# my_new_car.set_mileage(8000)
# print(my_new_car.print_mileage())

# my_new_car.print_mileage()
# my_new_car.set_mileage(5000)
# my_new_car.print_mileage()
# my_new_car.increase_mileage(1000)
# my_new_car.print_mileage()
#
