#! /usr/bin/python2.7
import sys
sys.path.append('/home/pi/.local/lib/python2.7/site-packages')
import serial
import RPi.GPIO as GPIO
import time
import os, sys #if start chmode 777 port
import struct, binascii #decode folat 32
# -*- coding: utf-8 -*-
import argparse
import calendar
import datetime
import pymysql
import ciso8601

from crc_SS import calc_crc
from send_SS import send_hex, test_crc
from receive_SS import receive_hex
from phas_SS import phas_data1
from command50 import command

from influxdb import InfluxDBClient
from imp import reload
reload(sys)

serialnum = []
f = open("/home/pi/Read.txt", 'r')
lines = f.readlines()
for line in lines:
    item = line.split(" ")
    Loc = item[item.index("loc")+1]
    Inverterend = int(item[item.index("end")+1])
    Inverternum = item[item.index("start")+1]
    Inverterstart = Inverternum
    serialnum.insert(1,item[item.index("serial1")+1])
    serialnum.insert(2,item[item.index("serial2")+1])
    serialnum.insert(3,item[item.index("serial3")+1])
    serialnum.insert(4,item[item.index("serial4")+1])
    serialnum.insert(5,item[item.index("serial5")+1])
    serialnum.insert(6,item[item.index("serial6")+1])
    serialnum.insert(7,item[item.index("serial7")+1])
    serialnum.insert(8,item[item.index("serial8")+1])
    serialnum.insert(9,item[item.index("serial9")+1])
    serialnum.insert(10,item[item.index("serial10")+1])
    #print(serialnum)
f.close()

########################################set chmod
EXPORT204 = "sudo chmod 777 /dev/ttyUSB0"
#EXPORT204 = "sudo chmod 777 /dev/ttyAMA0"
os.system(EXPORT204)
########################################set chmod

ser = serial.Serial('/dev/ttyUSB0', 19200, timeout=0.1)
#ser = serial.Serial('/dev/ttyAMA0', 19200, timeout=0.1)

COLLECTION_INTERVAL = 10  # seconds

# DB 
influx_host='222.105.216.167'
influx_port=8086
influx_user = 'root'
influx_password = 'root'
influx_dbname = 'ems_db'
influx_dbuser = 'root'
influx_dbuser_password = 'root'

##############################################################set Inverter End
#Inverternum = '1'
#Inverterend = '6'
Error_stack=0
Error=0
pinnum = 18
#Inverter_ = ""
#Inverter_ = float(0.0)
Inverter_size = float(0.0)
Inverter_presence = float(0.0)
Inverter_part = ""
Inverter_serial = ""
Inverter_datew = ""
Inverter_datey = ""
Inverter_type = ""
Inverter_grid = ""
Inverter_trans = ""
Inverter_model = ""
Inverter_global = float(0.0)
Inverter_alarm = float(0.0)
Inverter_dcdc = float(0.0)
Inverter_dcac = float(0.0)
Inverter_derating = float(0.0)
Inverter_daily = float(0.0)
Inverter_total= float(0.0)
Inverter_partial = float(0.0)
Inverter_week = float(0.0)
Inverter_month = float(0.0)
Inverter_year = float(0.0)
Inverter_acv = float(0.0)
Inverter_aca = float(0.0)
Inverter_ackw = float(0.0)
Inverter_absolute = float(0.0)
Inverter_dailypeak = float(0.0)
Inverter_outputfeedback = float(0.0)
Inverter_reactive = float(0.0)
Inverter_powerfact = float(0.0)
Inverter_freq = float(0.0)
Inverter_dcv = float(0.0)
Inverter_dca = float(0.0)
Inverter_dckw = float(0.0)
Inverter_internal = float(0.0)
Inverter_temp = float(0.0)
Inverter_isolate = float(0.0)
Inverter_max = float(0.0)
Inverter_family = ""
Inverter_product = ""
Inverter_major = ""
Inverter_minor = ""
Inverter_version = ""

flag = True
stack = 1
type1 = 0
check = 0

client = InfluxDBClient(influx_host, influx_port, influx_user, influx_password, influx_dbname)

