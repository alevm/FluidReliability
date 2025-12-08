---
layout: default
title: Framework
description: Three-Tier Theoretical Architecture and Five Core Practices
---

# The Framework: Three-Tier Theoretical Architecture

The Fluid Reliability framework synthesizes six theoretical sources organized into three tiers:

- **Tier 1 (Foundation):** Luhmann's semipermeable boundaries + Olivetti's human-centered community — the WHY and WHAT
- **Tier 2 (Learning):** Argyris & Schön's double-loop learning + Rogers' diffusion — HOW change happens
- **Tier 3 (Implementation):** Ohno's TPS + Anderson's Kanban — HOW work flows

---

## Tier 1: Foundation — Luhmann + Olivetti

### Luhmann: Semipermeable Boundaries (1995)

**Key Insight:** Organizations are autopoietic systems that maintain identity through communication boundaries. These boundaries must be semipermeable—filtering noise while transmitting relevant signals.

| Concept | Framework Application |
|---------|----------------------|
| **Gatekeeping = The Membrane** | Not about blocking work, but intelligent signal processing |
| **Kanban boards = Visible membrane** | Make the filtering transparent and trustable |
| **Triage criteria = Filter settings** | Define what passes through vs. queued |

### Olivetti: Human Dignity in Productive Work (1958)

> *"The factory cannot look only at the profit index. It must distribute wealth, culture, services, democracy."*

| Principle | Framework Application |
|-----------|----------------------|
| **Burnout prevention = Moral imperative** | Not efficiency optimization—human dignity |
| **Rotation = Whole-person development** | Engineers grow across contexts |
| **Team autonomy = Learning cells** | Teams responsible for rituals, improvement, peer development |

---

## Tier 2: Learning — Argyris/Schön + Rogers

### Argyris & Schön: Double-Loop Learning (1978)

**Key Insight:** Organizations learn in two modes:
- **Single-loop:** Correcting errors within existing norms
- **Double-loop:** Questioning and modifying the norms themselves

Quarterly Adaptation institutionalizes double-loop learning. The Management Oversight Board (MoB) exemplifies this: each quarterly review explicitly asks norm-questioning questions—"Does our shape match strategy?"—not just "Are we hitting targets?"

### Rogers: Diffusion of Innovation (2003)

**Key Insight:** Technical change cannot succeed without cultural adoption. Change spreads through social systems via legitimacy, peer modeling, and trust.

---

## Tier 3: Implementation — Ohno + Anderson

### Ohno: Toyota Production System (1978)

> *"All we are doing is looking at the time line from the moment the customer gives us an order to the point when we collect the cash."*

| Concept | Framework Application |
|---------|----------------------|
| **Kanban boards = Visual signals** | Make work visible |
| **Pull-based intake = Demand-driven** | SRE pulls work when capacity available |
| **WIP limits = Inventory control** | Limit work-in-progress to prevent overload |

### Anderson: Kanban Method for Knowledge Work (2010)

**Critical Connection:** Anderson explicitly states Kanban should be a "humane change method"—aligning with Olivetti. The Kanban board is the visible implementation of Luhmann's membrane.

---

## The Synthesis

> Kanban boards are the visible implementation of Luhmann's membrane, operated with Olivetti's human dignity, improved through Argyris's double-loop learning, spread through Rogers's diffusion patterns.

---

# The Five Core Practices

The framework consists of five interconnected practices that operate **fractally**—each can be applied at team, division, or enterprise levels.

<div class="pillar protect">
<h3>1. Structured Gatekeeping</h3>

**Purpose:** Shield technical teams from operational noise through structured intake processes, visual triage systems, and shared accountability models.

**Theoretical Grounding:**
- Tier 1 (Luhmann): Gatekeeping IS the semipermeable membrane
- Tier 3 (Ohno/Anderson): Kanban boards IMPLEMENT the membrane visually

**Gatekeeper Evolution: Manual to Intelligent**

| Phase | Period | Description |
|-------|--------|-------------|
| Phase 1 | 2021-2022 | Manual triage—gatekeepers review every ticket |
| Phase 2 | 2023-2024 | Pattern recognition—1,356 automation candidates flagged |
| Phase 3 | 2025+ | Intelligent membrane—automation handles routine cases |

**Validation:** 86.7% improvement work completion rate; 69% of TOIL handled by consolidated gatekeepers.
</div>

<div class="pillar prepare">
<h3>2. Rotational Development</h3>

**Purpose:** Develop engineers as rotationally fluent professionals through deliberate cross-pollination.

**Rotation as Cognitive Countermeasure:** Rotation serves as a structural countermeasure against echo chamber formation and knowledge silos.

**Validation:** 90% cross-functional capability; 70% leadership positions filled internally.
</div>

<div class="pillar pulse">
<h3>3. Quarterly Adaptation</h3>

**Purpose:** Conduct regular feedback loops assessing organizational structure alignment with business evolution.

**Management Oversight Board as Double-Loop Mechanism:**

| Quarter | Focus | Outcome |
|---------|-------|---------|
| Q1 2025 | Standardization focus | Establishing baselines |
| Q2 2025 | Active project execution | Zero security incidents |
| Q3 2025 | Scaling operations | Risk identification |
</div>

<div class="pillar pool">
<h3>4. Shared Resource Management</h3>

**Purpose:** Maintain shared talent pools that preserve delivery capabilities while enabling temporary reassignment.

**Compliance Certification Case Study:**

Rather than engaging external consultants, the organization leveraged internal SRE expertise for major compliance certifications:

- Team composition: 9 internal + 1 external (vs. typical all-external approach)
- Cost savings: 40% reduction vs. consultant-based model
- Knowledge retention: Expertise remains within organization

**Validation:** 2.7x seasonal variance successfully managed.
</div>

<div class="pillar promote">
<h3>5. Visibility & Culture</h3>

**Purpose:** Treat organizational culture as an engineered asset through intentional identification and amplification of culture carriers.

**Validation:** 15-20% higher retention than adjacent teams; eNPS scores 4.3-4.5/5.
</div>

---

## Communication Architecture

**Purpose:** Design organizational communication as a transmedia membrane system.

Information encounters resistance at every boundary. Effective membrane design creates **differential viscosity**: low resistance for legitimate escalations, high resistance for noise.

### Cadence Ecosystem

| Layer | Cadence | Purpose |
|-------|---------|---------|
| **Executive** | MoB (Quarterly) | Strategic decisions |
| **Leadership** | Monthly Syncs | Alignment, visibility |
| **Partner** | Ops Review, OLA (Monthly+) | Accountability |
| **Team** | Standups (Daily), Retrospectives (Sprint) | Coordination |
| **Artifact** | Documentation, Dashboards (Persistent) | Knowledge persistence |

---

<div class="card-grid">
  <a href="{{ '/framework/philosophy/' | relative_url }}" class="card-link">
    <div class="card">
      <h3>← The Mitochondrial Fallacy</h3>
      <p>Philosophical foundation for adaptive organizations.</p>
    </div>
  </a>

  <a href="{{ '/framework/evolution/' | relative_url }}" class="card-link">
    <div class="card">
      <h3>Evolution & Cycles →</h3>
      <p>Three organizational cycles and milestones.</p>
    </div>
  </a>
</div>
