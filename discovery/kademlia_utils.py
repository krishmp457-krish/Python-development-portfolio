
import secrets

# Generate a unique 160-bit node ID
def generate_node_id():
    return secrets.token_hex(20)


# Calculate XOR distance between two nodes
def xor_distance(node_id1, node_id2):
    id1 = int(node_id1, 16)
    id2 = int(node_id2, 16)

    return id1 ^ id2


# Find closest peers to a target node
def find_closest_peers(target_id, peers, count=3):

    sorted_peers = sorted(
        peers,
        key=lambda peer: xor_distance(
            target_id, peer["node_id"]
        )
    )

    return sorted_peers[:count]


if __name__ == "__main__":

    # Generate node IDs
    node_a = generate_node_id()
    node_b = generate_node_id()
    node_c = generate_node_id()
    node_d = generate_node_id()

    print("Node A:", node_a)
    print("Node B:", node_b)

    # Calculate distance
    distance = xor_distance(node_a, node_b)

    print("\nXOR Distance:", distance)

    # Create peer list
    peers = [
        {"name": "Node B", "node_id": node_b},
        {"name": "Node C", "node_id": node_c},
        {"name": "Node D", "node_id": node_d}
    ]

    # Find closest peers
    closest = find_closest_peers(
        node_a, peers, 2
    )

    print("\nClosest Peers:")

    for peer in closest:
        print(peer["name"], peer["node_id"])
