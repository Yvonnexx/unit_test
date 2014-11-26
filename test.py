#!/usr/bin/python
import unittest
import sample

class BaseTestCase(unittest.TestCase):
    http_get_return_200_url = 'http://should.return.200.com'
    http_get_return_404_url = 'http://should.return.404.com'
    http_get_exception_url = 'http://should.get.exception.com'
    def setUp(self):
        self.real_requests = sample.requests
        sample.requests = MockRequests()
    def tearDown(self):
        sample.requests = self.real_requests
    def test_func_a(self):
        self.assertEqual(sample.func_a(), 3)
    def test_func_b(self):
        a = 3
        self.assertEqual(sample.func_b(3), 5)
    def test_func_c(self):
        a = 4
        b = 10
        c = 3
        d = 15
        self.assertEqual(sample.func_c(a,b), 10)
        self.assertEqual(sample.func_c(c,d), 3)
    def test_func_d1(self):
        self.assertEqual(sample.func_d(), 3)
    def test_func_d2(self):
        MockRequests.get('https://google.com').status_code=200
        self.assertEqual(sample.func_d(), 1)
    def test_func_e(self):
        with self.assertRaises(Exception):
            list(sample.func_e())

class MockRequests(object):
    def get(self, url, *args, **kwargs):
        if url == BaseTestCase.http_get_return_200_url:
            return MockRequestResponseObject(url, status_code=200)
        elif url == BaseTestCase.http_get_return_404_url:
            return MockRequestResponseObject(url, status_code=404)
        elif url == BaseTestCase.http_get_exception_url:
            raise Exception('some reason')
        else:
            return MockRequestResponseObject(url, status_code=500)

class MockRequestResponseObject(object):
    def __init__(self, url, *args, **kwargs):
        self.url = url
        self.status_code = kwargs.get('status_code', 500)
    def __repr__(self):
        return '<MockRequestsResponseObject %s>' %self.url

if __name__ == "__main__":
    try:
        unittest.main()
    except Exception, e:
        print 'Test failed: %s' %e

