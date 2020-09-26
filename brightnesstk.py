import sys
import subprocess
from Tkinter import Tk, Frame, Button, LEFT

BINS = 20
BIN_WIDTH = 1
close_after = 1500 
change = ""
monitor = ""

def get_monitor():
    global monitor
    comm ='''xrandr --prop | grep " connected"'''
    result = subprocess.check_output(comm, shell=True)    
#    print("get_monitor> ")
#    print(result)
    monitor_name = result.strip().split('connected')[0].strip()
    monitor = monitor_name
    print("detected monitor: "+monitor_name)
    return monitor_name

def change_brightness():
    t = change.strip()
    try:
        ch = float(t)
    except:
        return -1
    curr_b = get_curr_brightness()
    if curr_b == -1:
        return -1
    new_b = ch + curr_b
    comm = '''xrandr --output %s --brightness %f''' % (monitor,new_b)
    result = subprocess.check_output(comm, shell=True)    
#    print("result: ")    
#    print(result)    
    print("New brightness: "+str(new_b))
    return new_b

def get_new_brightness(scale=20):
    new_b = change_brightness()
    if new_b == -1:
        return -1
    else:
        return int(new_b * scale)

def get_curr_brightness():
    comm = '''xrandr --prop --verbose | grep -A10 " connected" | grep "Brightness" '''
    result = subprocess.check_output(comm, shell=True)
    #print("result: ")
    #print(result)
    b_num = result.split(':')[1].strip()
    try:
        b_num_f = float(b_num) 
        print("current brightness: "+str(b_num_f))
        return b_num_f
    except:
        print("Error detecting the current brightness")
        return -1

#
#
#def get_brightness(scale=20):
#    comm = '''xrandr --prop --verbose | grep -A10 " connected" | grep "Brightness" '''
#    result = subprocess.check_output(comm, shell=True)
#    print("result: ")
#    print(result)
#    b_num = result.split(':')[1].strip()
#    a = float(b_num) * scale
#    try:
#        return int(round(a))
#    except:
#        return -1    
#

def main():
    root = Tk()
    frame = Frame(root)
    frame.pack()
    br = get_new_brightness(scale=BINS) # how many boxes/bins
    if br==-1:
        br=0
    active_bins = min(br, BINS)
    for i in range(active_bins):
        b = Button(frame, bg="blue", width=BIN_WIDTH)
        b.pack(side=LEFT)
    for i in range(BINS-br):
        b = Button(frame, bg="grey", width=BIN_WIDTH)
        b.pack(side=LEFT)
    for i in range(br-BINS):
        b = Button(frame, bg="red", width=BIN_WIDTH)
        b.pack(side=LEFT)
    root.after(close_after, lambda: root.destroy())
    root.mainloop()

if __name__ == '__main__':
    if len(sys.argv)==3:
        monitor = sys.argv[2]
        change = sys.argv[1]
        print(change)
        main()
    elif len(sys.argv)==2:
        get_monitor()
        change = sys.argv[1]
        main()       
        print("""The application tried to detect the monitor. Pass it as a second argument if it was wrongly detected""") 
    else:
        get_monitor()
        change="0"
        main()
        print("""The application tries to detect the monitor but without any change in the brightness regardless of the button you click expects the args <monitor name> and <+/-percentags>. e.g., python brightnesstk.py LVDS-0 0.2""")



