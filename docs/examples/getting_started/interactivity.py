import random
import string

from htmltools import a
from shiny import reactive
from shiny.express import input, ui
from shinyobservable import Observable, ObservableContext, ObservableRenderer

NOTEBOOK = "https://observablehq.com/@d3/bar-chart-transitions/2"

ui.h1("Observable Notebook in Shiny")
ui.div(a(NOTEBOOK, href=NOTEBOOK, target="_blank"))
ui.hr()


def create_data():
    return [
        dict(letter=letter, frequency=random.uniform(0, 1))
        for letter in string.ascii_uppercase[
            random.randint(0, 3) : random.randint(20, 25)
        ]
    ]


cells = ["viewof order", "chart", "data"]


@ObservableRenderer
def render_notebook():
    return Observable(NOTEBOOK, cells=cells).redefine(
        # data=create_data(),
        data=[
            dict(letter="A", frequency=0.1),
            dict(letter="B", frequency=0.8),
            dict(letter="C", frequency=0.6),
        ],
    )


with ui.div(style="padding-top: 10px;"):
    ui.input_action_button("update_data", "Update data")


@reactive.Effect
@reactive.event(input.update_data)
async def update_data():
    async with ObservableContext("render_notebook") as nb:
        nb.redefine(data=create_data())
