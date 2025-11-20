# Using the Agent Ontology with Schema.org for App and SaaS Developers

## 1. Why Describe Your Service with the Agent Ontology?

As a developer, you build applications and services with specific capabilities. The **Agent Ontology**, when used with Schema.org, provides a standard vocabulary to describe these capabilities so they can be understood and utilized within a broad ecosystem of **Agents**.

Crucially, an "Agent" in this context is not limited to software. It can be:
- **A Software Agent**: Your SaaS API, application, or AI model.
- **A Human Agent**: An individual expert, freelancer, or employee.
- **An Organizational Agent**: A company, a specific department, or a community group.

By adding a small block of JSON-LD to your website, you allow your service to interact within this rich ecosystem, enabling:

- **Enhanced Discoverability**: Allow other agents (AI, human, or organizational) to find your service when they need its specific function.
- **Automated Interoperability**: A common vocabulary allows different types of agents to understand and delegate tasks to each other, paving the way for complex, automated workflows.
- **Clear Accountability**: Clearly defining an agent's identity and functions is foundational for building a trustworthy and accountable ecosystem, where it's clear who or what is responsible for an action.

This document provides practical examples of how to describe your SaaS API or software application as an Agent.

## 2. Link to Ontology and Documentation

- **Stable Namespace URI**: `https://w3id.org/agent-ontology/`
- **GitHub Repository (Source of Truth)**: [https://github.com/w3c-cg/agent-ontology](https://github.com/w3c-cg/agent-ontology)
- **Human-Readable Documentation (Generated)**: [https://s-agent-comm.github.io/agent-ontology/](https://s-agent-comm.github.io/agent-ontology/)

The ontology is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/), which is compatible with Schema.org's terms.

## 3. Core Concepts for Developers

The ontology provides a unified model for different types of agents.

- **Agent (`agent:Agent`)**: The core concept. An autonomous entity with a verifiable identity that can perform actions. This is the parent class for software, people, and organizations.
- **Person (`agent:Person`)**: Represents a human agent. As a developer, you might use this to describe the author of a tool, a support contact, or a human expert whose skills are being represented. Mapped to `schema:Person`.
- **Organization (`agent:Organization`)**: Represents an organizational agent. This is typically used to describe the company or team that provides the software or service. Mapped to `schema:Organization`.
- **Capability (`cap:Capability`)**: A high-level, human-readable description of a function an agent can perform (e.g., "book a flight," "provide legal advice"). Mapped to `schema:Action`.
- **Skill (`cap:Skill`)**: The specific, machine-executable operation that implements a capability. For a software agent, this is where you link to your technical documentation (e.g., an OpenAPI endpoint ID). For a human agent, this might link to a contact form or booking page.
- **Identity (`id:AgentIdentity`)**: A verifiable identity for an agent, such as a Decentralized Identifier (DID), which helps establish trust.

As a developer describing a service, you will primarily focus on describing your `schema:Service` or `schema:SoftwareApplication` as a type of `agent:Agent`.

## 4. Example Usage for Developers

Here are two practical examples of how you can use the combined vocabularies.

### Example 1: Describing a SaaS API

If you offer a "Travel API," you can add the following JSON-LD to your developer portal or marketing site. This allows an AI agent marketplace or an orchestrator to discover your API and understand its capabilities.

```html
<script type="application/ld+json">
{
  "@context": {
    "schema": "http://schema.org/",
    "agent": "https://w3id.org/agent-ontology/agent#",
    "cap": "https://w3id.org/agent-ontology/capability#",
    "id": "https://w3id.org/agent-ontology/identity#"
  },
  "@type": ["schema:Service", "agent:Agent"],
  "schema:name": "Travel API",
  "schema:description": "A SaaS API for finding and booking flights and hotels.",
  "schema:provider": {
    "@type": "schema:Organization",
    "schema:name": "Global Travel Inc."
  },
  "agent:hasIdentity": {
    "@type": "id:AgentIdentity",
    "id:did": "did:key:z6MkpTHR8VNsBxYAAWHut2Geadd9jSwuBV8xRoAnwWsdvktH",
    "id:title": "Travel API Identity"
  },
  "core:hasCapability": [
    {
      "@type": "cap:Capability",
      "cap:capabilityExpression": "Find and book flights",
      "cap:hasSkill": {
        "@type": "cap:Skill",
        "cap:skillId": "api.travel.searchFlights",
        "cap:description": "Searches for available flights between two cities on a given date."
      }
    }
  ]
}
</script>
```

### Example 2: Describing a Software Application

If you've developed a web-based "Image Editor" application, you can describe its features so that an OS-level agent or another service could automate tasks within it.

```html
<script type="application/ld+json">
{
  "@context": {
    "schema": "http://schema.org/",
    "agent": "https://w3id.org/agent-ontology/agent#",
    "cap": "https://w3id.org/agent-ontology/capability#"
  },
  "@type": ["schema:SoftwareApplication", "agent:Agent"],
  "schema:name": "PhotoSpark Image Editor",
  "schema:description": "A web-based application for editing and enhancing photos.",
  "schema:author": {
    "@type": "schema:Organization",
    "schema:name": "Creative Software LLC"
  },
  "core:hasCapability": [
    {
      "@type": "cap:Capability",
      "cap:capabilityExpression": "Resize an image",
      "cap:hasSkill": {
        "@type": "cap:Skill",
        "cap:skillId": "photospark.resizeImage",
        "cap:description": "Changes the dimensions of an image to a specified width and height."
      }
    },
    {
      "@type": "cap:Capability",
      "cap:capabilityExpression": "Apply a visual filter",
      "cap:hasSkill": {
        "@type": "cap:Skill",
        "cap:skillId": "photospark.applyFilter"
      }
    }
  ]
}
</script>
```

## 5. It's a Semantic Layer, Not a Replacement for OpenAPI

It is important to clarify that the Agent Ontology provides a **semantic description** of your service's capabilities, not a replacement for your existing technical specifications.

-   **Agent Ontology (The "What")**: Defines *what* your service is and *what* it can do in a standard, machine-readable way. It's like a universal "menu" of its functions.
-   **OpenAPI/GraphQL (The "How")**: Defines *how* a specific `cap:Skill` is technically executed, including API endpoints, request/response formats, and authentication.

The two are complementary. The Agent Ontology allows an agent to *discover* your service and *understand* its purpose. The `cap:skillId` can then be used to link directly to your OpenAPI definition or other technical documentation, which provides the precise instructions for making the API call.

## 6. Community and Maintenance

The Agent Ontology is actively maintained by the W3C Semantic Agent Communication Community Group. We are committed to the long-term stability and evolution of this vocabulary to meet the needs of the AI and web developer communities. By adopting it, you are helping to build a more interoperable and discoverable ecosystem of AI agents and services on the web.