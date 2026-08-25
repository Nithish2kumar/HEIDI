from rich.console import Console #Formats the output
from rich.panel import Panel #Creates boxes around terminal
from rich.prompt import Prompt #Ask the user question
from rich.align import Align

from enc import encode
from dec import decode


con=Console()
def main():
    con.print(
        Align.center(
        Panel.fit(
            "[bold cyan]🔐 HEIDI[/bold cyan]\n"
            "[dim] Image Steganography[/dim]",
            border_style="cyan"
        ))
    )
    while(True):
        choice=Prompt.ask(
        "Choose an operation",
        choices=["encode","decode"],
        default="encode"
        )

        if choice=="encode":
            input_image=Prompt.ask("🖼️  Input image")
            output_image=Prompt.ask("💾 Output image")
            message=Prompt.ask("🔒 Secret message")

            try:
                encode(input_image,output_image,message)

                con.print(
                    Panel(
                        f"[green]Message successfully hidden[/green]\n"
                        f"Output: [cyan]{output_image}[/cyan]",
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

        elif choice == "decode":
            input_image = Prompt.ask("🖼️  Stego image")

            try:
                message = decode(input_image)

                con.print(
                    Panel(
                    message,
                    title="🔓 Hidden Message",
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

