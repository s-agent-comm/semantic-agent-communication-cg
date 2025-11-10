# Vocabulary for Del Ontology

## Classes

| Class | Definition |
|:------|:-----------|
| `del:Delegation` | 
    Represents a structured transfer of authority, allowing one Agent to act 
    under a bounded, semantically defined scope on behalf of another Agent.
     |
| `del:DelegationChain` | 
    A sequence of Delegation instances forming a multi-level authority graph.
    Useful for modeling nested or transitive delegation across agents.
     |
| `del:DelegationScope` | 
    Defines the semantic boundaries of delegated authority, including 
    capability constraints, intent framing, and operational limits.
     |
| `del:ExecutionConstraint` | Operational or environmental constraints limiting the delegate's permissible actions. |

## Properties

| Property | Domain | Range | Definition |
|:---------|:-------|:------|:-----------|
| `del:accountableFor` | `del:Delegation` | `del:None` | Connects a Delegation to the Actions executed under that delegated authority. |
| `del:allowedCapability` | `del:DelegationScope` | `del:None` | Capabilities the delegated Agent is authorized to perform. |
| `del:delegatedBy` | `del:Delegation` | `del:None` | Agent granting the authority. |
| `del:delegatesTo` | `del:Delegation` | `del:None` | Agent receiving delegated authority. |
| `del:delegationId` | `del:Delegation` | `xsd:string` |  |
| `del:delegationScope` | `del:Delegation` | `del:DelegationScope` |  |
| `del:executionConstraint` | `del:DelegationScope` | `del:ExecutionConstraint` |  |
| `del:hasDelegation` | `del:DelegationChain` | `del:Delegation` |  |
| `del:intentConstraint` | `del:DelegationScope` | `del:None` | Specifies the intent boundary under which the delegate may operate. |
| `del:note` | `del:Delegation` | `xsd:string` |  |
| `del:recordedIn` | `del:Delegation` | `del:None` | Records delegation-related events within the semantic accountability chain. |
| `del:validFrom` | `del:DelegationScope` | `xsd:dateTime` |  |
| `del:validUntil` | `del:DelegationScope` | `xsd:dateTime` |  |

