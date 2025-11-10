# Federated Digital Identity for Global Fintech Onboarding Use Case

## Introduction
This use case addresses a significant challenge in the global digital economy: enabling seamless and secure cross-border identity verification for financial services. It demonstrates how the Agent Ontology can act as a semantic mediation layer, allowing individuals to leverage diverse national digital identity systems (like EUDI Wallet, TWDIW, and JP MyNumber) to onboard with foreign financial institutions. The core innovation lies in using autonomous agents to orchestrate the aggregation, transformation, and secure presentation of verifiable credentials across different trust frameworks, without requiring deep technical integration between national identity infrastructures.

## User Story: A Japanese Citizen in Taiwan Opening a German Investment Account

**As a** Japanese citizen (Kenji) residing in Taiwan,
**I want to** open a high-yield investment account with a EuroTrust FinTech Bank using my existing digital identities (JP MyNumber, TWDIW),
**so that** I can complete the complex KYC (Know Your Customer) process quickly and securely without mailing physical documents.

## The Challenge: Bridging Disparate Identity Systems
EuroTrust FinTech Bank has stringent AML (Anti-Money Laundering) and KYC requirements, demanding verification of:
1.  **Primary Identity**: Issued by a trusted national government.
2.  **Proof of Residency**: Current residential address.
3.  **Tax Identification Number (TIN)**: For tax reporting compliance.

Kenji's digital identity attributes are distributed across three distinct systems:
*   **Sakura ID**: Contains his **primary citizen identity** and **Japanese Tax Identification Number**.
*   **Formosa ID Wallet**: Contains his **Taiwanese Alien Resident Certificate (ARC)** and **proof of current residential address**.
*   **EUDI Wallet Framework**: Although Kenji is not an EU citizen, the German bank's onboarding system is designed to accept verifiable credentials (VCs) that conform to the **EUDI framework** (e.g., eIDAS standards) for interoperability within the EU. This requires Kenji's agent to present credentials in a compatible format and trust model.

## Key Concepts Illustrated
This use case vividly demonstrates several advanced applications of the Agent Ontology:
*   **Multi-Agent Collaboration**: Orchestration between Kenji's Personal Finance Agent, Berlin FinTech Bank's Onboarding Agent, and national Digital Identity Wallet Agents (JP MyNumber, TWDIW).
*   **Intent-Driven Workflow**: The entire process is initiated and guided by Kenji's explicit `Intent` to open an account.
*   **Dynamic, Fine-Grained Delegation**: Kenji's Personal Finance Agent requests and receives specific, limited `Delegation` from his national Digital Identity Wallet Agents to access only the necessary identity attributes.
*   **Verifiable Credentials (VCs) & Verifiable Presentations (VPs)**: The core data exchange mechanism, where VCs from different sources are aggregated into a single, cryptographically secured VP.
*   **Semantic Mediation**: The Personal Finance Agent acts as a semantic translator, transforming VCs from national formats into an EUDI-compatible `VerifiablePresentation`.
*   **Secure Execution Context (`ExecutionContext`)**: Defining the trust anchors and policy frameworks under which cross-border identity verification occurs.
*   **SecurityBinding**: Ensuring the integrity, authenticity, and non-repudiation of VCs and VPs through cryptographic signatures.
*   **End-to-End Accountability (`TraceEvent`/`LedgerRecord`)**: An immutable audit trail of all identity requests, authorizations, data exchanges, and verification outcomes, crucial for regulatory compliance and dispute resolution.

## Workflow Breakdown and Ontology Mapping:

### 1. User's Initial Intent to Open Account
-   **Description**: Kenji initiates the process through his Personal Finance Application, expressing his desire to open an investment account with EuroTrust FinTech Bank.
    **Ontology Mapping**: A `core:Intent` instance, `:KenjiOnboardingIntent`, is created by Kenji's `:PersonalFinanceAgent`. Its `intent:objective` is "Open investment account with EuroTrust FinTech Bank." This `Intent` drives the entire subsequent workflow.

### 2. Negotiation and Data Requirement List
-   **Description**: Kenji's Personal Finance Agent communicates with EuroTrust FinTech Bank's Onboarding Agent to understand the KYC requirements. The bank's agent provides a structured list of required identity attributes and the acceptable trust frameworks (e.g., EUDI-compatible VCs).
-   **Ontology Mapping**: The `:BerlinFinTechOnboardingAgent` responds with a `core:Artifact`, `:KYCRequirementList`, which is a semantic representation of the required VCs (e.g., `ProofOfIdentity`, `ProofOfAddress`, `TaxID`) and their expected `SecurityBinding` properties.

