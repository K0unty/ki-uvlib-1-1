from rich.console import Console
from rich.panel import Panel


console = Console()

# Banner Function


def ba1(txt):
    panel = Panel.fit(
        txt,
        title="Mistress",
        subtitle="ToiletSlave",
        style="Italic",
        border_style="magenta",
    )
    # Print the Panel
    console.print(panel)
