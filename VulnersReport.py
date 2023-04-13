#!/usr/bin/env python3.8

import xml.dom.minidom
import vulners
import subprocess

def print_vulnerability_info(cpe_info, vulnerability_info):
    filtered_keys = ["id", "cvss", "href", "description"]
    results = [vulnerability_info.get(key) for key in filtered_keys]
    print(f"{cpe_info}:\n{'-'*100}\n"
          f"{filtered_keys[0].upper()}: {results[0]}\n"
          f"{filtered_keys[1].upper()}: {results[1]}\n"
          f"Hypertext Reference: {results[2]}\n"
          f"{filtered_keys[3].title()}: {results[3]}\n"
          f"{'-'*100}\n")

def get_vulnerabilities(cpe_info, vulners_api):
    try:
        results = vulners_api.cpeVulnerabilities(cpe_info)
        vulnerability_info_list = [results.get(key) for key in results if key not in ["info", "blog", "bugbounty"]]
        for vulnerability_info in vulnerability_info_list[0]:
            print_vulnerability_info(cpe_info, vulnerability_info)
    except ValueError:
        print(f"Invalid CPE format {cpe_info}\n")

def parse_nmap_xml(xml_file_path, vulners_api):
    dom_tree = xml.dom.minidom.parse(xml_file_path)
    nmaprun = dom_tree.documentElement
    for element in nmaprun.getElementsByTagName("cpe"):
        cpe_info = element.childNodes[0].data
        get_vulnerabilities(cpe_info, vulners_api)

def main():
    api_key = "your_api_key"
    vulners_api = vulners.Vulners(api_key)
    ip_address = input("ip_address > ")

    nmap_command = ["nmap", "-sV", "-O", "-T4", "-p", "1-1000", "-oX", "nmap_output.xml", ip_address]
    subprocess.run(nmap_command, capture_output=True, text=True)
    xml_file_path = "nmap_output.xml"
    parse_nmap_xml(xml_file_path, vulners_api)

if __name__ == '__main__':
    main()
