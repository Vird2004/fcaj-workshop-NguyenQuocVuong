---
title: "Event 2"
date: 2026-06-06
weight: 2
chapter: false
pre: " <b> 4.2. </b> "
---

# Summary Report: "Meeting 06/6"

### Event Objectives

- Explore in-depth cloud technologies and solutions (Docker, AWS WAF, WebSocket, GraphRAG).
- Learn from real-world experience about career development paths in the IT industry.
- Strengthen teamwork skills and system security awareness.

### Speakers

- **Bao Huynh** – Docker – A containerization technology
- **Le Hoang Gia Dai** – Combining AWS WAF with Machine Learning for Cyber Attack Detection
- **Nguyen Quoc Bao** – Multiplayer in the Cloud: Connecting Godot Clients with AWS WebSockets
- **Truong Huy Phuoc** – The art of effective teamwork
- **Tran Trung Vinh** – From IT Helpdesk to Senior Sysadmin
- **Viet Phat** – Build GraphRAG applications using Amazon Bedrock and Amazon Neptune

### Key Highlights

#### Docker – A containerization technology

- The difference between virtualization and containerization: containers are lighter, use fewer resources, and start faster than virtual machines (VMs).
- Benefits of Docker: runs consistently across environments, is easy to move, and is ideal for microservices architecture.
- Docker architecture: how Docker Images and Containers work, and the process of building an Image from a Dockerfile using basic commands.
- Real-world applications: CI/CD, cloud-native application development, and modernizing legacy systems.

#### Combining AWS WAF with Machine Learning for Cyber Attack Detection

- Limitations of traditional WAF: relies on predefined rules, making it hard to detect zero-day attacks or new abnormal behavior.
- A combined WAF + Machine Learning solution (NIDS): the system automatically learns from network data to detect new attack patterns without needing predefined rules.
- Model training process: using the CSE-CIC-IDS2018 dataset, processing data, balancing labels, and training with the LightGBM model.
- Real-world deployment: an AWS system architecture combining ALB, WAF, S3, Kinesis, Lambda, and a real-time monitoring dashboard.

#### Multiplayer in the Cloud: Connecting Godot Clients with AWS WebSockets

- Comparing network architectures for games: UDP (fast but complex), WebSocket (suitable for turn-based games, low latency, reliable), HTTP Polling (simple but high latency).
- AWS solution architecture: using API Gateway (WebSocket), Lambda Functions, and DynamoDB to manage player connections and state.
- Godot client integration: how to handle the `$connect`, `$disconnect`, and `$default` events to exchange JSON data in real time.
- Lessons learned: handling "dead" connections (GoneException), the cost of scanning DynamoDB tables (scan cost), and Lambda's stateless nature.

#### The art of effective teamwork

- Rule 1: Have clear and shared goals.
- Rule 2: Put the right person in the right place.
- Rule 3: Open communication and active listening.
- Rule 4: Personal accountability.
- Supporting tools: Trello, ClickUp, Google Workspace, Slack, Discord.

#### From IT Helpdesk to Senior Sysadmin

- The role of IT Helpdesk: builds the ability to troubleshoot under pressure, problem-solving mindset, and communication with users.
- The work of a System Admin: managing server infrastructure, security, patching, and system monitoring. Never "test in production."
- Moving toward Cloud/DevOps: cloud mindset (AWS, elastic scaling), Infrastructure as Code (Terraform), and DevOps culture (CI/CD, Docker, automation).
- Core lessons: focus deeply on 1-2 core skills, building real projects matters more than just collecting certificates, and don't be afraid to fail.

#### Build GraphRAG applications using Amazon Bedrock and Amazon Neptune

- The concept of RAG: enhancing an LLM by retrieving information from an external knowledge base.
- What GraphRAG is: using a knowledge graph to perform multi-hop reasoning and clearly identify relationships between entities.
- The fully-managed path: using Amazon Bedrock Knowledge Bases and Amazon Neptune Analytics to extract entities, generate embeddings, and store the graph.
- The custom path: using LlamaIndex together with Neptune to prepare data, build a knowledge graph, and run Cypher queries.

### Event Experience

Attending the "Meeting 06/6" event broadened my perspective on applying advanced cloud technologies in practice:

- **In-depth technical knowledge:** I learned how to combine Machine Learning with AWS WAF for automated security, how to build multiplayer games using WebSocket on AWS, and the clear differences between Docker and traditional virtual machines.
- **Keeping up with AI trends:** I understood the power of GraphRAG in enhancing AI's analysis and response capabilities through Amazon Bedrock and Neptune.
- **Career direction:** The journey from Helpdesk to Senior Sysadmin was truly inspiring, helping me realize the importance of building capability through real-world projects.
- **Soft skills:** The principles of effective teamwork are essential tools for complex technology projects.

![Picture meeting 13/06](./images/4-Event/meeting13-06.png)