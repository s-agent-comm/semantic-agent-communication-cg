# Vocabulary for Sec Ontology

## Classes

| Class | Definition |
|:------|:-----------|
| `sec:HardwareRootOfTrust` | TEE / TPM / Secure Element providing attested identity and execution guarantees. |
| `sec:KeyMaterial` | A cryptographic key associated with an agent identity. |
| `sec:KeyType` | Specifies the cryptographic algorithm or format (Ed25519, RSA, secp256k1). |
| `sec:SecurityBinding` | Represents the chain binding DID → Key Material → Hardware → Ledger verification. |
| `sec:TrustAnchor` | A root-level verifier or certificate authority validating hardware attestation. |

## Properties

| Property | Domain | Range | Definition |
|:---------|:-------|:------|:-----------|
| `sec:anchoredBy` | `sec:KeyMaterial` | `sec:HardwareRootOfTrust` |  |
| `sec:attestationReport` | `sec:HardwareRootOfTrust` | `xsd:string` |  |
| `sec:hasKeyMaterial` | `sec:None` | `sec:KeyMaterial` |  |
| `sec:keyType` | `sec:KeyMaterial` | `sec:KeyType` |  |
| `sec:keyValue` | `sec:KeyMaterial` | `xsd:string` |  |
| `sec:signsRecord` | `sec:KeyMaterial` | `sec:None` | Indicates ledger entries signed using this key material. |
| `sec:trustLevel` | `sec:HardwareRootOfTrust` | `xsd:string` |  |
| `sec:verifiedBy` | `sec:HardwareRootOfTrust` | `sec:TrustAnchor` |  |

