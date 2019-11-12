def command(stack, Inverternum):
        if stack == 1 :
          #############################################1001
          com = '0'+Inverternum+'0403e80001'
          type1 = 1
        elif stack == 2 : 
          com = '0'+Inverternum+'0403e90001'
          type1 = 1
        elif stack == 3 : 
          com = '0'+Inverternum+'0403ea0006'
          type1 = 3
        elif stack == 4 : 
          com = '0'+Inverternum+'0403f00006'
          type1 = 3
        elif stack == 5 : 
          com = '0'+Inverternum+'0403f60002'
          type1 = 3
        elif stack == 6 : 
          com = '0'+Inverternum+'0403f80002'
          type1 = 3
        elif stack == 7 : 
          com = '0'+Inverternum+'0403fa0001'
          type1 = 3
        elif stack == 8 : 
          com = '0'+Inverternum+'0403fb0001'
          type1 = 3
        elif stack == 9 : 
          com = '0'+Inverternum+'0403fc0001'
          type1 = 3
        elif stack == 10 : 
          com = '0'+Inverternum+'0403fd0001'
          type1 = 3
          
          #############################################1050
        elif stack == 11 : 
          com = '0'+Inverternum+'0404190001'
          type1 = 1
        elif stack == 12 : 
          com = '0'+Inverternum+'0404200001'
          type1 = 1
        elif stack == 13 : 
          com = '0'+Inverternum+'0404210001'
          type1 = 1
        elif stack == 14 : 
          com = '0'+Inverternum+'0404220001'
          type1 = 1
        elif stack == 15 : 
          com = '0'+Inverternum+'0404230001'
          type1 = 1
          
          #############################################1070
        elif stack == 16 : 
          com = '0'+Inverternum+'04042d0002'
          type1 = 1
        elif stack == 17 : 
          com = '0'+Inverternum+'04042f0002'
          type1 = 1
        elif stack == 18 : 
          com = '0'+Inverternum+'0404310002'
          type1 = 1
        elif stack == 19 : 
          com = '0'+Inverternum+'0404330002'
          type1 = 1
        elif stack == 20 : 
          com = '0'+Inverternum+'0404350002'
          type1 = 1
        elif stack == 21 : 
          com = '0'+Inverternum+'0404370002'
          type1 = 1
          
          #############################################1090
        elif stack == 22 : 
          com = '0'+Inverternum+'0404410002'
          type1 = 2
        elif stack == 23 : 
          com = '0'+Inverternum+'0404430002'
          type1 = 2
        elif stack == 24 : 
          com = '0'+Inverternum+'0404450002'
          type1 = 2
        elif stack == 25 : 
          com = '0'+Inverternum+'0404470002'
          type1 = 2
        elif stack == 26 : 
          com = '0'+Inverternum+'0404490002'
          type1 = 2
        elif stack == 27 : 
          com = '0'+Inverternum+'04044b0002'
          type1 = 2
        elif stack == 28 : 
          com = '0'+Inverternum+'04044d0002'
          type1 = 2
        elif stack == 29 : 
          com = '0'+Inverternum+'04044f0002'
          type1 = 2
        elif stack == 30 : 
          com = '0'+Inverternum+'0404510002'
          type1 = 2
        elif stack == 31 : 
          com = '0'+Inverternum+'0404530002'
          type1 = 2
        elif stack == 32 : 
          com = '0'+Inverternum+'0404550002'
          type1 = 2
        elif stack == 33 : 
          com = '0'+Inverternum+'0404570002'
          type1 = 2
          #############################################1120
        elif stack == 34 : 
          com = '0'+Inverternum+'04045f0002'
          type1 = 2
        elif stack == 35 : 
          com = '0'+Inverternum+'0404610002'
          type1 = 2
          
          #############################################1126
        elif stack == 36 : 
          com = '0'+Inverternum+'0404650002'
          type1 = 2
        elif stack == 37 : 
          com = '0'+Inverternum+'0404670002'
          type1 = 2
          
          #############################################3650
        elif stack == 38 : 
          com = '0'+Inverternum+'040e410001'
          type1 = 3
        elif stack == 39 : 
          com = '0'+Inverternum+'040e420001'
          type1 = 3
        elif stack == 40 : 
          com = '0'+Inverternum+'040e430001'
          type1 = 3
        elif stack == 41 : 
          com = '0'+Inverternum+'040e440001'
          type1 = 3
        elif stack == 42 : 
          com = '0'+Inverternum+'040e450001'
          type1 = 1
        com = com + str(type1)
        return com
########################################command