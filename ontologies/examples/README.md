# Agent Ontology Examples

This directory contains a collection of practical examples demonstrating the application of the Semantic Agent Communication Community Group's (SAC-CG) Agent Ontology. These examples are designed to illustrate how the core semantic concepts—such as Agent Identity, Capabilities, Intent, Delegation, Actions, Artifacts, and Accountability—can be used to model real-world multi-agent workflows and complex business scenarios.

Each subdirectory within `examples/` represents a distinct use case and typically includes:

*   **`README.md`**: A detailed explanation of the use case, including the user story, key concepts illustrated, workflow breakdown, and ontology mapping.
*   **`.ttl` files**: Turtle (Terse RDF Triple Language) files representing instances of the ontology, defining agents, intents, delegations, and other semantic entities.
*   **`.jsonld` files**: JSON-LD (JSON for Linking Data) representations of the ontology instances, often used for data exchange and integration with JSON-based systems.
*   **`.shacl.ttl` files**: SHACL (Shapes Constraint Language) files that define validation rules for the corresponding `.ttl` and `.jsonld` instances, ensuring data consistency and adherence to the ontology's constraints.

## Exploring the Examples

We encourage you to explore each example to understand how the Agent Ontology can be applied to various domains. Here are some of the key use cases currently available:

### 1. Cross-Border EUDI Wallet
*   **Description**: Demonstrates an agent facilitating secure cross-border interactions using a European Digital Identity (EUDI) wallet.
*   **Key Concepts**: Agent Identity, Operational Profile, Security Binding.
*   **Location**: `cross-border-eudi-wallet/`

### 2. Running Machine MVS (Minimal Viable Service)
*   **Description**: Models a simple agent representing a running machine, exposing basic control capabilities like start and stop.
*   **Key Concepts**: Agent Capabilities, Operational Triggers and I/O.
*   **Location**: `running-machine-mvs/`

### 3. Tax Backoffice Automation
*   **Description**: Illustrates an agent automating tax-related backoffice tasks, including calculation, form preparation, and submission.
*   **Key Concepts**: Agent Capabilities, Intent, Operational Profile.
*   **Location**: `tax-backoffice/`

### 4. Supplier Verification
*   **Description**: Details an agent verifying supplier credentials and compliance, crucial for supply chain integrity.
*   **Key Concepts**: Agent Capabilities, Verification Actions, Artifacts.
*   **Location**: `supplier-verification/`

### 5. AI Workforce Employee
*   **Description**: Represents an agent as an employee within an AI workforce, performing tasks like data analysis and report generation.
*   **Key Concepts**: Agent Profile, Purpose and Role, Capabilities.
*   **Location**: `ai-workforce-employee/`

### 6. Stablecoin Settlement
*   **Description**: Shows an agent facilitating stablecoin transactions, including value transfer and ledger recording.
*   **Key Concepts**: Economic Interfaces, Payment Methods, Actions.
*   **Location**: `stablecoin-settlement/`

### 7. ISO SC42 Mapping
*   **Description**: Demonstrates how the agent ontology can be mapped to the ISO/IEC AWI 23053 standard for Artificial Intelligence.
*   **Key Concepts**: Ontology Alignment, Agent Classification.
*   **Location**: `iso-sc42-mapping/`

### 8. AI Enterprise Organization
*   **Description**: Models an agent representing an entire AI-powered organization, managing other agents and delegating tasks.
*   **Key Concepts**: Multi-Agent Systems, Hierarchical Delegation, Organizational Structure.
*   **Location**: `ai-enterprise-organization/`

### 9. TEE Binding
*   **Description**: Illustrates how an agent's execution can be bound to a Trusted Execution Environment (TEE) for enhanced security.
*   **Key Concepts**: Security Binding, Trust Models, Execution Context.
*   **Location**: `tee-binding/`

### 10. Multi-Agent Delegation Chain
*   **Description**: Demonstrates a sequential chain of delegation between multiple agents for complex task execution.
*   **Key Concepts**: Delegation Chains, Task Decomposition, Agent Collaboration.
*   **Location**: `multi-agent-delegation-chain/`

### 11. Supplier Verification and Cross-Border Payment (Detailed User Story)
*   **Description**: A comprehensive multi-agent workflow for verifying a new international supplier and executing a cross-border payment, highlighting trust, compliance, and auditability.
*   **Key Concepts**: Intent, Multi-Layered Delegation, Security Binding, Payment Methods, End-to-End Accountability.
*   **Location**: `supplier-verification-cross-border-payment/`

### 12. The Journey of a Smart Thermostat: From Design to Global Brand (OBM/ODM/OEM - Detailed User Story)
*   **Description**: Illustrates the business model evolution of a Taiwanese company from OEM to ODM to OBM, showcasing dynamic shifts in capabilities, delegation, and strategic positioning.
*   **Key Concepts**: Business Model Transformation, Capability Evolution, Dynamic Delegation Scope, End-Consumer Interaction, Integrated Supply Chain.
*   **Location**: `smart-thermostat-obm-odm-oem/`

---

**How to Contribute**: If you have ideas for new examples or improvements to existing ones, please refer to the main [CONTRIBUTING.md](../../CONTRIBUTING.md) file and open an issue or pull request.