def insert_data():
        
        #print("PROCESS START")
        
        Date_Time = str(datetime.datetime.utcnow())
        #######################################################set Location
        Location = Loc
        
        Inverter_No = Inverternum
        size = Inverter_size
        presence = Inverter_presence
        part = Inverter_part
        serial = Inverter_serial
        datew = Inverter_datew
        datey = Inverter_datey
        type_1 = Inverter_type
        grid = Inverter_grid
        trans = Inverter_trans
        model = Inverter_model
        GlobalState = Inverter_global
        alarm = Inverter_alarm
        dcdc = Inverter_dcdc
        dcac = Inverter_dcac
        derating = Inverter_derating
        DailySum = Inverter_daily
        total = Inverter_total
        partial = Inverter_partial
        WeekSum = Inverter_week
        MonSum = Inverter_month
        year = Inverter_year
        ACV = Inverter_acv
        ACA = Inverter_aca
        ACKW = Inverter_ackw
        absolute = Inverter_absolute
        dailypeak = Inverter_dailypeak
        outputfeed = Inverter_outputfeedback
        reactive = Inverter_reactive
        powerfact = Inverter_powerfact
        freq = Inverter_freq
        DCV = Inverter_dcv
        DCA = Inverter_dca
        DCKW = Inverter_dckw
        internal = Inverter_internal
        Inverter_Temp = Inverter_temp
        isolate = Inverter_isolate
        max_1 = Inverter_max
        family = Inverter_family
        product = Inverter_product
        major = Inverter_major
        minor = Inverter_minor
        version = Inverter_version
        
        #(utc)
        time_value = ciso8601.parse_datetime(Date_Time)
        print(time_value)
        metric_time = calendar.timegm(time_value.timetuple()) * 1000000000


        
        data = [
            {
                ######## tag ########
                "measurement": "EMS_SOLAR",
                "time" : metric_time,  
                "tags": {                    
                    #"
                    "Location":Location,
                    "Inverter_No": Inverter_No,
                    "GlobalState": GlobalState,
                    "serial" : serial,
                    "model" : model
                },
                ######## field ########
                "fields": {
                    #"
                    "Size" : size,
                    "presence" : presence,
                    "part" : part,
                    "datew" : datew,
                    "datey" : datey,
                    "type" : type_1,
                    "grid" : grid,
                    "trans" : trans,
                    "alarm" : alarm,
                    "dcdc" : dcdc,
                    "dcac" : dcac,
                    "derating" : derating,
                    "DailySum": DailySum,
                    "total" : total,
                    "partial" : partial,
                    "WeekSum": WeekSum,
                    "MonSum": MonSum,
                    "year" : year,
                    "ACV" : ACV,
                    "ACA" : ACA,
                    "ACKW" : ACKW,
                    "abolute" : absolute,
                    "dailypeak" : dailypeak,
                    "outputfeed" : outputfeed,
                    "reactive" : reactive,
                    "powerfact" : powerfact,
                    "freq" : freq,
                    "DCKW": DCKW,
                    "DCV": DCV,
                    "DCA": DCA,
                    "internal" : internal,
                    "Inverter_Temp": Inverter_Temp,
                    "isolate" : isolate,
                    "max_1" : max_1,
                    "family" : family,
                    "product" : product,
                    "major" : major,
                    "minor" : minor,
                    "version" : version,
                    "maker": "goback"
                }
            }
        ]

        print("Write points: {0}".format(data))       
        client.write_points(data)
        client.close()
        
def main(host='***.***.***.***', port=8086):       
        insert_data()

def parse_args():
    parser = argparse.ArgumentParser(
        description='example code to play with InfluxDB')
    parser.add_argument('--host', type=str, required=False, default='***.***.***.***',
                        help='hostname of InfluxDB http API')
    parser.add_argument('--port', type=int, required=False, default=8086,
                        help='port of InfluxDB http API')
    return parser.parse_args()
    
phas_data = [[0]*43 for i in range(int(Inverterend)+1)]
save_data = [[0]*43 for i in range(int(Inverterend)+1)]


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pinnum, GPIO.OUT)

if __name__ == '__main__':
	  try : 
	    for i in range(int(Inverterstart), int(Inverterend)+1) :
	         for i in range(42) :
		         c = command(stack, Inverternum)
		         sleep = 2
		         type1 = c[-1]
		         c = c[:-1]
		         
		         
		         while flag :
			         #GPIO.output(pinnum, 1)
			         data = send_hex(c, ser)
			#++++++++++++++++++++++++++++receive+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
			         time.sleep(0.1)
			         #GPIO.output(pinnum, 0)
			         code1 = receive_hex(ser)
			         
			         if len(code1) > 10 :
			         	flag = test_crc(code1)
			         Error_stack += 1
			         if Error_stack >= 10 :
			         	Error_stack = 0
			         	Error += 1
			         	#print("wait "+str(sleep)+" second")
			         	time.sleep(0.1)
			         	if Error > 1 :
			         		Error = 99
			         		break;
			         		
		         flag = True
		         
		         if Error >= 99 :
				#Error = 10
				#stack = 1
				phas_data[int(Inverternum)][stack] = '0'
				if stack > 2 :
				        break;
				        
		         else :
				phas_data[int(Inverternum)][stack] = phas_data1(code1, type1)
		         
		         Error = 0
		         Error_stack = 0
		         
		         #print("stack = "+str(stack))
		         
		         if stack == 42 :
		             stack = 1 
		         else :
		             stack = stack + 1
		             
###################################if break ################################################################
	         Date_Time = str(datetime.datetime.utcnow())
	         save_data[int(Inverternum)-1][0] = ciso8601.parse_datetime(Date_Time)
	         phas_data[int(Inverternum)][0] = ciso8601.parse_datetime(Date_Time)
	         
	         Error = 0
	         stack = 1
###################################break time################################################################
	         time.sleep(5)
	         
	         if int(Inverternum) == int(Inverterend) :
	           Inverternum = Inverterstart
	         else :
	           Inverternum = str(int(Inverternum) + 1)
	    ##################################save file##################################################
	    f = open('data.txt', 'a')
	    f.write(str(phas_data)+'\n')
	    f.close()
	    ##################################save file##################################################
