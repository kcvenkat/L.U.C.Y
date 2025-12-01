import os
import subprocess

class Commands:
    def __init__(self):
        pass

    def do_command(self, s):
        parts = s.lower().split("|")
        if len(parts) < 2:
            return "Error: Missing fields in command."
        
        action = parts[0].split(":", 1)[1].strip()
        fname = parts[1].split(":", 1)[1].strip()
        if len(parts) > 2:
            content = parts[2].split(":", 1)[1].strip()
        else:
            content = ""

        if action in ("write", "create"):
            try:
                with open(fname, "w") as f:
                    f.write(content)
                print(f"File {fname} created successfully.")
                return f"File {fname} created successfully."
            except FileNotFoundError:
                print(f"File {fname} doesn't exist")
                return f"File {fname} doesn't exist"
            except Exception as e:
                print(f"Error: {e}. Could not create or write file {fname}.")
                return f"Error: {e}. Could not create or write file {fname}."
        elif action == "open":
            try:
                subprocess.run(["open", fname])
                print(f"File {fname} opened successfully.")
                return f"File {fname} opened successfully."
            except FileNotFoundError:
                print(f"File {fname} doesn't exist")
                return f"File {fname} doesn't exist"
            except Exception as e:
                print(f"Error: {e}. Could not open file {fname}.")
                return f"Error: {e}. Could not open file {fname}."
        elif action == "delete":
            try:
                os.remove(fname)
                print(f"Error: {e}. Could not delete file {fname}.")
                return f"File {fname} deleted successfully."
            except FileNotFoundError:
                print(f"File {fname} doesn't exist")
                return f"File {fname} doesn't exist"
            except Exception as e:
                print(f"Error: {e}. Could not delete file {fname}.")
                return f"Error: {e}. Could not delete file {fname}."
        elif action == "python3":
            try:
                process = subprocess.run(
                    ["python3", fname],
                    capture_output=True,
                    text=True
                )
                if process.returncode != 0:
                    print(f"Error executing {fname}: {process.stderr.strip() or 'Unknown error'}")
                    return f"Error executing {fname}: {process.stderr.strip() or 'Unknown error'}"
                print(f"File {fname} executed successfully.")
                return f"File {fname} executed successfully."
            except FileNotFoundError:
                print(f"File {fname} doesn't exist")
                return f"File {fname} doesn't exist"
            except Exception as e:
                print(f"Error {e}. Could not execute file {fname}.")
                return f"Error {e}. Could not execute file {fname}."
        else:
            print(f"Error: Unknown action '{action}'.")
            return f"Error: Unknown action '{action}'."
