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
- **GitHub Repository (Source of Truth)**: [https://github.com/s-agent-comm/agent-ontology](https://github.com/s-agent-comm/agent-ontology)
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

### Example 3: Describing an AI Agent

If you've developed an AI Agent that can provide personalized recommendations, you can describe its capabilities to allow other agents or platforms to delegate recommendation tasks to it.

```html
<script type="application/ld+json">
{
  "@context": {
    "schema": "http://schema.org/",
    "agent": "https://w3id.org/agent-ontology/agent#",
    "cap": "https://w3id.org/agent-ontology/capability#",
    "id": "https://w3id.org/agent-ontology/identity#"
  },
  "@type": ["schema:Thing", "agent:Agent"],
  "schema:name": "Personalized Recommendation AI",
  "schema:description": "An AI agent that provides personalized product or content recommendations.",
  "agent:hasIdentity": {
    "@type": "id:AgentIdentity",
    "id:did": "did:key:z6MkoPZ24eY8VNsBxYAAWHut2Geadd9jSwuBV8xRoAnwWsdvktH",
    "id:title": "Recommendation AI Identity"
  },
  "core:hasCapability": [
    {
      "@type": "cap:Capability",
      "cap:capabilityExpression": "Generate product recommendations",
      "cap:hasSkill": {
        "@type": "cap:Skill",
        "cap:skillId": "ai.recommendation.products",
        "cap:description": "Generates a list of product recommendations based on user preferences and history."
      }
    },
    {
      "@type": "cap:Capability",
      "cap:capabilityExpression": "Suggest content for users",
      "cap:hasSkill": {
        "@type": "cap:Skill",
        "cap:skillId": "ai.recommendation.content",
        "cap:description": "Suggests articles, videos, or other content tailored to a user's interests."
      }
    }
  ]
}
</script>
```

### Example 4: Describing an AI Employee

If you have an AI system acting as a virtual employee (e.g., a customer support bot, a data analyst bot), you can describe its role and capabilities as an `agent:Person` or `agent:Organization`.

```html
<script type="application/ld+json">
{
  "@context": {
    "schema": "http://schema.org/",
    "agent": "https://w3id.org/agent-ontology/agent#",
    "cap": "https://w3id.org/agent-ontology/capability#",
    "id": "https://w3id.org/agent-ontology/identity#"
  },
  "@type": ["schema:Person", "agent:Agent"],
  "schema:name": "Customer Support AI (Bot)",
  "schema:description": "An AI-powered virtual assistant for handling customer inquiries and providing support.",
  "agent:hasIdentity": {
    "@type": "id:AgentIdentity",
    "id:did": "did:key:z6MkoPZ24eY8VNsBxYAAWHut2Geadd9jSwuBV8xRoAnwWsdvktH",
    "id:title": "Customer Support AI Identity"
  },
  "core:hasCapability": [
    {
      "@type": "cap:Capability",
      "cap:capabilityExpression": "Answer frequently asked questions",
      "cap:hasSkill": {
        "@type": "cap:Skill",
        "cap:skillId": "ai.support.faq",
        "cap:description": "Provides answers to common customer questions based on a knowledge base."
      }
    },
    {
      "@type": "cap:Capability",
      "cap:capabilityExpression": "Process return requests",
      "cap:hasSkill": {
        "@type": "cap:Skill",
        "cap:skillId": "ai.support.returns",
        "cap:description": "Guides users through the product return process and initiates return labels."
      }
    }
  ]
}
</script>
```

### Example 5: Describing an AI Engineering Manager

An AI system designed to assist with engineering management tasks can be described as an `agent:Person` or `agent:Organization` with specific capabilities related to project oversight, team coordination, and technical guidance.

```html
<script type="application/ld+json">
{
  "@context": {
    "schema": "http://schema.org/",
    "agent": "https://w3id.org/agent-ontology/agent#",
    "cap": "https://w3id.org/agent-ontology/capability#",
    "id": "https://w3id.org/agent-ontology/identity#"
  },
  "@type": ["schema:Person", "agent:Agent"],
  "schema:name": "AI Engineering Manager",
  "schema:description": "An AI assistant for engineering managers, providing insights into project progress, team performance, and technical debt.",
  "agent:hasIdentity": {
    "@type": "id:AgentIdentity",
    "id:did": "did:key:z6MkoPZ24eY8VNsBxYAAWHut2Geadd9jSwuBV8xRoAnwWsdvktH",
    "id:title": "AI Engineering Manager Identity"
  },
  "core:hasCapability": [
    {
      "@type": "cap:Capability",
      "cap:capabilityExpression": "Monitor project progress",
      "cap:hasSkill": {
        "@type": "cap:Skill",
        "cap:skillId": "ai.em.projectProgress",
        "cap:description": "Tracks the progress of engineering projects, identifies bottlenecks, and predicts completion times."
      }
    },
    {
      "@type": "cap:Capability",
      "cap:capabilityExpression": "Analyze team performance",
      "cap:hasSkill": {
        "@type": "cap:Skill",
        "cap:skillId": "ai.em.teamPerformance",
        "cap:description": "Evaluates individual and team performance metrics to suggest areas for improvement."
      }
    },
    {
      "@type": "cap:Capability",
      "cap:capabilityExpression": "Identify technical debt",
      "cap:hasSkill": {
        "@type": "cap:Skill",
        "cap:skillId": "ai.em.technicalDebt",
        "cap:description": "Scans codebase and development practices to identify and quantify technical debt."
      }
    }
  ]
}
</script>
```

### Example 6: Describing an AI-Powered Product Division

An entire department or product line run by AI can be described as an `agent:Organization`. This allows for the representation of complex business units that are partially or fully automated.

```html
<script type="application/ld+json">
{
  "@context": {
    "schema": "http://schema.org/",
    "agent": "https://w3id.org/agent-ontology/agent#",
    "cap": "https://w3id.org/agent-ontology/capability#",
    "id": "https://w3id.org/agent-ontology/identity#"
  },
  "@type": ["schema:Organization", "agent:Agent"],
  "schema:name": "AI-Powered Product Division",
  "schema:description": "An autonomous division responsible for market analysis, product strategy, and financial reporting for a specific product line.",
  "agent:hasIdentity": {
    "@type": "id:AgentIdentity",
    "id:did": "did:key:z6MkoPZ24eY8VNsBxYAAWHut2Geadd9jSwuBV8xRoAnwWsdvktH",
    "id:title": "AI Product Division Identity"
  },
  "core:hasCapability": [
    {
      "@type": "cap:Capability",
      "cap:capabilityExpression": "Perform market analysis",
      "cap:hasSkill": {
        "@type": "cap:Skill",
        "cap:skillId": "ai.division.marketAnalysis",
        "cap:description": "Continuously analyzes market trends, competitor activities, and customer feedback."
      }
    },
    {
      "@type": "cap:Capability",
      "cap:capabilityExpression": "Develop product strategy",
      "cap:hasSkill": {
        "@type": "cap:Skill",
        "cap:skillId": "ai.division.productStrategy",
        "cap:description": "Formulates and adjusts product strategy based on market analysis and business goals."
      }
    },
    {
      "@type": "cap:Capability",
      "cap:capabilityExpression": "Generate financial reports",
      "cap:hasSkill": {
        "@type": "cap:Skill",
        "cap:skillId": "ai.division.financialReporting",
        "cap:description": "Automates the generation of financial reports, including revenue, costs, and profitability."
      }
    }
  ]
}
</script>
```

## 5. Encapsulating High-Level Capabilities: The "What" vs. The "How"

A crucial aspect of the Agent Ontology's design is the clear separation between a high-level `Capability` and its underlying `Skill` implementation. This allows Agents to encapsulate complex internal workflows and expose only their top-level functions to the broader ecosystem.

Consider an "AI Python Developer" Agent. On its "resume" (its `core:hasCapability` declarations), it might state:

```html
<script type="application/ld+json">
{
  "@context": {
    "schema": "http://schema.org/",
    "agent": "https://w3id.org/agent-ontology/agent#",
    "cap": "https://w3id.org/agent-ontology/capability#"
  },
  "@type": ["schema:Person", "agent:Agent"],
  "schema:name": "AI Python Developer",
  "schema:description": "An AI agent capable of developing, testing, and deploying Python applications.",
  "core:hasCapability": [
    {
      "@type": "cap:Capability",
      "cap:capabilityExpression": "Develop a new Python feature based on specifications",
      "cap:hasSkill": {
        "@type": "cap:Skill",
        "cap:skillId": "internal:python_feature_development_workflow",
        "cap:description": "Executes a comprehensive internal workflow including design, coding, testing, and deployment for Python features."
      }
    }
  ]
}
</script>
```

In this example:

*   **`cap:capabilityExpression` ("Develop a new Python feature...")**: This is the high-level "What" the Agent can do. It's a clear, human-readable promise of functionality.
*   **`cap:skillId` ("internal:python_feature_development_workflow")**: This points to an **internal** identifier or entry point within the AI Python Developer Agent. The external Agent requesting this capability doesn't need to know the specifics.
*   **Hidden Implementation Details**: The AI Python Developer Agent itself is responsible for how it achieves this capability. Internally, it might orchestrate multiple sub-skills:
    *   Writing code using specific libraries.
    *   Running unit tests with `pytest`.
    *   Formatting code with `black`.
    *   Committing changes to Git.
    *   Deploying to a cloud environment.

This encapsulation provides immense flexibility. The AI Python Developer Agent can change its internal tools or processes (e.g., switch from `pytest` to another testing framework) without affecting any external Agents that rely on its "Develop a new Python feature" capability. The external Agent only interacts with the declared `Capability`, simplifying inter-Agent communication and promoting a robust, modular ecosystem.

## 7. Collaboration between Department and Employee Agents: Discovery, Delegation, and Composition

The Agent Ontology facilitates a powerful collaboration model between high-level "Department" Agents and more specialized "Employee" Agents, mirroring real-world organizational structures. This collaboration is built upon the principles of **capability discovery, task delegation, and result composition**.

Consider an "AI-Powered Product Division" (a Department Agent) that needs to "Generate financial reports" (a high-level `Capability`).

1.  **High-Level Task Reception**: The Department Agent receives a request to perform its `Generate financial reports` capability.
2.  **Internal Task Decomposition**: The Department Agent's internal orchestration logic breaks down this complex task into smaller, manageable sub-tasks. For a financial report, this might include:
    *   Gathering sales data.
    *   Calculating operational costs.
    *   Analyzing market performance.
3.  **Capability Discovery and Delegation**: The Department Agent then acts as a coordinator. It discovers other specialized "Employee" Agents (e.g., an "AI Data Analyst" or an "AI Accountant") that possess the specific `Capabilities` required for each sub-task.
    *   It delegates "Gather sales data" to the "AI Data Analyst" Agent.
    *   It delegates "Calculate operational costs" to the "AI Accountant" Agent.
    *   Each delegation is a request for a specific `Capability` that the Employee Agent has declared.
4.  **Result Composition**: Once the Employee Agents complete their delegated tasks and return their respective results (e.g., raw sales figures, cost breakdowns), the Department Agent's composition logic integrates these pieces of information. It processes, formats, and synthesizes them into the final comprehensive financial report.
5.  **Delivery of High-Level Outcome**: The Department Agent then delivers the complete financial report as the outcome of its `Generate financial reports` capability to the original requester.

This model highlights:

*   **Department Agents as Orchestrators**: They manage complex workflows by understanding high-level goals, breaking them down, and coordinating specialized sub-agents.
*   **Employee Agents as Specialized Executors**: They focus on performing specific, well-defined `Capabilities` efficiently.
*   **Seamless Interoperability**: The entire collaboration relies on Agents understanding each other's declared `Capabilities`, without needing to know the intricate internal `Skill` implementations of each other. This promotes a modular, flexible, and scalable ecosystem where Agents can be easily added, updated, or replaced without disrupting the overall system.

## 8. It's a Semantic Layer, Not a Replacement for OpenAPI

It is important to clarify that the Agent Ontology provides a **semantic description** of your service's capabilities, not a replacement for your existing technical specifications.

-   **Agent Ontology (The "What")**: Defines *what* your service is and *what* it can do in a standard, machine-readable way. It's like a universal "menu" of its functions.
-   **OpenAPI/GraphQL (The "How")**: Defines *how* a specific `cap:Skill` is technically executed, including API endpoints, request/response formats, and authentication.

The two are complementary. The Agent Ontology allows an agent to *discover* your service and *understand* its purpose. The `cap:skillId` can then be used to link directly to your OpenAPI definition or other technical documentation, which provides the precise instructions for making the API call.

## 9. Community and Maintenance

The Agent Ontology is actively maintained by the W3C Semantic Agent Communication Community Group. We are committed to the long-term stability and evolution of this vocabulary to meet the needs of the AI and web developer communities. By adopting it, you are helping to build a more interoperable and discoverable ecosystem of AI agents and services on the web.
