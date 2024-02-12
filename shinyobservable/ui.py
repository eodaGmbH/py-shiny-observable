from htmltools import HTMLDependency, Tag
from shiny import ui
from shiny.module import resolve_id

observable_bindings_dep = HTMLDependency(
    "observable-bindings",
    version="1.0.0",
    source={"package": "shinyobservable", "subdir": "srcjs"},
    script={"src": "observable-bindings.js", "type": "module"},
    all_files=False,
)


def output_observable(id: str) -> Tag:
    """Create an output control for an `Observable` object

    Arguments:
        id: An output id.
    """
    return ui.div(
        observable_bindings_dep,
        # Use resolve_id so that our component will work in a module
        id=resolve_id(id),
        class_="shiny-observable-output",
    )
