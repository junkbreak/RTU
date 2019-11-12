crc = 0

########################################make CRC code
def calc_crc(date, c):
    crc = 0xFFFF
    for pos in date:
        crc ^= pos
        for i in range(8):
             if ((crc &1) != 0):
                  crc >>= 1
                  crc ^= 0xA001
             else:
                  crc >>= 1
    crc1 = "%04X"%(crc)
    crc = c+crc1[-2]+crc1[-1]+crc1[-4]+crc1[-3]
    return crc

#########################################output only crc 
def calc_test(date):
    crc = 0xFFFF
    for pos in date:
        crc ^= pos
        for i in range(8):
             if ((crc &1) != 0):
                  crc >>= 1
                  crc ^= 0xA001
             else:
                  crc >>= 1
    crc1 = "%04X"%(crc)
    crc = crc1[-2]+crc1[-1]+crc1[-4]+crc1[-3]
    return crc

########################################make HEX code
def leng_th(crc1) :
    result = len(crc1)
    temp = ""
     
    for i in range(result) :
      temp += format(crc1[i], '02x')+" "
     
    return temp