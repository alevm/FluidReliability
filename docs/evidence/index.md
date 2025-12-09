---
layout: default
title: Evidence & ROI
description: Quantitative validation and monetary benefits analysis
permalink: /evidence/
---

# Evidence & ROI

| Version | Date | Author |
|---------|------|--------|
| **{{ site.data.version.version }}** | **{{ site.data.version.date }}** | {{ site.data.version.author }} |

---

![Key Metrics Dashboard]({{ site.baseurl }}/assets/images/graphs/metrics_dashboard.png)
*Figure 1: Key metrics dashboard — Framework outcomes across all major indicators*

---

## Quantitative Validation

Comprehensive validation against **25,498 operational tickets** spanning September 2020 through November 2025.

![Ticket Volume]({{ site.baseurl }}/assets/images/graphs/ticket_volume.png)
*Figure 2: Ticket volume growth across 5 years — 25,498 total tickets analyzed*

---

## Data Sources

| Board | Tickets | Period |
|-------|---------|--------|
| Primary Operations Board | 16,799 | Dec 2023 - Nov 2025 |
| Legacy Platform Board | 5,093 | Sep 2020 - Present |
| Acquired Product Board | 3,606 | Jun 2022 - Present |
| **Total** | **25,498** | **5+ years** |

---

## TOIL Ratio Trajectory

TOIL ratio dropped from 83.9% (2023 peak) to 50.6% (2025)—a **33.3 percentage point reduction**.

![TOIL Trajectory]({{ site.baseurl }}/assets/images/graphs/toil_trajectory.png)
*Figure 3: TOIL ratio trajectory showing 33.3pp reduction and Google SRE target achievement*

| Year | Tickets | TOIL % | Context |
|------|---------|--------|---------|
| 2021 | 100 | 73.0% | Initial baseline |
| 2022 | 1,472 | 75.8% | First merger |
| 2023 | 8,045 | **83.9%** | Peak (multi-product stress) |
| 2024 | 9,054 | 63.4% | Framework maturity |
| 2025 | 6,824 | **50.6%** | Google <60% achieved |

### The 2023 Crisis: A Failure Metabolized

The 83.9% peak was lived experience. Multiple acquired teams brought their own cultures: different ticketing conventions, tribal knowledge, hero dependencies, and manual processes we thought we had eliminated. **We stepped backward in maturity.**

The framework's response: Quarterly Adaptation surfaced that the problem wasn't technical debt—it was *cultural debt* from acquisitions. Deliberate rotation moved engineers across merged boundaries. By 2025, the cultural tide had turned.

---

## Cycle Time Analysis

![Cycle Time Comparison]({{ site.baseurl }}/assets/images/graphs/cycle_time_comparison.png)
*Figure 4: Cycle time improvement — 47% mean reduction, 92% P95 reduction*

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| Mean Cycle Time | 17.91 days | 9.50 days | **47% reduction** |
| P95 Cycle Time | 294.60 days | ~23 days | **92% reduction** |
| Max Cycle Time | — | — | **81% reduction** |

---

## Incident MTTR

MTTR from SRE monitoring (distinct from ticket cycle time):

| Product | MTTR |
|---------|------|
| e-Builder | 43 minutes |
| Cityworks | 11 hours |
| AgileAssets | 22.59 hours |

---

## Statistical Significance

| Test | Value | Interpretation |
|------|-------|----------------|
| Chi-square | χ² = 285.4 | Highly significant |
| P-value | p < 0.001 | Not due to chance |
| Effect size (Cramér's V) | 0.13 | Medium effect |

---

## Monetary Benefits

![ROI Tiers]({{ site.baseurl }}/assets/images/graphs/roi_tiers.png)
*Figure 5: Three-tier confidence model with ROI ranging from 5.2:1 to 11.2:1*

### Tier 1: Directly Measurable (High Confidence) — $228,000/year

| Benefit | Annual Value | Basis |
|---------|--------------|-------|
| TOIL Capacity Freed | $153,000 | 1.02 FTE × $150K |
| Automation Potential | $75,000 | 995 hours × $75/hr |

### Tier 2: Modeled (Medium Confidence) — $345K-$691K/year

| Benefit | Range |
|---------|-------|
| Improvement Work Value | $120K-$241K |
| MTTR Maintenance | $143K-$287K |
| Context Switching Reduction | $29K-$58K |
| Retention Improvement | $53K-$105K |

### Tier 3: Strategic Cost Avoidance — Up to $3M

| Benefit | Potential Value |
|---------|-----------------|
| Major Incident Prevention | Up to $2.44M |
| Turnover Cost Avoidance | $450K-$600K |

---

## ROI Summary

| Confidence | ROI | Payback Period |
|------------|-----|----------------|
| Conservative | 5.2:1 - 7.0:1 | 4-6 months |
| Moderate | 8.4:1 - 11.2:1 | 2-4 months |

---

## Implementation Costs

~$82,000 annually:

| Component | Cost |
|-----------|------|
| Quarterly MoB | $13,680 |
| Rotation Coordination | $13,520 |
| Gatekeeping Function | $39,000 |
| Documentation | $9,000 |
| Training | $6,000 |

---

## Team Health (2025)

| Metric | Score |
|--------|-------|
| Communication Satisfaction | 4.3/5 |
| Relevance of Communication | 4.5/5 |
| Stress Level | 3.2/5 (manageable) |

### Voices from the Team

> *"Kanban has been a massive improvement for my day-to-day. This is the first time I can get a clear picture of what people are working on."*

> *"Micro teaming has been great—you get to know your coworkers as well as have extra advice right then and there."*

> *"I have never in my career experimented as much as in these few years."* — Principal Architect, 30 years experience

**Honest critiques** that drove refinement:
> *"Pairing between different geographical locations didn't seem to have worked well this quarter."*

---

## Current Operations (November 2025)

| Metric | Value |
|--------|-------|
| TOIL ratio | 50.6% |
| Migration pipeline | 54 total |
| Compliance | ISO 27001, SOC 2/3, FedRAMP, TX-RAMP |
| Security incidents | Zero (Q2 2025) |

---

[← Evolution](/framework/evolution/) | [About →](/about/)
