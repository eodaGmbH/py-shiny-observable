from __future__ import annotations

from os.path import join, relpath

BASE_URL = "https://observablehq.com"
BASE_API_URL = "https://api.observablehq.com"
API_VERSION = 4


class Observable(object):
    def __init__(self, notebook, width: int | str = None):
        if isinstance(width, int):
            width = f"{width}px"

        self.width = width
        if not "//api" in notebook:
            notebook = (
                f"{BASE_API_URL}/{relpath(notebook, BASE_URL)}.js?v={API_VERSION}"
            )

        self.notebook = notebook

    def to_dict(self):
        return dict(notebook=self.notebook, width=self.width)
