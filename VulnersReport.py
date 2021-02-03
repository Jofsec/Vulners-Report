#!/usr/bin/env python3.8


#import pyfiglet
import sys
import xml.dom.minidom
import vulners
import subprocess

#text = pyfiglet.figlet_format("\nVulners Report", font="roman")
#print(text)

def parse_nmap_xml(xml_file_path):
    vulners_api = vulners.Vulners(api_key="M7S14P5B16JGXAGI9MEIGS10ZUSVHVCFU1ZS7LQ6XHMEUHYAY5KSBPZOAMLP5O83")

    # create the XML object, usually known as a Tree
    dom_tree = xml.dom.minidom.parse(xml_file_path)
    # access the first element of the Tree
    nmaprun = dom_tree.documentElement
    # <cpe>cpe:/a:samba:samba</cpe>
    for element in nmaprun.getElementsByTagName("cpe"):
        # print(element.childNodes[0].data)
        cpe_info = element.childNodes[0].data
        # grab cpe string and call vulnerability with string
        try:
            cpe_results = vulners_api.cpeVulnerabilities(cpe_info)
            cpe_vulnerabilities_list = [cpe_results.get(key) for key in cpe_results if
                                        key not in ["info", "blog", "bugbounty"]]

            for cpe_list in cpe_vulnerabilities_list[0]:
                filtered_keys = ["id", "cvss", "href", "description"]
                results = [cpe_list[key] for key in filtered_keys]
                print(cpe_info + ":\n\n" + filtered_keys[0].upper() + ": " + str(results[0]) + "\n\n" + filtered_keys[1].upper() + ": " + str(results[1]) + "\n\n" + "Hypertext Reference: " + str(results[2]) + "\n\n" + filtered_keys[3].title() + ": " + str(results[3]))
                print( "-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------" + "\n")

        except ValueError:
            print("\nInvalid CPE format " + cpe_info +  "\n\n")
            continue


def main():
    ip_address = input("ip_address > ")

    subprocess.run(["nmap", "-sV", "-O", "-T4", "-p", "1-1000", "-oX", "nmap_output.xml", ip_address],
                                  capture_output=True, text=True)
    xml_file_path = "nmap_output.xml"
    parse_nmap_xml(xml_file_path)


if __name__ == '__main__':
    main()