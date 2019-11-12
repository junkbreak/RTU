from crc_SS import calc_crc, leng_th

def receive_hex(ser) :
   val = ser.readline()
   #print(val)
   ###################################format str->hex type
   val = bytearray(b""+val)
   val = leng_th(val)
   #print ("ans : "+val)
   ##################################save file##################################################
   if len(val) > 20 :
	   f = open('code.txt', 'a')
	   f.write(val+'\n')
	   f.close()
   ##################################save file##################################################
    
   return val  #code1