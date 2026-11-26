"""Figures for the OSF pages Background (01) and Research questions (02).

Run from the repository root:  python notes/osf/figures/make_figures.py
Reads only pre-registration inputs (results/models/m2/predictors_m2.csv).
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

REPO = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent

INK, MUTED, GRID = "#1f2328", "#6e7781", "#d0d7de"
BLUE, ORANGE, AQUA, YELLOW = "#257de0", "#f47230", "#00b894", "#f2a600"
FILL = {"blue": "#e3eefb", "orange": "#fde9df", "aqua": "#dcf5ef",
        "gray": "#f3f4f6", "yellow": "#fdf1d6"}

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 10, "text.color": INK,
    "axes.edgecolor": MUTED, "axes.labelcolor": INK,
    "xtick.color": MUTED, "ytick.color": MUTED, "savefig.dpi": 200,
})


def box(ax, x, y, w, h, text, fill="gray", edge=MUTED, size=10, weight="normal"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.06",
                                fc=FILL[fill], ec=edge, lw=1.2))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", size=size,
            weight=weight, linespacing=1.4)


def arrow(ax, p, q, color=MUTED, style="-|>", lw=1.4, rad=0.0, ls="-"):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle=style, mutation_scale=14, color=color,
                                 lw=lw, ls=ls, connectionstyle=f"arc3,rad={rad}"))


def canvas(w, h, xlim, ylim):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.axis("off")
    return fig, ax


# ---------------------------------------------------------------- 1. lens pipeline
def fig_lens():
    fig, ax = canvas(10, 2.9, (0, 10), (0.2, 3.0))
    y, h = 1.15, 1.1
    box(ax, 0.1, y, 1.6, h, "Face\nphotograph")
    box(ax, 2.2, y, 2.0, h, "Face-recognition\nnetwork\n(trained on identity)", "blue", BLUE)
    box(ax, 4.7, y, 1.6, h, "Embedding\n(128–4,096\nnumbers)", "blue", BLUE)
    box(ax, 6.8, y, 1.5, h, "Ridge read-out\none per trait", "orange", ORANGE)
    box(ax, 8.6, y, 1.3, h, "Predicted\ntrait scores", "orange", ORANGE)
    for a, b in [(1.7, 2.2), (4.2, 4.7), (6.3, 6.8), (8.3, 8.6)]:
        arrow(ax, (a, y + h / 2), (b, y + h / 2))
    # Brunswik mapping
    for x0, x1, lab in [(0.1, 1.7, "the face\n(trait not visible)"),
                        (2.2, 6.3, "proximal cues: the network's features"),
                        (6.8, 9.9, "the observer's judgment")]:
        ax.plot([x0, x1], [0.85, 0.85], color=MUTED, lw=1)
        ax.text((x0 + x1) / 2, 0.55, lab, ha="center", va="center", size=9, color=MUTED,
                style="italic", linespacing=1.3)
    ax.text(0.1, 2.6, "The network is chosen by recognition accuracy", size=10, color=BLUE,
            weight="bold")
    ax.text(6.8, 2.6, "Fitted to human ratings, then scores new faces", size=10,
            color=ORANGE, weight="bold")
    fig.savefig(OUT / "01_lens_pipeline.png", bbox_inches="tight")
    plt.close(fig)


# ------------------------------------------------- 2. alignment vs accuracy, 16 models
LABEL_OFFSET = {  # (dx, dy) in points, to avoid collisions
    "FaceNet": (6, -12), "FaceNet512": (-6, 9), "VGG-Face": (-8, -13), "IRV1-casia": (6, 7),
    "GhostFaceNet": (7, 2), "SFace": (7, -9), "OpenFace": (6, 5), "DeepFace": (6, -10),
    "ArcFace50": (6, 5), "ArcFace100": (6, 5), "swinface": (-8, -13), "w600k_r50": (-12, 9),
}
NAME = {"swinface": "SwinFace", "w600k_r50": "ResNet-50 WebFace600K",
        "IRV1-casia": "Inception-ResNet-v1 CASIA"}


def fig_models():
    df = pd.read_csv(REPO / "results/models/m2/predictors_m2.csv")
    df = df[~df.source.str.contains("gate")]
    assert len(df) == 16, len(df)
    fig, ax = plt.subplots(figsize=(7.6, 4.8))
    ax.grid(color=GRID, lw=0.6)
    ax.set_axisbelow(True)
    for src, col, mk, lab in [("release", MUTED, "o", "Hojjati et al. (14 core models)"),
                              ("own extraction", ORANGE, "D", "added in this study (2)")]:
        d = df[df.source == src]
        ax.errorbar(d.dprime, d.align_usafd, xerr=[d.dprime - d.d_lo, d.d_hi - d.dprime],
                    fmt="none", ecolor=col, elinewidth=1, alpha=0.6)
        ax.scatter(d.dprime, d.align_usafd, s=60, marker=mk, color=col, ec="white", lw=1.5,
                   zorder=3, label=lab)
    for _, r in df.iterrows():
        dx, dy = LABEL_OFFSET.get(r.model, (6, 4))
        ax.annotate(NAME.get(r.model, r.model), (r.dprime, r.align_usafd),
                    xytext=(dx, dy), textcoords="offset points", size=8.5, color=INK,
                    ha="right" if dx < 0 else "left")
    ax.set_xlabel("Recognition accuracy, d′ (CFD photograph pairs; bars: 95% CI)")
    ax.set_ylabel("Alignment with human similarity judgments\n(mean Spearman ρ, USAFD trials)")
    ax.set_xlim(0, 12.2)
    ax.set_ylim(0.08, 0.32)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.legend(frameon=False, loc="upper right", fontsize=9)
    fig.savefig(OUT / "01_alignment_vs_accuracy.png", bbox_inches="tight")
    plt.close(fig)


# ------------------------------------------------------------ 3. excess leakage
def fig_leakage():
    fig, ax = canvas(10, 4.2, (0, 10), (0, 4.2))
    # nodes
    box(ax, 0.2, 2.9, 2.2, 0.8, "Predicted\ntrustworthiness", "orange", ORANGE)
    box(ax, 4.4, 2.9, 2.0, 0.8, "Human\ntrustworthiness", "blue", BLUE)
    box(ax, 4.4, 0.5, 2.0, 0.8, "Human\nkindness", "blue", BLUE)
    arrow(ax, (2.4, 3.3), (4.4, 3.3), ORANGE, "-")
    ax.text(3.4, 3.45, "ρᵢ  accuracy", ha="center", size=9.5, color=INK)
    arrow(ax, (5.4, 2.9), (5.4, 1.3), BLUE, "-")
    ax.text(5.55, 2.1, "rᵢⱼ  human\ncorrelation", va="center", size=9.5, color=INK)
    arrow(ax, (2.0, 2.9), (4.4, 0.95), ORANGE, "-", ls="--")
    ax.text(2.35, 1.7, "Lᵢⱼ  leakage", size=9.5, color=INK, rotation=-38)
    # explanation panel
    x = 6.95
    ax.text(x, 3.75, "Expected leakage if the prediction is the true\ntrait plus noise:",
            size=9.5, va="top", linespacing=1.4)
    ax.text(x + 0.2, 2.95, "ρᵢ · rᵢⱼ / Rᵢ", size=12, va="top", weight="bold")
    ax.text(x, 2.35, "Excess leakage, the part not explained by\nhuman entanglement:",
            size=9.5, va="top", linespacing=1.4)
    ax.text(x + 0.2, 1.55, "ELᵢⱼ = Lᵢⱼ − ρᵢ · rᵢⱼ / Rᵢ", size=12, va="top", weight="bold")
    ax.text(x, 0.95, "L(m): average over all 182 ordered\npairs of the 14 traits",
            size=9.5, va="top", linespacing=1.4, color=MUTED)
    ax.text(0.2, 0.25, "Rᵢ = reliability of human ratings of trait i", size=8.5, color=MUTED)
    fig.savefig(OUT / "02_excess_leakage.png", bbox_inches="tight")
    plt.close(fig)


# ------------------------------------------------------------ 4. H1b design
def fig_h1b():
    fig, ax = canvas(10, 4.4, (0, 10), (0, 4.4))
    ax.text(0.1, 4.15, "Same network embeddings, four versions", size=10, weight="bold")
    rows = [("Raw embeddings", "gray", MUTED),
            ("Aligned (Hojjati et al. transformation)", "aqua", AQUA),
            ("Placebo (trained on shuffled triplets)", "yellow", YELLOW),
            ("Matched-spectrum random matrix", "yellow", YELLOW)]
    for k, (lab, f, e) in enumerate(rows):
        y = 3.2 - k * 0.85
        box(ax, 0.1, y, 3.4, 0.62, lab, f, e, size=9.5)
        arrow(ax, (3.5, y + 0.31), (4.3, 2.06), MUTED, lw=1.1)
    box(ax, 4.3, 1.55, 2.2, 1.0, "Ridge read-out\nfitted on the\n1,678 main faces", "orange",
        ORANGE, size=9.5)
    arrow(ax, (6.5, 2.05), (7.0, 2.05))
    box(ax, 7.0, 1.55, 2.0, 1.0, "L(m) on the\n544 hold-out\nfaces", "blue", BLUE, size=9.5)
    ax.text(7.0, 1.15, "ΔL = L(raw) − L(version)", size=9.5, weight="bold")
    ax.text(7.0, 0.45, "Support requires ΔL(aligned) > 0\nand larger than both controls",
            size=9, color=MUTED, linespacing=1.4)
    ax.text(0.1, 0.0, "No transformation was trained on any hold-out face.", size=8.5,
            color=MUTED)
    fig.savefig(OUT / "02_h1b_design.png", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    fig_lens()
    fig_models()
    fig_leakage()
    fig_h1b()
    print("written to", OUT)
