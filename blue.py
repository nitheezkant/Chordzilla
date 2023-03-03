import serial
uart_channel = serial.Serial("/dev/ttyAMA0",baudrate=9600,timeout=2)
data1=""
data2=""
while(1):
	data2=uart_channel.read(25)
	data2=str(data2.decode())
	data1+=data2
	if(data2!=""):
		break
	
	uart_channel.flush()
	data1=""
	data2=""
print(data1)

