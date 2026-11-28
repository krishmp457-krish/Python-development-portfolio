
import threading

# Networking modules
from networking import server
from networking import client

# Peer Discovery
from discovery.peer_discovery import PeerDiscovery

# Kademlia Utilities
from discovery.kademlia_utils import (
    generate_node_id,
    find_closest_peers
)


class Node:

    def __init__(self):

        print("\nInitializing MeshWeaver Node...")

        # 1. Initialize Peer Discovery
        self.discovery = PeerDiscovery()

        self.node_id = self.discovery.node_id
        self.running = False
        self.server_thread = None

        # 2. Access Routing Table
        self.routing_table = self.discovery.routing_table

        print("Node ID:", self.node_id)

        print("Peer Discovery Initialized")
        print("Routing Table Initialized")

    # Display all components
    def display_components(self):

        print("\n========== MESHWEAVER COMPONENTS ==========")

        print("\n1. Peer Discovery")
        self.discovery.display_network()

        print("\n2. Kademlia Routing Table")
        self.discovery.display_routing_table()

    # Find closest peers using Kademlia utilities
    def find_peers(self, target_id=None, count=5):

        if target_id is None:
            target_id = generate_node_id()

        peers = self.routing_table.get_all_peers()

        closest = find_closest_peers(
            target_id,
            peers,
            count
        )

        print("\nClosest Peers:")

        for peer in closest:
            print(peer)

        return closest

    # Start MeshWeaver
    def start(self):

        self.running = True

        print("\nStarting MeshWeaver Node...")

        # 3. Initialize and display components
        self.display_components()

        # 4. Start Networking Server
        print("\nStarting Networking Server...")

        self.server_thread = threading.Thread(
            target=server.start_server,
            daemon=True
        )

        self.server_thread.start()

        # 5. Wait for Server
        if server.SERVER_READY.wait(timeout=5):

            print("\nServer is ready!")

            # 6. Start Networking Client
            print("\nStarting Networking Client...")

            client.start_client()

        else:

            print("\nServer failed to start!")

        print("\nMeshWeaver Node execution completed!")

    # Stop Node
    def stop(self):

        self.running = False

        print("\nMeshWeaver Node stopped!")


if __name__ == "__main__":

    node = Node()
    node.start()
