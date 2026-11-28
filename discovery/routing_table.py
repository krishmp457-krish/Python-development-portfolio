
from collections import OrderedDict


class KBucket:
    """Stores a group of nearby peers."""

    def __init__(self, k=20):
        self.k = k
        self.peers = OrderedDict()

    def add_peer(self, peer_id, address):

        if peer_id in self.peers:
            self.peers.move_to_end(peer_id)
            self.peers[peer_id] = address
            return True

        if len(self.peers) < self.k:
            self.peers[peer_id] = address
            return True

        return False

    def remove_peer(self, peer_id):
        self.peers.pop(peer_id, None)


class RoutingTable:
    """Maintains the routing table of a node."""

    def __init__(self, node_id, k=20):

        self.node_id = self._to_int(node_id)
        self.k = k

        # 160-bit Kademlia routing table
        self.buckets = [KBucket(k) for _ in range(160)]

    @staticmethod
    def _to_int(peer_id):

        if isinstance(peer_id, str):
            peer_id = peer_id.replace("-", "")
            value = int(peer_id, 16)
        else:
            value = peer_id

        if not isinstance(value, int) or not 0 <= value < 2**160:
            raise ValueError("Node ID must be a valid 160-bit hexadecimal ID")

        return value

    def get_bucket_index(self, peer_id):

        peer_id = self._to_int(peer_id)

        distance = self.node_id ^ peer_id

        if distance == 0:
            return None

        return distance.bit_length() - 1

    def add_peer(self, peer_id, address):

        peer_id_int = self._to_int(peer_id)

        if peer_id_int == self.node_id:
            return False

        bucket_index = self.get_bucket_index(peer_id_int)

        return self.buckets[bucket_index].add_peer(
            peer_id_int, address
        )

    def remove_peer(self, peer_id):

        peer_id_int = self._to_int(peer_id)

        bucket_index = self.get_bucket_index(peer_id_int)

        if bucket_index is not None:
            self.buckets[bucket_index].remove_peer(peer_id_int)

    def find_closest_peers(self, target_id, count=None):

        target_id = self._to_int(target_id)

        all_peers = []

        for bucket in self.buckets:
            for peer_id, address in bucket.peers.items():

                distance = target_id ^ peer_id

                all_peers.append(
                    (distance, peer_id, address)
                )

        all_peers.sort(key=lambda peer: peer[0])

        if count is None:
            count = self.k

        return [
            {
                "node_id": format(peer_id, "040x"),
                "address": address
            }
            for distance, peer_id, address in all_peers[:count]
        ]

    def get_all_peers(self):

        peers = []

        for bucket in self.buckets:
            for peer_id, address in bucket.peers.items():

                peers.append({
                    "node_id": format(peer_id, "040x"),
                    "address": address
                })

        return peers
