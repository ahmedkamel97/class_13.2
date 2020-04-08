#Importing the libraries 
import os
import unittest
import sys
import requests

#Defining the  file path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from board import app, db

TEST_DB = 'test.db'

"""
Primary class containing all the tests 
"""
class Basic(unittest.TestCase):
    '''
    These instructions are executed prior to each test
    '''    
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()
    '''
    These instructions are executed after each test
    '''
    def tearDown(self):
        pass
    '''
    This function tests if the primary page is loaded or not 
    '''
    def test_main_page(self):        
        req = self.app.get('/main', follow_redirects=True)
        self.assertEqual(req.status_code, 200)
   
#Running the tests
if __name__ == "__main__":
    unittest.main()
