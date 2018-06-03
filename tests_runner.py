import unittest
import tests

TestSuite = unittest.TestSuite()
TestSuite.addTest(unittest.makeSuite(tests.TestList))
print("count of tests: " + str(TestSuite.countTestCases()))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(TestSuite)
