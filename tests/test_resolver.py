import unittest
from swede import resolver


class ResolverTest(unittest.TestCase):
    def testCreated(self):
        myRes = resolver.Resolver()
        self.failUnless(isinstance(myRes, resolver.Resolver))


def main():
    unittest.main()

if __name__ == '__main__':
    main()
