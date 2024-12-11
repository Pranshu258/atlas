import threading

class BaseLoadBalancer: 
    def __init__(self, servers):
        self.servers = servers
        self.lock = threading.Lock()

    def add_server(self, server):
        with self.lock:
            self.servers.add(server)