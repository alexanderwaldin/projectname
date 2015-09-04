import unittest
from projectname import first_module

class TestSecondModule(unittest.TestCase):
    '''Test class'''

    def setUp(self):
        '''set up unitTest'''
        pass

    def tearDown(self):
        '''tear down unitTest'''
        pass


    def test_read_data(self):
        '''tests read_data'''
        expected = "Hello World!"
        actual = first_module.read_model()
        self.assertEqual(expected, actual)




if __name__ == '__main__':
    unittest.main()
