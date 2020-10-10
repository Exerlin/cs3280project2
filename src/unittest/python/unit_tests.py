#! python3

__author__ = "Ethan Jensen"
__version__ = "1.0.0"

import unittest
import utils

class TestUtilsTests(unittest.TestCase):

    def test_valid_ip_address(self):
        self.assertTrue(utils.verify_ip_address_format('127.18.234.42'))
        self.assertTrue(utils.verify_ip_address_format('127.0.0.0'))

    def test_invalid_ip_address(self):
        self.assertFalse(utils.verify_ip_address_format('127.1811.234.42'))
        self.assertFalse(utils.verify_ip_address_format('127.18.234'))
        self.assertFalse(utils.verify_ip_address_format('127.18.234.42.'))

    def test_valid_subnet_mask(self):
        self.assertTrue(utils.verify_subnet_mask_format('128.0.0.0'))
        self.assertTrue(utils.verify_subnet_mask_format('0.0.0.0'))
        self.assertTrue(utils.verify_subnet_mask_format('255.255.255.254'))
        self.assertTrue(utils.verify_subnet_mask_format('0'))
        self.assertTrue(utils.verify_subnet_mask_format('15'))
        self.assertTrue(utils.verify_subnet_mask_format('23'))
        self.assertTrue(utils.verify_subnet_mask_format('31'))

    def test_invalid_subnet_mask(self):
        self.assertFalse(utils.verify_subnet_mask_format('0.128.0.0'))
        self.assertFalse(utils.verify_subnet_mask_format('0.0.0.128'))
        self.assertFalse(utils.verify_subnet_mask_format('223.128.0.0'))
        self.assertFalse(utils.verify_subnet_mask_format('255.255.255.255'))
        self.assertFalse(utils.verify_subnet_mask_format('-1'))
        self.assertFalse(utils.verify_subnet_mask_format('32'))

    def test_get_full_subnet_mask(self):
        self.assertEqual(utils.get_full_subnet_mask(0), '0.0.0.0')
        self.assertEqual(utils.get_full_subnet_mask(31), '255.255.255.254')
        self.assertEqual(utils.get_full_subnet_mask(9), '255.128.0.0')
        self.assertEqual(utils.get_full_subnet_mask(1), '128.0.0.0')
        self.assertFalse(utils.get_full_subnet_mask(-1))
        self.assertFalse(utils.get_full_subnet_mask(32))

    def test_apply_mask(self):
        self.assertEqual(utils.apply_mask('192.168.233.89', '255.255.255.0'), '192.168.233.0')
        self.assertEqual(utils.apply_mask('192.168.233.89', '255.255.255.254'), '192.168.233.88')
        self.assertEqual(utils.apply_mask('192.168.233.89', '0.0.0.0'), '0.0.0.0')
        self.assertEqual(utils.apply_mask('192.168.233.89', '255.0.0.0'), '192.0.0.0')
        self.assertEqual(utils.apply_mask('192.168.233.89', '255.0.0.0'), '192.0.0.0')
        self.assertEqual(utils.apply_mask('192.168.233.89', '1.0.0.0'), 'invalid entry')
        self.assertEqual(utils.apply_mask('192.168.233', '255.0.0.0'), 'invalid entry')

    def test_check_resource(self):
        self.assertTrue(utils.check_resource('/subnet?192.131.131.15&2'))
        self.assertTrue(utils.check_resource('/subnet?192.131.131.15&255.0.0.0'))
        self.assertFalse(utils.check_resource('subnet?192.131.131.15&255.0.0.0'))
        self.assertFalse(utils.check_resource('/subnet192.131.131.15&255.0.0.0'))
        self.assertFalse(utils.check_resource('/subnet?192.131.131.15255.0.0.0'))
        self.assertFalse(utils.check_resource('./subnet?192.131.131.15&255.0.0.0'))
        self.assertFalse(utils.check_resource('/subnet?192.131.131.15&255.0.0.0.'))

    def test_check_resource_start(self):
        self.assertTrue(utils.check_resource_start('/subnet?192.131.131.15&2'))
        self.assertTrue(utils.check_resource_start('/subnet'))
        self.assertTrue(utils.check_resource_start('/subnetblahblahthisstuffdoesntmatter'))
        self.assertFalse(utils.check_resource_start('subnet'))
        self.assertFalse(utils.check_resource_start('/subet'))

    def test_grab_subnet(self):
        self.assertEqual(utils.grab_subnet('/subnet?192.131.131.15&255.0.0.0'), '255.0.0.0')
        self.assertEqual(utils.grab_subnet('/subnet?192.131.131.15&2'), '2')

    def test_grab_ip_address(self):
        self.assertEqual(utils.grab_ip_address('/subnet?192.131.131.15&255.0.0.0'), '192.131.131.15')
        self.assertEqual(utils.grab_ip_address('/subnet?0.0.0.0&2'), '0.0.0.0')

    def test_grab_query(self):
        self.assertEqual(utils.grab_query('/subnet?192.131.131.15&255.0.0.0'), '192.131.131.15&255.0.0.0')
        self.assertEqual(utils.grab_query('/subnet?192.131.131.15&2'), '192.131.131.15&192.0.0.0')
    
if __name__ == '__main__':
    unittest.main()
