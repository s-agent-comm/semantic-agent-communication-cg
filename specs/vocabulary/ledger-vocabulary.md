# Vocabulary for Ledger Ontology

## Classes

| Class | Definition |
|:------|:-----------|
| `ledger:GovernanceLedgerEvent` | Represents governance or specification update events. |
| `ledger:LedgerEvent` | Canonical semantic event in append-only ledger stream. |
| `ledger:RuntimeLedgerEvent` | Represents execution of an agent-level runtime action. |

## Properties

| Property | Domain | Range | Definition |
|:---------|:-------|:------|:-----------|
| `ledger:accountabilityRecord` | `ledger:LedgerEvent` | `ledger:None` | Connects ledger event to accountability evaluation. |
| `ledger:action` | `ledger:RuntimeLedgerEvent` | `ledger:None` |  |
| `ledger:actor` | `ledger:LedgerEvent` | `ledger:None` | Agent or principal responsible for the event. |
| `ledger:aiActSection` | `ledger:LedgerEvent` | `xsd:string` |  |
| `ledger:appendOnly` | `ledger:LedgerEvent` | `xsd:boolean` | Enforces append-only semantics; always true. |
| `ledger:capabilityVersion` | `ledger:RuntimeLedgerEvent` | `xsd:string` |  |
| `ledger:delegation` | `ledger:LedgerEvent` | `ledger:None` | Delegation basis authorizing this event. |
| `ledger:environment` | `ledger:RuntimeLedgerEvent` | `xsd:string` | Additional semantic environment markers. |
| `ledger:eventId` | `ledger:LedgerEvent` | `xsd:string` |  |
| `ledger:executionContext` | `ledger:RuntimeLedgerEvent` | `ledger:None` |  |
| `ledger:governanceAction` | `ledger:GovernanceLedgerEvent` | `ledger:None` |  |
| `ledger:hardwareAnchor` | `ledger:RuntimeLedgerEvent` | `xsd:string` | Hardware-backed attestation anchor. |
| `ledger:hash` | `ledger:LedgerEvent` | `xsd:string` |  |
| `ledger:intent` | `ledger:RuntimeLedgerEvent` | `xsd:string` | High-level semantic intent of an action. |
| `ledger:previousEventHash` | `ledger:LedgerEvent` | `xsd:string` | Hash of preceding event in append-only chain. |
| `ledger:proofType` | `ledger:LedgerEvent` | `xsd:string` |  |
| `ledger:publicKey` | `ledger:LedgerEvent` | `xsd:string` |  |
| `ledger:result` | `ledger:RuntimeLedgerEvent` | `ledger:None` |  |
| `ledger:riskClassification` | `ledger:LedgerEvent` | `xsd:string` |  |
| `ledger:sandboxProfile` | `ledger:RuntimeLedgerEvent` | `xsd:string` |  |
| `ledger:sideEffect` | `ledger:RuntimeLedgerEvent` | `xsd:string` |  |
| `ledger:signature` | `ledger:LedgerEvent` | `xsd:string` |  |
| `ledger:specVersion` | `ledger:GovernanceLedgerEvent` | `ledger:None` |  |
| `ledger:stateChange` | `ledger:RuntimeLedgerEvent` | `xsd:string` |  |
| `ledger:timestamp` | `ledger:LedgerEvent` | `xsd:dateTime` |  |
| `ledger:usesCapability` | `ledger:RuntimeLedgerEvent` | `ledger:None` |  |
| `ledger:verifiedBy` | `ledger:LedgerEvent` | `xsd:string` | External verification entity or attestation provider. |

