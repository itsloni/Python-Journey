"""
Interactive Simulation Dashboard
Metabolically Paralyzed Trypanosomatid Vaccine Platform
Dual CRISPR Knockout: PEX5 + Trypanothione Reductase
"""

import streamlit as st
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import time

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="Metabolically Paralyzed Vaccine Platform",
    page_icon="🧬",
    layout="wide"
)

st.title("Metabolically Paralyzed Trypanosomatid Vaccine Platform")
st.markdown("**Interactive Conceptual Simulation** — Manufacturing / Vulnerability Phase Only")
st.markdown("---")

# --------------------------------------------------
# Simulation Parameters
# --------------------------------------------------
TOTAL_MIN = 240
DT = 1.0
TIME = np.arange(0, TOTAL_MIN + DT, DT)
N = len(TIME)

HW_START = 40
HW_END = 110
HW_PEAK = 72

# --------------------------------------------------
# Simulation Functions
# --------------------------------------------------
def simulate_wild_type():
    atp = 0.97 + 0.03 * np.sin(TIME / 12)
    recycling = 0.95 + 0.04 * np.sin(TIME / 9)
    pocket = np.full(N, 0.03)
    antigen = np.full(N, 0.02)
    accessibility = np.full(N, 0.03)
    presentation = np.full(N, 0.04)
    viability = np.ones(N)
    return dict(atp=atp, recycling=recycling, pocket=pocket,
                antigen=antigen, accessibility=accessibility,
                presentation=presentation, viability=viability)

def simulate_engineered(mode="both"):
    atp = np.ones(N)
    recycling = np.ones(N)
    pocket = np.zeros(N)
    antigen = np.zeros(N)
    accessibility = np.zeros(N)
    presentation = np.zeros(N)
    viability = np.ones(N)
    ros = np.zeros(N)

    pex5_factor = 1.0 if mode in ["pex5", "both"] else 0.0
    tr_factor   = 1.0 if mode in ["tr", "both"] else 0.0

    for i in range(1, N):
        t = TIME[i]

        pex5_c = min(1.0, max(0, (t - 5) / 30)) * pex5_factor
        tr_c   = min(1.0, max(0, (t - 8) / 40)) * tr_factor

        atp_loss = 0.018 * pex5_c + 0.009 * tr_c
        atp[i] = max(atp[i-1] * (1 - atp_loss), 0.02)

        ros[i] = tr_c * (1 - atp[i] * 0.3)
        if atp[i] > 0.65:
            recycling[i] = atp[i] * 0.92
        else:
            recycling[i] = max(0.02, recycling[i-1] * 0.91)

        pocket_drive = max(0, 0.5 - recycling[i]) * 2.0
        pocket[i] = min(1.0, pocket[i-1] + 0.06 * pocket_drive * (1 - pocket[i-1]))

        antigen[i] = min(1.0, antigen[i-1] + 0.045 * pocket[i] * (1 - antigen[i-1]))

        entry = 0.07 * pocket[i]
        clearance = 0.12 * recycling[i]
        accessibility[i] = min(1.0, max(0, accessibility[i-1] + entry - clearance))

        presentation[i] = min(1.0,
            0.15*(1 - recycling[i]) +
            0.55*antigen[i] +
            0.20*pocket[i] +
            0.10*ros[i]
        )

        if t < HW_START:
            viability[i] = 1.0
        else:
            death_rate = 0.003 + 0.008*(1 - atp[i]) + 0.004*ros[i]
            viability[i] = max(0.0, viability[i-1] * (1 - death_rate))

    return dict(atp=atp, recycling=recycling, pocket=pocket,
                antigen=antigen, accessibility=accessibility,
                presentation=presentation, viability=viability)

# --------------------------------------------------
# Sidebar Controls
# --------------------------------------------------
st.sidebar.header("Knockout Controls")

mode = st.sidebar.radio(
    "Select Knockout Mode:",
    ["Wild-type", "PEX5 Knockout", "TR Knockout", "Both (PEX5 + TR)"],
    index=3
)

mode_map = {
    "Wild-type": "wild",
    "PEX5 Knockout": "pex5",
    "TR Knockout": "tr",
    "Both (PEX5 + TR)": "both"
}
selected_mode = mode_map[mode]

show_harvest = st.sidebar.checkbox("Show Harvest Window", value=True)

# --------------------------------------------------
# Run Simulation
# --------------------------------------------------
wt = simulate_wild_type()

if selected_mode == "wild":
    eng = simulate_wild_type()
else:
    eng = simulate_engineered(selected_mode)

# --------------------------------------------------
# Tabs
# --------------------------------------------------
tab1, tab2, tab3 = st.tabs(["Core Mechanism", "Cross-Species & Phase Space", "Harvest Dashboard"])

