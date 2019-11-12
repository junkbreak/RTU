import struct, binascii #decode folat 32

def phas_data1(code1, type1) :
   a1 = code1
   #d = input("select 1.int 2.float 3.ASCII : ")
   d = type1
   #print("data Range = "+a1[7])
   
   if a1[7] == 'c' :
           a2 = a1[-24]+a1[-23]+a1[-21]+a1[-20]+a1[-18]+a1[-17]+a1[-15]+a1[-14]+a1[-12]+a1[-11]+a1[-9]+a1[-8]
           
   if a1[7] == '4' :
           a2 = a1[-18]+a1[-17]+a1[-15]+a1[-14]+a1[-12]+a1[-11]+a1[-9]+a1[-8]
           
   if a1[7] == '2' :
           a2 = a1[-12]+a1[-11]+a1[-9]+a1[-8]
           
   #print("length = "+a2)
   if d == '1' : ##int
           a2=int(a2,16)
           a2 = str(a2)
           #print("1save : "+a2)
           
   if d == '2' : ##float
           a2 = a2[4]+a2[5]+a2[6]+a2[7]+a2[0]+a2[1]+a2[2]+a2[3]
           a2 = bytearray.fromhex(a2)
           a2 = struct.unpack('>f',a2)
           a2 = str(a2)
           a2 = a2.replace("(","")
           a2 = a2.replace(")","")
           a2 = a2.replace(",","")
           #print("2save : "+a2)
           
   if d == '3' : ##ASCII
           a2 = a2.replace('00',"")
           a2 = bytearray.fromhex(a2)
           #print("3save : "+a2)
   return a2