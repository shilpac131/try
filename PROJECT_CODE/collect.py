import serial
import time
ser = serial.Serial('/dev/ttyUSB1', baudrate=9600, timeout=1)
time.sleep(1)
numPoints = 3
numRowsCollect = 1
dataList = [0]*numPoints


def getValues():
    ser.write(b'g')
    arduinoData = ser.readline().decode().split('\r\n')
    return arduinoData[0]


def seethis():
    while(1):
        for row in range(0, numRowsCollect):
            for i in range(0, numPoints):
                data = getValues()
                time.sleep(2)
                dataInt = int(float(data))
                dataList[i] = dataInt
                time.sleep(0)
        return(dataList)
