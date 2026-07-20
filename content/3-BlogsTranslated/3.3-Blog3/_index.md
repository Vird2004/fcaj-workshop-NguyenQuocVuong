---
title: "Blog 3"
date: 2024-01-01
weight: 3
chapter: false
pre: " <b> 3.3. </b> "
---

# Automating Oracle Database@AWS Provisioning with Terraform

When it comes to running high-performance Oracle Database workloads in the cloud, Oracle Database@AWS (ODB@AWS) is now one of the most powerful solutions available. This service brings Exadata — Oracle's most optimized database hardware platform — directly inside AWS data centers. As a result, the system achieves extremely low network latency and deep integration with native AWS services such as Amazon S3, AWS KMS, Amazon EC2, and Amazon EKS.

However, manually setting up a complex infrastructure spanning the ODB Network, Exadata Infrastructure, and the VM Cluster through the Console is time-consuming and carries a high risk of error. That's why Infrastructure as Code (IaC) — specifically Terraform — becomes a powerful tool for automating this entire process reliably.

In a recent post on the AWS Database Blog, authors Javeed Mohammed and Sharath Chandra Kampili walked through how to implement this solution in detail. The summary below covers the core points and the code-based deployment workflow.

---

## 1. Why Choose Terraform (IaC) for Oracle Database@AWS?

Defining infrastructure as code (HCL) delivers significant benefits for organizations:

- **End-to-end automation**: Eliminates manual clicking entirely, cutting the provisioning time for large systems from hours down to just minutes.
- **Environment consistency**: Ensures configuration across Development, Staging, and Production environments stays fully aligned, eliminating configuration drift.
- **Version control**: Infrastructure code can easily be stored in Git to track change history, run code reviews, and roll back quickly when incidents occur.

---

## 2. Core Architecture of Oracle Database@AWS

To deploy with Terraform, you need a clear understanding of the main architectural components that will be provisioned:

- **ODB Network**: A dedicated network infrastructure that creates a secure, high-speed private connection between AWS and Oracle Cloud Infrastructure (OCI).
- **Oracle Exadata Infrastructure**: The physical Exadata hardware system, placed directly within AWS Availability Zones (AZs).
- **Exadata VM Cluster / Autonomous VM Cluster**: A distributed virtual machine cluster running on the Exadata infrastructure, where your Oracle database actually runs.
- **ODB Peering Connection**: A private peering connection that links the VPC containing your applications (EC2, EKS, etc.) directly to the ODB Network for data access with minimal latency.

---

## 3. Prerequisites Before Deployment

For the Terraform code to run smoothly, make sure you complete the following preparation steps:

- **Onboarding process**: Contact Oracle to receive a Private Offer for the ODB@AWS service through AWS Marketplace.
- **Account linking**: Successfully link your AWS Account with your Oracle resource tenancy (OCI Tenancy).
- **Provider configuration**: Fully configure authentication credentials for both the AWS Provider and the OCI Provider in your Terraform code so it has permission to manage resources on both platforms.

---

## 4. Deployment Workflow with Terraform (Step Summary)

The infrastructure is provisioned automatically in the correct dependency order through dedicated resource blocks:

**Step 1: Create the ODB Network**

Create a secure network segment connecting AWS and OCI:

```terraform
resource "aws_oracle_odb_network" "example" {
  # Configure the CIDR block and the corresponding Availability Zone
}
```

**Step 2: Deploy the Exadata Infrastructure**

Configure the dedicated Exadata hardware located inside the AWS data center:

```terraform
resource "aws_oracle_odb_cloud_exadata_infrastructure" "example" {
  # Define the hardware size and link it to the ODB Network just created
}
```

**Step 3: Create the Exadata VM Cluster**

Create the virtualization environment to prepare the database configuration:

```terraform
resource "aws_oracle_odb_cloud_vm_cluster" "example" {
  # Configure the number of CPU cores, memory size, and Grid Infrastructure
}
```

**Step 4: Set Up the ODB Peering Connection**

Open a private connection so applications in your AWS VPC can access the database directly:

```terraform
resource "aws_oracle_odb_peering_connection" "example" {
  # Connect the VPC hosting your application to the ODB infrastructure just set up
}
```

---

## 5. Who This Solution Is For

- **Database Administrators (DBAs)**: Data professionals looking to modernize their skill set, moving from manual operations to modern infrastructure management practices.
- **DevOps / Cloud Engineers**: Those responsible for automating CI/CD pipelines for infrastructure, who want to manage Oracle Database the same way as any other cloud resource.
- **Enterprises**: Organizations with a roadmap to migrate core Oracle workloads from on-premises to AWS while still requiring the peak performance of Exadata.

---

## Conclusion

Using Terraform to provision Oracle Database@AWS not only speeds up project delivery but also optimizes operational costs and minimizes the risk of human configuration errors. It's a strategic, professional step for any organization looking to fully harness the computing power of Oracle Exadata together with the flexibility of the AWS cloud ecosystem.

Source: AWS Database Blog - Provision Oracle Database@AWS resources using Terraform.
