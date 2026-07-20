---
title: "Blog 1"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 3.1. </b> "
---

# Building a Numerology System (LunaGENZ) on a Serverless AWS Architecture Combined with GenAI

Hi everyone, after a while of self-studying and grinding, our team has started our capstone project: LunaGENZ – a system that uses AI to generate personalized numerology readings.

I'm writing this post not to show off, but to record our architectural decision-making process along with the mistakes we ran into — hoping it's useful for anyone working on a similar project, and we'd really appreciate feedback from more experienced folks so the team can learn even more.

## 1. Why We Chose a Serverless Architecture

Our initial goal was to avoid managing servers ourselves, while keeping costs at a level appropriate for a student project without stable revenue. The team chose:

- Frontend: Next.js, deployed via AWS Amplify
- Backend: API Gateway + AWS Lambda
- Database: Amazon DynamoDB (On-demand mode)

The pay-per-actual-usage model keeps infrastructure costs very low during testing, which suits a product that doesn't have real users yet. This fits our team's specific situation at this stage — it's not a general conclusion for every project, since as traffic grows, serverless architectures come with their own cost trade-offs that we're still exploring.

## 2. The Timeout Problem and How We Solved It with Amazon SQS

Initially, the system called the AI to generate content and export a PDF within the same request. Since these steps took time, the system kept hitting timeout errors due to API Gateway's 29-second limit.

Our fix: decouple the processing flow using Amazon SQS. A user request only pushes a message onto the queue and returns a "processing" response. A separate background Lambda picks up the message, calls the AI, generates the PDF, and then sends it to the user's email via Amazon SES. This eliminated the timeouts and reduced the risk of data loss when errors occur.

## 3. Choosing the AI Model

The team uses Claude 3 Haiku via Amazon Bedrock instead of larger models. The reason is that our Vietnamese-text interpretation task doesn't require overly complex reasoning, so a smaller, faster, cheaper model was a more sensible choice than using the strongest model available.

## 4. Security and CI/CD

- The payment flow is split into a separate Webhook Handler, independent from the AI interpretation logic.
- Sensitive keys are stored in AWS Secrets Manager, never hardcoded in the code.
- The entire frontend and backend are automatically deployed via GitLab CI/CD. Errors and performance are monitored with CloudWatch.

## A Few Things We Learned

This is the first time our team has applied a fairly complete serverless architecture, so there are definitely things that aren't optimized yet — for example, error handling when the background Lambda fails, or how to control costs at real scale, are problems we haven't tested at large scale.

Since this is also our first time building a project that involves external parties, we've made plenty of mistakes along the way. We'd love for more experienced folks to share feedback so we can keep improving. Thank you all for taking the time to read this post.
