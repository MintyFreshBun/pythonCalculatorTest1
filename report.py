from unittest import TestLoader, TestSuite
from HTMLTestRunner import HTMLTestRunner
import test_calculator1
import time

example_tests =TestLoader().loadTestsFromTestCase(test_calculator1.MyTestCase)

suite= TestSuite([example_tests])

now = time.strftime("%Y-%m-%d %H_%M_%S")
filename = 'C:\\Users\\Miguel Amaral\\Documents\\ESMAD documents and Works\\Year 2020-2021 year2\\second Semester\\TPW\\performance part\\python exercices\\projExer1\\reports\\' + now + "result.html"

fp =open(filename, 'w')
runner==HTMLTestRunner.HTMLTestRunner(stream=fp)

runner.run(suite)

fp.close()
