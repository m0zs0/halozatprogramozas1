# # #kérjűnk be 0 végjelű számokat és irjuk ki a összeguket
# # ossz=0
# # while True:
# #     beszam=int(input("kérek egy számot: "))
# #     if beszam!=0:
# #         ossz=ossz+beszam
# #     else:
# #         break

# # print (f"a bekért számok összege: {ossz}") 
# enter végjelig kerjunk be szamokat es kerjunk be vegjelig
# ossz=0
# while True:
#     bestring=input("kérek egy számot: ")
#     if bestring!="":
#         ossz=ossz+int(bestring)
#     else:
#         break

# print (f"a bekért számok összege: {ossz}") 

#kerjel be egy szamot es 0 tol eddig a paros szamokat irasd ki
hatar = int(input("kerem a hatar szamot: "))
szam1=0
while szam1!=hatar+1:
    if szam1 % 2==0:
        print (szam1)
    szam1+=1
