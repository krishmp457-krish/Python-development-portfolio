# MeshWeaver

## Distributed Computing System

### Project Overview
MeshWeaver is a Python-based distributed computing project designed to enable multiple nodes to communicate, discover peers, share system resources, and execute tasks remotely.

The project aims to create a network where multiple Python nodes cooperate and utilize their computing resources efficiently.

### Objectives
- Establish communication between multiple Python nodes.
- Implement asynchronous networking.
- Enable remote Python task execution.
- Implement peer discovery using Kademlia DHT.
- Monitor CPU and RAM utilization.
- Share resource information using the Gossip Protocol.

### Main Components

| Component | Description |
|---|---|
| Networking | Handles communication between nodes using TCP sockets and asyncio. |
| Task Execution | Supports remote execution of Python functions. |
| Serialization | Uses cloudpickle to serialize Python functions. |
| Peer Discovery | Helps nodes discover other participating nodes. |
| Resource Monitoring | Collects CPU and RAM information using psutil. |
| Gossip Protocol | Shares resource information between nodes. |

### Technologies
- Python
- PyCharm
- Asyncio
- Socket Programming
- Cloudpickle
- Kademlia DHT
- Psutil
- Git and GitHub

### Project Structure
The project is organized into separate modules for networking, task execution, peer discovery, and resource monitoring.

### Development Timeline
The project is planned to be developed over a 10-day sprint, covering the original two-week development scope.

### Expected Outcome
A working distributed computing prototype capable of node communication, peer discovery, resource monitoring, resource sharing, and remote task execution.

### Project Status
Initial planning and architecture design.
