from machine import I2C


print("I2C Scan")

i2c = I2C(I2C.I2C0, freq=100000, scl=30, sda=31)
devices = i2c.scan()
print(devices)

print("Done")

#for device in devices:
    #i2c.writeto(device, b'123')
    #i2c.readfrom(device, 3)

