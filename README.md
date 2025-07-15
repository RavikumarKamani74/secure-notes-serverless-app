# 🛡️ Secure Serverless Notes App

A fully serverless, secure, and scalable notes application built on AWS. This project demonstrates how to implement full CRUD functionality with serverless components, integrated security controls, and real-time monitoring — ideal for Cloud Security and DevOps portfolios.

## 🚀 Features

- ✍️ Create, Read, Update, Delete (CRUD) notes
- ☁️ Hosted frontend on **Amazon S3 + CloudFront**
- ⚙️ Backend using **AWS Lambda + API Gateway**
- 💾 Serverless storage with **DynamoDB**
- 🔐 API secured via **CORS** and **IAM least privilege**
- 📊 Real-time monitoring with **CloudWatch Alarms**
- 💸 Cost control using **AWS Budgets + SNS Alerts**

-- live link - [d1nl1hlmql4m3x.cloudfront.net](url)
---

## 🛠️ Architecture

![Architecture Diagram](https://user-images.githubusercontent.com/placeholder/your-architecture-diagram.png) <!-- Optional: add an architecture image -->

| Layer         | AWS Service              |
|---------------|--------------------------|
| Frontend      | S3 + CloudFront          |
| Backend       | Lambda (Python)          |
| API Gateway   | REST API with routes     |
| Database      | DynamoDB (NoSQL)         |
| Alerts        | SNS Notifications        |
| Monitoring    | CloudWatch + Budgets     |

---

## 🧪 Tech Stack

- **AWS Lambda** (Python)
- **API Gateway**
- **DynamoDB**
- **S3**
- **CloudFront**
- **SNS**
- **CloudWatch**
- **IAM (Least Privilege)**
- **HTML + JavaScript**

---

## 📂 Project Structure
📁 secure-notes-app/
├── lambda/
│ └── lambda_function.py
├── static-site/
│ ├── index.html
└── README.md


---

## 📦 Deployment Steps

1. **Upload HTML frontend** to an S3 bucket
2. Configure **CloudFront distribution** with the S3 origin
3. Deploy **Lambda function** for handling CRUD
4. Set up **API Gateway** routes:
   - `/note` → `POST`, `GET`
   - `/note/{id}` → `PUT`, `DELETE`
5. Add **IAM Role** to Lambda with least privilege for DynamoDB and SNS
6. Configure **CloudWatch alarm** + **AWS Budget** with SNS notification
7. Test full stack via frontend or Postman

---

## 🔐 Security Best Practices Implemented

- IAM Role with **least privilege** for Lambda
- **No public access** to S3 bucket (CloudFront only)
- **CORS headers** on API Gateway
- Budget and usage monitoring via **AWS Budgets + SNS**
- API route structure uses **resource-based routing** (`/note/{id}`)

---


## 📬 SNS Notifications Demo

Budget thresholds or application alerts will send real-time emails via Amazon SNS. Example:
Subject: AWS Budget Notification
Body: Your usage exceeded 80% of your budget for this month.

