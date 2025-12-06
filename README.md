# SecureLog
SecureLog is a real-time network monitoring and secure logging system that integrates Intrusion Detection, AES encryption, and Blockchain-based immutable storage.

## 1. Intrusion Detection (IDS):
Using Python’s Scapy, the system captures live network traffic and detects suspicious activities including port scanning, repeated failed logins, SYN flood patterns, and abnormal traffic spikes. Each alert includes a timestamp, IP information, attack type, and severity.

## 2. AES Encryption Layer
Detected events are encrypted using AES-256 (CBC mode) to ensure confidentiality. A small visual comparison of AES modes (ECB vs CBC vs CTR) is included to demonstrate why CBC/CTR are more secure.

## 3. Blockchain Log Storage
Each encrypted alert becomes a block containing encrypted data, timestamp, previous hash, SHA-256 hash, and a nonce. This ensures logs are tamper evident—any modification breaks the chain and is immediately detectable.
