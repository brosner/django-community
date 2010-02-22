import pprint
import json
import sys
import time
import urllib2

from django.test import TestCase

class NewTestCase(TestCase):
    def setUp(self):
        print '---in %s for %s---\n' % (sys._getframe().f_code.co_name, \
                                      self.__class__.__name__)
        
    def testMethod(self):
        print '---in %s for %s---\n' % (sys._getframe().f_code.co_name, \
                                      self.__class__.__name__)
        start = time.time()
        d = {
            'title':'Sr Django Engineer',
        }
        #data = json.dumps(d)
        data=d
        f = self.client.post('/api/jobs/something', data)
        page = f.content
        elapsed = time.time() - start
        print 'response: %s' % page
        print 'elapsed: %s, page length: %s' % (elapsed, len(page))

        
    def tearDown(self):
        print '---in %s for %s---\n' % (sys._getframe().f_code.co_name, \
                                      self.__class__.__name__)

