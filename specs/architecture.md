# Semantic Agent Communication: Architecture & Requirements

**W3C Community Group Report**

## Abstract

This document outlines the high-level architecture, requirements, and use cases for the Semantic Agent Communication standard. It defines the problem of "digital islands" in the AI agent ecosystem and proposes a solution based on a shared, machine-readable ontology for identity, capability, delegation, and accountability.

## 1. Introduction

In the rapidly growing world of AI, we are seeing an explosion of powerful, specialized AI agents. However, these agents often exist as "digital islands"—they cannot communicate, collaborate, or trust each other in a standardized way.

This specification defines a shared, open, and machine-readable "language" for AI agents, built on the principles of the World Wide Web and the Semantic Web.

### 1.1 Vision and Goals

Our vision is to create a universal standard for safe and effective semantic communication among AI agents.

**Key Goals:**
*   **Interoperability:** Define a shared vocabulary for cross-agent understanding.
*   **Protocol-Agnostic:** Focus on the semantic payload, independent of transport (HTTP, WebSockets, etc.).
*   **Security:** Anchor digital trust in physical reality via hardware roots of trust.
*   **Verifiability:** Create a complete, auditable chain of responsibility.
*   **Extensibility:** Provide a modular core for diverse applications.

## 2. Scope

### 2.1 In Scope

This Community Group focuses on the semantic structures for verifiable agent interaction:

1.  **Interaction Semantics:** Formal definitions for Intent, Delegation, Capability, and ExecutionRecord.
2.  **Identity & Verifiability:** Use of DIDs and Verifiable Credentials.
3.  **Narrative Model:** An append-only, context-complete semantic log.
4.  **Conformance:** Minimal requirements for interpreting CommunicativeActs.
5.  **AgentIDL:** An Interface Description Language for code generation.

### 2.2 Out of Scope

*   **Transport Protocols:** We do not define HTTP, TCP, etc.
*   **Internal Reasoning:** We do not define how LLMs think or plan.
*   **Execution Backends:** We do not specify CPU/GPU execution details.
*   **Economic Models:** We do not standardize payment rails or token models.

## 3. Architecture

### 3.1 The Unified Narrative

The core architectural concept is the **Unified Narrative**: an immutable, append-only, ordered log of **CommunicativeActs**.

*   **Emergent State:** System state is derived by replaying the log.
*   **Traceability:** Provides a complete audit trail for all actions.
*   **Lazy Consensus:** Conflicts are recorded, not prevented; interpretation is left to the observer.

### 3.2 Levels of Abstraction (LoA)

The architecture is layered to manage complexity:

*   **LoA 0: Mathematical Bedrock** (Logic of Possibility)
*   **LoA 1: Cryptographic Anchor** (DIDs, VCs - Verifiable Reality)
*   **LoA 2: Governance Framework** (Ontology + SHACL - Enforceable Order)
*   **LoA 3: Information Economy** (Valuation and Exchange)
*   **LoA 4: Economic Organization** (Firms and Delegation Chains)
*   **LoA 5: Sociological Structure** (Complex Collaboration)
*   **LoA 6: Semantic Interface** (Communicative Acts - The Language of Meaning)

## 4. Conformance

An implementation conforms to this specification if it:
1.  Uses W3C DIDs for agent identity.
2.  Produces and consumes `CommunicativeAct`s defined in the Core Ontology.
3.  Adheres to the minimal security requirements (signatures on all acts).

## 5. Use Cases

*   **Delegated Task Execution:** A personal agent delegates a travel booking task to a specialized airline agent.
*   **Verifiable Audit Trails:** A regulatory body audits an agent's actions by replaying its Narrative.
*   **Capability Discovery:** An agent searches a semantic registry to find another agent with specific skills.
