class OriginServer:
    def __init__(self, host, weight=1):
        self.host = host
        self.weight = weight

    def __str__(self):
        return f"{self.host} ({self.weight})"