# Semantic Agent Communication: Protocol & Transport

**W3C Community Group Report**

## Abstract

This specification defines the serialization formats and transport bindings for the Semantic Agent Communication standard. It describes how `CommunicativeAct`s are encoded and transmitted over standard network protocols.

## 1. Introduction

This standard defines the **semantic payload** (the "what") of agent communication. It is designed to be transport-agnostic, meaning the same semantic message can be sent over HTTP, WebSockets, or even non-digital channels.

## 2. Serialization

### 2.1 JSON-LD (Normative)
All `CommunicativeAct`s MUST be serializable as valid JSON-LD documents. This ensures human readability and compatibility with Semantic Web tools.

```json
{
  "@context": "https://w3id.org/sac/v1",
  "type": "Intent",
  "actor": "did:example:alice",
  "goalDescription": "Book a flight to Tokyo"
}
```

### 2.2 CBOR-LD (Optional)
For bandwidth-constrained environments, implementations MAY support CBOR-LD (Concise Binary Object Representation for Linked Data).

## 3. Transport Bindings

### 3.1 HTTP Binding
*   **Method:** POST
*   **Content-Type:** `application/ld+json`
*   **Body:** The serialized `CommunicativeAct`.

### 3.2 WebSocket Binding
*   **Message Format:** Text (JSON-LD) or Binary (CBOR-LD).
*   **Pattern:** Asynchronous, bidirectional stream of acts.

## 4. Interaction Patterns

### 4.1 Request-Response (TCP-like)
For critical acts (e.g., `Delegation`), the sender expects an explicit `Accept` or `Reject` act in return.

### 4.2 Fire-and-Forget (UDP-like)
For informational acts (e.g., `Report` telemetry), the sender does not wait for acknowledgement.

## 5. The Semantic Payload
The payload is treated as an opaque blob by the transport layer. The receiving agent is responsible for parsing the JSON-LD, verifying the signature, and interpreting the semantics according to the Core Ontology.
