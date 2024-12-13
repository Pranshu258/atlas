import asyncio

class OriginServer:
    def __init__(self, host, weight=1, cpu=0, local_rif=0, latency=0):
        self.host = host
        self.weight = weight
        self.local_rif = local_rif
        self.lock = asyncio.Lock()

    def __str__(self):
        return f"{self.host} ({self.weight}, {self.local_rif})"