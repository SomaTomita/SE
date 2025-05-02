# Requirements Elicitation Techniques – Detailed Reference

_A practical handbook for analysts, product managers, and UX researchers_

---

## Table of Contents

1. Interviews
2. Questionnaires
3. Facilitated Workshops
4. Customer Working Groups (CWGs)
5. Stakeholder Viewpoint Analysis
6. Brainstorming
7. Joint Application Development (JAD)
8. Requirements Workshops (Variants & Focus Groups)
9. Ethnography & Contextual Inquiry
10. Requirements Prioritization Techniques
11. Goal-Driven Elicitation

---

## 1. Interviews

_The most traditional and commonly used technique for requirements elicitation._

|                    |                                                                                                                                                                   |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Definition**     | A systematic conversation where an interviewer gathers information from stakeholders through direct questioning and discussion.                                   |
| **Types**          | • Unstructured: Conversational, exploratory, minimal control<br>• Structured: Predetermined questions, specific focus<br>• Semi-structured: Balanced combination  |
| **Best For**       | • Initial requirements gathering<br>• Stakeholder perspective understanding<br>• Detailed domain knowledge extraction<br>• Clarifying ambiguous requirements      |
| **Key Strengths**  | • Efficient collection of large amounts of data<br>• Direct interaction allows immediate clarification<br>• Flexibility to explore unexpected insights            |
| **Watch-outs**     | • Success depends heavily on interviewer skill<br>• Risk of focusing too much on some areas, neglecting others<br>• Structured interviews may limit new ideas     |
| **Best Practices** | • Prepare question templates (e.g., Volere)<br>• Record and transcribe for accuracy<br>• Follow up for clarification<br>• Mix different interview types as needed |
| **Example**        | A healthcare system project used structured interviews with doctors for clinical workflows, and unstructured interviews with patients for usability requirements. |

---

## 2. Questionnaires

_An efficient tool for gathering information from multiple stakeholders in early stages._

|                    |                                                                                                                                                                  |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Definition**     | Structured documents containing open and/or closed questions distributed to stakeholders to collect requirements-related information.                            |
| **Types**          | • Closed Questions: Multiple choice, ratings, rankings<br>• Open Questions: Free-text responses<br>• Mixed Format: Combination of both                           |
| **Best For**       | • Early requirements gathering<br>• Large stakeholder groups<br>• Geographically distributed teams<br>• Baseline data collection                                 |
| **Key Strengths**  | • Efficient collection from many stakeholders<br>• Standardized format for easy analysis<br>• Cost-effective for large groups<br>• Good for statistical analysis |
| **Limitations**    | • No opportunity for immediate clarification<br>• Limited depth of information<br>• Risk of misinterpretation<br>• Cannot explore new ideas dynamically          |
| **Best Practices** | • Define clear scope and objectives<br>• Use simple, unambiguous language<br>• Pilot test before full distribution<br>• Include space for additional comments    |
| **Example**        | An enterprise software upgrade project used questionnaires to gather initial requirements from 500+ users across 50 departments, identifying common pain points. |

---

## 3. Facilitated Workshops

|                     |                                                                                                                                                                                |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Definition**      | Time-boxed, highly structured sessions where a neutral facilitator guides cross-functional stakeholders to co-create requirements artifacts (e.g., story maps, domain models). |
| **Typical Inputs**  | High-level scope statement, stakeholder list, pre-read user scenarios.                                                                                                         |
| **Typical Outputs** | Agreed problem statement, prioritised feature list, preliminary acceptance criteria.                                                                                           |
| **Ideal When**      | • You need consensus across business, UX, and tech fast.<br>• The backlog is large and fuzzy.<br>• Calendar time is critical.                                                  |
| **Tool Support**    | Miro, Mural, Jira whiteboards, EventStorming canvases.                                                                                                                         |
| **Example**         | In an e-health project, a two-day workshop surfaced data-privacy constraints early, avoiding a later re-architecture.                                                          |
| **Watch-outs**      | Guard against scope creep; schedule short "cool-down" reviews to refine hurried artefacts.                                                                                     |

---

## 4. Customer Working Groups (CWGs)

_Long-running panels of real customers who collaborate with product management across releases._

- **Mechanics** Quarterly deep-dives + monthly check-ins. CWG members preview UX prototypes, rank backlog items, and validate road-map shifts.
- **Value Add** Domain realism, pragmatic prioritisation, marketing advocacy (super-users often become champions).
- **Governance Tip** Sign a Terms-of-Reference (ToR) agreeing on NDA, decision scope, and feedback cycle to avoid "road-map whiplash."
- **Case Example** A B2B SaaS vendor cut churn 15 % by letting a CWG steer reporting-feature increments over three releases.

---

## 5. Stakeholder Viewpoint Analysis

_Organises requirements by "who sees the system how."_

1. **Identify Viewpoints** – roles, personas, regulators, downstream ops teams.
2. **Capture Concerns** – goals, fears, compliance rules, KPIs.
3. **Reconcile Conflicts** – e.g., "Ops needs zero-downtime deployments" vs. "Finance wants monthly release gates."
4. **Outputs** – Viewpoint matrix, conflict log, traceability links to requirements items.
   > **Tip:** Pair with ArchiMate or SysML views to keep design traceable.

