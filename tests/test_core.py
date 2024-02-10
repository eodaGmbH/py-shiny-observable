from shinyobservable import Observable
from shinyobservable._core import API_VERSION


def test_observable():
    # Prepare
    notebook = "https://observablehq.com/@d3/zoomable-sunburst"

    # Act
    obs = Observable(notebook, width=700)

    # Assert
    expected_notebook = (
        f"https://api.observablehq.com/@d3/zoomable-sunburst.js?v={API_VERSION}"
    )
    assert obs.to_dict() == dict(
        notebook=expected_notebook, cells=None, data=dict(), width="700px"
    )
