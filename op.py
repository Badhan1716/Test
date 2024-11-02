# class student:
#     roll=""
#     gpa=""
# badhan=student()
# badhan.roll=17
# badhan.gpa=3.75
# print(badhan.roll)
# print(badhan.gpa)
# class baba :
#      car="BMW"
#      tk="100 crore"
#      home="10 floor"
# class baba2:
#     smartphone="iphone"
#     ac="walton"
# class baba3:
#     laptop="hp"
#     camera="fifine"
# class baba:
#     car = "BMW"
#     tk = "100 crore"
#     home = "10 floor"
#
#
# class son1(baba):
#     smartphone = "iphone"
#     ac = "walton"
#
#
# class son2(son1):
#     laptop = "hp"
#     camera = "fifine"
#
# class son3(son2):
#     brokenhome=""
# s=son3()
# print(s.laptop)
#python iterators
# list=[1,2,3,4,5,"badhan","dey","badhan dey"]
# # for i in list:
# #     print(i)
# x=iter(list)
# # print(x.__next__())
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
#scope
# a=20
# b=30
# def badhan():
#     x=100
#     print(x)
# badhan()
# print(a)
# a=20
# b=30
# def badhan():
#     global a
#     a=100
# badhan()
# print(a)
# #datetime
# import datetime
# a=datetime.datetime.now()
# print(a.strftime("%m"))
#constructor
# class parentinfo:
#     def badhansfamily(self,name,age):
#         print(f"my name is {name},my age is {age}")
# p1=parentinfo()
# p1.badhansfamily("badhan",24)
# class parentinfo:
#     def __init__(self,name,age):
#         print(f"my name is {name},& my age is {age}")
# p1=parentinfo("badhan",24)
# #methods
# class parentinfo:
#     def __init__(self,name,age):
#         print(f"my name is {name},& my age is {age}")
#     @classmethod
#     def myname(LMS):
#         print("hello world")
# p1=parentinfo("badhan",24)
# parentinfo.myname()












#abstraction
# #polymorphism
# class vehicle:
#     def __init__(self,model,brand,component):
#         self.model=model
#         self.brand=brand
#         self.component=component
# class plane(vehicle):
#     pass
# class car(vehicle):
#     pass
# p1=plane("badhan17","badhan","allcomp")
# c1=car("BMW","wuh","maincomp")
# print(c1.brand,c1.model)
# print(p1.brand)
#encapsulation













