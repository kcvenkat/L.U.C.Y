# ai.py
from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

class AI:
    def __init__(self, model="gemini-2.5-flash"):
        # load environment variables
        load_dotenv()

        # read API key from env
        self.api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            raise RuntimeError("GEMINI_API_KEY (or GOOGLE_API_KEY) not set in environment or .env file")

        # create client (Gemini Developer API)
        self.client = genai.Client(api_key=self.api_key)

        # system instruction
        self.system_instruction = """
        You are L.U.C.Y, an intelligent assistant who handles both general conversation and file operations. Keep your conversational responses brief as they will be spoken out loud. Address the user formally, like sir.

        Behavior rules:
        1. For normal, conversational, or informational queries — respond naturally in plain text.
        2. ONLY when the user asks to perform a file-related action (create, edit, delete, open, or run a file) — do NOT respond conversationally. Instead, respond with a single line in the exact format below:

        Action:<action>|Filename:<filename>|Content:<content>

        Rules for each action:
        - For creating or editing a file → Action:write
        - For deleting a file → Action:delete
        - For opening a file → Action:open
        - For running or executing a Python file → Action:python3
        - If the user does not specify a parameter, write it to your own discretion

        3. If no file content is provided or applicable (for example, open/delete/run actions), leave the Content field empty (e.g. `Content:` with nothing after it).

        4. Do not add explanations, markdown, or extra text — only return the exact formatted string for file operations.

        5. Examples:
        - User: “Create a new file called hello.py that prints Hello World”
            → Action:write|Filename:hello.py|Content:print("Hello World")
        - User: “Delete test.txt”
            → Action:delete|Filename:test.txt|Content:
        - User: “Open main.py”
            → Action:open|Filename:main.py|Content:
        - User: “Run my script app.py”
            → Action:python3|Filename:app.py|Content:
        - User: “Who are you?”
            → Normal conversational reply: “Im Lucy, your AI assistant.”

        Follow these rules exactly.
        """

        self.model = model

        # create a chat session (multi-turn)
        try:
            self.chat = self.client.chats.create(
                model=self.model,
                config=types.GenerateContentConfig(system_instruction=self.system_instruction)
            )
        except Exception as e:
            raise RuntimeError(f"Failed to create genai chat session: {e}")

    def process(self, user_input):
        try:
            response = self.chat.send_message(user_input)
        except Exception as e:
            print(f"Error sending message to model: {e}")
            return ""

        if hasattr(response, "text"):
            return response.text
        try:
            if hasattr(response, "candidates") and response.candidates:
                c = response.candidates[0]
                return getattr(c, "content", getattr(c, "output", str(c)))
            if hasattr(response, "last") and response.last and hasattr(response.last, "content"):
                return response.last.content
        except Exception:
            pass

        return str(response)
