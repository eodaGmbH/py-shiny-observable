import requests
from htmltools import a
from shiny.express import ui
from shinyobservable import Observable, ObservableRenderer

NOTEBOOK = "https://observablehq.com/@d3/zoomable-sunburst"

data = requests.get(
    "https://raw.githubusercontent.com/observablehq/examples/main/custom-data/population.json"
).json()

print(data)

ui.h1("Observable Notebook in Shiny")
ui.div(a(NOTEBOOK, href=NOTEBOOK, target="_blank"))
ui.hr()


@ObservableRenderer
def render_cells():
    # Update the 'data' cell with the data downloaded above
    return Observable(NOTEBOOK, cells=["chart"]).redefine(data=data)
