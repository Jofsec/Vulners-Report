# Vulner's Report
![ascii](./images/ascii.png.png)
#
Script that lets you enter in an IP address and it will search through your device or network for CPE's to find any common vulnerabilities and exploits within the system
#
# Run down of the Script
**Nmap Scan**

First thing we start with is an nmap scan that allows us to gather the information on the CPE's to be able to check for CVE's.  This starts with a prompt to enter an IP address that needs to be connected to the device you are using.  From there the script runs a specified Nmap scan which will output an XML file for us to parse through later.

screenshot goes here

**Parsing the XML File**

From there the script allows us to parse through said XML File to be able to locate the CPE's information to be able to be plugged in later. 

Screenshot goes here

**Output of the CPE Information**

Now that we have the CPE information, We will use the Vulner's API database to check for any CVE's and once we have that information it is about simplifying it so that it can be easily read.  We decided to only show specific info about the CVE's to not overwhelm our program or the user.  We went with showing the ID, the CVSS, the hypertext reference, and then the description so you would know a little more about the CVE for diving any deeper.

Screenshot goes here

**Using the Hypertext Reference for Solutions**

The main reason we output the Hypertext Reference is so that the user can go to that URL and read more about the specific CVE as well as posted solutions on how to fix it.  You can see an example of this below.

screenshot goes here

**Wrapping it Up**



