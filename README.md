# Vulner's Report
![ascii](./images/ascii.png.png)
#
The reason we built this script was to help people, specifically those working in Blue Team roles, to be able to streamline the process of looking up vulnerabilities for your software and OS versions.  With this script, it is as simple as just plugging in an IP Address instead of having to look up the software and OS versions to try and find any potential vulnerabilities.
#
# Run down of the Script
**Nmap Scan**

First thing we start with is an nmap scan that allows us to gather the information on the CPE's to be able to check for CVE's.  This starts with a prompt to enter an IP address that needs to be connected to the device you are using.  From there the script runs a specified Nmap scan which will output an XML file for us to parse through later.

![Nmap](./images/Nmap_Scan.png)

**Parsing the XML File**

From there the script allows us to parse through said XML File to be able to locate the CPE's information to be able to be plugged in later. 

![XML_File](./images/XML_File.png)

![Parsing_Script](./images/XML_Parsing_Script.png)

**Output of the CPE Information**

Now that we have the CPE information, We will use the Vulner's API database to check for any CVE's and once we have that information it is about simplifying it so that it can be easily read.  We decided to only show specific info about the CVE's to not overwhelm our program or the user.  We went with showing the ID, the CVSS, the hypertext reference, and then the description so you would know a little more about the CVE for diving any deeper.

![Output](./images/CPE_Output.png)

**Using the Hypertext Reference for Solutions**

The main reason we output the Hypertext Reference is so that the user can go to that URL and read more about the specific CVE as well as posted solutions on how to fix it.  You can see an example of this below.

![URL_Linked_Website](./images/URL_Linked_Website.png)

![Linked_Website](./images/Linked_Website_Explaining_Vulnerability.png)

**Extra Notes**

Testing with this script was done on a local host network using VM's provided to us by Fullstack Academy.  Currently, this version of script only works on Linux based OS's.  https://github.com/vulnersCom/api is Vulner's Github for different ways to use their database for your needs.  https://vulners.com/search?query=!bulletinFamily:ioc%20order:published is a link to the Vulner's Database if you are interesting in looking at what vulnerabilities they are reporting daily.

