
import uuid
import hashlib

from discovery.routing_table import RoutingTable


class PeerDiscovery:

    def __init__(self):

        # Generate unique node ID
        self.node_id = str(uuid.uuid4())

        # Store discovered peers
        self.peers = {}

        # Convert node ID into a 160-bit Kademlia ID
        routing_id = self.generate_routing_id(self.node_id)

        # Initialize routing table
        self.routing_table = RoutingTable(routing_id)

        print("Peer Discovery Initialized")

    @staticmethod
    def generate_routing_id(peer_id):

        return hashlib.sha1(
            str(peer_id).encode()
        ).hexdigest()

    def add_peer(self, peer_id, host, port):

        # Add peer to discovery dictionary
        self.peers[peer_id] = {
            "host": host,
            "port": port,
            "status": "ACTIVE"
        }

        # Add peer to routing table
        routing_id = self.generate_routing_id(peer_id)

        address = {
            "host": host,
            "port": port
        }

        self.routing_table.add_peer(
            routing_id,
            address
        )

        print(f"Peer added: {peer_id}")
        print("Peer added to Routing Table!")

    def get_peers(self):

        return self.peers

    def remove_peer(self, peer_id):

        if peer_id in self.peers:

            del self.peers[peer_id]

            # Remove peer from routing table
            routing_id = self.generate_routing_id(peer_id)

            self.routing_table.remove_peer(routing_id)

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

    def display_routing_table(self):

        print("\nMeshWeaver Routing Table")

        peers = self.routing_table.get_all_peers()

        if not peers:
            print("No peers in routing table.")
            return

        for peer in peers:

            print(
                "Node ID:", peer["node_id"],
                "Address:", peer["address"]
            )

    def find_closest_peers(self, target_id, count=5):

        target_routing_id = self.generate_routing_id(target_id)

        return self.routing_table.find_closest_peers(
            target_routing_id,
            count
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

    network.display_routing_table()
