# Vocabulary for Acc Ontology

## Classes

| Class | Definition |
|:------|:-----------|
| `acc:AccountabilityEvent` | Evaluative record assessing correctness, authorization, and compliance for an executed action. |
| `acc:ComplianceAssessment` | Assessment of regulatory compliance, including AI Act considerations. |
| `acc:DelegationBasis` | Chain of delegation evaluations supporting action legitimacy. |
| `acc:ResponsibilityAttribution` | Assigns responsibility among agents or principals based on execution evidence. |

## Properties

| Property | Domain | Range | Definition |
|:---------|:-------|:------|:-----------|
| `acc:action` | `acc:AccountabilityEvent` | `acc:None` |  |
| `acc:actor` | `acc:AccountabilityEvent` | `acc:None` |  |
| `acc:aiActSection` | `acc:ComplianceAssessment` | `xsd:string` |  |
| `acc:assignedTo` | `acc:ResponsibilityAttribution` | `acc:None` |  |
| `acc:compliance` | `acc:AccountabilityEvent` | `acc:ComplianceAssessment` |  |
| `acc:delegationChain` | `acc:AccountabilityEvent` | `acc:DelegationBasis` |  |
| `acc:eventId` | `acc:AccountabilityEvent` | `xsd:string` |  |
| `acc:intent` | `acc:AccountabilityEvent` | `xsd:string` |  |
| `acc:linkedLedgerEvent` | `acc:AccountabilityEvent` | `acc:None` | Formal relation connecting accountability evaluation to recorded runtime event. |
| `acc:rationale` | `acc:ResponsibilityAttribution` | `xsd:string` |  |
| `acc:referencesDelegation` | `acc:DelegationBasis` | `acc:None` |  |
| `acc:responsibility` | `acc:AccountabilityEvent` | `acc:ResponsibilityAttribution` |  |
| `acc:riskClass` | `acc:ComplianceAssessment` | `xsd:string` |  |
| `acc:timestamp` | `acc:AccountabilityEvent` | `xsd:dateTime` |  |

