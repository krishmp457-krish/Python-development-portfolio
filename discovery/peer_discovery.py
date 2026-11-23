
import uuid


class PeerDiscovery:

    def __init__(self):
        self.node_id = str(uuid.uuid4())
        self.peers = {}

    def add_peer(self, peer_id, host, port):
        self.peers[peer_id] = {
            "host": host,
            "port": port,
            "status": "ACTIVE"
        }

        print(f"Peer added: {peer_id}")

    def get_peers(self):
        return self.peers

    def remove_peer(self, peer_id):
        if peer_id in self.peers:
            del self.peers[peer_id]
            print(f"Peer removed: {peer_id}")

    def display_network(self):
        print("\nMeshWeaver Network")
        print("My Node ID:", self.node_id)

        for peer_id, details in self.peers.items():
            print(
                peer_id,
                details["host"],
                details["port"],
                details["status"]
            )


if __name__ == "__main__":

    network = PeerDiscovery()

    network.add_peer(
        "NODE_B",
        "127.0.0.1",
        5002
    )

    network.add_peer(
        "NODE_C",
        "127.0.0.1",
        5003
    )

    network.display_network()
