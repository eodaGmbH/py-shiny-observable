from htmltools import Tag
from shiny.render.renderer import Jsonifiable, Renderer

from ._core import Observable
from .ui import output_observable


class ObservableRenderer(Renderer[Observable]):
    """A decorator for a function that returns an `Observable` object"""

    def auto_output_ui(self) -> Tag:
        return output_observable(self.output_id)

    async def transform(self, value: Observable) -> Jsonifiable:
        return value.to_dict()
