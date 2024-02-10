from htmltools import a
from shiny.express import ui
from shinyobservable import Observable, ObservableRenderer

NOTEBOOK = "https://observablehq.com/@d3/zoomable-sunburst"
# NOTEBOOK = "https://observablehq.com/d/31ab0068a4664578"

ui.h1("Observable Notebook in Shiny")
ui.div(a(NOTEBOOK, href=NOTEBOOK))
ui.hr()


@ObservableRenderer
def render_notebook():
    return Observable(NOTEBOOK, cells=[0, "chart"])
