---
layout: default
title: Evidence & ROI
description: Complete dataset analysis and three-tier monetary benefits model
---

# Quantitative Validation — Complete Dataset Analysis

Comprehensive validation against **25,498 operational tickets** spanning September 2020 through November 2025.

---

## Data Sources

| Board | Tickets | Period |
|-------|---------|--------|
| OPSSRE Board (Etools) | 16,799 | Dec 2023 - Nov 2025 |
| PPMC Board | 5,093 | Sep 2020 - Present |
| Cityworks SRE Board | 3,606 | Jun 2022 - Present |
| **Total** | **25,498** | **5+ years** |

---

## TOIL Ratio Trajectory (2021-2025)

**KEY FINDING:** TOIL ratio dropped from 83.9% (2023 peak) to 50.6% (2025)—a **33.3 percentage point reduction**.

| Year | Tickets | TOIL % | Context |
|------|---------|--------|---------|
| 2021 | 100 | 73.0% | e-Builder baseline |
| 2022 | 1,472 | 75.8% | PPM integration |
| **2023** | 8,045 | **83.9% ▲ PEAK** | Unity stress |
| 2024 | 9,054 | 63.4% | Framework maturity |
| **2025** | 6,824 | **50.6% ▼ TARGET** | Google <60% achieved |

<div class="metrics-grid">
  <div class="metric-card">
    <div class="metric-value">83.9%</div>
    <div class="metric-label">2023 Peak TOIL</div>
  </div>
  <div class="metric-card">
    <div class="metric-value">50.6%</div>
    <div class="metric-label">2025 Current TOIL</div>
    <div class="metric-change">Beat Google's &lt;60% target</div>
  </div>
  <div class="metric-card">
    <div class="metric-value">33.3 pts</div>
    <div class="metric-label">Total Reduction</div>
  </div>
</div>

---

## Cycle Time Analysis

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| Mean Cycle Time | 17.91 days | 9.50 days | **47% reduction** |
| P95 Cycle Time | 294.60 days | ~23 days | **92% reduction** |
| Max Cycle Time | — | — | **81% reduction** |

---

## Incident MTTR (Actual Outage Duration)

MTTR from SRE monitoring (distinct from JIRA cycle time):

<div class="metrics-grid">
  <div class="metric-card">
    <div class="metric-value">43 min</div>
    <div class="metric-label">e-Builder MTTR</div>
  </div>
  <div class="metric-card">
    <div class="metric-value">11 hrs</div>
    <div class="metric-label">Cityworks MTTR</div>
  </div>
  <div class="metric-card">
    <div class="metric-value">22.6 hrs</div>
    <div class="metric-label">AgileAssets MTTR</div>
  </div>
</div>

---

## Seasonality Analysis

**2.7x variance** between peak (1,461 tickets) and low (544 tickets) months—successfully managed through Shared Resource Management practice.

---

## Statistical Significance

| Test | Value | Interpretation |
|------|-------|----------------|
| Chi-square test | χ² = 285.4 | Highly significant |
| P-value | p < 0.001 | Extremely unlikely to be chance |
| Effect size (Cramér's V) | 0.13 | Medium effect |

---

# Monetary Benefits Analysis — Three-Tier Confidence Model

## Tier 1: Directly Measurable Benefits (High Confidence) — $228,000

| Benefit | Annual Value | Calculation Basis |
|---------|--------------|-------------------|
| TOIL Capacity Freed | $153,000 | 1.02 FTE × $150K loaded salary |
| Automation Potential | $75,000 | 995 hours/year × $75/hr |
| **TIER 1 TOTAL** | **$228,000** | Directly calculable from JIRA |

## Tier 2: Modeled Benefits (Medium Confidence) — $345K-$691K

| Benefit | Range | Notes |
|---------|-------|-------|
| Improvement Work Value | $120K-$241K | Value of completed improvements |
| MTTR Maintenance | $143K-$287K | Incident cost avoidance |
| Context Switching Reduction | $29K-$58K | Engineering efficiency |
| Retention Improvement | $53K-$105K | Reduced turnover costs |

## Tier 3: Strategic Cost Avoidance (Lower Confidence) — Up to $3M

| Benefit | Potential Value | Notes |
|---------|-----------------|-------|
| Major Incident Prevention | Up to $2.44M | Based on industry averages |
| Turnover Cost Avoidance | $450K-$600K | 15-20% retention advantage |

---

## ROI Summary

<div class="metrics-grid">
  <div class="metric-card">
    <div class="metric-value">5.2:1 - 7.0:1</div>
    <div class="metric-label">Conservative ROI</div>
  </div>
  <div class="metric-card">
    <div class="metric-value">8.4:1 - 11.2:1</div>
    <div class="metric-label">Moderate ROI</div>
  </div>
  <div class="metric-card">
    <div class="metric-value">1.7-5.8 mo</div>
    <div class="metric-label">Payback Period</div>
  </div>
</div>

---

## Implementation Costs ($82K-$110K annually)

| Component | Annual Cost |
|-----------|-------------|
| Quarterly MoB | $13,680 |
| Rotation Coordination | $13,520 |
| Gatekeeping Function | $39,000 |
| Documentation & Process | $9,000 |
| Training & Onboarding | $6,000 |

---

## Team Health Metrics (2025 Year in Review)

### eNPS Survey Results

| Metric | Score |
|--------|-------|
| Communication Satisfaction | 4.3/5 |
| Relevance of Communication | 4.5/5 |
| Stress Level | 3.2/5 (manageable) |

### Direct Team Quotes

> *"Micro teaming has been great—you get to know your coworkers as well as have extra advice right then and there."*

> *"Kanban has been a massive improvement for my day-to-day. First time I can get a clear picture of what people are working on."*

---

## Current Operations (November 2025)

| Metric | Value |
|--------|-------|
| TOIL ratio | 50.6% (Google SRE <60% achieved) |
| Migration pipeline | 54 total (22 complete, 20 in progress, 12 pipeline) |
| Compliance | ISO 27001, SOC 2/3, FedRAMP, TX-RAMP, StateRAMP |
| Security incidents | Zero (Q2 2025) |

---

## Limitations and Future Research

### Study Limitations

- Single Organization Context
- Confounding Variables
- Self-Reported Metrics
- Retrospective Baseline

### External Validation Opportunities

- SREcon case study presentations
- Academic partnerships
- Industry benchmark comparisons

### Future Research Directions

- AI Integration
- Remote/Distributed Teams
- Scaling Limits

---

<div class="card-grid">
  <a href="{{ '/framework/evolution/' | relative_url }}" class="card-link">
    <div class="card">
      <h3>← Evolution & Cycles</h3>
      <p>See how these results emerged through three organizational transformations.</p>
    </div>
  </a>

  <a href="{{ '/about/' | relative_url }}" class="card-link">
    <div class="card">
      <h3>About & References →</h3>
      <p>Theoretical references and author information.</p>
    </div>
  </a>
</div>
