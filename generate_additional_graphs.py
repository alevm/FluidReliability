#!/usr/bin/env python3
"""
Generate additional visualizations for the Fluid Reliability Framework.
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

# Additional data from whitepaper
TOIL_CATEGORIES = {
    'Category': ['Configuration', 'Task', 'Bug', 'Support', 'Other'],
    'Percentage': [25, 20, 18, 15, 22],
    'Description': ['Config changes', 'Manual tasks', 'Bug fixes', 'User support', 'Misc ops']
}

SEASONALITY = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Tickets': [890, 720, 1100, 1461, 1200, 980,
                544, 650, 1150, 1380, 1250, 920]
}

GATEKEEPER_EVOLUTION = {
    'Phase': ['Phase 1\n(2021-2022)', 'Phase 2\n(2023-2024)', 'Phase 3\n(2025+)'],
    'Description': ['Manual Triage', 'Pattern Recognition', 'Intelligent Membrane'],
    'Efficiency': [40, 70, 90]
}

FRAMEWORK_PREDICTIONS = {
    'Prediction': ['TOIL Decrease', 'Cross-boundary Work', 'Retention Advantage',
                   'Cross-functional', 'Improvement Completion', 'Team Growth'],
    '2023_Predicted': ['Decrease TOIL', '20% rotation', 'Culture boost',
                       'Rotate over time', 'Kanban autonomy', 'Cross-pollinate'],
    '2025_Outcome': ['83.9%→50.6%', '70% cross-boundary', '15-20% advantage',
                     '90% capability', '86.7% completion', '850% growth'],
    'Validated': [True, True, True, True, True, True]
}

MTTR_BY_PRODUCT = {
    'Product': ['e-Builder', 'Cityworks', 'AgileAssets'],
    'MTTR_Minutes': [43, 660, 1355],  # converted to minutes for visualization
    'Category': ['Excellent', 'Good', 'Acceptable']
}

TICKET_VOLUME_BY_YEAR = {
    'Year': [2021, 2022, 2023, 2024, 2025],
    'Tickets': [100, 1472, 8045, 9054, 6824]
}

SELF_SERVICE_EVOLUTION = {
    'Tier': ['Tier 1: Instant', 'Tier 2: Guided', 'Tier 3: Concierge'],
    'Current': [55, 58, 57],
    'Target': [95, 85, 75],
    'Services': ['IP Whitelist, FTP, DB Backup', 'Sandbox, Site Changes', 'Site Setup, TUF']
}


def create_toil_categories():
    """TOIL category breakdown pie chart"""
    fig, ax = plt.subplots(figsize=(10, 8))

    df = pd.DataFrame(TOIL_CATEGORIES)
    colors = ['#3498db', '#2ecc71', '#e74c3c', '#f39c12', '#9b59b6']

    wedges, texts, autotexts = ax.pie(df['Percentage'], labels=df['Category'],
                                       autopct='%1.0f%%', colors=colors,
                                       explode=[0.05]*5, shadow=True,
                                       textprops={'fontsize': 12})

    for autotext in autotexts:
        autotext.set_fontweight('bold')
        autotext.set_color('white')

    ax.set_title('TOIL Category Breakdown\nConfiguration + Task = 45% of Total TOIL',
                 fontsize=14, fontweight='bold', pad=20)

    # Add legend with descriptions
    legend_labels = [f"{cat}: {desc}" for cat, desc in zip(df['Category'], df['Description'])]
    ax.legend(wedges, legend_labels, loc='lower center', bbox_to_anchor=(0.5, -0.1),
              ncol=2, fontsize=10)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'toil_categories.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print(f"Created: {OUTPUT_DIR / 'toil_categories.png'}")


def create_seasonality():
    """Ticket volume seasonality analysis"""
    fig, ax = plt.subplots(figsize=(12, 6))

    df = pd.DataFrame(SEASONALITY)

    # Color bars by intensity
    colors = ['#e74c3c' if t > 1200 else '#f39c12' if t > 900 else '#27ae60'
              for t in df['Tickets']]

    bars = ax.bar(df['Month'], df['Tickets'], color=colors, edgecolor='white', linewidth=2)

    # Add peak and low annotations
    max_idx = df['Tickets'].idxmax()
    min_idx = df['Tickets'].idxmin()

    ax.annotate(f'PEAK\n{df.iloc[max_idx]["Tickets"]}',
                xy=(max_idx, df.iloc[max_idx]['Tickets']),
                xytext=(max_idx, df.iloc[max_idx]['Tickets'] + 150),
                ha='center', fontweight='bold', color='#e74c3c',
                arrowprops=dict(arrowstyle='->', color='#e74c3c'))

    ax.annotate(f'LOW\n{df.iloc[min_idx]["Tickets"]}',
                xy=(min_idx, df.iloc[min_idx]['Tickets']),
                xytext=(min_idx, df.iloc[min_idx]['Tickets'] + 200),
                ha='center', fontweight='bold', color='#27ae60',
                arrowprops=dict(arrowstyle='->', color='#27ae60'))

    # Add average line
    avg = df['Tickets'].mean()
    ax.axhline(y=avg, color='#34495e', linestyle='--', linewidth=2,
               label=f'Average: {avg:.0f}')

    # Add variance annotation
    variance = df['Tickets'].max() / df['Tickets'].min()
    ax.text(0.02, 0.98, f'2.7x Variance\n(Peak/Low)', transform=ax.transAxes,
            fontsize=11, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

    ax.set_xlabel('Month', fontsize=12, fontweight='bold')
    ax.set_ylabel('Ticket Volume', fontsize=12, fontweight='bold')
    ax.set_title('Ticket Volume Seasonality\nManaged Through Shared Resource Management',
                 fontsize=14, fontweight='bold', pad=20)
    ax.legend(loc='upper right')
    ax.set_ylim(0, 1700)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'seasonality.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print(f"Created: {OUTPUT_DIR / 'seasonality.png'}")


def create_gatekeeper_evolution():
    """Gatekeeper evolution through phases"""
    fig, ax = plt.subplots(figsize=(10, 6))

    df = pd.DataFrame(GATEKEEPER_EVOLUTION)
    colors = ['#3498db', '#f39c12', '#27ae60']

    bars = ax.bar(df['Phase'], df['Efficiency'], color=colors, edgecolor='white', linewidth=2)

    # Add labels
    for bar, desc, eff in zip(bars, df['Description'], df['Efficiency']):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 2,
                f'{eff}%', ha='center', va='bottom', fontweight='bold', fontsize=14)
        ax.text(bar.get_x() + bar.get_width()/2., height/2,
                desc, ha='center', va='center', fontsize=10, color='white',
                fontweight='bold')

    ax.set_ylabel('Efficiency (%)', fontsize=12, fontweight='bold')
    ax.set_title('Gatekeeper Evolution: Manual to Intelligent\n1,356 Automation Candidates Identified',
                 fontsize=14, fontweight='bold', pad=20)
    ax.set_ylim(0, 110)

    # Add arrow showing progression
    ax.annotate('', xy=(2.3, 85), xytext=(-0.3, 35),
                arrowprops=dict(arrowstyle='->', color='#9b59b6', lw=2,
                               connectionstyle='arc3,rad=0.2'))

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'gatekeeper_evolution.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print(f"Created: {OUTPUT_DIR / 'gatekeeper_evolution.png'}")


def create_ticket_volume_trend():
    """Ticket volume by year"""
    fig, ax = plt.subplots(figsize=(10, 6))

    df = pd.DataFrame(TICKET_VOLUME_BY_YEAR)

    # Create bar chart
    colors = ['#3498db', '#3498db', '#e74c3c', '#f39c12', '#27ae60']
    bars = ax.bar(df['Year'], df['Tickets'], color=colors, edgecolor='white', linewidth=2)

    # Add trend line
    ax.plot(df['Year'], df['Tickets'], 'o--', color='#34495e', linewidth=2, markersize=8)

    # Add value labels
    for bar, val in zip(bars, df['Tickets']):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 200,
                f'{val:,}', ha='center', va='bottom', fontweight='bold', fontsize=11)

    # Annotate total
    total = df['Tickets'].sum()
    ax.text(0.98, 0.98, f'Total: {total:,} tickets\nacross 5 years',
            transform=ax.transAxes, ha='right', va='top', fontsize=11,
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

    ax.set_xlabel('Year', fontsize=12, fontweight='bold')
    ax.set_ylabel('Ticket Volume', fontsize=12, fontweight='bold')
    ax.set_title('Ticket Volume Growth (2021-2025)\n25,498 Total Tickets Analyzed',
                 fontsize=14, fontweight='bold', pad=20)
    ax.set_ylim(0, 11000)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'ticket_volume.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print(f"Created: {OUTPUT_DIR / 'ticket_volume.png'}")


def create_mttr_comparison():
    """MTTR by product comparison"""
    fig, ax = plt.subplots(figsize=(10, 6))

    df = pd.DataFrame(MTTR_BY_PRODUCT)
    colors = ['#27ae60', '#f39c12', '#e74c3c']

    bars = ax.barh(df['Product'], df['MTTR_Minutes'], color=colors,
                   edgecolor='white', linewidth=2)

    # Add labels
    for bar, mttr, cat in zip(bars, df['MTTR_Minutes'], df['Category']):
        width = bar.get_width()
        if mttr < 100:
            label = f'{mttr} min'
        else:
            label = f'{mttr/60:.1f} hrs'
        ax.text(width + 30, bar.get_y() + bar.get_height()/2,
                f'{label} ({cat})', ha='left', va='center', fontweight='bold')

    ax.set_xlabel('MTTR (minutes)', fontsize=12, fontweight='bold')
    ax.set_title('Mean Time to Recovery (MTTR) by Product\nFrom SRE Monitoring Data',
                 fontsize=14, fontweight='bold', pad=20)
    ax.set_xlim(0, 1600)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'mttr_comparison.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print(f"Created: {OUTPUT_DIR / 'mttr_comparison.png'}")


def create_self_service_roadmap():
    """Self-service evolution roadmap"""
    fig, ax = plt.subplots(figsize=(12, 6))

    df = pd.DataFrame(SELF_SERVICE_EVOLUTION)

    x = np.arange(len(df['Tier']))
    width = 0.35

    bars1 = ax.bar(x - width/2, df['Current'], width, label='Current Adherence',
                   color='#e74c3c', edgecolor='white')
    bars2 = ax.bar(x + width/2, df['Target'], width, label='Q3 2026 Target',
                   color='#27ae60', edgecolor='white')

    # Add value labels
    for bar in bars1:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{height:.0f}%', ha='center', va='bottom', fontweight='bold')

    for bar in bars2:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{height:.0f}%', ha='center', va='bottom', fontweight='bold')

    # Add service descriptions
    for i, services in enumerate(df['Services']):
        ax.text(i, -8, services, ha='center', va='top', fontsize=9,
                style='italic', wrap=True)

    ax.set_ylabel('OLA Adherence (%)', fontsize=12, fontweight='bold')
    ax.set_title('Self-Service Evolution Roadmap (2026)\nTarget: 85% Overall Adherence',
                 fontsize=14, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(df['Tier'], fontsize=11)
    ax.legend(loc='upper right')
    ax.set_ylim(0, 110)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'self_service_roadmap.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print(f"Created: {OUTPUT_DIR / 'self_service_roadmap.png'}")


def create_framework_validation():
    """2023 Predictions vs 2025 Outcomes validation"""
    fig, ax = plt.subplots(figsize=(12, 8))

    predictions = ['TOIL\nReduction', 'Cross-boundary\nWork', 'Retention\nAdvantage',
                   'Cross-functional\nCapability', 'Improvement\nCompletion', 'Team\nGrowth']
    outcomes = ['33.3pp\nreduction', '70%\nachieved', '15-20%\nadvantage',
                '90%\ncapability', '86.7%\ncompletion', '850%\ngrowth']

    # All validated
    colors = ['#27ae60'] * 6

    y_pos = np.arange(len(predictions))

    bars = ax.barh(y_pos, [100]*6, color=colors, edgecolor='white', linewidth=2, alpha=0.8)

    # Add prediction and outcome text
    for i, (pred, out) in enumerate(zip(predictions, outcomes)):
        ax.text(50, i, out, ha='center', va='center', fontsize=11,
                fontweight='bold', color='white')

    ax.set_yticks(y_pos)
    ax.set_yticklabels(predictions, fontsize=11)
    ax.set_xlim(0, 100)
    ax.set_xlabel('Validation Status', fontsize=12, fontweight='bold')
    ax.set_title('Framework Genesis: 2023 Predictions vs 2025 Outcomes\nAll 6 Core Predictions Validated',
                 fontsize=14, fontweight='bold', pad=20)

    # Hide x-axis ticks
    ax.set_xticks([])

    # Add checkmarks
    for i in range(len(predictions)):
        ax.text(95, i, '✓', ha='center', va='center', fontsize=20,
                fontweight='bold', color='white')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'framework_validation.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print(f"Created: {OUTPUT_DIR / 'framework_validation.png'}")


def create_fractal_levels():
    """Fractal application at different organizational levels"""
    fig, ax = plt.subplots(figsize=(12, 8))

    levels = ['Individual', 'Team', 'Organization']
    practices = ['Protect', 'Prepare', 'Pulse', 'Pool', 'Promote']

    # Create heatmap-style visualization
    data = np.ones((3, 5))  # All practices apply at all levels

    colors_map = plt.cm.Blues(np.linspace(0.3, 0.7, 5))

    for i, level in enumerate(levels):
        for j, practice in enumerate(practices):
            rect = plt.Rectangle((j, 2-i), 0.95, 0.95,
                                  facecolor=colors_map[j], edgecolor='white', linewidth=2)
            ax.add_patch(rect)

    # Add labels
    applications = [
        ['Shield from\ninterrupts', 'Cross-train\nskills', 'Regular\n1:1s', 'Share\nexpertise', 'Recognize\ngrowth'],
        ['Triage\nincoming', 'Rotation\nprograms', 'Sprint\nretros', 'Resource\nsharing', 'Team\nrituals'],
        ['Gatekeeping\nfunction', 'Follow-the\n-Sun', 'Quarterly\nreviews', 'Talent\npooling', 'Culture\ncarriers']
    ]

    for i in range(3):
        for j in range(5):
            ax.text(j + 0.475, 2-i + 0.475, applications[i][j],
                    ha='center', va='center', fontsize=9, fontweight='bold')

    ax.set_xlim(0, 5)
    ax.set_ylim(0, 3)
    ax.set_xticks([x + 0.475 for x in range(5)])
    ax.set_xticklabels(practices, fontsize=12, fontweight='bold')
    ax.set_yticks([0.475, 1.475, 2.475])
    ax.set_yticklabels(['Organization', 'Team', 'Individual'], fontsize=12, fontweight='bold')
    ax.set_title('Fractal Framework: Same Practices at Every Scale\nThe Five P\'s Apply at Individual, Team, and Organization Levels',
                 fontsize=14, fontweight='bold', pad=20)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'fractal_levels.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print(f"Created: {OUTPUT_DIR / 'fractal_levels.png'}")


if __name__ == '__main__':
    print("Generating additional Fluid Reliability visualizations...")
    print("-" * 50)

    create_toil_categories()
    create_seasonality()
    create_gatekeeper_evolution()
    create_ticket_volume_trend()
    create_mttr_comparison()
    create_self_service_roadmap()
    create_framework_validation()
    create_fractal_levels()

    print("-" * 50)
    print("All additional visualizations generated!")
