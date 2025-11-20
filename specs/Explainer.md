# Explainer: Semantic Agent Communication

**This is a proposal for a W3C Community Group Report.**

## Abstract

This document proposes a standard for **Semantic Agent Communication**. It defines a shared vocabulary and protocol that enables AI agents to securely delegate tasks, exchange capabilities, and maintain a verifiable audit trail of their interactions, regardless of the underlying model or transport.

## 1. The User Need

### The Problem: Digital Islands
Today, AI agents are "digital islands".
*   **Alice** has a personal assistant agent.
*   **Bob** (a travel agency) has a booking agent.
*   **Charlie** (a bank) has a payment agent.

Currently, Alice's agent cannot easily talk to Bob's agent to book a flight, nor can it securely authorize Charlie's agent to pay for it. They lack a shared language for:
1.  **Identity:** "Who are you?"
2.  **Capability:** "What can you do?"
3.  **Delegation:** "I authorize you to do this on my behalf."

### The Goal
We want to enable a world where Alice can say to her agent: **"Book me a flight to Tokyo for under $1000"**, and her agent can:
1.  **Discover** Bob's airline agent.
2.  **Verify** Bob is a legitimate travel agent.
3.  **Delegate** the task to Bob.
4.  **Authorize** payment only if the flight is successfully booked.
5.  **Record** the entire transaction for Alice to review later.

## 2. The Proposal

We propose a **Semantic Agent Communication Standard** consisting of three parts:

1.  **Core Ontology:** A shared vocabulary (RDF/OWL) for concepts like `Agent`, `Intent`, `Delegation`, and `ExecutionRecord`.
2.  **Unified Narrative:** A model where all interactions are recorded in an immutable, append-only log (the "Narrative"), providing a complete audit trail.
3.  **Security Binding:** Using W3C DIDs and Verifiable Credentials to anchor agent identity and authority to hardware roots of trust (TEEs).

### Example: The "Book Flight" Flow

Here is how the proposal changes the interaction. Instead of opaque API calls, agents exchange **Communicative Acts**.

**1. Alice's Agent sends an Intent:**
```json
{
  "@type": "sac:Intent",
  "actor": "did:example:alice-agent",
  "goal": "Book flight to Tokyo",
  "constraints": { "maxPrice": "1000 USD" }
}
```

**2. Alice's Agent Delegates Authority to Bob:**
```json
{
  "@type": "sac:Delegation",
  "delegator": "did:example:alice-agent",
  "delegatee": "did:example:bob-travel",
  "scope": "sac:FlightBookingCapability",
  "signature": "..."
}
```

**3. Bob's Agent Executes and Reports:**
```json
{
  "@type": "sac:ExecutionRecord",
  "actor": "did:example:bob-travel",
  "authorizedBy": "link-to-delegation-above",
  "result": { "flightId": "JL123", "status": "Confirmed" }
}
```

## 3. Key Concepts

### 3.1 Identity (W3C DIDs)
Every agent has a **Decentralized Identifier (DID)**. This allows agents to sign every message, proving origin and integrity without a central server.

### 3.2 Capabilities as Verifiable Credentials
How does Alice know Bob is a *real* travel agent? Bob presents a **Verifiable Credential** issued by a trusted authority (e.g., IATA), proving he has the `FlightBookingCapability`.

### 3.3 The Unified Narrative
All messages are appended to a shared log called the **Narrative**.
*   **Traceability:** If something goes wrong, Alice can replay the Narrative to see exactly who agreed to what.
*   **Explainability:** The Narrative serves as the "reasoning chain" for *why* an action was taken.

## 4. Alternatives Considered

### Why not just use HTTP APIs (OpenAPI)?
*   **Pros:** Mature, widely used.
*   **Cons:** APIs define *syntax* (endpoints), not *semantics* (meaning). They don't natively handle delegation ("I authorize you to use my auth token for this specific task") or long-running audit trails.

### Why not just use LLM Prompts (English)?
*   **Pros:** Flexible, easy for LLMs.
*   **Cons:** Ambiguous and unverifiable. "Book a flight" in English is not a contract. You cannot cryptographically sign a prompt's *intent* in a way that guarantees execution limits (e.g., "spend max $100").

## 5. FAQ

**Q: Does this replace LangChain or Semantic Kernel?**
No. This is a **protocol** that those frameworks can *speak*. It allows a LangChain agent to talk to a Semantic Kernel agent.

**Q: Is this a blockchain?**
No. The "Narrative" is a logical log. It *can* be stored on a blockchain for high security, but it can also be a simple JSON file or a database.

**Q: How do I start?**
See our [Architecture Document](./architecture.md) and [Core Ontology](./core-ontology.md).
