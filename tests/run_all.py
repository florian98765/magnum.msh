import unittest

testmodules = [
    'mesh_utils_test',
    'inp_utils_test'
    ]

suite = unittest.TestSuite()

for t in testmodules:
  try:
    # If the module defines a suite() function, call it to get the suite.
    mod = __import__(t, globals(), locals(), ['suite'])
    suitefn = getattr(mod, 'suite')
    suite.addTest(suitefn())
  except (ImportError, AttributeError):
    subsuite = unittest.TestSuite()
    # else, just load all the test cases from the module.
    subsuite.addTest(unittest.defaultTestLoader.loadTestsFromName(t))
    suite.addTest(subsuite)

#Timer.enable()
unittest.TextTestRunner().run(suite)
#Timer.print_report()
