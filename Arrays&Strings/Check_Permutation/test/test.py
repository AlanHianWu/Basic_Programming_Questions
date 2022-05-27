import unittest, time, sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

import Answer_python as ap

class TranscriptTest(unittest.TestCase):
    
    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print('%s: %.3f' % (self.id(), t))

    def test_01(self):
        t = 'abc'
        self.assertAlmostEqual(ap.check_permutation(t), True)
    
    def test_02(self):
        t = ''
        self.assertAlmostEqual(ap.check_permutation(t), True)
    
    def test_03(self):
        t = 'abcdefghijklmnopqrstuvwxyz'
        self.assertAlmostEqual(ap.check_permutation(t), True)

    def test_04(self):
        t = 'a1234567890a'
        self.assertAlmostEqual(ap.check_permutation(t), False)
        



if __name__ == '__main__':
 
    suite = unittest.TestLoader().loadTestsFromTestCase(TranscriptTest)
    unittest.TextTestRunner(verbosity=0).run(suite)
