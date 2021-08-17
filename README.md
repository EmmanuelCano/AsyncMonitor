# AsyncMonitor
Cisco Secure Web Appliance (aka WSA), Email Secure (aka ESA) are solutions used to protect customer infrastructures against email or web attacks while they are managed through Secure Email and Web Manager (aka SMA), however, there are limited options to monitor these solutions, being SNMP protocol the most used as prior to version 14.x, API does not have any verbs to achieve this. 

AsyncMonitor is a script developed in Python using Netmiko for automating the monitoring and gathering of information in terms of Hardware Resources utilization and general information from the device that is saved in a txt file. Given that the mentioned solutions run the same operating system (AsyncOs) and with the exception of Secure Email and Web Manager Nowadays (aka SMA) that requires minimal modification of one option, this script can be used with all of them.


This script  performs the following actions:
1. Gather and display hardware resources (CPU,RAM,Disk) utilization information from a single device every 5 minutes (300seconds) by default. 
Usage: This can be used to monitor resources for a period of time for troubleshooting purposes.

2. Gather and save in a txt file the following information: 
   - Hardware resources utilization.
   - Users connected to the device using SSH protocol.
   - Priviledges of your admin user.
   - Device version and general information.
   - Licenses installed along with expiration dates.
   - WCCP statistics (Only if the feature is enabled).
3. Gather and Save Device Version and general information in a txt file.
4. Gather and Save Users connected to the device using SSH protocol in a txt file.
5. Gather and Save Privileges of your admin user in a txt file.
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

