from textual.app import App, ComposeResult
from textual.widgets import Header, Footer



class SiteLevelApp(App):
    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
    ]

    def __init__(self, *args,debug=True,  **kwargs):
        # se)
        super().__init__(*args, **kwargs)
        setattr(self, "_debug", debug)

    @property
    def debug(self) -> bool:
        return getattr(self, "_debug", None)

    @debug.setter
    def debug(self, value: bool) -> None:
        setattr(self, "_debug", value)

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark



if __name__ == "__main__":
    app = SiteLevelApp(debug=True)
    app.run()
