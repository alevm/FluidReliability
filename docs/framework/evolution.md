---
layout: default
title: Evolution Through Cycles
description: How the Fluid Reliability Framework evolved through three major organizational transformations
---

# Evolution Through Three Organizational Cycles

The framework evolved through **cyclic, iterative, and fractal** application rather than linear deployment. Each cycle executed all five foundational phases, adapting to context while maintaining core principles.

![Framework Timeline]({{ '/assets/images/timeline.png' | relative_url }})
<p class="image-caption">Fluid Reliability Framework Timeline (2019-2025)</p>

---

## Cycle 1: e-Builder Standalone (2019–2021)

<div class="timeline">
<div class="timeline-item">
<span class="timeline-date">2019–2021</span>
<h4>Origin Laboratory</h4>

**Context**: Full autonomy with need to rebuild engineering culture around resilience.

**Execution Highlights**:
- Gatekeeping introduced structured triage and Kanban-style visual queues
- Rotational patterns developed internally to reduce siloing
- Quarterly organizational shape reviews established
- Early automation pipelines and Terraform adoption reduced TOIL
- Partnerships with xOps teams created L1 support boundaries

**Outcomes**: SRE became proactive, engineering morale improved, internal trust in ops processes rose significantly.
</div>
</div>

---

## Cycle 2: PPM Franchise (2021–Mid 2022)

<div class="timeline">
<div class="timeline-item">
<span class="timeline-date">2021–2022</span>
<h4>Merger Integration</h4>

**Context**: Merger with ProjectSight, Proliance, and Prolog requiring scaling across multiple platforms with differing maturity.

**Execution Highlights**:
- Rotation across product boundaries distributed SRE culture
- Semipermeable roles provided consistent visibility and boundary definition
- Shared Kanban boards enabled visibility across siloed teams and geographies
- Service cataloging and automation enabled platform-wide support abstraction
- Clear xOps collaboration model maintained escalation control

**Outcomes**: Model proved scalable and interoperable across legacy product stacks.
</div>
</div>

---

## Cycle 3: Unity Suite (Mid 2022–Present)

<div class="timeline">
<div class="timeline-item">
<span class="timeline-date">2022–Present</span>
<h4>Multi-Product Convergence</h4>

**Context**: Larger multi-product convergence with Cityworks, AgileAssets, and Utilities incorporating new cloud models.

**Execution Highlights**:
- All five phases reapplied with institutional memory
- Gatekeeping scaled with automated triage pipelines and shared dashboards
- IaC standardized infrastructure across divergent environments
- Resource Pooling matured with dynamic staff deployment backed by data
- xOps became full partner—support, infra, and platform teams worked as mesh
- Increased visibility exposed tribal practices, enhancing security posture

**Outcomes**: Fluid Reliability proved portable, scalable, and deeply resilient, becoming the cultural backbone of SRE through successive integrations.
</div>
</div>

---

## The Fractal Nature

Each cycle demonstrates a key insight: the framework operates **fractally**. The same five pillars apply at different scales:

![Fractal Timeline]({{ '/assets/images/fractal-timeline.png' | relative_url }})
<p class="image-caption">Fractal view: The same patterns repeat at individual, team, and organization levels</p>

| Scale | Protect | Prepare | Pulse | Pool | Promote |
|-------|---------|---------|-------|------|---------|
| **Individual** | Shield from interrupts | Cross-train skills | Regular 1:1s | Share expertise | Recognize growth |
| **Team** | Triage incoming work | Rotation programs | Sprint retros | Resource sharing | Team rituals |
| **Organization** | Gatekeeping function | Follow-the-Sun | Quarterly reviews | Talent pooling | Culture carriers |

---

## Current Experiments and Continuous Evolution

### Workload Categorization and Analysis

Systematic Jira categorization to:
- Identify distinct workstreams (improvements, support, service requests)
- Uncover data-driven insights for resource allocation
- Enhance predictive capacity for delivery timelines
- Distribute workload types evenly across team members

### Value-Driven Epic Refinement

Transitioning from time-bound to value-centric approach:
- Keep Epics open until business value is realized
- Treat Jira stories as units of deliverable value
- Promote iterative value delivery through smaller, consumable pieces

### Strategic Epic Prioritization

Moving from "sprinkle and hope" to focused strategy:
- Clearly prioritized Epic queue with dedicated resources
- Committed resource allocation ensuring continuity
- Accelerated high-value feature delivery

---

## Key Learnings

> "Each merger that could have fractured us instead made us more cohesive, because the framework was designed to metabolize change."

1. **Prediction preceded outcome**: The 2023 proposal documented hypotheses before validation
2. **Stakeholder concerns became success criteria**: Every objection we documented became a validation target
3. **Theoretical grounding shaped design choices**: References to Luhmann, Olivetti, and systems thinking weren't decorative—they guided implementation
4. **Rotation is an organizational primitive**: It re-nerves a severed organization

---

<div class="card-grid">
  <a href="{{ '/framework/' | relative_url }}" class="card-link">
    <div class="card">
      <h3>← Back to Framework</h3>
      <p>Review the five core pillars and technical enablers.</p>
    </div>
  </a>

  <a href="{{ '/evidence/' | relative_url }}" class="card-link">
    <div class="card">
      <h3>Evidence & Results →</h3>
      <p>See the quantified outcomes from each cycle.</p>
    </div>
  </a>
</div>
