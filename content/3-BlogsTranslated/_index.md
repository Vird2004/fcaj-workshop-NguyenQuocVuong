---
title: "Translated Blogs"
date: 2024-01-01
weight: 3
chapter: false
pre: " <b> 3. </b> "
---

This section lists the blogs I researched and translated during the internship, covering serverless architecture, GenAI applications on AWS, and infrastructure automation:

###  [Blog 1 - Building a Numerology System (LunaGENZ) on a Serverless AWS Architecture Combined with GenAI](3.1-Blog1/)
This post recounts how the team built LunaGENZ – a system that uses AI to generate personalized numerology readings – on a serverless architecture (Next.js/Amplify, API Gateway, Lambda, DynamoDB). It covers why serverless was chosen to optimize cost, how AI-call timeouts were solved with Amazon SQS, why Claude 3 Haiku via Amazon Bedrock was chosen, and security (Secrets Manager) and CI/CD practices.

###  [Blog 2 - How Cara Pioneers Domain-Specific AI for Enterprise Insurance Brokerages with AWS](3.2-Blog2/)
This post introduces Cara, an AI-native solution on AWS that automates back-office workflows for insurance brokerages. It examines why general-purpose AI falls short in insurance, the architecture built on Amazon EKS (orchestration, tenant isolation) and Amazon Bedrock (AI inference), and the measurable results in time savings and customer onboarding speed.

###  [Blog 3 - Automating Oracle Database@AWS Provisioning with Terraform](3.3-Blog3/)
This post summarizes how to use Terraform (Infrastructure as Code) to automate the provisioning of Oracle Database@AWS (ODB@AWS), including the ODB Network, Exadata Infrastructure, VM Cluster, and ODB Peering Connection. It also outlines the prerequisites (Oracle onboarding, AWS-OCI account linking) and the benefits of IaC over manual Console setup.
