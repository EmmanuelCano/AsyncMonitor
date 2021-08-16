# AsyncMonitor

Cisco Secure Web Appliance (aka WSA), Email Secure (aka ESA) are solutions used to protect customer infraestructres against email or web attacks while they are managed through Secure Email and Web Manager Nowadays (aka SMA), however, there are limited options to monitor these solutions, being SNMP protocol the most used as prior to version 14.x, API does not have any verbs to achieve this. 

AsyncMonitor is a script developed in Python using Netmiko for automating the monitoring and gathering of information in terms of Hardware Resources utilization and general information from the device that is saved in a txt file. Given that the mentioned solutions run the same operating system (AsyncOs) and with the exception of Secure Email and Web Manager Nowadays (aka SMA) that requires minimal modification of one option, this script can be used with all of them.


This script  performs the following actions:
1. Gather and display hardware resources (CPU,RAM,Disk) utilization information from a single device every 5 minutes (300seconds) by default. 
   Usage: This can be used to monitor resources for a period of time for troubleshooting porpuses.
2. Gather and save in a txt file the following information: 
   - Hardware resources utilization.
   - Users connected to the device using SSH protocol.
   - Priviledges of your admin user.
   - Device version and general information.
   - Licenses installed along with expiration dates.
   - WCCP statistics (Only if the feature is enabled).
3. Gather and Save Device Version and general information in a txt file.
4. Gather and Save Users connected to the device using SSH protocol in a txt file.
5. Gather and Save Priviledges of your admin user in a txt file.
6. Gather and Save Hardware resources utilization in a txt file.
7. Gather and Save Licenses installed along with expiration information in a txt file.
8. Gather and Save WCCP statistcs in a txt file (Only if the feature is enabled).

Note: The script can perform actions from 2 to 8 on one or more devices by defining Ip Addresses in the IPAddressList txt 
Note: Dependeing of the number of addresses the script excution may take up to 25 seconds to gather and save the information.

# Setting up the environment

- Python v.3.8.2 or above and Netmiko v.2.4.2 or above must be installed. This must be the only python version in the virtual environment or host OS

Install the dependencies included in this repository with the following command:
```
pip install -r requirements.txt
```

The following is a more detailed explanation of the main Variables:

- **username**= Admin user username. This user must exists in all devices listed in IPAddressList file. 
- **password**= Admin user password. This password must exists in all devices listed in IPAddressList file.
- **ip_add_file**=This is the path will be used to save the txt file(s), if no path is defined the file will be saved in the same path of the script


# Installation

1. Clone this repository 

https://github.com/EmmanuelCano/AsyncOSMonitor

2. change into directory

cd AsyncMonitor

3. Update IPAddressList.txt with the devices IP addresses


# Running the Script

In order to run the script issue the following command:

```
Python3 AsyncMonitor.py

```

# Example Menu
```
········································································· 

·······················Welcome to AsyncMonitor tool······················ 

········································································· 

Please select the option from the Menu: 
 1.-Monitor every 5 mins 
 2.-Get all info  
 3.-Device Version 
 4.-Users conected to the device 
 5.-Information of your User 
 6.-CPU, Memory usage 
 7.-Licenses installed 
 8.-WCCP Information (Only if this feature is enabled) 
 9.-Exit 
 
 Type the number of the option:   
```

Developed by [Emmanuel Cano - Cisco](https://www.linkedin.com/in/emmanuel-cano/)

