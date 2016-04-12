import sys, serial, time, re
import winsound

ser = serial.Serial('COM6', 9600, timeout=2)
#ser.close()

b1 = "beep-01c.wav"
b2 = "beep-02c.wav"
b3 = "beep-04c.wav"
b4 = "beep-06.wav"
b5 = "beep-01&2.wav"
b6 = "beep-01&3.wav"
b7 = "beep-01&4.wav"
b8 = "beep-02&3.wav"
b9 = "beep-02&4.wav"
b10 = "beep-03&4.wav"


def read_arduino():
    time.sleep(.1)
    data = ser.readline().decode("utf-8")
    if data is None:
        return 0
    else:
        return data
    

def parse_s1(data):
    if "sensor1" in data:
        d = re.findall('\d+', data)
        try:
            sensor1 = d[1]
            return sensor1
        except:
            print("err " + sensor1)

def parse_s2(data):
    if "sensor2" in data:
        d = re.findall('\d+', data)
        try:
            sensor2 = d[3]
            return sensor2
        except:
            print("error " + sensor2)
            
def parse_s3(data):
    if "sensor3" in data:
        d = re.findall('\d+', data)
        try:
            sensor3 = d[5]
            return sensor3
        except:
            print("error " + sensor3)

def parse_s4(data):
    if "sensor4" in data:
        d = re.findall('\d+', data)
        try:
            sensor4 = d[7]
            return sensor4
        except:
            print("error " + sensor4)
    
def seq(s1, s2, s3, s4):
    if s1 is not None and s2 is not None:
        if int(s1) > 600 and int(s2) > 700:
            winsound.PlaySound(b5, winsound.SND_FILENAME)
            print(5)
            return 5
        elif int(s1) > 600 and int(s3) > 800:
            winsound.PlaySound(b6, winsound.SND_FILENAME)
            print(6)
            return 6
        elif int(s1) > 600 and int(s4) > 700:
            winsound.PlaySound(b7, winsound.SND_FILENAME)
            print(7)
            return 7
        elif int(s2) > 700 and int(s3) > 800:
            winsound.PlaySound(b8, winsound.SND_FILENAME)
            print(8)
            return 8
        elif int(s2) > 700 and int(s4) > 700:
            winsound.PlaySound(b9, winsound.SND_FILENAME)
            print(9)
            return 9
        elif int(s3) > 800 and int(s4) > 700:
            winsound.PlaySound(b10, winsound.SND_FILENAME)
            print(10)
            return 10
        elif int(s1) > 550:
            winsound.PlaySound(b1, winsound.SND_FILENAME)
            print(1)
            return 1
        elif int(s2) > 700:
            winsound.PlaySound(b2, winsound.SND_FILENAME)
            print(2)
            return 2
        elif int(s3) > 800:
            winsound.PlaySound(b3, winsound.SND_FILENAME)
            print(3)
            return 3
        elif int(s4) > 700:
            winsound.PlaySound(b4, winsound.SND_FILENAME)
            print(4)
            return 4

    
def sensor_input():
    sensor = None
    while sensor is None:
        data = read_arduino()
        s1 = parse_s1(data)
        s2 = parse_s2(data)
        s3 = parse_s3(data)
        s4 = parse_s4(data)
        sequence = seq(s1, s2, s3, s4)
        if sequence is not None:
            sensor = sequence
            return sensor

def arduino_write(d):
    if d is 10:
        ser.write(bytes('d', 'UTF-8'))
    else:
        ser.write(bytes(str(d), 'UTF-8'))
        
#while True:
    #sensor_input()
#main()
