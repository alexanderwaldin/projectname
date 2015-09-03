import unittest
from projectname.subpackageone import second_module


class TestSecondModule(unittest.TestCase):
    '''Test class'''

    def setUp(self):
        '''set up unitTest'''
        pass

    def tearDown(self):
        '''tear down unitTest'''
        pass

    def test_read_model(self):
        '''tests load_data'''
        expected = "Hello World!"
        actual = second_module.read_model()
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