---

## 6. Brainstorming

_A collaborative technique for rapid idea generation through informal group discussion._

|                          |                                                                                                                               |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| **Purpose**              | Rapid generation of ideas without immediate critique or detailed exploration                                                  |
| **Key Principles**       | • No immediate criticism of ideas<br>• Quantity over quality<br>• Build on others' ideas<br>• Encourage innovative thinking   |
| **Best For**             | • Early project stages<br>• Mission statement development<br>• Problem exploration<br>• Innovation seeking                    |
| **Facilitation Tips**    | • "Round-robin" for equal participation<br>• Time-boxed "silent ideation"<br>• Visual documentation<br>• Encourage wild ideas |
| **Common Outputs**       | • Initial mission statements<br>• Problem space exploration<br>• Innovation opportunities<br>• Preliminary solution ideas     |
| **Success Factors**      | • Diverse participant mix<br>• Safe environment for sharing<br>• Clear scope and objectives<br>• Effective idea capture       |
| **Follow-up Activities** | • Idea clustering<br>• Priority setting<br>• Detailed analysis in other forums<br>• Action item assignment                    |

---

## 7. Joint Application Development (JAD)

_A structured group technique for rapid requirements definition and decision-making._

|                         |                                                                                                                                                                |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Definition**          | A structured group process focusing on business and user needs, with predefined steps and roles for rapid decision-making.                                     |
| **When to Use**         | • After high-level goals are established<br>• When rapid decisions are needed<br>• For business-focused requirements<br>• When stakeholder availability allows |
| **Core Roles**          | • Executive sponsor<br>• Business owner<br>• End-user representatives<br>• Solution architect<br>• Specialist facilitator<br>• Scribe                          |
| **Session Structure**   | • Pre-session preparation<br>• Structured discussion phases<br>• Decision-making points<br>• Action item documentation                                         |
| **Key Differentiators** | • More structured than brainstorming<br>• Business/user focus over technical<br>• Rapid decision-making emphasis<br>• Professional facilitation                |
| **Best Practices**      | • Clear agenda and objectives<br>• Right stakeholder mix<br>• Proper documentation<br>• Immediate decision implementation                                      |
| **When to Avoid**       | • Early concept stages<br>• Highly political situations<br>• When key stakeholders unavailable<br>• Regulatory environments requiring formal documentation     |

---

## 8. Requirements Workshops & Focus Groups

_Specialized group meetings focused on requirements development and discovery._

### Types of Requirements Workshops

1. **Cross-Functional Workshops**

   - Participants from different business areas
   - Focus on business process mapping
   - Integration point identification
   - End-to-end requirement validation

2. **Co-operative Requirements Capture (CRC)**

   - Structured activities and deliverables
   - Strong development community involvement
   - Use-case walkthroughs
   - Object-role modeling
   - Technical feasibility assessment

3. **Creativity Workshops**

   - Innovation-focused sessions
   - SCAMPER technique application
   - Crazy 8s ideation
   - Future scenario exploration
   - Out-of-box thinking encouragement

4. **Focus Groups**
   - Market research orientation
   - 8–12 target users per session
   - Concept demonstration and feedback
   - Iterative refinement
   - Marketing-driven insights

### Workshop Components

|                     |                                                                                                              |
| ------------------- | ------------------------------------------------------------------------------------------------------------ |
| **Planning**        | • Participant selection<br>• Agenda development<br>• Pre-work distribution<br>• Logistics arrangement        |
| **Execution**       | • Clear objective setting<br>• Structured activities<br>• Time management<br>• Documentation capture         |
| **Deliverables**    | • Requirements documentation<br>• Process models<br>• Decision logs<br>• Action items                        |
| **Success Factors** | • Skilled facilitation<br>• Appropriate participant mix<br>• Clear scope definition<br>• Effective follow-up |

### Best Practices

1. **Preparation**

   - Define clear objectives
   - Select appropriate participants
   - Distribute pre-reading materials
   - Prepare facilitation materials

2. **Execution**

   - Start with clear ground rules
   - Maintain focused discussions
   - Document decisions real-time
   - Manage time effectively

3. **Follow-up**
   - Distribute workshop minutes
   - Track action items
   - Validate outcomes
   - Plan next steps

---

## 9. Ethnography & Contextual Inquiry

### Ethnography (Long-form)

- Analyst immerses in the workplace for days/weeks.
- **Strengths** Uncovers tacit workarounds and cultural norms; vital when replacing legacy line-of-business tools.
- **Output** Rich stories, swim-lane diagrams detailing role interactions, pain-point heat-maps.

### Contextual Inquiry (Short-form)

1. "Master–apprentice" interview while user performs real task.
2. Ask "Why?" after each micro-step.
3. Capture artifacts (screenshots, paper forms).  
   _Produces actionable UI tweaks and task-time metrics._

---

## 10. Requirements Prioritization Techniques

