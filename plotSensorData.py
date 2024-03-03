import serial
import time
from itertools import count
from matplotlib import pyplot as plt
import matplotlib.animation as animation


com = input("Enter the COM port : ")    # Asks the com port from the User.
ser = serial.Serial(com, baudrate = 9600, timeout = 1)  # Serial communication Begins

index = count()
time.sleep(3)       # sleeps for 3 seconds & gives the microcontroller time to start properly.

data = [0]
d_List = [0]      # variable to store the Serial data.
data_List = [0]      # variable to store the Serial data.
new_dataList = [0]

fig = plt.figure()    


def getValues():        # This function stores the Serial data to 'dtatList' after sending 'n' 
    ser.write(b'n')
    arduinoData_string = ser.readline().decode('ascii')
    Reading_list =[0]
    for i in arduinoData_string:
      if( i != ','):
        Reading_list.append(int(i))
      else:
         continue
    print("Reading_list", Reading_list)
    return Reading_list


class AnimationPlot:                                     
    
    a = 0
    b = 0
    c = 0
    d = 0

    def __init__(self, *newList):
        self.d = newList[-1]
        self.c = newList[-2]
        self.b = newList[-3]
        self.a = newList[-4]


    def animate(self):                                      # this function loops over and over inside the FuncAnimation()
        
        x_vals = []
        x_vals.append(next(index))
      
        ax1 = plt.subplot(2,2,1)
        ax2 = plt.subplot(2,2,2)
        ax3 = plt.subplot(2,2,3) 
        ax4 = plt.subplot(2,2,4)

    #   plt.style.use('seaborn')           
    #   ax1.clear()                                         # Clear last data frame
        plt.cla()                                        
        
        # Plot 1: Scatter plot of x vs. y
        fig.add_subplot(2, 2, 1)
        ax1.plot(x_vals, self.a)
        ax1.set_ylim([0, 450])                              # Set Y axis limit of plot
        ax1.set_title("Sensor_1")                           # Set title of figure
        ax1.set_ylabel("cm_Value")                          # Set title of y axis  
        ax1.autoscale(True, True)
        ax1.legend()

        # Plot 2: Line plot of x vs. z
        fig.add_subplot(2, 2, 2)
        ax2.plot(x_vals, self.b)
        ax2.set_ylim([0, 450])                              # Set Y axis limit of plot
        ax2.set_title("Sensor_2")                           # Set title of figure
        ax2.set_ylabel("cm_Value")                          # Set title of y axis  
        ax2.autoscale(True, True)
        ax2.legend()

        # Plot 3: Histogram of y
        fig.add_subplot(2, 2, 3)
        ax3.plot(x_vals, self.c)
        ax3.set_ylim([0, 450])                              # Set Y axis limit of plot
        ax3.set_title("Sensor_3")                           # Set title of figure
        ax3.set_ylabel("cm_Value")                          # Set title of y axis  
        ax3.autoscale(True, True)
        ax3.legend()


        # Plot 4: Bar plot of name vs. z
        fig.add_subplot(2, 2, 4)
        ax4.plot(x_vals, self.d)
        ax4.set_ylim([0, 450])                              # Set Y axis limit of plot
        ax4.set_title("Sensor_4")                           # Set title of figure
        ax4.set_ylabel("cm_Value")                          # Set title of y axis 
        ax4.autoscale(True, True)
        ax4.legend()

        plt.tight_layout()


# initial loop
for i in range(20):                                         # gathers first 50+ data points
  data.append(getValues())

# main loop
while(1):

    data.append(getValues())
    print("data", data)
    for i in data: 
      d_List.append(int(i))
    print("d_list", d_List)

    for i in d_List: 
      data_List.append(int(i))
    print("data_List", data_List)

    new_dataList.append(data_List[-50:])
    for i in new_dataList:
        print("for new_datalist", i)
   
    realTimePlot = AnimationPlot(new_dataList)                          # Object decleared
    
    # Matplotlib Animation Fuction that takes takes care of real time plot.
    # Note that 'fargs' parameter is where we pass in our dataList and Serial object. 
    ani = animation.FuncAnimation(fig, realTimePlot.animate, frames=50, interval=50) 

    plt.show()                                          # Keep Matplotlib plot persistent on screen until it is closed