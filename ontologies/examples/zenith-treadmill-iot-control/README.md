# BH Treadmill IoT Control Use Case

## Introduction
This use case demonstrates how the Agent Ontology can be applied to the Internet of Things (IoT) domain, specifically for controlling a physical device. It models a Zenith Treadmill as an autonomous agent, capable of receiving commands, executing actions, and reporting its status. This scenario highlights how a user can securely delegate control of their personal device to a third-party application, enabling a rich, integrated ecosystem of fitness services while maintaining user control and security.

## User Story: Delegating Treadmill Control to a Third-Party Fitness App

**As a** user of a Zenith smart treadmill,
**I want to** authorize a third-party fitness application (e.g., "FitTrack Pro") to control my treadmill's speed and incline during a guided workout session,
**so that** I can have a seamless, hands-free, and interactive training experience.

## Key Concepts Illustrated
This use case effectively demonstrates several core concepts of the Agent Ontology:
*   **Agent**: The Zenith Treadmill itself is modeled as a `core:Agent` (`:ZenithTreadmillAgent`), representing a physical device with a digital identity and capabilities.
*   **Intent**: The user's high-level goal, e.g., "Start a 30-minute hill climb workout using FitTrack Pro."
*   **Delegation**: The core of this use case. The user, through a primary control interface (like the BH mobile app or the treadmill's console), creates a `delegation:Delegation` to grant the "FitTrack Pro" agent limited, revocable control over the treadmill.
*   **Capability**: The specific functions the treadmill agent can perform, such as `SetSpeed`, `SetIncline`, and `GetWorkoutData`. The `delegationScope` will be limited to these capabilities.
*   **Action**: The execution of a specific command by the treadmill agent, e.g., setting the speed to 10 km/h.
*   **Artifact**: The output from an action, such as a "Workout Data Report" containing metrics like distance, time, and calories burned.
*   **SecurityBinding**: Ensures that commands sent from the authorized third-party app are authentic and have not been tampered with, likely using a signed JWT or a similar mechanism.

## Workflow Breakdown and Ontology Mapping:

### 1. User Initiates a Guided Workout
-   **Description**: The user opens the "FitTrack Pro" application on their phone and selects a guided workout. The app needs to connect to and control the user's BH treadmill.
-   **Ontology Mapping**: The user's action creates a `core:Intent` with an `intent:objective` like "Complete the 'Andes Ascent' guided workout."

### 2. Authorization and Delegation Request
-   **Description**: The "FitTrack Pro" app (represented by `:FitTrackProAgent`) discovers the user's `:ZenithTreadmillAgent` and requests permission to control it for the duration of the workout.
-   **Ontology Mapping**: The `:FitTrackProAgent` requests a `delegation:Delegation`. This request is presented to the user for approval via the primary BH control interface.

### 3. User Grants Limited Control
-   **Description**: The user is prompted on their Zenith app or the treadmill console: "Allow 'FitTrack Pro' to control speed and incline for this session?" The user approves.
-   **Ontology Mapping**: A `delegation:Delegation` instance is created.
    *   `delegation:delegatedBy`: The user's primary agent (e.g., `:UserControlAgent` or the `:BHTreadmillAgent` itself, acting on behalf of the owner).
    *   `delegation:delegatesTo`: `:FitTrackProAgent`.
    *   `delegation:delegationScope`: A precise set of capabilities, e.g., ["SetSpeed", "SetIncline"]. It might also include constraints, such as a maximum speed limit or a time limit for the delegation's validity.

### 4. Third-Party App Executes Control Actions
-   **Description**: During the workout, the "FitTrack Pro" app sends commands to the treadmill to adjust speed and incline according to the pre-programmed session.
-   **Ontology Mapping**: The `:FitTrackProAgent` initiates `core:Action` instances, such as "Set Speed to 10 km/h." Each action must be performed within the `core:contextOf` the granted `Delegation`. The commands would be cryptographically signed, and this is modeled via a `security:SecurityBinding` on the action or its context.

### 5. Treadmill Agent Executes Physical Actions
-   **Description**: The `:ZenithTreadmillAgent` receives the signed commands, verifies that they are from an authorized delegate (`:FitTrackProAgent`) and that the requested action is within the `delegationScope`. If valid, it executes the physical action (e.g., increases the motor speed).
-   **Ontology Mapping**: The `:BHTreadmillAgent` validates the incoming `Action` against the `Delegation`'s scope. Successful execution results in a change of the physical device's state.

### 6. Data Reporting and Workout Completion
-   **Description**: Throughout the session, the treadmill reports workout data back to the "FitTrack Pro" app. At the end of the workout, the delegation is revoked or expires.
-   **Ontology Mapping**: The `:ZenithTreadmillAgent` can perform a `core:Action` like "Report Workout Data," which `core:producesArtifact` in the form of a data log. Upon workout completion, the `Delegation` becomes invalid, and the `:FitTrackProAgent` can no longer control the treadmill.

## Ontology Instance Example (`bh-treadmill.ttl` / `.jsonld`)

The provided `.ttl` and `.jsonld` files in this directory define the `:ZenithTreadmillAgent` and its core profile, including its identity, purpose, and capabilities. The example illustrates the agent's state and how it can be controlled through the semantic structures defined in the ontology.