| Technique            | Best For                      | How It Works                                                              | Caveats                                                 |
| -------------------- | ----------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------- |
| **MoSCoW**           | Fast backlog grooming         | 4-bucket sort                                                             | Prone to "everything is a Must."                        |
| **100-Point Method** | Mid-size stakeholder groups   | Each member spends 100 points across items                                | Needs facilitation to avoid "points inflation."         |
| **AHP / Pair-wise**  | Complex, high-stakes projects | Compare every item against every other on set criteria; derive weightings | O(n²) scaling pain; use software (e.g., Expert Choice). |
| **Kano**             | User satisfaction mapping     | Classify Must-Be, Performance, Delighters                                 | Qualitative; best with survey sample ≥ 30.              |

---

## 11. Goal-Driven Elicitation

_The fundamental approach that drives the entire requirements engineering process by focusing on the "why" behind system requirements._

### Overview

Goal-driven approaches are essential in requirements engineering for several reasons:

- They help overcome traditional approaches' limitations that often lead to technically sound but functionally inadequate systems
- They establish intentional relationships between the usage world and system world
- They address both domain requirements (facts of nature) and user-defined requirements (stakeholder intentions)

|                      |                                                                                                                                                                        |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Definition**       | A systematic approach that identifies, models, and reasons about the objectives that a system must achieve, driving the entire requirements engineering process.       |
| **Key Benefits**     | • Systematic exploration of design choices<br>• Requirements completeness verification<br>• Pre-traceability assurance<br>• Early detection of conflicts and risks     |
| **Process Steps**    | • Goal elicitation and refinement<br>• Goal modeling and specification<br>• Goal-based reasoning<br>• Goal operationalization into requirements                        |
| **Practical Impact** | Studies show 60-70% of system failures are due to poor requirements. Goal-driven approaches help address this by ensuring requirements align with business objectives. |

### Goal Elicitation Process

| Step                           | Description                                                    | Example                                          | Key Considerations                            |
| ------------------------------ | -------------------------------------------------------------- | ------------------------------------------------ | --------------------------------------------- |
| **Elicit Goals (Why)**         | Interview execs, analyse strategy docs, extract OKRs.          | "Reduce claims processing time by 50%."          | Consider both current and future conditions   |
| **Refine to Sub-goals**        | Break into measurable objectives.                              | Automate fraud-check, parallelise document scan. | Ensure hierarchical decomposition is complete |
| **Derive Requirements (What)** | Translate each leaf goal into functional/quality requirements. | API latency ≤ 200 ms, OCR confidence ≥ 95%.      | Map to concrete system features               |
| **Design Exploration (How)**   | Compare solution options via goal-satisfaction matrices.       | Microservice vs. monolith scores.                | Consider variability in implementation        |
| **Traceability Links**         | <goal-id> ↔ <req-id> ↔ <design-decision-id>                    | Ensures future change impact analysis.           | Maintain bidirectional traceability           |

### Variability Handling

Modern software systems must address:

- Multi-purpose nature across different organizations
- Adaptability to different usage scenarios
- Customization for various stakeholder groups

| Aspect                | Consideration                                   |
| --------------------- | ----------------------------------------------- |
| **Goal Models**       | Must explicitly represent variability points    |
| **Reasoning Process** | Must support selection of appropriate variants  |
| **Implementation**    | Must enable configuration for specific contexts |

### Best Practices

1. **Goal Identification**

   - Start with high-level strategic goals
   - Consider both internal operations and external market factors
   - Document the "why" behind each requirement

2. **Goal Refinement**

   - Use AND/OR decomposition for systematic breakdown
   - Apply "Why" and "How" questioning techniques
   - Validate refinements with stakeholders

3. **Conflict Resolution**

   - Identify conflicting goals early
   - Document trade-offs and decisions
   - Use goal satisfaction analysis

4. **Traceability Management**
   - Maintain links between goals and requirements
   - Document impact of changes
   - Enable backward and forward tracing

### Common Pitfalls

- Over-focusing on system features without clear goals
- Insufficient stakeholder involvement in goal definition
- Inadequate handling of goal conflicts
- Poor documentation of goal-requirement relationships

---

## Cross-Cutting Analyst Skills

1. **Facilitation & Group Dynamics** – keep discussions inclusive, time-boxed.
2. **Conflict Mediation** – seek "win-conditions," document trade-offs openly.
3. **Visual Modelling** – BPMN, C4, story-mapping.
4. **Lean Documentation** – write just enough for downstream dev, QA, and audit.

---

### Quick Technique-Selection Cheat-Sheet

| Project Characteristic      | Recommended Mix                                                 |
| --------------------------- | --------------------------------------------------------------- |
| Green-field, fuzzy scope    | Brainstorm → Creativity WS → Goal-driven modelling              |
| Regulated, multi-site       | Viewpoint analysis → Facilitated workshops → AHP prioritisation |
| Mature product, new module  | CWG → JAD → Focus group validation                              |
| Mission-critical ops revamp | Ethnography → Viewpoint analysis → Goal traceability            |
