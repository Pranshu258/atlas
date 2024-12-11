import threading

class BaseLoadBalancer: 
    def __init__(self, servers):
        self.servers = servers
        self.lock = threading.Lock()

    def add_server(self, server):
        if server not in self.servers:
            with self.lock:
                self.servers.append(server)