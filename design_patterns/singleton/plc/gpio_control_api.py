import spidev
import time
import Jetson.GPIO as gpio
import os

#os.chdir("../")
from common_logger.common_util import log

class gpio_control():
    #Created SPI object for Inputs chip ISO1I811TXUMA1
    #Created SPI object fro Output chip ISO1H812G
    #GPIO Mode set
    #CS0 Pin for Input Chip
    #CS1 Pin For Output Chip
    def __init__(self):
        self.spiInput = spidev.SpiDev()       
        self.spiOutput = spidev.SpiDev()      
        gpio.setmode(gpio.BCM)                
        self.inputCS = 8              
        self.outputCS = 23                  
        self.previousWriteByte = 0
        self.initStatus = False
        self.init_spi_gpios()

    def __del__(self):
        log.info("gpio destructor called",{"sub_module_id": "GPIO"})
        lights = 1
        for lights in range(8):
            self.write_pin(lights,False)
        print("Object is deleted!")

    #(0,0):(device,bus) for taking inputs we use /dev/spidev0.0 port
    #(2,1):(device,bus) for setting outputs we use /dev/spidev2.1 port
    #SPI Frequency Set For Input Chip is 5MHz(Maximum Frequency)
    #SPI Frequency Set For Output Chip is 20MHz(Maximum Frequency)
    #Setup Input chip CS Pin as OUTPUT 
    #Setup Output chip CS Pin as OUTPUT
    def init_spi_gpios(self):
        try:
            self.spiInput.open(0,0)                   
            self.spiOutput.open(2,1)                  
            self.spiInput.max_speed_hz = 5000000      
            self.spiOutput.max_speed_hz = 20000000
            gpio.setwarnings(False)
            gpio.setup(self.inputCS,gpio.OUT)         
            gpio.setup(self.outputCS,gpio.OUT)
            self.initStatus = True
        except Exception as e:
            self.initStatus = False
            print("Error Occured In Initialisation:",e)


    #read_pin API required pinNumber, it should be between 1 to
    #This API will Return the Value on that specific Pin Number
    #It should be either 1 or 0
    #If any exception Occurs API will print exception and return
    #False Flag.
    def read_pin(self,pinNumber):
        try:                                
            self.spiInput.open(0,0)                   
            pinNumber = pinNumber-1                                            
            gpio.output(self.inputCS, gpio.LOW)                               
            returnVal = self.spiInput.readbytes(1)                           
            gpio.output(self.inputCS,gpio.HIGH)
            pinNumberStatus = bin(returnVal[0])[2:].zfill(8)[::-1][pinNumber]
            self.spiInput.close()
            print("Pin status:", pinNumberStatus)
            return pinNumberStatus
        except Exception as e:
            self.initStatus = False
            print("Error Occured in Reading Pin:",e)
            return False

    #write_pin API required Pin Number and Flag, Pin Number should be
    #between 1 to 8 and flag should be either True or False.
    #Flag True means 1(ON) signal and False means 0(OFF) signal
    #This API will return True Flag after doing sucessfull execution
    #If Exception occurs it will print the Exception and return False Flag
    def write_pin(self,pinNumber,flag):                                
        try:  
            self.spiOutput.open(2,1)                  
            print("write pin call")                                                          
            startTime = time.time()                                     
            pinNumber = pinNumber-1                                    
            mask = 1<<pinNumber                                         
            if flag == True:
                self.previousWriteByte |= mask
            elif flag == False:
                self.previousWriteByte &= ~mask
            gpio.output(self.outputCS, gpio.LOW)
            print(self.previousWriteByte)
            returnVal = self.spiOutput.xfer([self.previousWriteByte])
            gpio.output(self.outputCS, gpio.HIGH)
            self.spiOutput.close()
            print("returnVal:", returnVal)

            return self.previousWriteByte
        except Exception as e:
            self.initStatus = False
            print("Error Occured in Write Pin:",e)
            return False


#############Demo code########################
if __name__ == '__main__':
    gpioControl = gpio_control()
    val = gpioControl.read_pin(3)
    print("Val:", val)
    time.sleep(2)
    gpioControl.write_pin(1,True)
