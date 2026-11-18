# MeshWeaver – System Architecture

## 1. Overview
MeshWeaver follows a modular distributed computing architecture in which multiple Python nodes communicate and cooperate over a network.

Each node can participate in communication, peer discovery, resource monitoring, and remote task execution.

## 2. Main Architectural Components

### 2.1 Networking Module
Responsible for communication between nodes.

Technologies:
- TCP sockets
- Python asyncio

### 2.2 Task Management Module
Responsible for transferring and executing Python tasks remotely.

Technologies:
- Cloudpickle
- Python execution logic

### 2.3 Peer Discovery Module
Responsible for identifying and discovering other nodes in the distributed network.

Technology:
- Kademlia Distributed Hash Table (DHT)

### 2.4 Resource Monitoring Module
Responsible for collecting system resource information.

Monitored resources:
- CPU utilization
- RAM utilization

Technology:
- Psutil

### 2.5 Gossip Protocol
Responsible for distributing resource information between participating nodes through periodic communication.

## 3. Basic Workflow

1. A node starts and initializes its identity.
2. The node joins the distributed network.
3. Peer discovery helps locate other nodes.
4. Nodes communicate using the networking module.
5. CPU and RAM information is collected.
6. The gossip protocol shares resource information.
7. A node can send a task to another node for remote execution.
8. The receiving node executes the task and returns the result.

## 4. Proposed Project Modules

- networking/
- tasks/
- discovery/
- monitoring/
- tests/

## 5. Development Approach

The implementation will be completed incrementally, beginning with basic communication and progressing toward peer discovery, resource sharing, and integrated remote task execution.

**Note:** This document describes the initial proposed architecture. Implementation details may be refined during development.