# Output of Option 2 for 2 Devices
```
####################################################################################################

....................Device Version and additional information for Device : X.X.X.X.............


Current Version
===============
Product: Cisco S000V Web Security Virtual Appliance
Model: S000V
Version: 11.8.3-018
Build Date: 2021-01-20
Install Date: 2021-07-11 07:23:52
Serial #: 4224770FEE4D3F5EED03-BE9083A17C1C
BIOS: 6.00
CPUs: 1 expected, 4 allocated
Memory: 4096 MB expected, 8192 MB allocated
Hard disk: 200 GB, or 250 GB expected; 300 GB allocated
RAID: NA
RAID Status: Unknown
RAID Type: NA
BMC: NA
Cisco DVS Engine: 1.0 (Never Updated)
Cisco DVS Malware User Agent Rules: 0.554 (Never Updated)
Cisco DVS Object Type Rules: 0.554 (Never Updated)
Cisco Trusted Root Certificate Bundle: 1.9 (Mon May 10 15:40:08 2021)
Cisco Certificate Blacklist: 1.3 (Wed Mar 17 18:57:03 2021)
How-Tos: 1.0 (Never Updated)
L4 Traffic Monitor Anti-Malware Rules: 1629194402 (Tue Aug 17 06:10:09 2021)
Cisco Web Usage Controls - Web Categorization Engine: 1.12.4.944 (Never
Updated)
Cisco Web Usage Controls - Dynamic Content Analysis Engine: 2.1.0-016 (Never
Updated)
Cisco Web Usage Controls - Dynamic Content Analysis Engine Data: 3.1.0001
(Never Updated)
Cisco Web Usage Controls - Application Visibility and Control Engine: 1.1.0-076
(Never Updated)
Cisco Web Usage Controls - Application Visibility and Control Data:
1.1.0.67-001 (Mon Jul 12 13:18:37 2021)
Web Reputation IP Filters: 1629206445 (Tue Aug 17 09:23:26 2021)
Web Reputation Rules: 1625666389 (Tue Jul 27 00:56:38 2021)
Web Reputation URL Queries Database: 1629206668 (Tue Aug 17 09:29:01 2021)
Talos Intelligence engine: 1.12.4.944 (Never Updated)
Webroot Anti-Malware Engine: 2.1.5.8 (Never Updated)
Webroot Engine Definition: 2.1.5.8 (Never Updated)
Webroot Malware Categories DATs: 1353 (Never Updated)
Sophos Engine: 3.2.07.358.1_5.11 (Never Updated)
Sophos IDE:  (Never Updated)
Advanced Malware Protection - Engine: 1.0 (Never Updated)
Advanced Malware Protection - Engine Definition: 1.0 
Advanced Malware Protection - Pre-class Engine: 1.0 (Never Updated)
Advanced Malware Protection - Cisco Internal Certificates: 1.0.0-101 (Wed Mar
17 18:56:16 2021)

##################################################################################################

.................Users connected to the devices for Device: X.X.X.X...........................


Username  Role           Login Time  Idle Time  Remote Host   What
========  =============  ==========  =========  ============  ====
admin1    Administrator  09:30AM     0s         10.X.X.X      CLI

##################################################################################################

................Information of user logged for Device: X.X.X.X................................


Username: admin1
Full Name: admin
Groups: admin, operators, config, log, guest

##################################################################################################

..................Resources utilization for Device: X.X.X.X...................................


Enter "status detail" for more information.

Status as of:                  Tue Aug 17 09:31:09 2021 AST
Up since:                      Sun Jul 11 07:22:16 2021 AST (37d 2h 8m 54s)
System Resource Utilization:
  CPU                                    20.5%
  RAM                                    53.4%
  Reporting/Logging Disk                  8.6%
Transactions per Second:
  Average in last minute                     0
Bandwidth (Mbps):
  Average in last minute                 0.000
Response Time (ms):
  Average in last minute                     0
Connections:
  Total connections                          0



##################################################################################################

...............................Device Licenses for Device: X.X.X.X............................


Virtual License
===============
vln                      VLNWSA31457904
begin_date               Mon Oct 19 20:26:44 2020 GMT
end_date                 Fri Nov 05 20:26:44 2021 GMT
company                  Cisco SWIFT - Email:User2@cisco.com
seats                    1
serial                   2C8D32
email                    User2@cisco.com
issue                    d48861cdc4304582915b95e95ecce396
license_version          1.1


##################################################################################################

..WCCP Statistics (Only if this feature is enable) for Device: X.X.X.X..

WCCP seems inactive!!
=====================================================================

####################################################################################################

....................Device Version and additional information for Device: X.X.X.X.............


Current Version
===============
Product: Cisco S100V Web Security Virtual Appliance
Model: S100V
Version: 12.5.1-043
Build Date: 2021-02-05
Install Date: 2021-07-11 11:36:03
Serial #: 42248781599CE29812E2-75CEBE72BEBA
BIOS: 6.00
CPUs: 3 expected, 3 allocated
Memory: 8192 MB expected, 8192 MB allocated
Hard disk: 200 GB, or 250 GB expected; 200 GB allocated
RAID: NA
RAID Status: Unknown
RAID Type: NA
BMC: NA
Cisco DVS Engine: 1.0 (Never Updated)
Cisco DVS Malware User Agent Rules: 0.554 (Never Updated)
Cisco DVS Object Type Rules: 0.554 (Never Updated)
Cisco Trusted Root Certificate Bundle: 1.9 (Tue May 04 17:28:57 2021)
Cisco Certificate Blocked List: 1.3 (Thu Mar 18 15:20:26 2021)
How-Tos: 1.0 (Never Updated)
Youtube Categorization engine: 1.0.0 (Never Updated)
L4 Traffic Monitor Anti-Malware Rules: 1616098872 (Thu Mar 18 20:33:34 2021)
Cisco Web Usage Controls - Web Categorization Engine: 1.12.4.944 (Tue Aug 17
13:29:31 2021)
Cisco Web Usage Controls - Dynamic Content Analysis Engine: 2.1.0-016 (Never
Updated)
Cisco Web Usage Controls - Dynamic Content Analysis Engine Data: 3.1.0001
(Never Updated)
Cisco Web Usage Controls - Application Visibility and Control Engine: 1.1.0-076
(Never Updated)
Cisco Web Usage Controls - Application Visibility and Control Data:
1.1.0.67-001 (Tue Jul 13 16:15:53 2021)
Web Reputation IP Filters: 1625914336 (Tue Aug 17 13:29:31 2021)
Web Reputation Rules: 1625666389 (Tue Aug 17 13:29:31 2021)
Web Reputation URL Queries Database: 1625912478 (Tue Aug 17 13:29:31 2021)
Talos Intelligence engine: 1.12.4.944 (Never Updated)
Webroot Anti-Malware Engine: 2.1.5.8 (Never Updated)
Webroot Engine Definition: 2.1.5.8 (Never Updated)
Webroot Malware Categories DATs: 2947 (Tue Aug 17 01:19:49 2021)
Sophos Engine: 3.2.07.382.1_5.84 (Wed Jul 07 15:40:33 2021)
Sophos IDE: 2021081701 (Tue Aug 17 05:14:21 2021)
Advanced Malware Protection - Engine: 1.0 (Never Updated)
Advanced Malware Protection - Engine Definition: 1.0.0-119 
Advanced Malware Protection - Pre-class Engine: 1.0.0-118 (Thu Mar 18 15:20:31
2021)
Advanced Malware Protection - Cisco Internal Certificates: 1.0.0-101 (Thu Mar
18 15:20:07 2021)

##################################################################################################

.................Users connected to the devices for Device: X.X.X.X...........................


Username  Role           Login Time  Idle Time  Remote Host   What
========  =============  ==========  =========  ============  ====
admin1    Administrator  01:30PM     1s         X.X.X.X       CLI

##################################################################################################

................Information of user logged for Device: X.X.X.X................................


Username: admin1
Full Name: admin
Groups: admin, operators, config, log, guest

##################################################################################################

.........Resources utilization for Device: X.X.X.X.....................................


Enter "status detail" for more information.

Status as of:                  Tue Aug 17 13:30:59 2021 GMT
Up since:                      Sun Jul 11 11:28:46 2021 GMT (37d 2h 2m 14s)
System Resource Utilization:
  CPU                                    14.6%
  RAM                                    46.7%
  Reporting/Logging Disk                 12.1%
Transactions per Second:
  Average in last minute                     0
Bandwidth (Mbps):
  Average in last minute                 0.000
Response Time (ms):
  Average in last minute                     0
Connections:
  Total connections                          0



##################################################################################################

....................Device Licenses for Device: X.X.X.X............................


Virtual License
===============
vln                      VLNWSA1600879
begin_date               Wed Feb 17 18:03:38 2021 GMT
end_date                 Sun Mar 06 18:03:37 2022 GMT
company                  Cisco SWIFT - Email:user1@cisco.com
seats                    1
serial                   448ECE
email                    user1@cisco.com
issue                    9d5715cb286e4582ba616d052dbfeb24
license_version          1.1


##################################################################################################

..WCCP Statistics (Only if this feature is enable) for Device: X.X.X.X..


WCCP seems inactive!!
=====================================================================

```


Developed by [Emmanuel Cano - Cisco](https://www.linkedin.com/in/emmanuel-cano/)