### 3. Multi-Source Delegation for Credential Access
-   **Description**: Kenji's Personal Finance Agent, knowing the requirements, identifies that the necessary credentials are held in his JP MyNumber Wallet and TWDIW. It then requests explicit authorization from Kenji (via his respective wallet applications) to access these specific attributes.
-   **Ontology Mapping**:
    *   **Delegation to Sakura ID Wallet Agent**: A `delegation:Delegation` instance, `:Delegation_FinanceToJPMynumber`, is created. `delegation:delegatedBy` is `:PersonalFinanceAgent`, `delegation:delegatesTo` is `:JPMynumberWalletAgent`. `delegation:delegationScope` is precisely defined: "Provide Verifiable Credential containing primary citizen identity and Japanese Tax Identification Number."    *   **Delegation to Formosa ID Wallet Agent**: Similarly, `:Delegation_FinanceToTWDIW` is created. `delegation:delegatedBy` is `:PersonalFinanceAgent`, `delegation:delegatesTo` is `:TWDIWAgent`. `delegation:delegationScope` is: "Provide Verifiable Credential containing Taiwanese Alien Resident Certificate and current residential address."    *   Kenji's approval in his wallet apps completes these delegations.

### 4. Aggregation and EUDI-Compatible Verifiable Presentation Generation
-   **Description**: Upon receiving the authorized VCs from both Sakura ID and Formosa ID Wallet, Kenji's Personal Finance Agent performs a crucial aggregation and transformation step. It combines these disparate VCs into a single `VerifiablePresentation` that adheres to the EUDI framework's data model and cryptographic requirements.
-   **Ontology Mapping**: The `:PersonalFinanceAgent` executes a `core:Action`, `:GenerateEUDIVPAction`. This `Action` takes the VCs from JP MyNumber and TWDIW as implicit inputs and `core:producesArtifact` which is the `:EUDI_Compatible_VP`. This `Artifact` will have a `security:SecurityBinding` (e.g., `cryptographicBinding: JWS`, `trustModel: eIDAS-compliant`) to ensure its integrity and compliance with EU standards.

### 5. Secure Submission in Defined Execution Context
-   **Description**: Kenji's Personal Finance Agent securely transmits the EUDI-compatible `VerifiablePresentation` to Berlin FinTech Bank's Onboarding Agent. This submission occurs within a defined `ExecutionContext` that specifies the legal and technical trust parameters.
-   **Ontology Mapping**: The `:PersonalFinanceAgent` performs a `core:Action`, `:SubmitEUDIVPAction`. This `Action` is performed within a `core:ExecutionContext`, `:GlobalKYCExecutionContext`. This context defines `execution-context:trustAnchors` (e.g., references to EU, JP, TW PKI roots) and `execution-context:policy` (e.g., "EU-Japan-Taiwan Data Exchange Agreement"). The `core:producesArtifact` of this action is the submission confirmation.

### 6. Bank Verification and Account Onboarding
-   **Description**: Berlin FinTech Bank's Onboarding Agent receives the VP, verifies its cryptographic signatures, checks the validity of the underlying VCs against the specified trust anchors, and processes Kenji's application. Upon successful verification, the account is opened.
-   **Ontology Mapping**: The `:BerlinFinTechOnboardingAgent` performs a `core:Action`, `:VerifyEUDIVPAction`, which consumes the `:EUDI_Compatible_VP`. If successful, it `core:producesArtifact`, `:InvestmentAccountDetails`, containing Kenji's new account information.

### 7. End-to-End Accountability and Audit Trail
-   **Description**: Every interaction, from Kenji's initial intent to the final account opening, is meticulously recorded. This creates an immutable, cryptographically verifiable audit trail essential for regulatory compliance, anti-fraud measures, and dispute resolution across international borders.
-   **Ontology Mapping**: `accountability:LedgerRecord` or `core:TraceEvent` instances are generated for each `Intent`, `Delegation`, `Action`, and `Artifact` throughout the workflow. These records link all entities, timestamps, and cryptographic proofs, providing a comprehensive and tamper-proof history of the entire onboarding process.
