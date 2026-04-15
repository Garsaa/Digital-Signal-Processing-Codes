"""Reusable plotting helpers."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

import matplotlib.pyplot as plt


def plot_series(
    series: Sequence[dict[str, Any]],
    title: str,
    xlabel: str,
    ylabel: str,
    figsize: tuple[float, float] = (12, 6),
    grid: bool = True,
    legend: bool = True,
    tight_layout: bool = True,
) -> None:
    """Plot one or more series on the same figure.

    Each item in ``series`` must include a ``y`` value and can optionally
    include ``x`` and ``plot_kwargs`` to customize the corresponding line.
    """

    plt.figure(figsize=figsize)

    for item in series:
        x_values = item.get("x")
        y_values = item["y"]
        plot_kwargs = item.get("plot_kwargs", {})

        if x_values is None:
            plt.plot(y_values, **plot_kwargs)
        else:
            plt.plot(x_values, y_values, **plot_kwargs)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(grid)

    if legend:
        plt.legend()

    if tight_layout:
        plt.tight_layout()

    plt.show()
