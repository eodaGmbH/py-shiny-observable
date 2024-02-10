from shinyobservable import Observable


def test_observable():
    # Prepare
    notebook = "https://observablehq.com/@d3/zoomable-sunburst"

    # Act
    obs = Observable(notebook)

    # Assert
    assert obs.to_dict() == dict(notebook=notebook)
