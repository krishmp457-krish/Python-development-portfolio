
import time


class GossipManager:
    """Manages sharing of resource information between nodes."""

    def __init__(self, node_id):
        self.node_id = node_id
        self.peer_resources = {}

    def create_gossip_message(self, resource_info):
        """Create a message containing local resource information."""

        message = {
            "sender": self.node_id,
            "resources": resource_info,
            "timestamp": time.time()
        }

        return message

    def receive_gossip_message(self, message):
        """Receive and store another node's resource information."""

        sender = message.get("sender")
        resources = message.get("resources")

        if not sender or sender == self.node_id:
            return False

        if not isinstance(resources, dict):
            return False

        self.peer_resources[sender] = {
            "resources": resources,
            "timestamp": message.get("timestamp", time.time())
        }

        return True

    def get_peer_resources(self):
        """Return resource information of known peers."""

        return self.peer_resources


if __name__ == "__main__":

    # Create two simulated nodes
    node_a = GossipManager("Node_A")
    node_b = GossipManager("Node_B")

    # Node A's resource information
    node_a_resources = {
        "cpu_usage": 35,
        "ram_usage": 60
    }

    # Node A creates a gossip message
    message = node_a.create_gossip_message(node_a_resources)

    # Node B receives the message
    node_b.receive_gossip_message(message)
    # Node B shares its resource information with Node A
    node_b_resources = {
        "cpu_usage": 20,
        "ram_usage": 45
    }

    message_b = node_b.create_gossip_message(node_b_resources)

    node_a.receive_gossip_message(message_b)

    print("\nNode A received resource information:")
    print(node_a.get_peer_resources())

    # Display received information
    print("Node B received resource information:")
    print(node_b.get_peer_resources())
