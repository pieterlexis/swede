import unittest
from dns.exception import SyntaxError
from swede import resolver


class ResolverTest(unittest.TestCase):
    def testCreation(self):
        myRes = resolver.Resolver()
        self.assertTrue(isinstance(myRes, resolver.Resolver))

        with self.assertRaises(SyntaxError):
            resolver.Resolver(rootAnchor='invalid')


def main():
    unittest.main()

if __name__ == '__main__':
    main()
