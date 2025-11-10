# Vocabulary for Agent Ontology

## Classes

| Class | Definition |
|:------|:-----------|
| `agent:AgentIdentity` | Identity attributes for an Agent, including DID, versioning, and associated metadata. |
| `agent:CapabilityBundle` | Declared capabilities and skills for an Agent. |
| `agent:IdentityBinding` |  |
| `agent:IdentitySet` |  |
| `agent:InputSpec` |  |
| `agent:InterfaceSpec` |  |
| `agent:OperationalProfile` | Triggers, input schema, and output schema of an Agent. |
| `agent:OutputSpec` |  |
| `agent:PurposeRole` | Declares the operational purpose and ownership of the Agent. |
| `agent:SystemIntegration` | Dependency and interface declarations for OS-level agent execution. |
| `agent:Trigger` |  |
| `agent:Contract` |  |
| `agent:ContractSet` |  |
| `agent:Wallet` |  |
| `agent:WalletSet` |  |
| `agent:DecommissionRecord` |  |
| `agent:GenesisRecord` |  |
| `agent:HealthCheckSpec` |  |
| `agent:LifecycleRecord` |  |

## Properties

| Property | Domain | Range | Definition |
|:---------|:-------|:------|:-----------|
| `agent:capabilities` | `agent:None` | `agent:CapabilityBundle` |  |
| `agent:contractualInterfaces` | `agent:None` | `agent:ContractSet` |  |
| `agent:coreIdentity` | `agent:None` | `agent:AgentIdentity` |  |
| `agent:dependsOn` | `agent:SystemIntegration` | `agent:None` |  |
| `agent:did` | `agent:AgentIdentity` | `xsd:string` | Primary DID associated with the Agent. |
| `agent:economicInterfaces` | `agent:None` | `agent:WalletSet` |  |
| `agent:has profile` | `agent:None` | `agent:None` | Links an Agent to its pragmatic / behavioral profile. |
| `agent:identity` | `agent:IdentitySet` | `agent:IdentityBinding` |  |
| `agent:identityInterfaces` | `agent:None` | `agent:IdentitySet` |  |
| `agent:input` | `agent:OperationalProfile` | `agent:InputSpec` |  |
| `agent:interface` | `agent:SystemIntegration` | `agent:InterfaceSpec` |  |
| `agent:keyManagementSystem` | `agent:IdentityBinding` | `xsd:string` |  |
| `agent:lifecycleManagement` | `agent:None` | `agent:LifecycleRecord` |  |
| `agent:objective` | `agent:PurposeRole` | `xsd:string` |  |
| `agent:operationalTriggersAndIO` | `agent:None` | `agent:OperationalProfile` |  |
| `agent:output` | `agent:OperationalProfile` | `agent:OutputSpec` |  |
| `agent:owner` | `agent:PurposeRole` | `xsd:string` |  |
| `agent:purposeAndRole` | `agent:None` | `agent:PurposeRole` |  |
| `agent:skill` | `agent:CapabilityBundle` | `xsd:string` |  |
| `agent:systemIntegrationAndDependencies` | `agent:None` | `agent:SystemIntegration` |  |
| `agent:title` | `agent:AgentIdentity` | `xsd:string` |  |
| `agent:trigger` | `agent:OperationalProfile` | `agent:Trigger` |  |
| `agent:version` | `agent:AgentIdentity` | `xsd:string` |  |
| `agent:contract` | `agent:ContractSet` | `agent:Contract` |  |
| `agent:termsUri` | `agent:Contract` | `xsd:anyURI` |  |
| `agent:address` | `agent:Wallet` | `xsd:string` |  |
| `agent:wallet` | `agent:WalletSet` | `agent:Wallet` |  |
| `agent:decommissionRecord` | `agent:LifecycleRecord` | `agent:DecommissionRecord` |  |
| `agent:genesisRecord` | `agent:LifecycleRecord` | `agent:GenesisRecord` |  |
| `agent:healthCheck` | `agent:LifecycleRecord` | `agent:HealthCheckSpec` |  |
| `agent:state` | `agent:LifecycleRecord` | `xsd:string` |  |

