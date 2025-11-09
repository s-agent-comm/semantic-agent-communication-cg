# Core Ontology Specification (Draft)

**Version:** 0.1.0  
**Status:** Draft

## 1. Introduction

This document provides the formal specification for the Core module of the AI Agent Ontology. The Core ontology defines the foundational, high-level concepts that form the basis for all other modules in this project. It establishes the primary classes of entities and the fundamental relationships between them.

The namespace for the Core Ontology is `https://ns.slashlife.ai/agent/core#`. The recommended prefix is `core`.

## 2. Core Classes

This section details the primary classes defined in the Core Ontology.

### 2.1 Agent
*   **URI:** `core:Agent`
*   **Subclass Of:** `core:AgentEntity`
*   **Definition:** An autonomous actor capable of perceiving, interpreting, or executing actions within a delegated semantic environment.
*   **Key Properties:**
    *   `core:hasIntent`: Associates an Agent with its intended objective or semantic purpose.
    *   `core:hasCapability`: Associates an Agent with a Capability it is able to perform.
    *   `core:executesAction`: Associates an Agent with an Action it performs.

### 2.2 Capability
*   **URI:** `core:Capability`
*   **Definition:** A describable functional competence or operational capacity of an Agent.
*   **Description:** This class represents what an agent *can do*. Capabilities can be simple (e.g., "send an email") or complex (e.g., "manage a supply chain"). They are the units of authority that are granted in a Delegation.

### 2.3 Delegation
*   **URI:** `core:Delegation`
*   **Definition:** A structured semantic relation where one Agent authorizes another to act within a defined scope.
*   **Key Properties:**
    *   `core:delegatedBy`: Indicates the Agent granting delegated authority.
    *   `core:delegatesTo`: Indicates the Agent receiving delegated authority.
    *   `core:delegationScope`: Specifies the scope of allowed capabilities within a Delegation relation.

### 2.4 Action
*   **URI:** `core:Action`
*   **Definition:** A concrete execution event initiated by an Agent, producing observable or verifiable consequences.
*   **Description:** An Action is a record of something that *happened*. It is the result of an Agent exercising a Capability.
*   **Key Properties:**
    *   `core:producesArtifact`: Specifies the Artifact produced by an Action.
    *   `core:recordedIn`: Links an Action to its verifiable trace record (`core:TraceEvent`).

### 2.5 Other Core Classes

*   **`core:AgentEntity`**: A general semantic entity participating in agent communication, delegation, or execution. It is the superclass for `core:Agent`.
*   **`core:Intent`**: A semantic expression of purpose, objective, or expected action outcome.
*   **`core:ExecutionContext`**: A contextual frame describing conditions, trust anchors, or constraints associated with an Agent action.
*   **`core:Artifact`**: A produced output or result generated through agent execution.
*   **`core:TraceEvent`**: A verifiable record linking an Agent, an Action, and contextual constraints.

## 3. Core Properties

This section details the primary object properties that connect the core classes.

| Property | Domain | Range | Description |
| :--- | :--- | :--- | :--- |
| `core:hasIntent` | `core:Agent` | `core:Intent` | Associates an Agent with its intended objective. |
| `core:hasCapability` | `core:Agent` | `core:Capability` | Links an Agent to a Capability it can perform. |
| `core:delegatedBy` | `core:Delegation` | `core:Agent` | The Agent granting authority. |
| `core:delegatesTo` | `core:Delegation` | `core:Agent` | The Agent receiving authority. |
| `core:delegationScope` | `core:Delegation` | `core:Capability` | The scope of capabilities allowed in a Delegation. |
| `core:executesAction` | `core:Agent` | `core:Action` | Associates an Agent with an Action it performs. |
| `core:producesArtifact` | `core:Action` | `core:Artifact` | The Artifact produced by an Action. |
| `core:recordedIn` | `core:Action` | `core:TraceEvent` | Links an Action to its trace record. |
| `core:contextOf` | `core:ExecutionContext` | `core:Action` | The context that applies to a specific Action. |
