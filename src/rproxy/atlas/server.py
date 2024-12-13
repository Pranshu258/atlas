class OriginServer:
    def __init__(self, host, weight=1, cpu=0, rif=0, latency=0):
        self.host = host
        self.weight = weight
        self.cpu = cpu
        self.rif = rif
        self.latency = latency

    def __str__(self):
        return f"{self.host} ({self.weight})"