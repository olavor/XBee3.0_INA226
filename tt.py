import ina as ina226
import time,micropython,xbee
from machine import Pin
Pin("P1", Pin.OUT, value=0);Pin("D1", Pin.OUT, value=0);
from machine import I2C
i2c = I2C(1)
ina = ina226.INA226(i2c, 64, Rs = 0.5, voltfactor = 1 )
ina.set_calibration_custom( calValue=10250)
ina.set_current_lsb  (0.001)
i=0
while True:
    v, i, p = ina.get_VIP()
    I1 = 10000*i
    I = int(I1)
    print('normal')
    print( V, '\t', I)
# Get voltage, current and power using Calibration, Current and Power registers,
# as TI wants us to do. Is probably faster, but calibration register must be set:
    v, i, p = ina.get_VIP_TI()
    V1 = 100*v
    V =  V1
    I1 = 10*i
    I = '%2.3f' % I1
    P = '%2.3f' % p
    print('TI')
    print(V, '\t', I)
    print()
    time.sleep(1)




buf = bytearray(2);
buf[0] = 68; buf[1] = 71;
buf2 = bytearray(2)
i2c.writeto_mem(64, 0, buf,addrsize=16)
i2c.readfrom_mem_into(64,1,buf2)
s = buf2[0] << 8 | buf2[1]
s2 = s * 0.01; s1 =int(s2);
ccr = bytearray(2)
i2c.readfrom_mem_into(64,4,ccr)
time.sleep_ms(600)
corrente = ccr[0] << 8 | ccr[1]
curren = corrente*1000; curr = int(curren);
