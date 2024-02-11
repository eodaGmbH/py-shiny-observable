from htmltools import a
from shiny.express import ui
from shinyobservable import Observable, ObservableRenderer

NOTEBOOK = "https://observablehq.com/@d3/zoomable-sunburst"
# NOTEBOOK = "https://observablehq.com/d/31ab0068a4664578"

ui.h1("Observable Notebook in Shiny")
ui.div(a(NOTEBOOK, href=NOTEBOOK, target="_blank"))
ui.hr()


@ObservableRenderer
def render_cells():
    return Observable(NOTEBOOK, cells=["chart"])
    # return Observable(NOTEBOOK, cells=["mapView", "viewof mapView", "viewof h3Res"])


# @ObservableRenderer
def render_notebook():
    return Observable(NOTEBOOK)
