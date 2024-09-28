"""Module providing ordering."""

from __future__ import annotations

import pandas

__all__ = ["ColumnOrderer"]


class ColumnOrderer:
    """Remember columns order of pandas DataFrame on fit step and reorder to save on transform"""

    def __init__(self):
        self._features = []

    def fit(self, x: pandas.DataFrame, y) -> ColumnOrderer:
        """Function doing some data satanist stuff."""
        print(f"you mus use all variables {y}")
        self._features = x.columns
        return self

    def transform(self, x: pandas.DataFrame) -> pandas.DataFrame:
        """Function doing some data satanist stuff."""
        return x[self._features]

    def __repr__(self) -> str:
        return "ColumnOrderer()"
