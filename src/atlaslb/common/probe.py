import time
from atlaslb.common.originserver import OriginServer

class PrequalProbe: 
    """
    """
    def __init__(self, origin: OriginServer):
        """
        """
        self.timestamp = time.time()
        self.origin = origin
        self.rif = origin.local_rif
        self.latency = origin.latency