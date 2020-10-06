#!/usr/bin/env python3
'''
Main script that accepts user input and provides methods.
'''

import re

def regex_ip_address_check_for_errors(the_address):
    '''
    regex_ip_address_check_for_errors(the_address) that returns a boolean
    Returns True if the given address is in the format of an ip address.
    Returns False otherwise.
    '''
    regex_string_ip_address = re.compile(r'^[0-9]{3}[.]{1}([0-9]{1,3}[.]{1}){2}[0-9]{1,3}$')

    if regex_string_ip_address.search(the_address) is not None:
        return True
    return False

def regex_subnet_mask_check_for_errors(the_subnet_mask):
    '''
    regex_subnet_mask_check_for_errors(the_subnet_mask) that returns a boolean
    Returns True if the given subnet mask is in the format of a subnet mask.
    Returns False otherwise.
    '''
    regex_string_subnet_mask_address_format = re.compile(r'^[0-9]{3}([0-9]{1,3}){3}$')
    regex_string_subnet_mask_bit_format = re.compile(r'^[0-2]?[0-9]$|^3[0,1]$')

    if regex_string_subnet_mask_address_format.search(the_subnet_mask) is not None:
        return True
    if regex_string_subnet_mask_bit_format.search(the_subnet_mask) is not None:
        return True
    return False

def test_method():
    print(regex_ip_address_check_for_errors('192.168.0.0'))
    print(regex_ip_address_check_for_errors('192.16.011.0'))
    print(regex_ip_address_check_for_errors('192.168.0.0.'))

    print(regex_subnet_mask_check_for_errors('0'))
    print(regex_subnet_mask_check_for_errors('01'))
    print(regex_subnet_mask_check_for_errors('1'))
    print(regex_subnet_mask_check_for_errors('20'))
    print(regex_subnet_mask_check_for_errors('29'))
    print(regex_subnet_mask_check_for_errors('30'))
    print(regex_subnet_mask_check_for_errors('31'))
    print(regex_subnet_mask_check_for_errors('32'))
    print(regex_subnet_mask_check_for_errors('40'))
    print(regex_subnet_mask_check_for_errors('a'))

def main():
    '''
    Launch method
    '''
    test_method()

if __name__ == "__main__":
    main()
