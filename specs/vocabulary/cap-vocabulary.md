# Vocabulary for Cap Ontology

## Classes

| Class | Definition |
|:------|:-----------|
| `cap:Capability` | 
    A functional competence of an Agent. Describes an operation, method,
    or action family that can be executed under explicit identity and context.
     |
| `cap:CapabilityClass` | 
    Categorizes capability types, useful for policy, delegation, or competency grouping.
     |
| `cap:CapabilityConstraint` | 
    Restrictions on the use of a capability, including safety,
    context limitations, or policy-bound execution gates.
     |
| `cap:CapabilityProvenance` | Captures origin, version, or derivation lineage of a capability. |
| `cap:CompositeCapability` | 
    Aggregates multiple capabilities into a higher-level operational construct.
    Used for modeling workflows, multi-step tasks, or protocol sequences.
     |
| `cap:ExecutionPattern` | 
    Formal structure describing expected execution behavior,
    including determinism, interaction, or dependency modes.
     |
| `cap:InputSchema` | Defines required input structure for capability invocation. |
| `cap:OutputSchema` | Defines generated output structure for capability execution. |
| `cap:PrimitiveCapability` | Indivisible functional element representing a minimal semantic operation. |

## Properties

| Property | Domain | Range | Definition |
|:---------|:-------|:------|:-----------|
| `cap:allowedContext` | `cap:CapabilityConstraint` | `xsd:string` | Context(s) in which capability execution is permitted. |
| `cap:capabilityId` | `cap:Capability` | `xsd:string` |  |
| `cap:capabilityVersion` | `cap:CapabilityProvenance` | `xsd:string` |  |
| `cap:classifiedAs` | `cap:Capability` | `cap:CapabilityClass` |  |
| `cap:dependsOnCapability` | `cap:Capability` | `cap:Capability` | Declares capability-level dependencies within an agent or delegation scope. |
| `cap:description` | `cap:Capability` | `xsd:string` |  |
| `cap:executionPattern` | `cap:Capability` | `cap:ExecutionPattern` |  |
| `cap:hasConstraint` | `cap:Capability` | `cap:CapabilityConstraint` |  |
| `cap:includes` | `cap:CompositeCapability` | `cap:Capability` | Capability elements that form part of a composite capability. |
| `cap:producesOutput` | `cap:Capability` | `cap:OutputSchema` |  |
| `cap:prohibitedContext` | `cap:CapabilityConstraint` | `xsd:string` |  |
| `cap:provenance` | `cap:Capability` | `cap:CapabilityProvenance` |  |
| `cap:requiresInput` | `cap:Capability` | `cap:InputSchema` |  |
| `cap:requiresPermission` | `cap:CapabilityConstraint` | `xsd:string` |  |
| `cap:sourceSpec` | `cap:CapabilityProvenance` | `xsd:anyURI` |  |

