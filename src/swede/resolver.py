"""Class that can be instanciated to do secure lookups

Part of Swede. (c) Pieter Lexis. Licensed under the GNU GPL version 3 or higher
"""


import unbound


ROOTKSK = (". IN DNSKEY 257 3 8 AwEAAagAIKlVZrpC6Ia7gEzahOR+9W29euxhJhVVLOyQbS"
           "EW0O8gcCjFFVQUTf6v58fLjwBd0YI0EzrAcQqBGCzh/RStIoO8g0NfnfL2MTJRkxoX"
           "bfDaUeVPQuYEhg37NZWAJQ9VnMVDxP/VHL496M/QZxkjf5/Efucp2gaDX6RS6CXpoY"
           "68LsvPVjR0ZSwzz1apAzvN9dlzEheX7ICJBBtuA6G3LQpzW5hOA2hzCTMjJPJ8LbqF"
           "6dsV6DoBQzgul0sGIcGOYl7OyQdXfZ57relSQageu+ipAdTTJ25AsRTAoub8ONGcLm"
           "qrAmRLKBP1dfwhYB4N7knNnulqQxA+Uk1ihz0=")


class Resolver:
    """Securely resolve records"""
    unboundCtx = None

    def __init__(self, rootAnchor=ROOTKSK):
        """

        Keyword arguments:
        rootAnchor - The KSK of the root zone in zonefile format
        """
        self.unboundCtx = unbound.ub_ctx()
        self.addRootAnchor(rootAnchor)

    def addRootAnchor(self, rootAnchor=ROOTKSK):
        """Add the root trust anchor

        Keyword arguments:
        rootAnchor - The KSK of the root zone in zonefile format
        """
        res = self.unboundCtx.add_ta(rootAnchor)
        # XXX This always returns 0, add check
        if res != 0:
            raise Exception("Invalid root anchor: '%s'" % rootAnchor)

    def addDlvAnchor(self, dlvAnchor):
        """Add a DLV (Domain Look-aside Validation) trust anchor to the
        resolver.

        Keyword arguments:
        dlvAnchor - The DLV record in zonefile format
        """
        res = self.unboundCtx.set_option('dlv-anchor:',
                                         dlvAnchor)
        # XXX This always returns 0, add check
        if res != 0:
            raise Exception("Invalid dlv anchor: '%s'" % dlvAnchor)

    def getRecord(self):
        pass
