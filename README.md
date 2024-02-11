# shinyobservable

Embed [Observable Notebooks](https://observablehq.com/) in [Shiny for Python](https://shiny.posit.co/py/).

Create any kind of visualizations with JavaScript and let Shiny handle the interactivity. 

## Features

* Embed entire notebooks
* Embed selected cells only
* Update data cells to update visualizations

## Quickstart

```python
from htmltools import a
from shiny.express import ui
from shinyobservable import Observable, ObservableRenderer

NOTEBOOK = "https://observablehq.com/@d3/zoomable-sunburst"

ui.h1("Observable Notebook in Shiny")
ui.div(a(NOTEBOOK, href=NOTEBOOK, target="_blank"))
ui.hr()

# Render entire notebook
@ObservableRenderer
def render_notebook():
    return Observable(NOTEBOOK)


# Render single cells only
@ObservableRenderer
def render_cells():
    return Observable(NOTEBOOK, cells=["chart"])
```

Enjoy your Observable Notebook in Shiny!

See [docs/examples/getting_started/playground.py](docs/examples/getting_started/playground.py) for a detailed example.

![](docs/images/complete-notebook.png)
