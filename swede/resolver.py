"""Class that can be instanciated to do secure lookups

Part of Swede. (c) Pieter Lexis. Licensed under the GNU GPL version 3 or higher
"""

import dns.rdatatype
import dns.rdata
import dns.rdataset
import dns.rdatatype
import dns.rdataclass

_ROOTKSK = ("257 3 8 AwEAAagAIKlVZrpC6Ia7gEzahOR+9W29euxhJhVVLOyQb"
            "SEW0O8gcCjFFVQUTf6v58fLjwBd0YI0EzrAcQqBGCzh/RStIoO8g0NfnfL2MTJRkx"
            "oXbfDaUeVPQuYEhg37NZWAJQ9VnMVDxP/VHL496M/QZxkjf5/Efucp2gaDX6RS6CX"
            "poY68LsvPVjR0ZSwzz1apAzvN9dlzEheX7ICJBBtuA6G3LQpzW5hOA2hzCTMjJPJ8"
            "LbqF6dsV6DoBQzgul0sGIcGOYl7OyQdXfZ57relSQageu+ipAdTTJ25AsRTAoub8O"
            "NGcLmqrAmRLKBP1dfwhYB4N7knNnulqQxA+Uk1ihz0=")

_ROOTHINTS = {
   'A.ROOT-SERVERS.NET.': ['198.41.0.4', '2001:503:BA3E::2:30'],
   'B.ROOT-SERVERS.NET.': ['192.228.79.201', '2001:500:84::B'],
   'C.ROOT-SERVERS.NET.': ['192.33.4.12', ' 2001:500:2::C'],
   'D.ROOT-SERVERS.NET.': ['199.7.91.13', '2001:500:2D::D'],
   'E.ROOT-SERVERS.NET.': ['192.203.230.10'],
   'F.ROOT-SERVERS.NET.': ['192.5.5.241', '2001:500:2F::F'],
   'G.ROOT-SERVERS.NET.': ['192.112.36.4'],
   'H.ROOT-SERVERS.NET.': ['128.63.2.53', '2001:500:1::803F:235'],
   'I.ROOT-SERVERS.NET.': ['192.36.148.17', '2001:7FE::53'],
   'J.ROOT-SERVERS.NET.': ['192.58.128.30', '2001:503:C27::2:30'],
   'K.ROOT-SERVERS.NET.': ['193.0.14.129', '2001:7FD::1'],
   'L.ROOT-SERVERS.NET.': ['199.7.83.42', '2001:500:3::42'],
   'M.ROOT-SERVERS.NET.': ['202.12.27.33', '2001:DC3::35']
   }


class Resolver:
    """Securely resolve records"""
    _rootAnchor = None
    _rootHints = None

    def __init__(self, rootAnchor=_ROOTKSK, rootHints=_ROOTHINTS):
        """

        Keyword arguments:
        rootAnchor - The KSK of the root zone in zonefile format
        rootHints - Dict of root nameservers in the format
                    { name: [address1, address2...], .. }
        """
        self.setRootAnchor(rootAnchor)
        self.setRootHints(rootHints)

    def setRootAnchor(self, rootAnchor=_ROOTKSK):
        """Add the root trust anchor

        Keyword arguments:
        rootAnchor - The KSK of the root zone in zonefile format
        """
        if rootAnchor is None:
            self._rootAnchor = None
            return

        try:
            rootAnchor = dns.rdata.from_text(dns.rdataclass.IN,
                                             dns.rdatatype.DNSKEY,
                                             rootAnchor)
        except:
            raise

        self._rootAnchor = rootAnchor

    def setRootHints(self, rootHints=_ROOTHINTS):
        self._rootHints = rootHints

    def resolve(self, qname, rdtype=dns.rdatatype.A):
        rdtype = dns.rdatatype._by_text(rdtype)
