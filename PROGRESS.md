# MeshWeaver – Daily Development Progress

## Day 1: Project Understanding and Architecture Design

### Objective
Understand the MeshWeaver project requirements and prepare the initial system architecture.

### Work Log
- Studied the fundamentals of distributed computing.
- Understood the concept of nodes and peer-to-peer communication.
- Identified the major components of MeshWeaver.
- Explored networking and remote task execution concepts.
- Studied the purpose of Kademlia DHT and the Gossip Protocol.
- Designed the initial modular system architecture.
- Identified the technologies and Python libraries required.

### Technologies Identified
- Python
- PyCharm
- Asyncio
- Socket Programming
- Cloudpickle
- Kademlia
- Psutil

### Outcome
Developed an initial understanding of the project requirements and prepared the proposed system architecture.

### Next Steps
- Set up the PyCharm development environment.
- Create the project directory structure.
- Begin implementing TCP socket communication between two Python nodes.

### Status
In Progress

## Day 2 – Networking Implementation

- Implemented TCP socket communication.
- Created a TCP server.
- Created a TCP client.
- Established localhost connection.
- Implemented message sending and receiving.
- Tested client-server communication.

Status: Completed

## Day 3 – Asynchronous Networking

### Tasks Completed
- Implemented asynchronous TCP server using asyncio.
- Implemented asynchronous client communication.
- Used asyncio.start_server() for server creation.
- Used asyncio.open_connection() for client connections.
- Used asyncio.gather() to handle multiple client operations concurrently.
- Tested communication between three clients and one server.

### Files Created
- networking/async_server.py
- networking/async_client.py

### Outcome
Successfully implemented asynchronous
communication for the MeshWeaver project.

### Next Step
Implement Python function serialization
using cloudpickle.


## Day 4 – Cloudpickle and Task Serialization

### Tasks Completed
- Installed cloudpickle.
- Implemented task serialization.
- Implemented task deserialization.
- Created an asynchronous task server.
- Created an asynchronous task client.
- Transferred Python functions over TCP.
- Executed received functions remotely.
- Returned execution results to the sender.

### Files Created
- tasks/serializer.py
- networking/task_server.py
- networking/task_client.py

### Testing
- Tested remote addition function.
- Tested remote multiplication function.
- Verified successful result transfer.

### Outcome
Successfully implemented basic remote Python
function execution using cloudpickle and asyncio.

### Next Step
Implement peer identification and peer discovery.


## Day 5 – Remote Task Execution and Integration

### Tasks Completed
- Integrated remote task execution components.
- Tested asynchronous task communication.
- Implemented unique task identification using UUID.
- Created TaskManager class.
- Added task status tracking.
- Tested remote multiplication function.

### Files Created
- tasks/task_manager.py

### Outcome
Implemented initial task tracking and verified
remote Python function execution.

---

## Day 6 – Node Identification and Peer Discovery

### Tasks Completed
- Implemented unique node identification.
- Created PeerDiscovery class.
- Implemented peer registration.
- Added peer information storage.
- Implemented peer listing.
- Implemented peer removal.
- Tested local peer registry with multiple nodes.

### Files Created
- discovery/peer_discovery.py
- discovery/__init__.py

### Outcome
Implemented the initial peer management
foundation for MeshWeaver.

### Next Step
Implement automatic peer discovery and
Kademlia-based distributed lookup.


## Day 7 – Kademlia DHT Fundamentals

### Tasks Completed
- Studied the fundamentals of Kademlia DHT.
- Implemented unique 160-bit node ID generation.
- Implemented XOR distance calculation.
- Developed closest peer selection.
- Tested node ID generation and distance calculation.

### Files Created
- discovery/kademlia_utils.py

### Outcome
Implemented the basic mathematical
foundation required for Kademlia-based
peer discovery.

### Next Step
Implement system resource monitoring using Python's psutil library to track CPU and RAM usage of MeshWeaver nodes.

## Day 8 – System Resource Monitoring

### Tasks Completed
- Explored system resource monitoring using Python.
- Installed and utilized the psutil library.
- Implemented CPU usage monitoring.
- Implemented RAM usage monitoring.
- Retrieved total, used, and available memory information.
- Developed functions to collect system resource information.
- Tested the resource monitoring module.

### Files Created
- monitoring/resource_monitor.py

### Outcome
Implemented a basic system resource monitoring module capable of collecting CPU and RAM usage information for MeshWeaver nodes.

### Next Step
Implement Kademlia routing tables, K-buckets, and peer lookup functionality.

## Day 9 – Kademlia Routing and Peer Lookup

### Tasks Completed
- Studied Kademlia routing table architecture.
- Implemented K-bucket data structures.
- Developed peer addition and removal functionality.
- Implemented XOR-based bucket selection.
- Developed closest peer lookup functionality.
- Tested routing table operations with multiple peer IDs.

### Files Created
- discovery/routing_table.py
- discovery/test_routing.py

### Outcome
Implemented a basic Kademlia routing table that organizes known peers into K-buckets and identifies the closest peers using XOR distance.

### Next Step
Implement the Gossip protocol for sharing system resource information between MeshWeaver nodes.
