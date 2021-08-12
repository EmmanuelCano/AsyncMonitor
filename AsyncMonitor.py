import netmiko
import sys

Deviceip="10.207.195.178"
username="admin"
password="Cano09101207#"


print('········································································· \n')
print('·······················Welcome to AsyncMonitor tool······················ \n')
print('········································································· \n')
#print('The tool will obtain and save the following data from the AsyncOS Device:\n')
#print('\n 1.-Device Version \n 2.-Users conected to the device \n 3.-CPU, Memory usage \n 4.-Licenses installed \n 5.-Active Alerts\n\n')
Option=int(input('Please select the option from the Menu: \n 1.-Get all info  \n 2.-Device Version \n 3.-Users conected to the device \n 4.-CPU, Memory usage \n 5.-Licenses installed \n 6.-WCCP Information (Only if this feature is enabled) \n 7.-Running Conf\n \n Type the number of the option:'))

filename=str(input('Please define the name of the txt file WITHOUT the extension: '))
Path=str(input('Please define the path where the TXT file will be save in the following format: /Users/Desktop/): '))
print('Please wait while data is processed and saved...')

if Option == 1:
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

#print(connection.send_command("show ip int brief"))

elif Option == 2:

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

elif Option == 3:
 fd = open(r''+Path+filename+'.txt','w') # Where you want the file to save to.'txt/Users/ecanogut/Desktop/Splunk/WSA_Info.txt
 old_stdout = sys.stdout
 sys.stdout = fd

 connection= netmiko.ConnectHandler(ip=Deviceip,device_type="cisco_ios",
                                   username=username,password=password)

 print('\n###################################################################\n')
 print('...................Users connected to the devices....................\n')
 output = connection.send_command('who')
 print(output)
 connection.disconnect()

elif Option == 4:
 fd = open(r''+Path+filename+'.txt','w') # Where you want the file to save to.'txt/Users/ecanogut/Desktop/Splunk/WSA_Info.txt
 old_stdout = sys.stdout
 sys.stdout = fd

 connection= netmiko.ConnectHandler(ip=Deviceip,device_type="cisco_ios",
                                   username=username,password=password)

 print('\n###################################################################\n')
 print('...................Resources utilization.............................\n')
 output = connection.send_command('status')
 print(output)
 connection.disconnect()

elif Option == 5:
 fd = open(r''+Path+filename+'.txt','w') # Where you want the file to save to.'txt/Users/ecanogut/Desktop/Splunk/WSA_Info.txt
 old_stdout = sys.stdout
 sys.stdout = fd

 connection= netmiko.ConnectHandler(ip=Deviceip,device_type="cisco_ios",
                                   username=username,password=password)

 print('\n###################################################################\n')
 print('...................Device Licenses...................................\n')
 output = connection.send_command('showlicense')
 print(output)
 connection.disconnect()

elif Option == 6:
 fd = open(r''+Path+filename+'.txt','w') # Where you want the file to save to.'txt/Users/ecanogut/Desktop/Splunk/WSA_Info.txt
 old_stdout = sys.stdout
 sys.stdout = fd

 connection= netmiko.ConnectHandler(ip=Deviceip,device_type="cisco_ios",
                                   username=username,password=password)

 print('\n###################################################################\n')
 print('................WCCP Statistics (Only if this feature is enable).....\n')
 output = connection.send_command('wccpstat')
 print(output)
 connection.disconnect()

elif Option == 7:
  fd = open(r''+Path+filename+'.txt','w') # Where you want the file to save to.'txt/Users/ecanogut/Desktop/Splunk/WSA_Info.txt
  old_stdout = sys.stdout
  sys.stdout = fd

  connection= netmiko.ConnectHandler(ip=Deviceip,device_type="cisco_ios",
                                    username=username,password=password)

  print('\n###################################################################\n')
  print('................Running config (Only if this feature is enable).....\n')
  output = connection.send_command('showconfig')
  print(output)
  connection.disconnect()

  print('=====================================================================\n')
