# Vocabulary for Payment Ontology

## Classes

| Class | Definition |
|:------|:-----------|
| `payment:Payment Intent` | A semantic expression of an intent to transfer value from one agent to another. |
| `payment:Settlement Interface` | Describes the technical and semantic requirements for settling a payment. |

## Properties

| Property | Domain | Range | Definition |
|:---------|:-------|:------|:-----------|
| `payment:acceptedMethod` | `payment:Settlement Interface` | `xsd:string` |  |
| `payment:Amount` | `payment:Payment Intent` | `xsd:decimal` |  |
| `payment:category` | `payment:Settlement Interface` | `xsd:string` |  |
| `payment:has settlement interface` | `payment:Payment Intent` | `payment:Settlement Interface` |  |
| `payment:Payee` | `payment:Payment Intent` | `payment:None` |  |
| `payment:Payer` | `payment:Payment Intent` | `payment:None` |  |
| `payment:Reason` | `payment:Payment Intent` | `xsd:string` |  |
| `payment:Unit` | `payment:Payment Intent` | `xsd:string` |  |

