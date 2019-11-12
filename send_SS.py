from crc_SS import calc_crc, leng_th, calc_test

flag = True

def send_hex(c, ser) :
    data = bytearray.fromhex(c)
    crc = calc_crc(data, c)
    crc1 = bytearray.fromhex(crc)
    ser.write(crc1)
    crc1 = leng_th(crc1)
    #print ("pass : "+crc1)
    return crc
    
def test_crc(code1) :
    code = code1[:-6]
    recrc = code1[-6]+code1[-5]+code1[-3]+code1[-2]
    data = bytearray.fromhex(code)
    crc = calc_test(data)
    crc1 = bytearray.fromhex(crc)
    crc2 = bytearray.fromhex(recrc)

    if crc1 == crc2 :
        flag = False
    elif code1[3] == 8 :
        print("in")
        flag = False
    else : 
        flag = True
    return flag