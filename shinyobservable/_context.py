from shiny.session import Session, require_active_session


class ObservableContext(object):
    """Create an Observable context instance"""

    data = dict()

    def __init__(self, id: str, session: Session = None) -> None:
        self.id = id
        self._session = require_active_session(session)
        self._message_queue = []

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.render()

    def redefine(self, **kwargs) -> None:
        self.data = kwargs

    async def render(self):
        await self._session.send_custom_message(
            f"observable-{self.id}", {"id": self.id, "data": self.data}
        )
