import unittest

class TestAsserts:
    def test1_exe(self):
        self.assertEqual('foo'.upper(), 'FOO')
        self.assertNotEqual('foo'.upper(), 'FOO')
        self.assertTrue()
        self.assertFalse()