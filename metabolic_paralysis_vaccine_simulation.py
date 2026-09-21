"""
Conceptual Simulation of the Metabolically Paralyzed Trypanosomatid Vaccine Platform
------------------------------------------------------------------------------------
This is an EDUCATIONAL / ILLUSTRATIVE model only.
It is NOT a predictive biological simulator.

It demonstrates the core mechanism described in the Nigerian provisional patent:
"Genetically Engineered Metabolically Paralyzed Trypanosomatid Vaccine Platforms..."

Key idea simulated:
  CRISPR dual knockout of PEX5 + Trypanothione Reductase
  → ATP & redox collapse
  → surface recycling stalls (~12 min cycle broken)
  → flagellar pocket deforms / expands
  → invariant internal antigens (PFR1/PFR2 etc.) become exposed
  → delayed-death harvest window
  → coat-independent immune visibility

Author: Conceptual demo for Ayoola Oluwalonimi Emmanuel
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import textwrap

# ============================================================
# SIMULATION PARAMETERS (tunable)
# ============================================================
TOTAL_MINUTES = 180          # total simulation time
DT = 1.0                     # time step in minutes
TIME = np.arange(0, TOTAL_MINUTES + DT, DT)

# Wild-type baseline
WT_RECYCLING_TIME = 12.0     # minutes for full surface turnover
WT_ATP_PRODUCTION = 1.0
WT_ATP_CONSUMPTION = 0.08

# Engineered (after dual PEX5 + TR knockout at t=0)
KO_ATP_PRODUCTION_FACTOR = 0.15   # severe drop in ATP generation
KO_ATP_DECAY = 0.045              # progressive collapse
RECYCLING_STALL_THRESHOLD = 0.25  # ATP level below which recycling collapses
POCKET_OPEN_RATE = 0.035
ANTIGEN_EXPOSURE_RATE = 0.04
HARVEST_WINDOW_START = 25         # minutes after knockout
HARVEST_WINDOW_END = 95

# ============================================================
# HELPER FUNCTIONS
# ============================================================
def simulate_wild_type(time):
    """Wild-type parasite: stable ATP, fast recycling, almost no internal antigen exposure"""
    n = len(time)
    atp = np.ones(n)
    recycling = np.ones(n)                 # 1.0 = full 12-min cycle speed
    pocket = np.zeros(n)                   # closed
    antigen = np.zeros(n)                  # internal antigens hidden
    viability = np.ones(n)
    immune_score = np.zeros(n)             # almost invisible to adaptive immunity on invariants

    for i in range(1, n):
        # ATP homeostasis
        atp[i] = atp[i-1] + (WT_ATP_PRODUCTION - WT_ATP_CONSUMPTION * atp[i-1]) * DT
        atp[i] = np.clip(atp[i], 0.7, 1.2)

        # Fast continuous recycling
        recycling[i] = 1.0

        # Pocket stays closed, antigens stay internal
        pocket[i] = 0.02 * np.random.rand()   # tiny noise
        antigen[i] = 0.01 * np.random.rand()

        # Immune system sees almost nothing of the invariant core
        immune_score[i] = 0.05 + 0.03 * np.random.rand()

        viability[i] = 1.0

    return {
        "atp": atp,
        "recycling": recycling,
        "pocket": pocket,
        "antigen": antigen,
        "viability": viability,
        "immune": immune_score
    }


def simulate_engineered(time):
    """
    Engineered cell after dual CRISPR knockout of PEX5 + TR at t = 0.
    Progressive metabolic paralysis → recycling stall → pocket expansion → antigen exposure.
    """
    n = len(time)
    atp = np.ones(n)
    recycling = np.ones(n)
    pocket = np.zeros(n)
    antigen = np.zeros(n)
    viability = np.ones(n)
    immune_score = np.zeros(n)

    for i in range(1, n):
        t = time[i]

        # 1. ATP collapses after knockout
        production = WT_ATP_PRODUCTION * KO_ATP_PRODUCTION_FACTOR
        atp[i] = atp[i-1] + (production - KO_ATP_DECAY * atp[i-1] * 1.8) * DT
        atp[i] = max(atp[i], 0.0)

        # 2. Recycling rate depends on available ATP
        if atp[i] > RECYCLING_STALL_THRESHOLD:
            recycling[i] = atp[i] ** 1.5          # still working but slowing
        else:
            # Hard stall once ATP is critically low
            recycling[i] = max(0.02, recycling[i-1] * 0.92)

        # 3. Flagellar pocket progressively opens as recycling fails
        if recycling[i] < 0.4:
            pocket[i] = pocket[i-1] + POCKET_OPEN_RATE * (1.0 - pocket[i-1]) * DT
        else:
            pocket[i] = pocket[i-1] * 0.98
        pocket[i] = np.clip(pocket[i], 0.0, 1.0)

        # 4. Invariant internal antigens become exposed
        antigen[i] = antigen[i-1] + ANTIGEN_EXPOSURE_RATE * pocket[i] * DT
        antigen[i] = np.clip(antigen[i], 0.0, 1.0)

        # 5. Immune recognition score (coat-independent)
        #    Rises strongly once antigens are exposed and recycling is stalled
        immune_score[i] = (
            0.15 * (1.0 - recycling[i]) +
            0.55 * antigen[i] +
            0.30 * pocket[i]
        )
        immune_score[i] = np.clip(immune_score[i], 0.0, 1.0)

        # 6. Viability declines slowly (delayed-death phenotype)
        if t < 20:
            viability[i] = 1.0
        else:
            viability[i] = viability[i-1] - 0.0045 * (1.0 - atp[i]) * DT
            viability[i] = max(viability[i], 0.0)

    return {
        "atp": atp,
        "recycling": recycling,
        "pocket": pocket,
        "antigen": antigen,
        "viability": viability,
        "immune": immune_score
    }
def print_homology_summary():
    """
    Displays the in-silico homology results from the patent
    (low sequence identity to human proteins = lower autoimmunity risk)
    """
    print("\n" + "="*70)
    print("HOMOLOGY / SAFETY SUMMARY (from Patent Disclosure)")
    print("="*70)
    print(textwrap.dedent("""
    In-silico BLASTp screening against human proteome (taxid:9606):

    T. brucei PEX5          →  ~35.1% identity to human PEX5
    T. brucei TR            →  ~37.5% identity to human glutathione reductase
    T. cruzi  PEX5          →  ~38.6% identity to human PEX5
    T. cruzi  TR            →  ~35.3% identity to human glutathione reductase

    Interpretation:
    • Sequence identity is well below typical autoimmunity concern thresholds
    • Large portions of the parasite proteins are unique
    • Supports the design goal of exposing invariant parasite antigens
      while minimizing risk of cross-reactivity with human proteins
    """).strip())
    print("="*70)

# ============================================================
# RUN SIMULATION
# ============================================================
print("Running conceptual simulation of metabolically paralyzed vaccine platform...")
wt = simulate_wild_type(TIME)
eng = simulate_engineered(TIME)

# ============================================================
# PLOTTING
# ============================================================
plt.style.use("seaborn-v0_8-whitegrid")
fig, axes = plt.subplots(3, 2, figsize=(14, 12))
fig.suptitle("Conceptual Simulation: Metabolically Paralyzed Trypanosomatid Vaccine Platform\n"
             "(Dual PEX5 + TR Knockout → Recycling Stall → Invariant Antigen Exposure)",
             fontsize=14, fontweight="bold", y=0.98)

# --- ATP ---
ax = axes[0, 0]
ax.plot(TIME, wt["atp"], label="Wild-type", color="#1f77b4", linewidth=2)
ax.plot(TIME, eng["atp"], label="Engineered (PEX5+TR KO)", color="#d62728", linewidth=2.5)
ax.axvspan(HARVEST_WINDOW_START, HARVEST_WINDOW_END, alpha=0.15, color="green",
           label="Harvest Window")
ax.set_ylabel("Relative ATP Level")
ax.set_title("ATP / Energy Homeostasis")
ax.legend(loc="upper right")
ax.set_ylim(0, 1.3)

# --- Recycling rate ---
ax = axes[0, 1]
ax.plot(TIME, wt["recycling"], label="Wild-type (≈12 min cycle)", color="#1f77b4", linewidth=2)
ax.plot(TIME, eng["recycling"], label="Engineered – Recycling Stalls", color="#d62728", linewidth=2.5)
ax.axvspan(HARVEST_WINDOW_START, HARVEST_WINDOW_END, alpha=0.15, color="green")
ax.set_ylabel("Relative Recycling Rate")
ax.set_title("Surface Coat Recycling (Flagellar Pocket Endocytosis)")
ax.legend(loc="upper right")
ax.set_ylim(0, 1.15)

# --- Flagellar pocket openness ---
ax = axes[1, 0]
ax.plot(TIME, wt["pocket"], label="Wild-type (closed)", color="#1f77b4", linewidth=2)
ax.plot(TIME, eng["pocket"], label="Engineered – Pocket Expands", color="#d62728", linewidth=2.5)
ax.axvspan(HARVEST_WINDOW_START, HARVEST_WINDOW_END, alpha=0.15, color="green")
ax.set_ylabel("Pocket Openness (0–1)")
ax.set_title("Flagellar Pocket Deformation / Expansion")
ax.legend(loc="upper left")
ax.set_ylim(0, 1.05)

# --- Invariant antigen exposure ---
ax = axes[1, 1]
ax.plot(TIME, wt["antigen"], label="Wild-type (hidden)", color="#1f77b4", linewidth=2)
ax.plot(TIME, eng["antigen"], label="Engineered – Antigens Exposed", color="#d62728", linewidth=2.5)
ax.axvspan(HARVEST_WINDOW_START, HARVEST_WINDOW_END, alpha=0.15, color="green")
ax.set_ylabel("Antigen Exposure (0–1)")
ax.set_title("Invariant Internal Antigens (PFR1/PFR2, etc.)")
ax.legend(loc="upper left")
ax.set_ylim(0, 1.05)

# --- Immune recognition score ---
ax = axes[2, 0]
ax.plot(TIME, wt["immune"], label="Wild-type (coat-dependent escape)", color="#1f77b4", linewidth=2)
ax.plot(TIME, eng["immune"], label="Engineered – Coat-Independent Visibility", color="#d62728", linewidth=2.5)
ax.axvspan(HARVEST_WINDOW_START, HARVEST_WINDOW_END, alpha=0.15, color="green")
ax.set_ylabel("Immune Recognition Score")
ax.set_xlabel("Time (minutes after knockout)")
ax.set_title("Coat-Independent Immune Visibility")
ax.legend(loc="upper left")
ax.set_ylim(0, 1.05)

# --- Viability + Harvest window ---
ax = axes[2, 1]
ax.plot(TIME, eng["viability"], label="Engineered Cell Viability", color="#d62728", linewidth=2.5)
ax.axvspan(HARVEST_WINDOW_START, HARVEST_WINDOW_END, alpha=0.25, color="green",
           label="Optimal Harvest Window\n(structurally intact + antigens exposed)")
ax.axvline(HARVEST_WINDOW_START, color="green", linestyle="--", alpha=0.7)
ax.axvline(HARVEST_WINDOW_END, color="green", linestyle="--", alpha=0.7)
ax.set_ylabel("Relative Viability")
ax.set_xlabel("Time (minutes after knockout)")
ax.set_title("Delayed-Death Phenotype & Harvest Window")
ax.legend(loc="upper right")
ax.set_ylim(0, 1.1)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig("metabolic_paralysis_vaccine_simulation.png", dpi=200, bbox_inches="tight")
plt.show()

# ============================================================
# TEXT SUMMARY
# ============================================================
print("\n" + "="*70)
print("SIMULATION SUMMARY")
print("="*70)
print(f"Knockout time:                t = 0 min (PEX5 + Trypanothione Reductase)")
print(f"Recycling stall begins:       ~ when ATP < {RECYCLING_STALL_THRESHOLD}")
print(f"Harvest window:               {HARVEST_WINDOW_START} – {HARVEST_WINDOW_END} minutes")
print(f"Peak antigen exposure:        {eng['antigen'].max():.2f}")
print(f"Peak immune recognition:      {eng['immune'].max():.2f}")
print(f"Viability at end of window:   {eng['viability'][int(HARVEST_WINDOW_END)]:.2f}")
print()
print("Interpretation:")
print("  • Wild-type maintains high recycling → antibodies cleared → immune escape")
print("  • Engineered cell undergoes metabolic paralysis → recycling stalls")
print("  • Flagellar pocket expands → invariant antigens become visible")
print("  • This creates a coat-independent target for the immune system")
print("  • Cells are ideally harvested inside the green window while still intact")
print("="*70)
print_homology_summary()
print("\nFigure saved as: metabolic_paralysis_vaccine_simulation.png")
