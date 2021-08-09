import matplotlib.pyplot as plt
from nptdms import TdmsFile
print('Enter the file name, along with the extension, e.g.: "my_file.tdms"')
while True:
    try:
        filename=input('FILE NAME: ')
        tdms_file=TdmsFile.read(filename)
        break
    except FileNotFoundError:
        print('File not found')
group=tdms_file['Group']
RPchannels=len(group.channels())
xvals1=[]
xvals2=[]
yvals1=[]
yvals2=[]
if RPchannels==1:
    temp_yvals=[]
    temp_xvals=[]
    channel=group.channels()[0]
    for term in range(len(channel)):
        temp_yvals.append(channel[term])
        temp_xvals.append(term)
    if str(group.channels()[0])[33:36]=='ch1':
        yvals1=temp_yvals
        xvals1=temp_xvals
        label1='ch1'
        channel_name='ch1'
        label2=None
        MAX=max(yvals1)
        MIN=min(yvals1)
    elif str(group.channels()[0])[33:36]=='ch2':
        yvals2=temp_yvals
        xvals2=temp_xvals
        label2='ch2'
        channel_name='ch2'
        label1=None
        MAX=max(yvals2)
        MIN=min(yvals2)
    plt.plot(xvals1,yvals1, color='blue', label=label1)
    plt.plot(xvals2,yvals2, color='red', label=label2)
    plt.title(filename)
    plt.xlabel('Sample Number')
    plt.ylabel('Voltage (V)')
    plt.legend()
    print()
    print('BASE PROPERTIES')
    print('==========================================')
    print('Name:', channel_name)
    print('Maximum:', MAX)
    print('Minimum:', MIN)
    print('==========================================')
elif RPchannels==2:
    channel1=group.channels()[0]
    channel2=group.channels()[1]
    for term in range(len(channel1)):
        yvals1.append(channel1[term])
        yvals2.append(channel2[term])
        xvals1.append(term)
        xvals2.append(term)
    print()
    print('Graphs displayed together? (Y/N)')
    while True:
        ans=input('ENTER (Y/N):')
        if ans=='Y' or ans=='N':
            break
    if ans=='Y':
        plt.plot(xvals1,yvals1, color='blue', label='ch1')
        plt.plot(xvals2,yvals2, color='red', label='ch2')
        plt.title(filename)
        plt.xlabel('Sample Number')
        plt.ylabel('Voltage (V)')
        plt.legend()
    elif ans=='N':
        fig1=plt.figure()
        fig2=plt.figure()
        ax1=fig1.add_subplot()
        ax1.plot(xvals1,yvals1, color='blue', label='ch1')
        ax2=fig2.add_subplot()
        ax2.plot(xvals2,yvals2, color='red', label='ch2')
        ax1.set_title(filename)
        ax1.set_xlabel('Sample Number')
        ax1.set_ylabel('Voltage (V)')
        ax2.set_title(filename)
        ax2.set_xlabel('Sample Number')
        ax2.set_ylabel('Voltage (V)')
        ax1.legend()
        ax2.legend()
    print()
    print('BASE PROPERTIES')
    print('==========================================')
    print('Name: ch1')
    print('Maximum:', max(yvals1))
    print('Minimum:', min(yvals1))
    print('==========================================')
    print('Name: ch2')
    print('Maximum:', max(yvals2))
    print('Minimum:', min(yvals2))
    print('==========================================')
print()
print('PROGRAM FINISHED')