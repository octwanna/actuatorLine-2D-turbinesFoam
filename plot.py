#!/usr/bin/env python
"""
This script plots results from `paramsweep.py`.
"""
from __future__ import division, print_function
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import seaborn as sns

U_infty = 1.0


if __name__ == "__main__":
    sns.set(style="white", context="paper", font_scale=1.5,
            rc={"axes.grid": True, "legend.frameon": True})
    df = pd.read_csv("processed/alpha_sweep.csv")
    fig, ax = plt.subplots()
    ax.plot(df.alpha_geom_deg, df.alpha_deg, "o", label="Detected")
    ax.plot(df.alpha_geom_deg, df.alpha_geom_deg, "--", label="Geometric")
    ax.set_xlabel(r"$\alpha$ (geometric, degrees)")
    ax.set_ylabel(r"$\alpha$ (detected, degrees)")
    ax.legend(loc="lower right")
    fig.tight_layout()
    plt.show()
