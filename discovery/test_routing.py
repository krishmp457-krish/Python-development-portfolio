
from routing_table import RoutingTable

# Create a node with a 160-bit ID
my_node_id = "0000000000000000000000000000000000000001"

# Create routing table
routing = RoutingTable(my_node_id)

# Add other peers
routing.add_peer(
    "0000000000000000000000000000000000000002",
    "192.168.1.2:5000"
)

routing.add_peer(
    "0000000000000000000000000000000000000003",
    "192.168.1.3:5000"
)

routing.add_peer(
    "0000000000000000000000000000000000000005",
    "192.168.1.5:5000"
)

# Display all peers
print("All Known Peers:")
print(routing.get_all_peers())

# Find closest peers
target_id = "0000000000000000000000000000000000000004"

print("\nClosest Peers:")
print(routing.find_closest_peers(target_id, 2))
