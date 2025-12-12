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

Using strict content-based analysis against Google SRE's 5-point TOIL definition, TOIL ratio dropped from **59.7% (2024) to 44.7% (2025)**—a **15.0 percentage point reduction** and beating Google's <60% target.

![TOIL Reduction]({{ site.baseurl }}/assets/images/graphs/toil_reduction_yoy.png)
*Figure 3: Real TOIL reduction — Configuration tickets dropped 73%, representing primary TOIL source*

| Year | Tickets | Strict TOIL % | Context |
|------|---------|---------------|---------|
| 2024 | 6,833 | **59.7%** | Baseline (validated methodology) |
| 2025 | 7,085 (Jan-Nov) | **44.7%** | Google <60% achieved |

### Configuration TOIL: The Primary Victory

Configuration tickets—the largest TOIL category—dropped from 1,466 (2024) to 577 (2025), a **61% reduction**. This represents deliberate automation investment and self-service enablement.

### Methodology Note

Strict analysis applies Google SRE's 5-point TOIL definition (manual, repetitive, automatable, scales with growth, no enduring value) with weighted rates by issue type. The 44.7% result is validated against the JIRA TOIL field (49.4% of marked tickets = Yes), confirming methodological soundness.

---

## Cycle Time Analysis

![Cycle Time Compression]({{ site.baseurl }}/assets/images/graphs/cycle_time_compression.png)
*Figure 4: 2025 cycle time analysis — Mean 12.6 days, Median 3.0 days, P95 56.8 days*

### Historical Before/After

| Metric | Before (Pre-2025) | 2025 (Jan-Nov) | Improvement |
|--------|-------------------|----------------|-------------|
| Mean Cycle Time | 17.91 days | 12.6 days | **30% reduction** |
| P95 Cycle Time | 294.60 days | 56.8 days | **81% reduction** |
| Median Cycle Time | — | 3.0 days | Stable throughput |

### 2025 Quarterly Breakdown

*Data Source: 7,085 tickets (Jan-Nov 2025)*

| Quarter | Tickets | Mean CT | Median CT | P95 CT |
|---------|---------|---------|-----------|--------|
| Q1 | 1,826 | 16.1 days | 3.0 days | 80.8 days |
| Q2 | 1,855 | 9.5 days | 2.0 days | 38.6 days |
| Q3 | 2,017 | 12.8 days | 2.0 days | 61.0 days |
| Q4 (Oct-Nov) | 1,387 | 12.1 days | 3.0 days | 40.4 days |

**Result:** Q2 achieved best mean cycle time (9.5 days). Median cycle time consistently at 2-3 days demonstrates stable throughput.

> **Note:** Q1 elevated metrics reflect 12.6% December 2024 backlog spillover (230 of 1,826 tickets).

---

## Incident MTTR

MTTR from SRE monitoring (distinct from ticket cycle time):

| Product | MTTR |
|---------|------|
| Product A (Primary) | 43 minutes |
| Product B (Acquired) | 11 hours |
| Product C (Acquired) | 22.59 hours |

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

## Cross-BA Collaboration (Rotation Success)

![Cross-BA Collaboration]({{ site.baseurl }}/assets/images/graphs/cross_ba_collaboration.png)
*Figure 6: Cross-BA collaboration rate growth — 63% → 74% (+11pp)*

Monthly tracking demonstrates rotation and pooling success:

| Month | Single-BA | Cross-BA | Cross-BA % |
|-------|-----------|----------|------------|
| January | 14 | 24 | 63% |
| April | 13 | 25 | 66% |
| July | 12 | 24 | 67% |
| **October** | 10 | 28 | **74%** |

**Result:** Cross-BA collaboration increased **11 percentage points** (63% → 74%).

*Definition: Cross-BA Workers = Engineers with tickets in 2+ Business Areas per month*

---

## Partner OLA Trajectory (2025)

![OLA Quarterly Recovery]({{ site.baseurl }}/assets/images/graphs/ola_quarterly_recovery.png)
*Figure 7: Quarterly OLA adherence recovery — 42% → 80.3% (+38pp)*

| Quarter | Within SLA | Total | Adherence | Change |
|---------|------------|-------|-----------|--------|
| Q1 2025 | 29 | 69 | **42.0%** | Baseline |
| Q2 2025 | 43 | 76 | **56.6%** | +14.6 pp |
| Q3 2025 | 176 | 240 | **73.3%** | +16.7 pp |
| **Q4 2025** | 61 | 76 | **80.3%** | **Target Met** |

**Result:** OLA improved from 42% to 80.3%—a **38 percentage point improvement**.

---

## Current Operations (December 2025)

| Metric | Value |
|--------|-------|
| Strict TOIL | 44.7% |
| Cross-BA Collaboration | 74% |
| Partner OLA | 80.3% |
| Rework Rate | 13.3% |
| Monthly Throughput | 644 tickets |
| Migration pipeline | 54 total |
| Compliance | ISO 27001, SOC 2/3, FedRAMP, TX-RAMP |
| Security incidents | Zero (Q2-Q4 2025) |

---

## Operational Reporting Framework

Continuous measurement enables ongoing framework validation. The operational reporting system produces three automated reports:

### SRE Operations Report
- **Volume Analysis:** Monthly/quarterly ticket trends with MoM comparison
- **TOIL Measurement:** Dual methodology (Proxy by Issue Type + Content Scan by keywords)
- **Cycle Time Distribution:** Mean, Median, P95 with bucket analysis (0-7d, 8-14d, 15-30d, 31-60d, >60d)
- **Component Breakdown:** Workload distribution across business units

### OLA Performance Report
- **Business Days Calculation:** Excludes weekends for accurate SLA measurement
- **Service Type Analysis:** Per-request-type adherence rates
- **Back-and-Forth Detection:** Comment count correlation identifies root causes
- **Missed OLA Analysis:** Specific tickets and delay patterns

### Personnel Allocation Report
- **Team Structure:** Manager-based organization view
- **BU Distribution:** Effort allocation across business units (100% model)
- **Migration Tracking:** Keyword-based identification of migration work
- **Workload Tiers:** High/Medium/Low/Minimal distribution analysis

### Measurement Philosophy

> *"What gets measured gets managed, but only if the measurement methodology is sound."*

The framework emphasizes:
1. **Multiple methodologies:** Cross-validate metrics using different approaches
2. **Trend over absolute:** Focus on direction of change, not single-point values
3. **Root cause visibility:** Identify *why* metrics change, not just *that* they changed
4. **Reproducibility:** Documented methodology enables consistent measurement

---

[← Evolution](/framework/evolution/) | [About →](/about/)
