# Semantic Delegation & Agent Communication Community Group

## Draft Charter v0.1

---

### 1. Motivation

Current multi-agent systems rely heavily on model-dependent patterns and lack a minimal, interoperable interface for intent exchange, semantic delegation, and responsibility boundaries.

The goal of this Community Group is to define a cross-model, cross-runtime, cross-platform **Semantic Delegation Interface** that enables verifiable communication between agents, humans, and mixed systems. This group focuses on the smallest universally adoptable layer.

### 2. Scope

The Community Group will define and maintain the following:

#### 2.1 Agent Intent Primitives
A minimal vocabulary describing fundamental communicative acts:
- `lookup`
- `act`
- `ask`
- `delegate`
- `ack`
- `report`
- `handover`

#### 2.2 Semantic Delegation Model
Structures describing:
- Task boundaries
- Authority delegation
- Responsibility chain
- Rights to further delegate
- Constraints and conditions

#### 2.3 Unified Narrative Primitives
A minimal vocabulary for an immutable, append-only, ordered log of `CommunicativeAct`s, forming a coherent `Narrative`:
- `Narrative-ID` (for context boundary)
- `CommunicativeAct` types (e.g., `Intent`, `Delegate`, `Execute`, `Query`, `Report`, `Accept`, `Reject`)
- Verifiable audit information (signed, timestamped acts)

#### 2.4 Communicative Act Schema
A runtime-agnostic schema defining the structure of `CommunicativeAct`s within a `Narrative`:
- Agent-to-agent communication
- Human-to-agent interface
- Multi-model interoperability

**Note:** This group focuses exclusively on the **semantic payload** of a communication. It does not define transport protocols (e.g., TCP/IP, HTTP), agent implementation details (e.g., LLMs, internal reasoning models), or specific A2A communication patterns. The defined ontology represents the "content of the message," not the "envelope" or the "delivery mechanism."

#### 2.5 Safety Signaling
Minimal runtime safety signals such as:
- `busy`
- `idle`
- `blocked`
- `handover-needed`
- `unsafe-to-proceed`

These enable predictable and responsible behavior across heterogeneous systems.

### 3. Out of Scope

The following topics are important but are **not** included in the initial scope. They may be added in later versions but are excluded from v1.0 specifications:
- Cultural language behavior (politeness, tone, socio-pragmatics)
- SemanticEnergy (semantic resource metric)
- Narrative memory lifecycle (short-term, long-term, meta-cognition)
- Agent inner communication ontology
- Agent self-reflection mechanisms
- Agent emotional signaling
- Full reasoning frameworks
- Application-specific UI or implementation details
- Model architecture constraints

These areas are implementation-dependent and should remain flexible for regional or platform-specific ecosystems.

### 4. Deliverables

The Community Group intends to publish:

1.  **Semantic Delegation Ontology v1.0:** Published in Turtle and JSON-LD.
2.  **Communicative Act Schema:** A model-neutral minimal schema describing `CommunicativeAct`s within a `Narrative`, intent, delegation, and safety.
3.  **Safety & Responsibility Notes:** A set of implementation and governance notes for traceability, responsibility boundaries, and safe delegation patterns.
4.  **Interoperability Best Practices:** Guidelines for how agent runtimes, OS-level systems, and model providers can adopt the minimum schema.

### 5. Dependencies

This Community Group intentionally aligns with, but does not replace, work in the following areas:
- **W3C DID / Verifiable Credentials**: Leverages Decentralized Identifiers (DIDs) for agent identity and Verifiable Credentials (VCs) for creating verifiable delegation chains. An agent's identity and relationships are represented as entities within its knowledge management graph.
- RDF, RDFS, OWL, JSON-LD
- W3C Conversational Interfaces discussions
- Agent MCP (Model Context Protocol)
- A2A protocols (agent-to-agent protocols)
- ETH 8004 Resource Model (hardware/software resources)

This group focuses on the semantic layer above these systems. For example, while ETH 8004 describes OS resources, this group describes semantic resources and delegation semantics.

### 6. Participation

Relevant participants include:
- Developers of agent frameworks
- Semantic Web / Knowledge Representation (KR) researchers
- Cognitive AI and Level of Abstraction (LoA) scholars
- Human-computer interaction researchers
- AI governance and AI Act technical documentation teams
- Multi-agent simulation researchers
- OS-level semantic architecture engineers

Participation is open to all individuals and organizations.