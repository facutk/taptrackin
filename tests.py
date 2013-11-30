#!venv/bin/python
import unittest
import hello

class TestCase( unittest.TestCase ):

    def setUp( self ):
        self.app = hello.app.test_client()

    def test_ok( self ):
        expected = 1
        actual = 1
        assert expected == actual

    def test_error( self ):
        expected = 1
        actual = 1
        assert expected == actual

    def test_hello_world( self ):
        expected = 'Hello World!'
        actual = self.app.get('/')
        assert expected in actual.data

    def tearDown( self ):
        pass

if __name__ == '__main__':
    unittest.main()