###################################break time################################################################
	    for i in range(int(Inverterstart), int(Inverterend)+1) :
	    	for i in range(42) :
	    	    #print ("data = "+str(phas_data[int(Inverternum)][stack]))
		    if (stack >= 3 and stack <= 10) or stack >= 38 :
			phas_data[int(Inverternum)][stack] = str(phas_data[int(Inverternum)][stack])
			if stack == 3 :
				Inverter_part = phas_data[int(Inverternum)][stack]
			elif stack == 4 :
				Inverter_serial = serialnum[int(Inverternum)-1]
			elif stack == 5 :
				Inverter_datew = phas_data[int(Inverternum)][stack]
			elif stack == 6 :
				Inverter_datey = phas_data[int(Inverternum)][stack]
			elif stack == 7 :
				Inverter_type = phas_data[int(Inverternum)][stack]
			elif stack == 8 :
				Inverter_grid = phas_data[int(Inverternum)][stack]
			elif stack == 9 :
				Inverter_trans = phas_data[int(Inverternum)][stack]
			elif stack == 10 :
				Inverter_model = phas_data[int(Inverternum)][stack]
			elif stack == 38 :
				Inverter_family = phas_data[int(Inverternum)][stack]
			elif stack == 39 :
				Inverter_product = phas_data[int(Inverternum)][stack]
			elif stack == 40 :
				Inverter_major = phas_data[int(Inverternum)][stack]
			elif stack == 41 :
				Inverter_minor = phas_data[int(Inverternum)][stack]
			elif stack == 42 :
				Inverter_version = phas_data[int(Inverternum)][stack]
		    else :
			phas_data[int(Inverternum)][stack] = round(float(phas_data[int(Inverternum)][stack]),2)
			if stack == 1 :
				Inverter_size = phas_data[int(Inverternum)][stack]
			elif stack == 2 :
				Inverter_presence = phas_data[int(Inverternum)][stack]
			elif stack == 11 :
				Inverter_global = phas_data[int(Inverternum)][stack]
			elif stack == 12 :
				Inverter_alarm = phas_data[int(Inverternum)][stack]
			elif stack == 13 :
				Inverter_dcdc = phas_data[int(Inverternum)][stack]
			elif stack == 14 :
				Inverter_dcac = phas_data[int(Inverternum)][stack]
			elif stack == 15 :
				Inverter_derating = phas_data[int(Inverternum)][stack]
			elif stack == 16 :
				Inverter_daily = phas_data[int(Inverternum)][stack]
			elif stack == 17 :
				Inverter_total = phas_data[int(Inverternum)][stack]
			elif stack == 18 :
				Inverter_partial = phas_data[int(Inverternum)][stack]
			elif stack == 19 :
				Inverter_week = phas_data[int(Inverternum)][stack]
			elif stack == 20 :
				Inverter_month = phas_data[int(Inverternum)][stack]
			elif stack == 21 :
				Inverter_year = phas_data[int(Inverternum)][stack]
			elif stack == 22 :
				Inverter_acv = phas_data[int(Inverternum)][stack]
			elif stack == 23 :
				Inverter_aca = phas_data[int(Inverternum)][stack]
			elif stack == 24 :
				Inverter_ackw = phas_data[int(Inverternum)][stack]
			elif stack == 25 :
				Inverter_absolute = phas_data[int(Inverternum)][stack]
			elif stack == 26 :
				Inverter_dailypeak = phas_data[int(Inverternum)][stack]
			elif stack == 27 :
				Inverter_outputfeedback = phas_data[int(Inverternum)][stack]
			elif stack == 28 :
				Inverter_reactive = phas_data[int(Inverternum)][stack]
			elif stack == 29 :
				Inverter_powerfact = phas_data[int(Inverternum)][stack]
			elif stack == 30 :
				Inverter_freq = phas_data[int(Inverternum)][stack]
			elif stack == 31 :
				Inverter_dcv = phas_data[int(Inverternum)][stack]
			elif stack == 32 :
				Inverter_dca = phas_data[int(Inverternum)][stack]
			elif stack == 33 :
				Inverter_dckw = phas_data[int(Inverternum)][stack]
			elif stack == 34 :
				Inverter_internal = phas_data[int(Inverternum)][stack]
			elif stack == 35 :
				Inverter_temp = phas_data[int(Inverternum)][stack]
			elif stack == 36 :
				Inverter_isolate = phas_data[int(Inverternum)][stack]
			elif stack == 37 :
				Inverter_max = phas_data[int(Inverternum)][stack]
		    stack += 1
		    
	    	##################goback
	    	args = parse_args()
	    	main(host=args.host, port=args.port)
	    	##################goback
	    	
	    	stack = 1
	    	Inverternum = str(int(Inverternum) + 1)
	    	time.sleep(5)
	    	
	    stack = 1
	    Inverternum = Inverterstart
	  except StopRTU:
	        pass