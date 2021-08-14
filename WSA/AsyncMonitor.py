import netmiko
import sys
import time
import schedule


username="admin1"
password="password"


print('········································································· \n')
print('·······················Welcome to AsyncMonitor tool······················ \n')
print('········································································· \n')
Option=int(input('Please select the option from the Menu: \n 1.-Monitor every 5 mins \n 2.-Get all info  \n 3.-Device Version \n 4.-Users conected to the device \n 5.-Information of your User \n 6.-CPU, Memory usage \n 7.-Licenses installed \n 8.-WCCP Information (Only if this feature is enabled) \n 9.-Exit \n \n Type the number of the option: '))

#if Option == 1:
# ip_add_file = open(r'/Users/ecanogut/Desktop/Splunk/IPAddressList.txt','r') # a simple list of IP addresses you want to connect to each one on a new line
# for host in ip_add_file:
#     host = host.strip()
#     print(host)

ip_add_file=open(r'/Users/IPAddressList.txt','r') # a simple list of IP addresses you want to connect to each one on a new line

if Option == 1:
  ip=str(input('Please define the Device IP address will be monitored: '))
  print('Hardware utilization will be displayed every 5 minutes')
  while(True):
    connection= netmiko.ConnectHandler(ip=ip,device_type="cisco_ios",
                                   username=username,password=password)

    print('\n####################################################################################################\n')
    print('.......................Hardware utilization Statistics for Device: '+ip+'.............................\n')
    output = connection.send_command('status')
    print(output)
    time.sleep(10)


elif Option == 2:
 filename=str(input('Please define the name of the txt file WITHOUT the extension: '))
 Path=str(input('Please define the path where the TXT file will be save in the following format: /Users/Desktop/): '))
 print('Please wait while data is processed and saved...')

 fd = open(r''+Path+filename+'.txt','w') # Where you want the file to save to.
 old_stdout = sys.stdout
 sys.stdout = fd

 ip_add_file = open(r'/Users/IPAddressList.txt','r') # a simple list of IP addresses you want to connect to each one on a new line
 for host in ip_add_file:
     host = host.strip()

     connection= netmiko.ConnectHandler(ip=host,device_type="cisco_ios",
                                   username=username,password=password)

     print('####################################################################################################\n')

     print('.........................Device Version and additional information for Device: '+host+'.............\n')
     output = connection.send_command('version')
     print(output)

     print('\n##################################################################################################\n')

     print('......................Users connected to the devices for Device: '+host+'...........................\n')
     output = connection.send_command('who')
     print(output)

     print('\n##################################################################################################\n')

     print('.....................Information of user logged for Device: '+host+'................................\n')
     output = connection.send_command('whoami')
     print(output)

     print('\n##################################################################################################\n')

     print('...................Resources utilization for Device: '+host+'.......................................\n')
     output = connection.send_command('status')
     print(output)

     print('\n##################################################################################################\n')

     print('....................................Device Licenses for Device: '+host+'............................\n')
     output = connection.send_command('showlicense')
     print(output)

     print('\n##################################################################################################\n')

     print('..WCCP Statistics (Only if this feature is enable) for Device: '+host+'..\n')
     output = connection.send_command('wccpstat')
     print(output)

     print('=====================================================================\n')



elif Option == 3:

 filename=str(input('Please define the name of the txt file WITHOUT the extension: '))
 Path=str(input('Please define the path where the TXT file will be save in the following format: /Users/Desktop/): '))
 print('Please wait while data is processed and saved...')

 fd = open(r''+Path+filename+'.txt','w') # Where you want the file to save to.
 old_stdout = sys.stdout
 sys.stdout = fd

 ip_add_file = open(r'/Users/IPAddressList.txt','r') # a simple list of IP addresses you want to connect to each one on a new line
 for host in ip_add_file:
     host = host.strip()

     connection= netmiko.ConnectHandler(ip=host,device_type="cisco_ios",
                                   username=username,password=password)

     print('#####################################################################################################\n')

     print('..................Device Version and additional information for Device: '+host+'.....................\n')
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

 ip_add_file = open(r'/Users/IPAddressList.txt','r') # a simple list of IP addresses you want to connect to each one on a new line
 for host in ip_add_file:
     host = host.strip()

     connection= netmiko.ConnectHandler(ip=host,device_type="cisco_ios",
                                   username=username,password=password)

     print('\n################################################################################################\n')
     print('..........................Users connected to the device '+host+'..................................\n')
     output = connection.send_command('who')
     print(output)
     connection.disconnect()

