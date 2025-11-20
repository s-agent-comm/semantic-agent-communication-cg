# Semantic Agent Communication: Security & Attestation

**W3C Community Group Report**

## Abstract

This specification defines the security model for the Semantic Agent Communication standard. It details the minimal threat model, the use of Verifiable Credentials for capability and delegation, and the binding of agent identities to hardware roots of trust.

## 1. Introduction

Security in agent communication goes beyond transport encryption. It requires verifiable proof of *who* is acting, *what* authority they have, and *where* their code is executing.

## 2. Threat Model

We identify the following critical threat categories:

*   **Semantic Misalignment:** Agents interpreting data differently.
*   **Intent Ambiguity:** Unclear or conflicting goals.
*   **Capability Misrepresentation:** Agents lying about what they can do.
*   **Identity & Delegation Spoofing:** Unauthorized agents acting on behalf of others.
*   **Resource Exhaustion:** Denial of service via expensive semantic tasks.

## 3. Identity and Trust

### 3.1 Decentralized Identifiers (DIDs)
All agents MUST be identified by a W3C DID. This provides a cryptographically verifiable root of identity independent of any central registry.

### 3.2 Verifiable Credentials (VCs)
VCs are the primary mechanism for establishing trust.

*   **Capability VCs:** Issued by authoritative bodies to prove an agent's skills (e.g., "Licensed Accountant").
*   **Delegation VCs:** A delegation act is itself a VC, where the issuer is the delegator and the subject is the delegatee.

## 4. Hardware Attestation

To anchor digital trust in physical reality, agents MAY provide hardware attestation reports.

### 4.1 Security Binding
An agent's DID can be bound to a specific hardware environment (TEE, TPM).

*   **Attestation Report:** A signed document from the hardware manufacturer (e.g., Intel SGX Quote, ARM PSA Token) proving the integrity of the hardware and the running code.
*   **Binding Mechanism:** The key used to control the DID is generated inside the TEE and never leaves it.

## 5. Mitigation Strategies

1.  **Signature Requirement:** All `CommunicativeAct`s MUST be signed by the agent's DID key.
2.  **Chain Validation:** Receivers MUST validate the entire delegation chain back to the root authority.
3.  **Resource Limits:** Execution contexts MUST define explicit resource constraints (gas, tokens, time).
