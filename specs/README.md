# Semantic Agent Communication Specifications  

This directory contains the specification suite for the Semantic Agent Communication framework.  
Documents are organized according to a W3C-consistent structure, covering explainers, core specifications, vocabularies, mappings, and security materials.  
This index provides a unified entry point for the entire specification set.


============================================================
1. Status of This Document
============================================================

This is an early-stage, work-in-progress draft prepared within the Semantic Agent Communication Community Group.  
The contents in this directory do not yet represent a W3C Recommendation or a work item of any W3C Working Group.  
These documents are exploratory and intended to guide future proposals, technical discussion, and standardization alignment.

Editors assume that portions of this specification suite may be submitted as Community Group Reports, and—if adopted—may serve as input to a future Working Group.


============================================================
2. Document Structure Overview
============================================================

The specification suite is organized into six layers:

A. Explainer and Introductory Documents  
B. Core Specification Layer  
C. Architecture and Protocol  
D. Vocabulary Suite (JSON-LD / RDF-oriented)  
E. Interoperability and Mapping Documents  
F. Security and Threat Model Materials  
G. W3C-Formatted Output (HTML)


Each category below lists the corresponding files already present in this repository.


============================================================
3. A. Explainer and Introductory Documents
============================================================

- specs/Explainer.md  
- specs/primer.md  
- specs/legal-primer.md


Purpose:
These documents introduce motivations, use cases, conceptual framing, and legal foundations.  
They represent the "onboarding" layer for implementers and reviewers.


============================================================
4. B. Core Specification Layer
============================================================

- specs/core-ontology.md  
- specs/core-ontology-diagram.md  
- specs/scope-alignment.md  
- specs/iso-mapping.md  
- specs/iso-nwip-draft.md  
- specs/agent-idl.md  
- specs/mapping.md


Purpose:
These files provide formal definitions, terminology, structural semantics, diagrams, ISO-aligned mappings, and the proposed Agent IDL extensions.  
They form the foundation of the technical model.


============================================================
5. C. Architecture and Protocol
============================================================

- specs/architecture.md  
- specs/protocol.md


Purpose:
These documents describe the execution model, interaction patterns, delegation flow, contract binding, lifecycle rules, and protocol behaviors for semantic agents.


============================================================
6. D. Vocabulary Suite
============================================================

Directory: specs/vocabulary/

- accountability-vocabulary.md  
- agent-profile-vocabulary.md  
- agent-vocabulary.md  
- capability-vocabulary.md  
- core-vocabulary.md  
- delegation-vocabulary.md  
- execution-context-vocabulary.md  
- identity-vocabulary.md  
- intent-vocabulary.md  
- ledger-vocabulary.md  
- ontology-vocabulary.md  
- payment-vocabulary.md  
- security-binding-vocabulary.md  
- threat-model-vocabulary.md


Purpose:
The vocabulary suite defines machine-interpretable terms, classes, properties, and constraints used across agent identity, delegation, capability description, ledger entries, and security-binding mechanisms.  
These vocabularies are intended to align with JSON-LD contexts and RDF semantics.


============================================================
7. E. Interoperability and External Alignments
============================================================

- specs/schema-org-mapping.md  
- specs/mapping.md  
- specs/iso-mapping.md


Purpose:
These materials provide conceptual and formal crosswalks between the Semantic Agent framework and external standards, including Schema.org, ISO/IEC work items, and related ecosystems.


============================================================
8. F. Security and Threat Model
============================================================

- specs/minimal-threat-model.md  
- specs/security.md  
- specs/vocabulary/threat-model-vocabulary.md


Purpose:
These documents describe threat vectors, risk surfaces, defensive assumptions, and minimal security requirements for semantic agent systems.  
They complement the identity, delegation, and ledger models defined in the core specifications.


============================================================
9. G. W3C-Formatted Output
============================================================

- specs/w3c/core-ontology.html


Purpose:
This file demonstrates the emerging structure of a W3C-styled specification (HTML format).  
It is not yet a complete Working Draft but may serve as the starting point for a future ED (Editor’s Draft) or WD (Working Draft).


============================================================
10. Future Deliverables (Optional)
============================================================

The following documents may be introduced as the specification matures:

- Use Case & Requirements (UCR)  
- Comprehensive Architecture Overview (expanded)  
- Test Suite  
- Conformance requirements  
- Security considerations (fully formalized)  
- Implementation Guide  
- Interoperability Matrix (consolidated version)  
- Community Group Final Report  
- Candidate W3C Working Draft (if chartered)


============================================================
11. Versioning Notes
============================================================

- All documents in this directory are versioned independently.  
- Cross-references between documents should use relative paths.  
- Future revisions may group documents into formal “deliverables” for W3C submission.  
- Vocabulary documents should remain stable once incorporated into JSON-LD contexts.


============================================================
12. Contact
============================================================

Editors and contributors should coordinate through the Semantic Agent Communication Community Group communication channels.  
Feedback, issues, and pull requests are welcome.
