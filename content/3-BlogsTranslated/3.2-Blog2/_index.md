---
title: "Blog 2"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 3.2. </b> "
---

# How Cara Pioneers Domain-Specific AI for Enterprise Insurance Brokerages with AWS

Insurance is an $8 trillion global industry burdened by manual processes and a growing talent shortage. Cara delivers an AI-native solution on AWS that automates back-office workflows for insurance brokerages.

Insurance agents routinely spend hours on repetitive tasks: completing applications, analyzing coverage, re-entering data across multiple systems, and relaying information between clients and carriers. As the industry faces a persistent talent shortage, brokerages need to grow revenue without growing headcount at the same rate.

In this post, we explore how Cara, built in collaboration with AWS, addresses these challenges. We walk through the technical design decisions and the AWS services powering the solution, and share measurable results Cara has delivered for enterprise brokerages.

---

## The Challenge: Why General-Purpose AI Falls Short in Insurance

Insurance brokerages operate in a heavily regulated environment. Every transaction demands accuracy, auditability, and regulatory compliance. The data involved includes sensitive personally identifiable information (PII), financial records, and underwriting details.

General-purpose AI tools weren't built for this complexity. Effective AI in insurance must understand domain-specific data models and broker workflows. It also has to handle carrier-specific requirements and regulatory constraints, all while meeting enterprise security standards.

Cara's founding team saw these gaps firsthand. Vic Yeh, Nikhil Kansal, and Jon Patel previously founded a digital insurance brokerage. They grew and sold the company to The McGowan Companies, one of the largest privately held insurance organizations in the US.

Along the way, the team built an internal AI copilot powered by large language models (LLMs). The copilot reduced processing time, improved data accuracy, and streamlined agent workflows. Encouraged by the high adoption rate, they expanded the concept into a standalone product: Cara.

---

## Architecture Overview

Cara is built on AWS services chosen for their reliability, scalability, and security.

### Compute and Orchestration

Cara runs on Amazon Elastic Kubernetes Service (Amazon EKS) to orchestrate containers across multiple Availability Zones. EKS manages Cara's microservices, including the ingestion pipeline, workflow engine, and inference layer.

This architecture supports elastic scaling to handle demand during peak renewal and servicing periods. It supports thousands of concurrent users and workflows per brokerage. Each organization's workloads run in separate namespaces for tenant isolation.

### AI and Inference

Cara's AI capabilities are powered by LLMs hosted on Amazon Bedrock. Amazon Bedrock provides access to foundation models through a fully managed API. This lets Cara run inference without managing GPU infrastructure. Cara uses Amazon Bedrock for several core capabilities:

- **Coverage and quote intelligence** – comparing carrier quotes, summarizing coverage differences, and highlighting exclusions or gaps.
- **Application and form automation** – cross-filling ACORD forms and supplemental applications using source documents, prior applications, and agent instructions.
- **Proposal and renewal generation** – producing client-ready branded proposals and renewal spreadsheets.
- **Knowledge-based workflows** – referencing agency-specific guidelines, carrier risk appetite, and transaction history to guide decisions.

### Security and Data Isolation

Data protection is a foundational requirement for insurance organizations. Cara's architecture uses per-account deployment on AWS. Each brokerage's data and workflows are isolated in dedicated, secure workspaces. This design supports compliance with industry regulations and provides organization-level auditability.

### Integrations

Cara integrates with leading agency management systems (AMS) and customer relationship management (CRM) tools. It syncs accounts, policies, and documents to reduce duplicate data entry. AI-driven workflows operate directly within existing brokerage technology stacks, minimizing changes to the systems agents already use.

---

## Deployment and Operational Characteristics

One of Cara's design goals is to deliver value quickly. Enterprise brokerages can be onboarded in hours and custom workflows deployed within days. Cara's deployment on EKS uses parameterized templates for each new tenant, provisioning dedicated namespaces, storage, and inference endpoints without manual setup.

In production, Cara's AWS infrastructure delivers:

- **High availability** – multi-AZ deployment on EKS with automatic failover.
- **Elastic scaling** – Kubernetes Horizontal Pod Autoscaler adjusts capacity to actual demand, supporting thousands of concurrent users during peak periods.
- **Enterprise security** – tenant-level data isolation, encryption at rest and in transit, and integration with AWS Identity and Access Management (AWS IAM).

---

## Measurable Results

Cara's AI-driven workflows have delivered quantifiable results for enterprise insurance brokerages:

| Metric | Result |
| --- | --- |
| Time saved per user | ~10 hours/week through process automation and contextual knowledge retrieval |
| Onboarding speed | Enterprise brokerages onboarded in hours; custom workflows live within days |
| Concurrent capacity | Thousands of concurrent users and workflows per brokerage |
| Adoption | Used by hundreds of leading agencies and insurance brokerages |

These results come from organization-specific process automation and contextual knowledge retrieval, powered by Cara's domain-specific AI and the scalable, secure infrastructure provided by AWS.

---

## Looking Ahead

The insurance industry is still in the early stages of AI adoption. As enterprise demand grows, Cara continues to expand its AI-driven workflows across sales, service, and operations.

"We're excited to keep pushing the boundaries of domain-specific AI in real-world insurance applications together with AWS," said Vic Yeh, CEO of Cara. "Our goal is to help insurance professionals get back to the core of the business: relationships."

---

## Conclusion

In this post, we showed how Cara built a domain-specific AI solution for insurance brokerages using Amazon EKS and Amazon Bedrock. This architecture provides tenant-isolated workspaces with elastic scalability, supporting thousands of concurrent users while meeting the security and compliance requirements of the insurance industry.

To learn more about building AI applications on AWS, visit the AWS Architecture Center. To get started with Amazon Bedrock, see Getting Started with Amazon Bedrock. For Amazon EKS, see Getting Started with Amazon EKS.

Source: <https://aws.amazon.com/blogs/machine-learning/how-cara-pioneers-domain-specific-ai-for-enterprise-insurance-brokerages-with-aws/>
