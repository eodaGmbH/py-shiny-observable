# shinyobservable

Embed any [Observable Notebook or Cells](https://observablehq.com/) in [Shiny for Python](https://shiny.posit.co/py/).

## Quickstart

```python
from htmltools import a
from shiny.express import ui
from shinyobservable import Observable, ObservableRenderer

NOTEBOOK = "https://observablehq.com/@d3/zoomable-sunburst"

ui.h1("Observable Notebook in Shiny")
ui.div(a(NOTEBOOK, href=NOTEBOOK))
ui.hr()


@ObservableRenderer
def render_notebook():
    return Observable(NOTEBOOK)
```

Enjoy your Observable Notebook in Shiny!

![](docs/images/complete-notebook.png)