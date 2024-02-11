from __future__ import annotations

from os.path import join, relpath

BASE_URL = "https://observablehq.com"
BASE_API_URL = "https://api.observablehq.com"
API_VERSION = 4


class Observable(object):
    """Create an Observable notebook instance

    Args:
        notebook: The URL of the notebook to be embedded.
        cells: The cells to be embedded. If `None`, the entire notebook is embedded.
        width: The width of the notebook element.
    """

    data = dict()

    def __init__(
        self, notebook: str, cells: list = None, width: int | str = None
    ) -> None:
        if isinstance(width, int):
            width = f"{width}px"

        self.width = width
        if "//api" not in notebook:
            notebook = (
                f"{BASE_API_URL}/{relpath(notebook, BASE_URL)}.js?v={API_VERSION}"
            )

        self.notebook = notebook
        self.cells = cells

    def redefine(self, **kwargs) -> Observable:
        self.data = kwargs
        return self

    def to_dict(self):
        return dict(
            notebook=self.notebook, cells=self.cells, data=self.data, width=self.width
        )
