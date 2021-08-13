import netmiko
import sys
import time
import schedule
import re

Deviceip="10.207.195.178"
username="admin"
password="Cano09101207#"


print('········································································· \n')
print('·······················Welcome to WSAMonitor tool······················ \n')
print('········································································· \n')

Option=int(input('Please select the option from the Menu: \n 1.-Monitor every 5 mins \n 2.-Get all info  \n 3.-Device Version \n 4.-Users conected to the device \n 5.-CPU, Memory usage \n 6.-Licenses installed \n 7.-WCCP Information (Only if this feature is enabled) \n 8.-Exit \n \n Type the number of the option: '))


if Option == 1:
  while(True):
    connection= netmiko.ConnectHandler(ip=Deviceip,device_type="cisco_ios",
                                   username=username,password=password)

    print('\n###################################################################\n')
    print('...................Users connected to the devices....................\n')
    output = connection.send_command('status')
    print(output)
    time.sleep(10)
     #connection.disconnect()

elif Option == 2:
 filename=str(input('Please define the name of the txt file WITHOUT the extension: '))
 Path=str(input('Please define the path where the TXT file will be save in the following format: /Users/Desktop/): '))


 print('Please wait while data is processed and saved...')

 fd = open(r''+Path+filename+'.txt','w') # Where you want the file to save to.'txt/Users/ecanogut/Desktop/Splunk/WSA_Info.txt
 old_stdout = sys.stdout
 sys.stdout = fd

 connection= netmiko.ConnectHandler(ip=Deviceip,device_type="cisco_ios",
                                   username=username,password=password)

 print('#####################################################################\n')

 print('...............Device Version and additional information.............\n')
 output = connection.send_command('version')
 print(output)

 print('\n###################################################################\n')

 print('...................Users connected to the devices....................\n')
 output = connection.send_command('who')
 print(output)

 print('\n###################################################################\n')

 print('...................Resources utilization.............................\n')
 output = connection.send_command('status')
 print(output)

 print('\n###################################################################\n')

 print('...................Device Licenses...................................\n')
 output = connection.send_command('showlicense')
 print(output)

 print('\n###################################################################\n')

 print('................WCCP Statistics (Only if this feature is enable).....\n')
 output = connection.send_command('wccpstat')
 print(output)

 print('=====================================================================\n')


elif Option == 3:

 filename=str(input('Please define the name of the txt file WITHOUT the extension: '))
 Path=str(input('Please define the path where the TXT file will be save in the following format: /Users/Desktop/): '))
 print('Please wait while data is processed and saved...')

 fd = open(r''+Path+filename+'.txt','w') # Where you want the file to save to.'txt/Users/ecanogut/Desktop/Splunk/WSA_Info.txt
 old_stdout = sys.stdout
 sys.stdout = fd

 connection= netmiko.ConnectHandler(ip=Deviceip,device_type="cisco_ios",
                                   username=username,password=password)

 print('#####################################################################\n')

 print('...............Device Version and additional information.............\n')
 output = connection.send_command('version')
 print(output)
 connection.disconnect()

elif Option == 4:

 filename=str(input('Please define the name of the txt file WITHOUT the extension: '))
 Path=str(input('Please define the path where the TXT file will be save in the following format: /Users/Desktop/): '))
 print('Please wait while data is processed and saved...')

 fd = open(r''+Path+filename+'.txt','w') # Where you want the file to save to.
 old_stdout = sys.stdout
 sys.stdout = fd

 connection= netmiko.ConnectHandler(ip=Deviceip,device_type="cisco_ios",
                                   username=username,password=password)

 print('\n###################################################################\n')
 print('...................Users connected to the devices....................\n')
 output = connection.send_command('who')
 print(output)
 connection.disconnect()

elif Option == 5:

 filename=str(input('Please define the name of the txt file WITHOUT the extension: '))
 Path=str(input('Please define the path where the TXT file will be save in the following format: /Users/Desktop/): '))
 print('Please wait while data is processed and saved...')

 fd = open(r''+Path+filename+'.txt','w')
 old_stdout = sys.stdout
 sys.stdout = fd

 connection= netmiko.ConnectHandler(ip=Deviceip,device_type="cisco_ios",
                                   username=username,password=password)

 print('\n###################################################################\n')
 print('...................Resources utilization.............................\n')
 output = connection.send_command('status')
 print(output)
 connection.disconnect()

elif Option == 6:
 filename=str(input('Please define the name of the txt file WITHOUT the extension: '))
 Path=str(input('Please define the path where the TXT file will be save in the following format: /Users/Desktop/): '))
 print('Please wait while data is processed and saved...')

 fd = open(r''+Path+filename+'.txt','w') # Where you want the file to save to.
 old_stdout = sys.stdout
 sys.stdout = fd

 connection= netmiko.ConnectHandler(ip=Deviceip,device_type="cisco_ios",
                                   username=username,password=password)

 print('\n###################################################################\n')
 print('...................Device Licenses...................................\n')
 output = connection.send_command('showlicense')
 print(output)
 connection.disconnect()

elif Option == 7:

 filename=str(input('Please define the name of the txt file WITHOUT the extension: '))
 Path=str(input('Please define the path where the TXT file will be save in the following format: /Users/Desktop/): '))
 print('Please wait while data is processed and saved...')

 fd = open(r''+Path+filename+'.txt','w') # Where you want the file to save to.
 old_stdout = sys.stdout
 sys.stdout = fd

 connection= netmiko.ConnectHandler(ip=Deviceip,device_type="cisco_ios",
                                   username=username,password=password)

 print('\n###################################################################\n')
 print('................WCCP Statistics (Only if this feature is enable).....\n')
 output = connection.send_command('wccpstat')
 print(output)
 connection.disconnect()



elif Option == 8:
  exit()

else:
  print ("Number not Valid")

