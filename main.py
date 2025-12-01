from speech import Speech
from ai import AI
from commands import Commands
import pyfiglet
from rich.console import Console

console = Console()
banner = pyfiglet.figlet_format("L.U.C.Y V1", font="slant")
console.print(banner, style="bold rgb(85,0,130)")

ai = AI()
speech = Speech()
commands = Commands()

try:
    while True:
        print("Listening...")
        user_input = speech.capture()
        if not user_input.strip():
            continue
        print("You said: ", user_input)
        if user_input == "bye" or user_input == "goodbye":
            break
        response = ai.process(user_input)
        
        if "Action:" in response and "|" in response:
            cmd_return = commands.do_command(response)
            speech.speak(cmd_return)
            print()
        else:
            print(response)
            speech.speak(response)
            print()
except Exception as e:
    print(f"Error: {e}")
