
from discovery.routing_table import RoutingTable
from discovery.peer_discovery import PeerDiscovery


print("\n========== ROUTING TABLE TEST ==========")

# TEST 1: Create Routing Table
my_node_id = "0000000000000000000000000000000000000001"

routing = RoutingTable(my_node_id)

print("\nTEST 1: Routing Table Initialized")
print("PASS")


# TEST 2: Add Peers
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

assert len(routing.get_all_peers()) == 3

print("\nTEST 2: Add Peers")
print("PASS")


# TEST 3: Display Peers
print("\nTEST 3: All Known Peers")

print(routing.get_all_peers())


# TEST 4: Find Closest Peers
target_id = "0000000000000000000000000000000000000004"

closest = routing.find_closest_peers(target_id, 2)

print("\nTEST 4: Closest Peers")
print(closest)

assert len(closest) == 2

print("PASS")


# TEST 5: Remove Peer
routing.remove_peer(
    "0000000000000000000000000000000000000003"
)

assert len(routing.get_all_peers()) == 2

print("\nTEST 5: Remove Peer")
print("PASS")


# TEST 6: Peer Discovery Integration
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

assert len(network.routing_table.get_all_peers()) == 2

print("\nTEST 6: Peer Discovery Integration")
print("PASS")


print("\n========== ALL TESTS COMPLETED SUCCESSFULLY ==========")
