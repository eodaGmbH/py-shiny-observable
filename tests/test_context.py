# from shiny.express import ui
import pytest
from shinyobservable._context import ObservableContext


@pytest.mark.skip(reason="Not implemented")
def test_observable_context():
    # Prepare
    output_id = "notebook"

    # Act
    ctx = ObservableContext(output_id)
    ctx.redefine(data=[10, 20])

    # Assert
    assert ctx.data == [10, 20]
    assert ctx.id == output_id
