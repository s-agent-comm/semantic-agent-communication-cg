# Semantic Agent Communication: Core Ontology

**W3C Community Group Report**

## Abstract

This specification defines the Core Ontology for the Semantic Agent Communication standard. It provides the normative RDF/OWL vocabulary for Agents, Capabilities, Delegations, and the Unified Narrative model.

## 1. Introduction

The Core Ontology establishes the foundational classes and properties that enable interoperable agent communication. It focuses on **interaction semantics** rather than general knowledge representation.

**Namespace:** `https://w3id.org/sac/core#`
**Prefix:** `sac`

## 2. Core Classes

### 2.1 Agent
*   **URI:** `sac:Agent`
*   **Definition:** An autonomous entity capable of perceiving, interpreting, and executing actions within a shared semantic environment.
*   **Properties:**
    *   `sac:identifier`: The W3C DID of the agent.
    *   `sac:hasCapability`: Links to `sac:Capability`.

### 2.2 CommunicativeAct
*   **URI:** `sac:CommunicativeAct`
*   **Definition:** An atomic unit of interaction within a Narrative. All specific acts (Intent, Delegation, etc.) are subclasses of this.
*   **Properties:**
    *   `sac:actor`: The Agent performing the act.
    *   `sac:timestamp`: When the act occurred.
    *   `sac:signature`: Cryptographic proof of authorship.

### 2.3 Intent
*   **URI:** `sac:Intent`
*   **Subclass Of:** `sac:CommunicativeAct`
*   **Definition:** A declaration of a goal or desired outcome.
*   **Properties:**
    *   `sac:goalDescription`: Natural language or formal description of the goal.

### 2.4 Delegation
*   **URI:** `sac:Delegation`
*   **Subclass Of:** `sac:CommunicativeAct`
*   **Definition:** A formal transfer of authority from one agent to another.
*   **Properties:**
    *   `sac:delegator`: The Agent granting authority.
    *   `sac:delegatee`: The Agent receiving authority.
    *   `sac:scope`: The `sac:Capability` or constraints being delegated.
    *   `sac:parentDelegation`: Link to a previous delegation (for chaining).

### 2.5 ExecutionRecord
*   **URI:** `sac:ExecutionRecord`
*   **Subclass Of:** `sac:CommunicativeAct`
*   **Definition:** A verifiable proof that an action was executed.
*   **Properties:**
    *   `sac:result`: The outcome (success/failure/artifact).
    *   `sac:authorizedBy`: Link to the `sac:Delegation` that authorized this.

### 2.6 Narrative
*   **URI:** `sac:Narrative`
*   **Definition:** An ordered, append-only log of `CommunicativeAct`s.
*   **Properties:**
    *   `sac:hasEvent`: Links to the acts contained in the narrative.

## 3. Core Properties

| Property | Domain | Range | Description |
| :--- | :--- | :--- | :--- |
| `sac:actor` | `sac:CommunicativeAct` | `sac:Agent` | The agent performing the act. |
| `sac:delegator` | `sac:Delegation` | `sac:Agent` | The agent granting authority. |
| `sac:delegatee` | `sac:Delegation` | `sac:Agent` | The agent receiving authority. |
| `sac:authorizedBy` | `sac:ExecutionRecord` | `sac:Delegation` | The delegation that authorized the act. |

## 4. Conformance

Implementations MUST support the serialization of these classes in JSON-LD.
