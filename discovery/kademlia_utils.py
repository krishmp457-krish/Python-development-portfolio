
import secrets


# Generate a unique 160-bit node ID
def generate_node_id():
    return secrets.token_hex(20)


# Validate and convert node ID
def convert_node_id(node_id):

    if not isinstance(node_id, str):
        raise ValueError("Node ID must be a string")

    if len(node_id) != 40:
        raise ValueError("Node ID must contain 40 hexadecimal characters")

    try:
        return int(node_id, 16)
    except ValueError:
        raise ValueError("Invalid hexadecimal node ID")


# Calculate XOR distance
def xor_distance(node_id1, node_id2):

    id1 = convert_node_id(node_id1)
    id2 = convert_node_id(node_id2)

    return id1 ^ id2


# Find closest peers
def find_closest_peers(target_id, peers, count=3):

    if count < 0:
        raise ValueError("Count cannot be negative")

    sorted_peers = sorted(
        peers,
        key=lambda peer: xor_distance(
            target_id,
            peer["node_id"]
        )
    )

    return sorted_peers[:count]


if __name__ == "__main__":

    print("MESHWEAVER KADEMLIA UTILITIES")

    # Generate node IDs
    node_a = generate_node_id()
    node_b = generate_node_id()
    node_c = generate_node_id()
    node_d = generate_node_id()

    print("\nGenerated Node IDs:")

    print("Node A:", node_a)
    print("Node B:", node_b)
    print("Node C:", node_c)
    print("Node D:", node_d)

    # Calculate XOR distance
    distance = xor_distance(node_a, node_b)

    print("\nXOR Distance:")
    print(distance)

    # Create peer list
    peers = [
        {"name": "Node B", "node_id": node_b},
        {"name": "Node C", "node_id": node_c},
        {"name": "Node D", "node_id": node_d}
    ]

    # Find closest peers
    closest = find_closest_peers(
        node_a,
        peers,
        2
    )

    print("\nClosest Peers:")

    for peer in closest:
        print(peer["name"], peer["node_id"])

    print("\nKademlia Utilities Working Successfully!")
