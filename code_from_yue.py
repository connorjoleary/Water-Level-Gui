import serial
import csv
import os
from time import gmtime, strftime
from datetime import datetime
from pathlib import Path
from _sqlite3 import Row

counter = [0]*10 
counter_file = Path("counter.txt")
if counter_file.is_file():
    with open('counter.txt') as f:
        lines = f.readlines()
        counter[0] = int(lines[0])
        counter[1] = int(lines[1])
        counter[2] = int(lines[2])
        counter[3] = int(lines[3])
        counter[4] = int(lines[4])
        counter[5] = int(lines[5])
        counter[6] = int(lines[6])
        counter[7] = int(lines[7])
        counter[8] = int(lines[8])
        counter[9] = int(lines[9])
    f.close
else:
    with open('counter.txt','w') as f:
        for item in counter:
            f.write("%s\n" % item)
            f.close
            
def write_to_to_file(tank_number, battery_level,water_level):
    tank_number = str(tank_number)
    file_name = "tank" + tank_number + ".csv"
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    counter_number = int(tank_number)-1
    counter[counter_number] = counter[counter_number]+1
    with open('counter.txt','w') as f:
        for item in counter:
            f.write("%s\n" % item)
            f.close
        
    my_file = Path(file_name)
    
    if my_file.is_file() == False:
        with open(file_name,'w') as csvfile:
            fieldnames = ['time','battery','water','counter']
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames,lineterminator='\n')
            writer.writeheader()
            writer = csv.writer(csvfile,lineterminator='\n')  
            for num in range(0,336):
                writer.writerow(['1/1/1111  0:00:00 AM','0','0','0'])
            csvfile.close
        
    original_data = []   
    with open(file_name,'r') as csvfile:
        original = csv.reader(csvfile)
        original_data.extend(original)   
        csvfile.close 
              
    current_row = counter[counter_number]%336+1
    line_to_override = {current_row:[current_time,battery_level,water_level,counter[counter_number]]}    
             
    with open(file_name,'w') as csvfile:        
        writer = csv.writer(csvfile,lineterminator='\n')
        for line,row in enumerate(original_data):   
            data = line_to_override.get(line,row)
            writer.writerow(data)
        csvfile.close()
    return;
                
#ser = serial.Serial('COM7', baudrate=9600, timeout=2, xonxoff=False, rtscts=False, dsrdtr=False)
#ser.flushInput()
#ser.flushOutput()
n=3500
while n>0:
    n=n-1
    #data_raw = ser.readline()  
    data_raw = b'\xc0\x00\x82\xa0\xa8\xa8h@`\xa8\x82\x9c\x96@@d\xae\x92\x88\x8a@@a\x03\xf0T#074,515,303,294,328,323,00000011\xc0'
    if data_raw != b'':
        print('not blank')
        c = data_raw.decode("utf-8", "ignore")
        if '#' in c:
            print(c.split(","))
            d = c.split(",")
            if len(c.split(",")) == 7:
                print("battery " + d[1])
                print("water" + d[2])
                d[3] = int(d[3])
                if d[3] < 100:
                    print('100')
                    write_to_to_file(1,d[1],d[2])
                elif d[3] < 200 and d[3] >= 100:
                    print('200')
                    write_to_to_file(2,d[1],d[2])
                elif d[3] < 300 and d[3] >= 200:
                    print('300')
                    write_to_to_file(3,d[1],d[2])
                elif d[3] < 400 and d[3] >= 300:
                    print('400')
                    write_to_to_file(4,d[1],d[2])
                elif d[3] < 500 and d[3] >= 400:
                    print('500')
                    write_to_to_file(5,d[1],d[2])
                elif d[3] < 600 and d[3] >= 500:
                    print('600')
                    write_to_to_file(6,d[1],d[2])
                elif d[3] < 700 and d[3] >= 600:
                    print('700')
                    write_to_to_file(7,d[1],d[2])
                elif d[3] < 800 and d[3] >= 700:
                    print('800')
                    write_to_to_file(8,d[1],d[2])
                elif d[3] < 900 and d[3] >= 800:
                    print('900')
                    write_to_to_file(9,d[1],d[2])
                elif d[3] < 1000 and d[3] >= 900:
                    print('1000')
                    write_to_to_file(10,d[1],d[2]) 
        
        
        
        