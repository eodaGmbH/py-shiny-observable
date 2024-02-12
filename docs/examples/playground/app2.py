from htmltools import a
from shiny.express import ui
from shinyobservable import Observable, ObservableRenderer

NOTEBOOK = "https://observablehq.com/@eoda/playground"

ui.h1("Observable Notebook in Shiny")
ui.div(a(NOTEBOOK, href=NOTEBOOK, target="_blank"))
ui.hr()


# Embed selected cells
@ObservableRenderer
def render_cells():
    return (
        Observable(NOTEBOOK, cells=["viewof echart", "echart"])
        .redefine(
            chartData=dict(x=["A", "B", "C", "D", "E"], y=[100, 150, 120, 40, 80])
        )
        .redefine(lineColor="green")
    )


# Include entire notebook
# @ObservableRenderer
def render_notebook():
    return Observable(NOTEBOOK)
