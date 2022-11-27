#!/usrbin/python3
"""DBStorage tests module"""

import unittest
from models.engine import db_storage

class TestDBS(unittest.TestCase):
    """DBStorage test class"""
    
    def test_doc_dbs(self):
        """Test doc"""
        self.assertTrue(db_storage.__doc__)