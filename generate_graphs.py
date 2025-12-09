#!/usr/bin/env python3
"""
Generate visualizations for the Fluid Reliability Framework whitepaper and website.
Based on JIRA ticket data and framework metrics.
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import numpy as np
from pathlib import Path

# Set style
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("Blues_d")

OUTPUT_DIR = Path("docs/assets/images/graphs")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Framework validated data from whitepaper
TOIL_DATA = {
    'Year': [2021, 2022, 2023, 2024, 2025],
    'Tickets': [100, 1472, 8045, 9054, 6824],
    'TOIL_Percent': [73.0, 75.8, 83.9, 63.4, 50.6],
    'Context': ['Initial baseline', 'First merger', 'PEAK - Multi-product stress', 'Framework maturity', 'Google <60% achieved']
}

TEAM_GROWTH = {
    'Year': [2019, 2020, 2021, 2022, 2023, 2024, 2025],
    'Team_Size': [4, 6, 8, 16, 24, 32, 38],
    'Cycle': ['Cycle 1', 'Cycle 1', 'Cycle 1', 'Cycle 2', 'Cycle 3', 'Cycle 3', 'Cycle 3']
}

CYCLE_TIME = {
    'Metric': ['Mean Cycle Time', 'P95 Cycle Time'],
    'Before': [17.91, 294.6],
    'After': [9.50, 23.0],
    'Unit': ['days', 'days']
}

OLA_ADHERENCE = {
    'Quarter': ['Q1 2025', 'Q2 2025', 'Q3 2025', 'Q4 2025'],
    'Tickets': [200, 172, 65, 25],
    'Adherence': [55.5, 52.3, 50.8, 76.0]
}

ROI_TIERS = {
    'Tier': ['Tier 1: Direct', 'Tier 2: Modeled (Low)', 'Tier 2: Modeled (High)', 'Tier 3: Strategic'],
    'Value': [228000, 345000, 691000, 3000000],
    'Confidence': ['High', 'Medium', 'Medium', 'Lower']
}

BURNOUT_STATS = {
    'Category': ['At Risk of Burnout', 'SREs >50% TOIL', 'Platform Eng Drop'],
    'Percentage': [82, 57, 14],
    'Source': ['Fortune/DHR 2024', 'Catchpoint 2025', 'DORA 2024']
}

FIVE_PRACTICES = {
    'Practice': ['Gatekeeping', 'Rotation', 'Quarterly\nAdaptation', 'Resource\nPooling', 'Visibility\n& Culture'],
    'Mnemonic': ['Protect', 'Prepare', 'Pulse', 'Pool', 'Promote'],
    'Color': ['#1f77b4', '#2ca02c', '#ff7f0e', '#9467bd', '#d62728']
}


def create_toil_trajectory():
    """TOIL ratio trajectory 2021-2025 with annotations"""
    fig, ax = plt.subplots(figsize=(12, 7))

    df = pd.DataFrame(TOIL_DATA)

    # Create bar chart with gradient colors
    colors = ['#3498db' if t < 60 else '#e74c3c' if t > 80 else '#f39c12' for t in df['TOIL_Percent']]
    bars = ax.bar(df['Year'], df['TOIL_Percent'], color=colors, edgecolor='white', linewidth=2)

    # Add Google SRE target line
    ax.axhline(y=60, color='#27ae60', linestyle='--', linewidth=2, label='Google SRE Target (<60%)')

    # Add value labels on bars
    for bar, val, ctx in zip(bars, df['TOIL_Percent'], df['Context']):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{val}%', ha='center', va='bottom', fontweight='bold', fontsize=12)

    # Highlight peak and achievement
    ax.annotate('PEAK\n83.9%', xy=(2023, 83.9), xytext=(2023, 95),
                ha='center', fontsize=10, fontweight='bold', color='#e74c3c',
                arrowprops=dict(arrowstyle='->', color='#e74c3c'))

    ax.annotate('TARGET\nACHIEVED', xy=(2025, 50.6), xytext=(2025, 38),
                ha='center', fontsize=10, fontweight='bold', color='#27ae60',
                arrowprops=dict(arrowstyle='->', color='#27ae60'))

    # Add trend line
    z = np.polyfit([2023, 2024, 2025], [83.9, 63.4, 50.6], 1)
    p = np.poly1d(z)
    ax.plot([2023, 2024, 2025], p([2023, 2024, 2025]), '--', color='#9b59b6',
            linewidth=2, alpha=0.7, label='Recovery Trend')

    ax.set_xlabel('Year', fontsize=12, fontweight='bold')
    ax.set_ylabel('TOIL Ratio (%)', fontsize=12, fontweight='bold')
    ax.set_title('TOIL Ratio Trajectory (2021-2025)\n33.3 Percentage Point Reduction',
                 fontsize=14, fontweight='bold', pad=20)
    ax.set_ylim(0, 100)
    ax.legend(loc='upper right')
    ax.set_xticks(df['Year'])

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'toil_trajectory.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print(f"Created: {OUTPUT_DIR / 'toil_trajectory.png'}")


def create_team_growth():
    """Team growth visualization with cycle annotations"""
    fig, ax = plt.subplots(figsize=(12, 7))

    df = pd.DataFrame(TEAM_GROWTH)

    # Color by cycle
    cycle_colors = {'Cycle 1': '#3498db', 'Cycle 2': '#2ecc71', 'Cycle 3': '#9b59b6'}
    colors = [cycle_colors[c] for c in df['Cycle']]

    # Create line and scatter
    ax.plot(df['Year'], df['Team_Size'], 'o-', color='#34495e', linewidth=2, markersize=10)
    ax.scatter(df['Year'], df['Team_Size'], c=colors, s=200, zorder=5, edgecolors='white', linewidth=2)

    # Add value labels
    for x, y in zip(df['Year'], df['Team_Size']):
        ax.annotate(f'{y}', (x, y), textcoords="offset points", xytext=(0, 15),
                    ha='center', fontweight='bold', fontsize=11)

    # Add cycle backgrounds
    ax.axvspan(2019, 2021.5, alpha=0.1, color='#3498db', label='Cycle 1: e-Builder')
    ax.axvspan(2021.5, 2022.5, alpha=0.1, color='#2ecc71', label='Cycle 2: PPM Franchise')
    ax.axvspan(2022.5, 2025.5, alpha=0.1, color='#9b59b6', label='Cycle 3: Unity Suite')

    # Add growth annotation
    ax.annotate('850% Growth\n4 → 38 engineers', xy=(2022, 20), fontsize=12,
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

    ax.set_xlabel('Year', fontsize=12, fontweight='bold')
    ax.set_ylabel('Team Size (Engineers)', fontsize=12, fontweight='bold')
    ax.set_title('Team Growth Through Three Organizational Cycles\nZero Critical Knowledge Loss',
                 fontsize=14, fontweight='bold', pad=20)
    ax.legend(loc='upper left')
    ax.set_xlim(2018.5, 2025.5)
    ax.set_ylim(0, 45)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'team_growth.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print(f"Created: {OUTPUT_DIR / 'team_growth.png'}")


def create_cycle_time_comparison():
    """Before/After cycle time comparison"""
    fig, ax = plt.subplots(figsize=(10, 6))

    metrics = ['Mean Cycle Time\n(days)', 'P95 Cycle Time\n(days)']
    before = [17.91, 294.6]
    after = [9.50, 23.0]
    improvements = ['47%', '92%']

    x = np.arange(len(metrics))
    width = 0.35

    bars1 = ax.bar(x - width/2, before, width, label='Before', color='#e74c3c', edgecolor='white')
    bars2 = ax.bar(x + width/2, after, width, label='After', color='#27ae60', edgecolor='white')

    # Add value labels
    for bar in bars1:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}', ha='center', va='bottom', fontweight='bold')

    for bar in bars2:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}', ha='center', va='bottom', fontweight='bold')

    # Add improvement annotations
    for i, (b, a, imp) in enumerate(zip(before, after, improvements)):
        ax.annotate(f'↓{imp}', xy=(i, max(b, a) + 20), ha='center',
                    fontsize=14, fontweight='bold', color='#27ae60')

    ax.set_ylabel('Days', fontsize=12, fontweight='bold')
    ax.set_title('Cycle Time Improvement\nFrom Framework Implementation',
                 fontsize=14, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(metrics, fontsize=11)
    ax.legend()
    ax.set_ylim(0, 350)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'cycle_time_comparison.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print(f"Created: {OUTPUT_DIR / 'cycle_time_comparison.png'}")


def create_ola_trajectory():
    """OLA adherence quarterly trajectory"""
    fig, ax = plt.subplots(figsize=(10, 6))

    df = pd.DataFrame(OLA_ADHERENCE)

    # Bar chart with color coding
    colors = ['#f39c12' if a < 60 else '#27ae60' for a in df['Adherence']]
    bars = ax.bar(df['Quarter'], df['Adherence'], color=colors, edgecolor='white', linewidth=2)

    # Add trend line
    ax.plot(df['Quarter'], df['Adherence'], 'o--', color='#34495e', linewidth=2, markersize=8)

    # Add value labels
    for bar, val in zip(bars, df['Adherence']):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{val}%', ha='center', va='bottom', fontweight='bold', fontsize=11)

    # Highlight recovery
    ax.annotate('+25.2 pts\nRecovery', xy=(3, 76), xytext=(2.3, 85),
                ha='center', fontsize=11, fontweight='bold', color='#27ae60',
                arrowprops=dict(arrowstyle='->', color='#27ae60'))

    ax.set_ylabel('OLA Adherence (%)', fontsize=12, fontweight='bold')
    ax.set_title('Partner OLA Adherence Trajectory\nQ4 2025 Sharp Recovery',
                 fontsize=14, fontweight='bold', pad=20)
    ax.set_ylim(0, 100)
    ax.axhline(y=80, color='#27ae60', linestyle='--', alpha=0.5, label='Target (80%)')
    ax.legend()

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'ola_adherence.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print(f"Created: {OUTPUT_DIR / 'ola_adherence.png'}")


def create_roi_visualization():
    """ROI three-tier confidence model"""
    fig, ax = plt.subplots(figsize=(11, 7))

    tiers = ['Tier 1:\nDirect Benefits\n(High Confidence)',
             'Tier 2:\nModeled Benefits\n(Medium Confidence)',
             'Tier 3:\nStrategic Avoidance\n(Lower Confidence)']
    values = [228, 518, 3000]  # in thousands
    colors = ['#27ae60', '#f39c12', '#3498db']

    bars = ax.barh(tiers, values, color=colors, edgecolor='white', linewidth=2, height=0.6)

    # Add value labels
    for bar, val in zip(bars, values):
        width = bar.get_width()
        label = f'${val:,}K' if val < 1000 else f'${val/1000:.1f}M'
        ax.text(width + 50, bar.get_y() + bar.get_height()/2,
                label, ha='left', va='center', fontweight='bold', fontsize=12)

    # Add ROI annotations
    ax.text(228/2, 0, '5.2:1 ROI', ha='center', va='center',
            fontweight='bold', fontsize=10, color='white')
    ax.text(518/2, 1, '8.4:1 - 11.2:1 ROI', ha='center', va='center',
            fontweight='bold', fontsize=10, color='white')

    ax.set_xlabel('Annual Value ($K)', fontsize=12, fontweight='bold')
    ax.set_title('Monetary Benefits: Three-Tier Confidence Model\nImplementation Cost: $82K-$110K/year',
                 fontsize=14, fontweight='bold', pad=20)
    ax.set_xlim(0, 3500)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'roi_tiers.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print(f"Created: {OUTPUT_DIR / 'roi_tiers.png'}")


def create_burnout_crisis():
    """Industry burnout crisis statistics"""
    fig, ax = plt.subplots(figsize=(10, 6))

    categories = ['Employees at Risk\nof Burnout', 'SREs Spending\n>50% on TOIL',
                  'Platform Eng Drop\n(without culture)']
    values = [82, 57, 14]
    colors = ['#e74c3c', '#f39c12', '#9b59b6']
    sources = ['Fortune/DHR 2024', 'Catchpoint 2025', 'DORA 2024']

    bars = ax.bar(categories, values, color=colors, edgecolor='white', linewidth=2)

    # Add value labels
    for bar, val, src in zip(bars, values, sources):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{val}%', ha='center', va='bottom', fontweight='bold', fontsize=14)
        ax.text(bar.get_x() + bar.get_width()/2., height/2,
                src, ha='center', va='center', fontsize=9, color='white',
                style='italic')

    ax.set_ylabel('Percentage (%)', fontsize=12, fontweight='bold')
    ax.set_title('The 2024-2025 SRE Burnout Crisis\nIndustry Context for Fluid Reliability',
                 fontsize=14, fontweight='bold', pad=20)
    ax.set_ylim(0, 100)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'burnout_crisis.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print(f"Created: {OUTPUT_DIR / 'burnout_crisis.png'}")


def create_five_practices_wheel():
    """Five Core Practices visualization"""
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'))

    practices = ['Gatekeeping\n(Protect)', 'Rotation\n(Prepare)',
                 'Quarterly\nAdaptation\n(Pulse)', 'Resource\nPooling\n(Pool)',
                 'Visibility\n& Culture\n(Promote)']

    # Create equal segments
    N = len(practices)
    theta = np.linspace(0, 2 * np.pi, N, endpoint=False)
    width = 2 * np.pi / N

    colors = ['#1f77b4', '#2ca02c', '#ff7f0e', '#9467bd', '#d62728']

    bars = ax.bar(theta, [1]*N, width=width*0.9, bottom=0.3,
                  color=colors, edgecolor='white', linewidth=3, alpha=0.8)

    # Add practice labels
    for angle, practice in zip(theta, practices):
        ax.text(angle, 1.5, practice, ha='center', va='center',
                fontsize=11, fontweight='bold')

    # Add center text
    ax.text(0, 0, 'Fluid\nReliability', ha='center', va='center',
            fontsize=14, fontweight='bold', transform=ax.transAxes)

    ax.set_ylim(0, 2)
    ax.set_yticks([])
    ax.set_xticks([])
    ax.spines['polar'].set_visible(False)

    ax.set_title('The Five Core Practices\nFractal Framework for Organizational Transformation',
                 fontsize=14, fontweight='bold', pad=30, y=1.08)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'five_practices.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print(f"Created: {OUTPUT_DIR / 'five_practices.png'}")


def create_key_metrics_summary():
    """Summary dashboard of key metrics"""
    fig = plt.figure(figsize=(14, 10))

    # Create grid
    gs = fig.add_gridspec(2, 3, hspace=0.3, wspace=0.3)

    # TOIL reduction
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.bar(['2023\nPeak', '2025\nCurrent'], [83.9, 50.6], color=['#e74c3c', '#27ae60'])
    ax1.axhline(y=60, color='gray', linestyle='--', alpha=0.5)
    ax1.set_ylabel('TOIL %')
    ax1.set_title('TOIL Reduction\n-33.3 pp', fontweight='bold')
    ax1.set_ylim(0, 100)
    for i, v in enumerate([83.9, 50.6]):
        ax1.text(i, v + 2, f'{v}%', ha='center', fontweight='bold')

    # Team growth
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.bar(['2019', '2025'], [4, 38], color=['#3498db', '#2ecc71'])
    ax2.set_ylabel('Engineers')
    ax2.set_title('Team Growth\n850%', fontweight='bold')
    for i, v in enumerate([4, 38]):
        ax2.text(i, v + 1, str(v), ha='center', fontweight='bold')

    # Cycle time
    ax3 = fig.add_subplot(gs[0, 2])
    ax3.bar(['Before', 'After'], [17.91, 9.50], color=['#e74c3c', '#27ae60'])
    ax3.set_ylabel('Days')
    ax3.set_title('Mean Cycle Time\n-47%', fontweight='bold')
    for i, v in enumerate([17.91, 9.50]):
        ax3.text(i, v + 0.5, f'{v:.1f}', ha='center', fontweight='bold')

    # P95 Cycle time
    ax4 = fig.add_subplot(gs[1, 0])
    ax4.bar(['Before', 'After'], [294.6, 23.0], color=['#e74c3c', '#27ae60'])
    ax4.set_ylabel('Days')
    ax4.set_title('P95 Cycle Time\n-92%', fontweight='bold')
    for i, v in enumerate([294.6, 23.0]):
        ax4.text(i, v + 10, f'{v:.0f}', ha='center', fontweight='bold')

    # ROI
    ax5 = fig.add_subplot(gs[1, 1])
    ax5.bar(['Conservative', 'Moderate'], [5.2, 11.2], color=['#f39c12', '#27ae60'])
    ax5.set_ylabel('ROI Ratio')
    ax5.set_title('Return on Investment\n5.2:1 to 11.2:1', fontweight='bold')
    for i, v in enumerate([5.2, 11.2]):
        ax5.text(i, v + 0.3, f'{v}:1', ha='center', fontweight='bold')

    # Tickets analyzed
    ax6 = fig.add_subplot(gs[1, 2])
    ax6.text(0.5, 0.6, '25,498', ha='center', va='center', fontsize=36, fontweight='bold', color='#3498db')
    ax6.text(0.5, 0.35, 'Tickets Analyzed', ha='center', va='center', fontsize=14)
    ax6.text(0.5, 0.2, '6 Years | 3 JIRA Boards', ha='center', va='center', fontsize=11, color='gray')
    ax6.text(0.5, 0.08, 'p < 0.001', ha='center', va='center', fontsize=10, style='italic')
    ax6.axis('off')
    ax6.set_title('Statistical Validation', fontweight='bold')

    fig.suptitle('Fluid Reliability Framework: Key Metrics Dashboard',
                 fontsize=16, fontweight='bold', y=0.98)

    plt.savefig(OUTPUT_DIR / 'metrics_dashboard.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print(f"Created: {OUTPUT_DIR / 'metrics_dashboard.png'}")


def create_theoretical_tiers():
    """Three-tier theoretical architecture visualization"""
    fig, ax = plt.subplots(figsize=(12, 8))

    # Create pyramid-like structure
    tiers = [
        ('Tier 3: Implementation\n(HOW work flows)', ['Ohno TPS (1978)', 'Anderson Kanban (2010)'], '#3498db', 0),
        ('Tier 2: Learning\n(HOW change happens)', ['Argyris Double-Loop (1978)', 'Rogers Diffusion (2003)'], '#f39c12', 1),
        ('Tier 1: Foundation\n(WHY and WHAT)', ['Luhmann Systems (1995)', 'Olivetti Community (1958)'], '#27ae60', 2),
    ]

    for tier_name, sources, color, idx in tiers:
        y = idx * 2.5
        rect = plt.Rectangle((0.5, y), 11, 2, facecolor=color, edgecolor='white', linewidth=3, alpha=0.8)
        ax.add_patch(rect)
        ax.text(6, y + 1.3, tier_name, ha='center', va='center', fontsize=13, fontweight='bold', color='white')
        ax.text(6, y + 0.5, ' | '.join(sources), ha='center', va='center', fontsize=10, color='white')

    ax.set_xlim(0, 12)
    ax.set_ylim(-0.5, 8)
    ax.axis('off')
    ax.set_title('Three-Tier Theoretical Architecture\nSynthesis of Six Academic Sources',
                 fontsize=14, fontweight='bold', pad=20)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'theoretical_tiers.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print(f"Created: {OUTPUT_DIR / 'theoretical_tiers.png'}")


if __name__ == '__main__':
    print("Generating Fluid Reliability Framework visualizations...")
    print(f"Output directory: {OUTPUT_DIR.absolute()}")
    print("-" * 50)

    create_toil_trajectory()
    create_team_growth()
    create_cycle_time_comparison()
    create_ola_trajectory()
    create_roi_visualization()
    create_burnout_crisis()
    create_five_practices_wheel()
    create_key_metrics_summary()
    create_theoretical_tiers()

    print("-" * 50)
    print("All visualizations generated successfully!")
    print(f"\nImages saved to: {OUTPUT_DIR.absolute()}")
