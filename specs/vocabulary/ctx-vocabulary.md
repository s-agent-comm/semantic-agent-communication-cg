# Vocabulary for Ctx Ontology

## Classes

| Class | Definition |
|:------|:-----------|
| `ctx:ExecutionEnvironment` | Describes the host environment where an action is executed. |
| `ctx:InputState` | Represents the inputs provided to an action. |
| `ctx:OutputState` | Represents the outputs returned by an action. |
| `ctx:SecurityContext` | Security-related constraints and guarantees active during execution. |

## Properties

| Property | Domain | Range | Definition |
|:---------|:-------|:------|:-----------|
| `ctx:envType` | `ctx:ExecutionEnvironment` | `xsd:string` | e.g., native, sandbox, container, vm, TEE. |
| `ctx:hasEnvironment` | `ctx:None` | `ctx:ExecutionEnvironment` |  |
| `ctx:hasSecurityContext` | `ctx:None` | `ctx:SecurityContext` |  |
| `ctx:inputState` | `ctx:None` | `ctx:InputState` |  |
| `ctx:inputValue` | `ctx:InputState` | `xsd:string` |  |
| `ctx:outputState` | `ctx:None` | `ctx:OutputState` |  |
| `ctx:outputValue` | `ctx:OutputState` | `xsd:string` |  |
| `ctx:usesKeySlot` | `ctx:SecurityContext` | `xsd:string` |  |
| `ctx:usesTEE` | `ctx:SecurityContext` | `xsd:boolean` |  |

