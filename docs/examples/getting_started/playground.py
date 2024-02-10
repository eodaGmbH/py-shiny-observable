import random
import string

from htmltools import a
from shiny.express import ui
from shinyobservable import Observable, ObservableRenderer

NOTEBOOK = "https://observablehq.com/@d3/zoomable-sunburst"
# NOTEBOOK = "https://observablehq.com/d/31ab0068a4664578"
NOTEBOOK = "https://observablehq.com/@d3/bar-chart-race"
NOTEBOOK = "https://observablehq.com/@d3/bar-chart-transitions/2"

ui.h1("Observable Notebook in Shiny")
ui.div(a(NOTEBOOK, href=NOTEBOOK))
ui.hr()


def create_data():
    return [
        dict(letter=letter, frequency=random.uniform(0, 1))
        for letter in string.ascii_uppercase
    ]


@ObservableRenderer
def render_notebook():
    return Observable(NOTEBOOK, cells=["viewof order", "chart", "data"]).redefine(
        data=create_data(),
        # data=[
        #    dict(letter="A", frequency=0.1),
        #    dict(letter="B", frequency=0.8),
        #    dict(letter="C", frequency=0.6),
        # ],
    )
