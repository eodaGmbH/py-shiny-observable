from shinyobservable import Observable


def test_observable():
    # Prepare
    notebook = "https://observablehq.com/@d3/zoomable-sunburst"

    # Act
    obs = Observable(notebook, width=700)

    # Assert
    expected_notebook = "https://api.observablehq.com/@d3/zoomable-sunburst.js?v=3"
    assert obs.to_dict() == dict(notebook=expected_notebook, width="700px")
