#!/usr/bin/env python3
'''
Main script that accepts user input and provides methods.
'''

import re
import utils

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

def test_method():
    print(utils.verify_ip_address_format('192.168.0.0'))
    print(utils.verify_ip_address_format('192.16.011.0'))
    print(utils.verify_ip_address_format('192.168.0.0.'))

    print(utils.verify_subnet_mask_format('255.254.0.0'))
    print(utils.verify_subnet_mask_format('255.255.128.0'))
    print(utils.verify_subnet_mask_format('255.255.0.255'))

def main():
    '''
    Launch method
    '''
    test_method()

if __name__ == "__main__":
    main()