elif Option == 5:

 filename=str(input('Please define the name of the txt file WITHOUT the extension: '))
 Path=str(input('Please define the path where the TXT file will be save in the following format: /Users/Desktop/): '))
 print('Please wait while data is processed and saved...')

 fd = open(r''+Path+filename+'.txt','w') # Where you want the file to save to.
 old_stdout = sys.stdout
 sys.stdout = fd

 ip_add_file = open(r'/Users/IPAddressList.txt','r') # a simple list of IP addresses you want to connect to each one on a new line
 for host in ip_add_file:
     host = host.strip()

     connection= netmiko.ConnectHandler(ip=host,device_type="cisco_ios",
                                   username=username,password=password)

     print('\n#############################################################################################\n')
     print('...............Information for the Admin User logged on the device:  '+host+'..................\n')
     output = connection.send_command('whoami')
     print(output)
     connection.disconnect()

elif Option == 6:
 filename=str(input('Please define the name of the txt file WITHOUT the extension: '))
 Path=str(input('Please define the path where the TXT file will be save in the following format: /Users/Desktop/): '))
 print('Please wait while data is processed and saved...')

 fd = open(r''+Path+filename+'.txt','w') # Where you want the file to save to.
 old_stdout = sys.stdout
 sys.stdout = fd

 ip_add_file = open(r'/Users/IPAddressList.txt','r') # a simple list of IP addresses you want to connect to each one on a new line
 for host in ip_add_file:
     host = host.strip()

     connection= netmiko.ConnectHandler(ip=host,device_type="cisco_ios",
                                   username=username,password=password)

     print('\n#############################################################################################\n')
     print('...................Resources utilization for the device:  '+host+'.............................\n')
     output = connection.send_command('status')
     print(output)
     connection.disconnect()

elif Option == 7:

 filename=str(input('Please define the name of the txt file WITHOUT the extension: '))
 Path=str(input('Please define the path where the TXT file will be save in the following format: /Users/Desktop/): '))
 print('Please wait while data is processed and saved...')

 fd = open(r''+Path+filename+'.txt','w') # Where you want the file to save to.
 old_stdout = sys.stdout
 sys.stdout = fd

 ip_add_file = open(r'/Users/IPAddressList.txt','r') # a simple list of IP addresses you want to connect to each one on a new line
 for host in ip_add_file:
     host = host.strip()

     connection= netmiko.ConnectHandler(ip=host,device_type="cisco_ios",
                                   username=username,password=password)

     print('\n#############################################################################################\n')
     print('...................Device Licenses for the device:  '+host+'...................................\n')
     output = connection.send_command('showlicense')
     print(output)
     connection.disconnect()

elif Option == 8:

 filename=str(input('Please define the name of the txt file WITHOUT the extension: '))
 Path=str(input('Please define the path where the TXT file will be save in the following format: /Users/Desktop/): '))
 print('Please wait while data is processed and saved...')

 fd = open(r''+Path+filename+'.txt','w') # Where you want the file to save to.
 old_stdout = sys.stdout
 sys.stdout = fd

 ip_add_file = open(r'/Users/IPAddressList.txt','r') # a simple list of IP addresses you want to connect to each one on a new line
 for host in ip_add_file:
     host = host.strip()

     connection= netmiko.ConnectHandler(ip=host,device_type="cisco_ios",
                                   username=username,password=password)

     print('\n###################################################################\n')
     print('................WCCP Statistics (Only if this feature is enable) for the device:  '+host+'.....\n')
     output = connection.send_command('wccpstat')
     print(output)
     connection.disconnect()


elif Option == 9:
  exit()

else:
  print ("Number not Valid")

