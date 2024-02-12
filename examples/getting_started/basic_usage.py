from htmltools import a
from shiny.express import ui
from shinyobservable import Observable, ObservableRenderer

NOTEBOOK = "https://observablehq.com/@d3/zoomable-sunburst"

ui.h1("Observable Notebook in Shiny")
ui.div(a(NOTEBOOK, href=NOTEBOOK, target="_blank"))
ui.hr()


# Embed selected cells
@ObservableRenderer
def render_cells():
    return Observable(NOTEBOOK, cells=["chart"])


# Include entire notebook
# @ObservableRenderer
def render_notebook():
    return Observable(NOTEBOOK)
