# Core Ontology Diagram

This diagram provides a high-level visualization of the core classes and properties defined in the `core.ttl` ontology module. It illustrates the fundamental relationships between agents, actions, capabilities, intents, and delegation.

```mermaid
classDiagram
    direction LR

    class AgentEntity {
        <<Abstract>>
    }
    class Agent {
        <<Class>>
    }
    class Capability {
        <<Class>>
    }
    class Intent {
        <<Class>>
    }
    class Delegation {
        <<Class>>
    }
    class ExecutionContext {
        <<Class>>
    }
    class Action {
        <<Class>>
    }
    class Artifact {
        <<Class>>
    }
    class TraceEvent {
        <<Class>>
    }
    class Task {
        <<Class>>
    }
    class TaskNode {
        <<Class>>
    }
    class TaskDependency {
        <<Class>>
    }

    Agent --|> AgentEntity

    Agent "1" -- "*" Intent : hasIntent
    Agent "1" -- "*" Capability : hasCapability
    Agent "1" -- "*" Action : executesAction
    Agent "1" -- "*" Task : performsTask

    Delegation "1" -- "1" Agent : delegatedBy
    Delegation "1" -- "1" Agent : delegatesTo
    Delegation "1" -- "*" Capability : delegationScope

    Action "1" -- "*" Artifact : producesArtifact
    Action "1" -- "1" TraceEvent : recordedIn
    ExecutionContext "1" -- "1" Action : contextOf

    Task "1" -- "*" Capability : requiresCapability
    Task "1" -- "*" Task : hasSubtask
    TaskNode "1" -- "*" TaskNode : hasDependency

    Intent "1" -- "*" Task : IntentAlignsWithTask

    note for Intent "Semantic expression of purpose."

    note for Task "Well-defined action unit."
    
    note for Capability "Functional competence."
    
    note for Delegation "Structured transfer of authority."
    
    note for Action "Concrete execution event."

```
