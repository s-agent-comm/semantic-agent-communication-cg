# Vocabulary for Core Ontology

## Classes

| Class | Definition |
|:------|:-----------|
| `core:Action` | A concrete execution event initiated by an Agent, producing observable or verifiable consequences. |
| `core:Agent` | An autonomous actor capable of perceiving, interpreting, or executing actions within a delegated semantic environment. |
| `core:AgentEntity` | A general semantic entity participating in agent communication, delegation, or execution. |
| `core:Artifact` | A produced output or result generated through agent execution. |
| `core:Capability` | A describable functional competence or operational capacity of an Agent. |
| `core:Delegation` | A structured semantic relation where one Agent authorizes another to act within a defined scope. |
| `core:ExecutionContext` | A contextual frame describing conditions, trust anchors, or constraints associated with an Agent action. |
| `core:Intent` | A semantic expression of purpose, objective, or expected action outcome. |
| `core:TraceEvent` | A verifiable record linking an Agent, an Action, and contextual constraints. |

## Properties

| Property | Domain | Range | Definition |
|:---------|:-------|:------|:-----------|
| `core:contextOf` | `core:ExecutionContext` | `core:Action` | Indicates that an ExecutionContext applies to a specific Action. |
| `core:delegatedBy` | `core:Delegation` | `core:Agent` | Indicates the Agent granting delegated authority. |
| `core:delegatesTo` | `core:Delegation` | `core:Agent` | Indicates the Agent receiving delegated authority. |
| `core:delegationScope` | `core:Delegation` | `core:Capability` | Specifies the scope of allowed capabilities within a Delegation relation. |
| `core:description` | `core:Artifact` | `xsd:string` | A human-readable description of an Artifact. |
| `core:executesAction` | `core:Agent` | `core:Action` | Associates an Agent with an Action it performs. |
| `core:hasCapability` | `core:Agent` | `core:Capability` | Associates an Agent with a Capability it is able to perform. |
| `core:hasIntent` | `core:Agent` | `core:Intent` | Associates an Agent with its intended objective or semantic purpose. |
| `core:producesArtifact` | `core:Action` | `core:Artifact` | Specifies the Artifact produced by an Action. |
| `core:recordedIn` | `core:Action` | `core:TraceEvent` | Links an Action to its verifiable trace record. |
| `core:timestamp` | `core:TraceEvent` | `xsd:dateTime` | Timestamp corresponding to the trace event. |

