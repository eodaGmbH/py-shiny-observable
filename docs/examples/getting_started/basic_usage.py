from shiny.express import ui
from shinyobservable import Observable
from shinyobservable.render import ObservableRenderer

NOTEBOOK = "https://observablehq.com/@d3/zoomable-sunburst"


@ObservableRenderer
def render_notebook():
    return Observable(NOTEBOOK)
