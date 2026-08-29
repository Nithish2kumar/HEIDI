from rich.console import Console #Formats the output
from rich.panel import Panel #Creates boxes around terminal
from rich.prompt import Prompt #Ask the user question
from rich.align import Align

from receiver import receive
from sender import sendMsg

con=Console()
def main():
    con.print(
        Align.center(
        Panel.fit(
            "[bold cyan]🔐 HEIDI[/bold cyan]\n"
            "[dim] Network Steganography[/dim]",
            border_style="cyan"
        ))
    )
    while(True):
        choice=Prompt.ask(
        "Choose an operation",
        choices=["Send","Receive"],
        default="Receive"
        )

        if choice=="Receive":
            con.print(
                    Panel.fit(
                        "[dim] Receiving[/dim]",
                        border_style="cyan"
                    )
                )

            try:

                mes=receive()

                con.print(
                    Panel(
                        f"[green]Message received successfully[/green]\n"
                        f"Output: [cyan]{mes}[/cyan]",
                        title="✅ Success",
                        border_style="green"
                    )
                )

            except Exception as e:
                con.print(
                    Panel(
                    f"[red]{e}[/red]",
                    title="❌ Error",
                    border_style="red"
                    )
                )

        elif choice == "Send":
            inMes = Prompt.ask("🔓 Enter the Message: ")

            try:
                sendMsg(inMes)
                con.print(
                    Panel(
                    inMes,
                    title="🔓 Message",
                    border_style="green"
                    )
                )

            except Exception as e:
                con.print(
                    Panel(
                    f"[red]{e}[/red]",
                    title="❌ Error",
                    border_style="red"
                    )
                )

if __name__ =="__main__":
    main()

