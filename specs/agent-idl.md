# Semantic Agent Communication: AgentIDL

**W3C Community Group Report**

## Abstract

This specification defines AgentIDL, an Interface Description Language for AI Agents. It extends WebIDL to support semantic annotations, enabling the automatic generation of type-safe, semantically-aware client libraries and agent skeletons.

## 1. Introduction

AgentIDL bridges the gap between the abstract Core Ontology and concrete software implementation. It allows developers to define agent capabilities in a familiar, strongly-typed syntax, which can then be compiled into code (e.g., TypeScript, Python) and semantic definitions (RDF/SHACL).

## 2. Syntax

AgentIDL is a superset of WebIDL. It adds the following features:

### 2.1 Semantic Annotations
Methods and interfaces can be annotated with URIs from the Core Ontology to bind them to semantic concepts.

```webidl
[Semantic="sac:Capability"]
interface FlightBooking {
  [Semantic="sac:Intent", Goal="Book a flight"]
  Promise<Ticket> bookFlight(FlightRequest request);
};
```

### 2.2 Agent-Specific Types
*   `Agent`: Represents a DID-identified agent.
*   `Delegation`: Represents a verifiable delegation chain.
*   `Proof`: Represents a cryptographic signature.

## 3. Mapping to Core Ontology

The AgentIDL compiler MUST produce an RDF representation of the defined interfaces.

*   **Interface** -> `sac:Capability` subclass
*   **Method** -> `sac:Skill` or specific `sac:Intent`
*   **Argument** -> `sac:Parameter`

## 4. Code Generation Requirements

Conformant AgentIDL compilers MUST support:
1.  **Type Generation:** Generating native types for the target language.
2.  **Stub Generation:** Creating abstract base classes for agent implementation.
3.  **Client Generation:** Creating proxy clients that handle the serialization of `CommunicativeAct`s.

## 5. Example

```webidl
namespace travel {
  struct FlightRequest {
    DOMString from;
    DOMString to;
    Date date;
  };

  [Semantic="ex:TravelAgent"]
  interface TravelService {
    Promise<boolean> checkAvailability(FlightRequest req);
  };
}
```
