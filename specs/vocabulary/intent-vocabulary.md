# Vocabulary for Intent Ontology

## Classes

| Class | Definition |
|:------|:-----------|
| `intent:Action` | An executable operation derived from an intent. |
| `intent:ActionType` | Category of an actionable execution unit. |
| `intent:ExecutionContext` | Run-time context under which an action is executed. |
| `intent:Intent` | A semantic statement expressing what an agent aims to achieve. |
| `intent:IntentParameter` | Typed parameters specifying the scope and execution conditions of an intent. |
| `intent:IntentType` | Categorizes an intent (e.g., fetch-data, make-decision, generate-artifact). |

## Properties

| Property | Domain | Range | Definition |
|:---------|:-------|:------|:-----------|
| `intent:authorizedBy` | `intent:Intent` | `intent:None` | Links an intent to the delegation statement that authorizes it. |
| `intent:executedIn` | `intent:Action` | `intent:ExecutionContext` |  |
| `intent:hasActionType` | `intent:Action` | `intent:ActionType` |  |
| `intent:hasIntentType` | `intent:Intent` | `intent:IntentType` |  |
| `intent:hasParameter` | `intent:Intent` | `intent:IntentParameter` |  |
| `intent:loggedAs` | `intent:Action` | `intent:None` | Links an executed action to its ledger record. |
| `intent:paramName` | `intent:IntentParameter` | `xsd:string` |  |
| `intent:paramType` | `intent:IntentParameter` | `xsd:string` |  |
| `intent:paramValue` | `intent:IntentParameter` | `xsd:string` |  |
| `intent:producesAction` | `intent:Intent` | `intent:Action` |  |

