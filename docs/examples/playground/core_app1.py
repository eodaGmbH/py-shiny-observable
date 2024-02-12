from pathlib import Path

from htmltools import a
from shiny import App, ui
from shinyobservable import Observable, ObservableRenderer, output_observable

NOTEBOOK = "https://observablehq.com/@eoda/playground"
# NOTEBOOK = "http://localhost:8000/f79314d948ee7a3c@150.js"
app_dir = Path(__file__).parent

app_ui = ui.page_fluid(
    ui.h1("Observable Notebook in Shiny"),
    ui.div(a(NOTEBOOK, href=NOTEBOOK, target="_blank")),
    ui.hr(),
    output_observable("render_observable"),
)


def server(input, output, session):
    # Embed selected cells
    @ObservableRenderer
    def render_observable():
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
        return Observable(NOTEBOOK, validate=True)


app = App(app_ui, server, static_assets=app_dir / "js")
