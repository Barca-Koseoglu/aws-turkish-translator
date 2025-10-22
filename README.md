# Serverless Translation API on AWS

This repository contains the code for a lightweight, scalable, and cost-effective translation microservice built entirely on AWS.

It provides a simple HTTP endpoint that accepts text and a target language code, and it returns the translated text.

## Core Functionality

-   **Endpoint:** Receives an HTTP POST request with a JSON payload.
-   **Input:** `{"text": "Hello world", "target_language_code": "es"}`
-   **Output:** `{"original_text": "Hello world", "translated_text": "Hola mundo", ...}`

## Architecture

This project uses a simple, serverless architecture:

1.  **Application Load Balancer (ALB):** Provides a public HTTP URL, handles incoming web traffic, and provides TLS termination.
2.  **AWS Lambda:** The ALB forwards requests to this function. The Python code (in `lambda_function.py`) parses the request, calls the Amazon Translate service, and formats the response.
3.  **Amazon Translate:** The underlying machine translation service that performs the translation.

**Flow:**
`Client Request (curl)` $\rightarrow$ `Application Load Balancer` $\rightarrow$ `AWS Lambda` $\rightarrow$ `Amazon Translate` $\rightarrow$ `Client Response`

## Key Benefits

-   **Serverless:** No servers to manage. AWS Lambda scales automatically.
-   **Cost-Effective:** You only pay for the Lambda execution time and the number of characters translated.
-   **Scalable:** The architecture can handle thousands of requests without manual intervention.

## How to Deploy

1.  **IAM Role:** Create an AWS IAM Role for Lambda with the `TranslateFullAccess` policy.
2.  **Lambda Function:** Create an AWS Lambda function, attach the IAM role, and paste the code from `lambda_function.py`.
3.  **Application Load Balancer (ALB):**
    -   Create a Target Group with the "Lambda function" target type, pointing to your new function.
    -   Create an Application Load Balancer (Internet-facing) with an HTTP listener on port 80.
    -   Configure the listener's default action to forward traffic to your Lambda target group.
