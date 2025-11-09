# Semantic Agent Communication Community Group  
*W3C Community Group — Draft Repository Overview*

## 1. Scope and Purpose

The **Semantic Agent Communication Community Group (SAC-CG)** aims to define a shared, interoperable semantic model for communication between AI Agents across different systems, vendors, and jurisdictions.  
This includes foundational ontology layers for **identity binding**, **capability description**, **delegation structures**, **intent semantics**, and **verifiable execution records** supporting secure and auditable agent-to-agent interaction.

The ontology developed here is abstracted from operational cross-border systems to ensure practical applicability and technical feasibility.  
The long-term objective is alignment with frameworks such as the **EU AI Act**, **EUDI Wallet**, **EU Business Wallet**, **Data Act**, and future **ISO/IEC** tracks for AI interoperability.

---

## 2. Repository Structure

This repository is organized to support the technical work of the Community Group:

### **2.1 `ontologies/` — Core Semantic Definitions**
- `.ttl` ontology files defining Agents, capabilities, identity, delegation, ledger semantics.  
- `context/`: JSON-LD contexts mapping JSON payloads to ontology definitions.  
- `profiles/`: JSON Schemas for API-level validation.  
- `examples/`: Concrete samples illustrating ontology usage.

### **2.2 `specs/` — Human-Readable Specifications**
Documents explaining design considerations, conceptual models, and intended usage.

### **2.3 `discussions/` — Community Collaboration**
Meeting notes, proposals, design discussions, and alternative approaches.

### **2.4 `tests/` — Consistency and Conformance**
Validation resources (e.g., SHACL) ensuring logical correctness and interoperability.

---

## 3. Reference Implementation

The ontology is informed by and validated against a real operational environment:  
**AI Workforce OS**, an agent-native runtime designed for cross-border operational use cases.

The CG encourages additional independent implementations.  
The ontology is intended to be generic and not tied to any single runtime.

---

## 4. Goals of the Community Group

The CG seeks to develop:

- A unified semantic model for Agent **identity**, **capabilities**, **delegation**, and **intent**.  
- Machine-interpretable structures enabling **verifiable execution**, **traceability**, and **auditability**.  
- Interoperable building blocks across **multi-vendor**, **multi-jurisdiction**, and **cross-layer** environments.  
- A clear path toward potential future W3C Notes and downstream **ISO/IEC** standardization.

---

## 5. Participation

The Community Group is open to all.

To join, visit:  
**https://www.w3.org/community/semantic-agent-communication/**  
(*Activation pending 5 supporters.*)

---

## 6. License

Ontology files and specifications will follow open licenses (e.g., W3C Software and Document License) to support broad adoption and interoperability.

