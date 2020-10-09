#!/usr/bin/env python3
'''
Script that contains code to verify the validity of IP and subnet addresses.
Can also get the subnet given an IP address.
'''

import re

def verify_ip_address_format(the_address):
    '''
    verify_ip_address_format(the_address) that returns a boolean
    Returns True if the given address is in the format of an ip address.
    Returns False otherwise.
    '''
    regex_string_ip_address = re.compile(r'^[0-9]{3}[.]{1}([0-9]{1,3}[.]{1}){2}[0-9]{1,3}$')

    if regex_string_ip_address.search(the_address) is not None:
        return True
    return False

def verify_subnet_mask_format(the_subnet_mask):
    '''
    verify_subnet_mask_format(the_subnet_mask) that returns a boolean
    Returns True if the given subnet mask is in the format of a subnet mask.
    Returns False otherwise.
    '''
    regex_string_subnet_mask_address_format = re.compile(r'^(((128|192|224|240|248|252|254|255|0(?=\.0))\.){3}(128|192|224|240|248|252|254|255|0))$')
    if regex_string_subnet_mask_address_format.search(the_subnet_mask) is None:
        return False
    divided_subnet_mask = the_subnet_mask.split(".")
    if divided_subnet_mask[0] < divided_subnet_mask[1] or divided_subnet_mask[1] < divided_subnet_mask[2] or divided_subnet_mask[2] < divided_subnet_mask[3]:
        return False
    return True

def get_full_subnet_mask(number_of_bits):
    '''
    Returns a formatted subnet mask given a number of bits.
    Returns False if number of bits given is invalid.
    '''
    if number_of_bits > 31 or number_of_bits < 0:
        return False
    full_subnet_mask = ""
    for current_division in range(4):
        if not full_subnet_mask == "":
            full_subnet_mask += "."
            
        if number_of_bits > 7:
            full_subnet_mask += "255"
            number_of_bits -= 8
        elif number_of_bits == 7:
            full_subnet_mask += "254"
            number_of_bits -= 7
        elif number_of_bits == 6:
            full_subnet_mask += "252"
            number_of_bits -= 6
        elif number_of_bits == 5:
            full_subnet_mask += "248"
            number_of_bits -= 5
        elif number_of_bits == 4:
            full_subnet_mask += "240"
            number_of_bits -= 4
        elif number_of_bits == 3:
            full_subnet_mask += "224"
            number_of_bits -= 3
        elif number_of_bits == 2:
            full_subnet_mask += "192"
            number_of_bits -= 2
        elif number_of_bits == 1:
            full_subnet_mask += "128"
            number_of_bits -= 1
        elif number_of_bits == 0:
            full_subnet_mask += "0"
            number_of_bits -= 0
    return full_subnet_mask

def apply_mask(ip_address, subnet_mask):
    '''
    Returns the subnet given an ip address and subnet mask.
    '''
    if verify_ip_address_format and verify_subnet_mask_format:
        subnet_to_return = ""
        divided_ip_address = ip_address.split(".")
        divided_subnet_mask = subnet_mask.split(".")
        for current_division in range(4):
            division_to_add = int(divided_ip_address[current_division]) & int(divided_subnet_mask[current_division])
            subnet_to_return += str(division_to_add)
            if not current_division == 3:
                subnet_to_return += "."
        return subnet_to_return
    return "invalid entry"





    