# --------------------------------------------------
# TAB 1 — Core Mechanism
# --------------------------------------------------
with tab1:
    st.subheader("Core Mechanism — Manufacturing / Vulnerability Phase")

    fig = make_subplots(
        rows=3, cols=3,
        subplot_titles=(
            "① ATP / Energy Homeostasis",
            "② Surface Recycling Rate",
            "③ Flagellar Pocket Openness",
            "④ Structural Accessibility",
            "⑤ Invariant Antigen Exposure",
            "⑥ Presentation Potential",
            "⑦ Cell Viability",
            "⑧ Harvest Quality Score",
            "⑨ Summary View"
        ),
        vertical_spacing=0.12,
        horizontal_spacing=0.08
    )

    def add_trace(fig, y_wt, y_eng, row, col, name_wt="Wild-type", name_eng="Engineered"):
        fig.add_trace(go.Scatter(x=TIME, y=y_wt, name=name_wt, line=dict(color="#2166AC", width=2),
                                 showlegend=(row==1 and col==1)), row=row, col=col)
        fig.add_trace(go.Scatter(x=TIME, y=y_eng, name=name_eng, line=dict(color="#D6604D", width=2.5),
                                 showlegend=(row==1 and col==1)), row=row, col=col)

    add_trace(fig, wt["atp"], eng["atp"], 1, 1)
    add_trace(fig, wt["recycling"], eng["recycling"], 1, 2)
    add_trace(fig, wt["pocket"], eng["pocket"], 1, 3)
    add_trace(fig, wt["accessibility"], eng["accessibility"], 2, 1)
    add_trace(fig, wt["antigen"], eng["antigen"], 2, 2)
    add_trace(fig, wt["presentation"], eng["presentation"], 2, 3)
    add_trace(fig, wt["viability"], eng["viability"], 3, 1)

    # Harvest quality
    harvest_quality = 0.40*eng["antigen"] + 0.35*eng["viability"] + 0.25*eng["presentation"]
    fig.add_trace(go.Scatter(x=TIME, y=harvest_quality, name="Harvest Quality",
                             line=dict(color="#4DAC26", width=2.5)), row=3, col=2)

    # Summary
    fig.add_trace(go.Scatter(x=TIME, y=eng["antigen"], name="Antigen", line=dict(color="#2CA02C")), row=3, col=3)
    fig.add_trace(go.Scatter(x=TIME, y=eng["viability"], name="Viability", line=dict(color="#D6604D")), row=3, col=3)

    if show_harvest:
        for r in range(1, 4):
            for c in range(1, 4):
                fig.add_vrect(x0=HW_START, x1=HW_END, fillcolor="#4DAC26", opacity=0.12,
                              line_width=0, row=r, col=c)

    fig.update_layout(height=900, title_text=f"Current Mode: {mode}", showlegend=True)
    st.plotly_chart(fig, use_container_width=True)

# --------------------------------------------------
# TAB 2 — Cross Species (Simplified)
# --------------------------------------------------
with tab2:
    st.subheader("Cross-Species Antigen Exposure & Phase Space")

    col1, col2 = st.columns(2)

    with col1:
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=TIME, y=eng["antigen"], name="Engineered (Current Mode)",
                                  line=dict(color="#D6604D", width=3)))
        fig2.add_trace(go.Scatter(x=TIME, y=wt["antigen"], name="Wild-type",
                                  line=dict(color="#2166AC", width=2)))
        if show_harvest:
            fig2.add_vrect(x0=HW_START, x1=HW_END, fillcolor="#4DAC26", opacity=0.15, line_width=0)
        fig2.update_layout(title="Invariant Antigen Exposure Over Time",
                           xaxis_title="Time (min post-KO)",
                           yaxis_title="Antigen Exposure")
        st.plotly_chart(fig2, use_container_width=True)

    with col2:
        fig3 = go.Figure()
        fig3.add_trace(go.Scatter(
            x=eng["recycling"], y=eng["antigen"],
            mode="markers",
            marker=dict(size=5, color=TIME, colorscale="Plasma", showscale=True,
                        colorbar=dict(title="Time (min)")),
            name="Engineered trajectory"
        ))
        fig3.update_layout(title="Phase Space: Recycling vs Antigen Exposure",
                           xaxis_title="Recycling Rate",
                           yaxis_title="Antigen Exposure")
        st.plotly_chart(fig3, use_container_width=True)

# --------------------------------------------------
# TAB 3 — Harvest Dashboard
# --------------------------------------------------
with tab3:
    st.subheader("Harvest Window Optimisation")

    harvest_quality = 0.40*eng["antigen"] + 0.35*eng["viability"] + 0.25*eng["presentation"]

    fig4 = go.Figure()
    fig4.add_trace(go.Scatter(x=TIME, y=eng["antigen"], name="Antigen Exposure",
                              line=dict(color="#2CA02C", width=2)))
    fig4.add_trace(go.Scatter(x=TIME, y=eng["viability"], name="Viability",
                              line=dict(color="#D6604D", width=2)))
    fig4.add_trace(go.Scatter(x=TIME, y=harvest_quality, name="Harvest Quality",
                              line=dict(color="#4DAC26", width=3)))

    fig4.add_vline(x=HW_PEAK, line_dash="dash", line_color="black",
                   annotation_text=f"Optimal ≈ {HW_PEAK} min")

    if show_harvest:
        fig4.add_vrect(x0=HW_START, x1=HW_END, fillcolor="#4DAC26", opacity=0.12, line_width=0)

    fig4.update_layout(title="Harvest Quality Over Time",
                       xaxis_title="Time (min post-KO)",
                       yaxis_title="Score")
    st.plotly_chart(fig4, use_container_width=True)

    st.info(f"**Current Mode:** {mode}  |  **Suggested Harvest Window:** {HW_START}–{HW_END} min  |  **Peak around:** {HW_PEAK} min")

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("---")
st.caption("Educational / Illustrative conceptual model only. Not predictive biological data.")