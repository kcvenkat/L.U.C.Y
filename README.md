#L.U.C.Y

##Overview
L.U.C.Y (Literally Understands Commands and Yaps) is a lightweight, always-listening voice assistant designed for developers, creators, and power users who want a hands-free way to ask questions, run commands, and automate tasks on macOS. Unlike traditional voice assistants that are locked to specific ecosystems, L.U.C.Y is fully customizable, open-source, and modular, giving you complete control over how it listens, responds, and interacts with your system.
Built with Python, L.U.C.Y continuously runs in the background and responds instantly to your voice. Whether you're coding, multitasking, or simply away from the keyboard, you can speak a command or ask a question and get immediate results without ever touching a button. With built-in voice recognition powered by Google Speech API, offline text-to-speech, and a flexible command execution system, L.U.C.Y becomes a natural extension of your workflow.

##Why use L.U.C.Y?
When I’m working, I like to open something like ChatGPT and ask it a question in order to clarify a doubt I have. My goal with L.U.C.Y was to have a lightweight program that could continuously run in the background so I could speak my question aloud and it could give me a response back. This way, all I need to do for a question is ask, and it will be answered. There’s no need to run anything or press a button, and it’s always in the background simply waiting.

##Features
- Modular architecture, making it easy to add new functions
- Voice recognition powered by Google Speech API
- Text-to-speech responses via pyttsx3
- Always running in the background, ready to answer
- Ability to read, write, create, run, and delete files through macOS subprocesses

##Architecture
L.U.C.Y runs on a modular architecture where each of her functions lives in a separate Python module. The core modules to L.U.C.Y are:
- ai.py: This hosts the AI class. The initializer function hardcodes values like the API key and the configuration of the LLM. It also has the process() function that makes the call to the client and returns the response.
- speech.py: This hosts the Speech class. This module has an initializer function that creates instances of the Speech Recognition library for voice recognition and the pyttsx3 library for text-to-speech. The capture() function captures whatever the user is saying, and the speak() function converts the LLM’s response text into speech.

These are the core modules because without them, L.U.C.Y wouldn’t be able to talk. Any other module is a new feature. The current features of L.U.C.Y are:
- commands.py: This hosts the Commands class. The do_command() function from this module allows L.U.C.Y to read, write, create, delete, and run Python files. This is done by prompting the LLM to return a very specifically formatted string whenever the user asks for an operation, parse that string, and perform actions accordingly.

Note that for proper functionality, it is necessary to rewrite the system prompt in the ai.py page. The current prompt that L.U.C.Y has is designed to either return a string formatted for file operations or respond conversationally. This may not be optimal for all customizations and the prompt will need to be engineered accordingly.

##Installation
###Requirements
L.U.C.Y requires the following system and environmental components.
####Operating System
- macOS 11 (Big Sur) or later.
 (L.U.C.Y uses macOS-specific subprocess commands. Linux/Windows support is planned but not yet implemented.)

####Python
- Python 3.9 or later
- All required Python libraries are listed in requirements.txt
  
####External Services
- Google Cloud Speech-to-Text API key
- A configured service account JSON file for authentication
- Active internet connection for speech recognition requests

####Hardware
- A working microphone
- Speakers or headphones for audio output

####System Permissions
- Ensure the following are enabled under System Settings → Privacy & Security:
- Microphone access for Terminal / Python
- Full Disk Access or file permissions (if using file-related commands)
- Automation permissions as required by subprocess calls

####Recommended
- Use a Python virtual environment
- Keep the microphone at a reasonable distance to avoid TTS echo
- Stable network for Gemini API calls and speech recognition

###Setup
1. Clone the repository, ensuring that all the following files are included:
  - main.py
  - ai.py
  - speech.py
  - commands.py
  - requirements.txt

2. Install all required Python dependencies using:
```
pip3 install -r requirements.txt
```

3. Place your Google Cloud Speech API Key somewhere accessible, like an environment variable. You can set the environment variable by running this in your terminal: 
```
export GEMINI_API_KEY="key-here" 
```
4. Verify microphone and file permissions under macOS settings.

###Running L.U.C.Y

Once everything is set up:
1. Navigate to the project directory on your computer:

```
cd path/to/LUCY
```

2. Run the program:

```
python3 main.py
```

L.U.C.Y will start listening immediately. You can now talk to it, ask questions, run commands, and interact hands-free.

##Usage
###Voice Commands
L.U.C.Y is currently designed to return a specifically formatted string whenever the user asks for a file operation. Because of this, telling L.U.C.Y to create, write, make, and such words that correlate to file operations will trigger her to return the string formatted for file operations. So, if you just want to talk to her, it’s best to use verbiage like “tell me more about x.” Currently, L.U.C.Y can write, create, delete, open, and execute files with python3. So, any verbiage telling her to do something of the sort will trigger the file operation.

###Example Interactions
Below are sample conversations showing how L.U.C.Y responds to spoken commands.
These examples illustrate typical use cases, including asking questions and running file commands.

####Asking General Questions:
User: “L.U.C.Y, what is a Lambda function in Python?”
L.U.C.Y: “"A lambda function is a small anonymous function defined with the lambda keyword..."

User: “L.U.C.Y, tell me more about Franz Kafka”
L.U.C.Y: “Franz Kafka (1883–1924) was an influential German-language writer from Prague…”

Running Commands:
When asking L.U.C.Y to run scripts, you will see the stdout of the script in place of L.U.C.Y’s regular dialogue.

User: “L.U.C.Y, run hello_world.py”
L.U.C.Y: “hello world!” (says ‘Executed hello_world.py successfully’)

Note: Google Speech Recognition often struggles with filenames. For example, saying “hello underscore world dot py” may transcribe literally as “hello underscore world dot py” rather than “hello_world.py”. L.U.C.Y uses Gemini to reconstruct the intended filename from these pieces, but it may not always be perfect.
Also, L.U.C.Y cannot change directories yet, so any file you want to run must be in the same directory as main.py. 

####Creating, Deleting, and Editing files:
User: “Create a file named notes.txt”
L.U.C.Y:  “File notes.txt created successfully” (creates an empty file called notes.txt in the same directory as main.py)

User: “Write ‘hello’ into notes.txt”
L.U.C.Y: “File notes.txt written successfully” (“hello” written to notes.txt)

User: “Delete notes.txt”
L.U.C.Y: “Notes.txt deleted successfully” (notes.txt deleted”

The same note mentioned about filenames in the “running commands” section above applies here. Again, L.U.C.Y cannot change directories, so she will only make files in the same directory as main.py. 

###Background Operation
Since L.U.C.Y is a terminal command, you could run her in the terminal and have that process running in the background as you open other applications. Note that this will, however, take up an entire shell session as L.U.C.Y is a continuous loop of user input. You can terminate her by manually pressing ctrl + C or by saying “bye” or “goodbye.” 

##Adding New Functions
Since L.U.C.Y is built on modular architecture, all you have to do to add a new feature is write a Python module with a class and the desired functions under the class, import the class into main.py, and add the logic to implement it into the main loop.

Let’s say that you built a module that allowed L.U.C.Y to say a joke and called that script joke.py. joke.py would look like this:

```
class Joke:
	def __init__(self):
		pass
	
	def say_joke(self):
		return “Why did the chicken cross the road? I don’t know, that joke’s overused.”
```

The class is called Joke and the module is called joke.py. So, in main.py, you would import the Joke class using

```
from joke import Joke
```

Then, you would create an instance of Joke inside a variable to call the class’s commands.

```
jk = Joke()
```

You can now call Joke’s functions like this:

```
some_joke = jk.say_joke()
```

Now all that’s left to do is implement the logic. Let’s say that you want to check whether the substring “joke” is present in the user’s input. So, after user_input is declared and assigned with Speech’s capture() function, the logic would be:

```
if “joke” in user_input:
	some_joke = jk.say_joke()
	print(some_joke)
```

###Configuration
####Speech Recognition
L.U.C.Y uses Python’s SpeechRecognition library, which relies on the PyAudio backend to capture audio from the system’s default microphone. Because of this, L.U.C.Y automatically uses whichever microphone your operating system is currently set to use. If you want to switch microphones, simply change your default input device in your operating system audio settings.
If you want to replace SpeechRecognition with another speech to text library, update the import in speech.py and rewrite the capture() method inside the Speech class. The new capture() method must record audio, perform recognition, and return a text string. As long as capture() returns a string, the rest of the program will continue to function without any changes.
If you switch to a different speech recognition library, you will probably need to update the Speech class initializer to set any library specific variables or configuration.

####Text-to-Speech
L.U.C.Y uses the pyttsx3 library for text to speech. If you decide to use another text to speech provider, for example Azure or ElevenLabs, you must update the speak() function in the speech module.
Pyttsx3 uses the voice models installed on your system. For example, on macOS you can set the voice name to something like Samantha, which is a built-in system voice. If you switch to another text to speech provider, you will likely need to modify both the initializer and the speak() function so that they match the requirements of the new library.
The speak() function does not return anything. It simply speaks the text string that is passed into it. As long as speak() receives a string argument, it will work as intended.

####API Keys and Environment Variables
L.U.C.Y uses environment variables to store all AI provider keys. For Gemini, the key must be stored as GEMINI_API_KEY. The project uses the dotenv library to load a local .env file so the key is available as a normal environment variable during development.
To change the Gemini key, open your .env file and update the GEMINI_API_KEY value. The new key is loaded automatically the next time you start L.U.C.Y.
The ai.py module reads GEMINI_API_KEY inside its initializer and uses it to create the Gemini client. If you switch to another AI provider, update the initializer to load that provider’s key and configuration, and update the initial instructions for the LLM so it understands its role and purpose. The process() function should send the prompt to the provider and return a text string. As long as process() returns plain text, the rest of L.U.C.Y does not need any changes.
Use .env only for local development and keep it out of version control. In production, set GEMINI_API_KEY directly in the environment or through your hosting provider’s secrets system.

##Security Considerations
###Least Privilege and Access Control
Never run L.U.C.Y as root. Use a non-privileged user account.
Restrict filesystem access to L.U.C.Y’s own directory whenever possible.
Require explicit confirmation for any destructive actions like deleting files.

####Sandboxing and Runtime Isolation
If you build any module that gives L.U.C.Y deeper access to the system, for example a malware scanner or anything that reads system files, ALWAYS RUN HER IN AN ISOLATED ENVIRONMENT. Never give full system access to the AI process.
- Run the AI inside a container, VM, or sandboxed environment.
- Use OS tools such as seccomp, AppArmor, or SELinux to limit what the process can do.
- Allow only the directories and system capabilities L.U.C.Y actually needs.

####Safe Handling of Secrets
Store API keys in environment variables or a secret manager.
Keep .env files out of version control and rotate keys regularly.
Never log or print secret values.

####Input, Output, and Command Safety
Treat model outputs as untrusted and validate paths or commands before using them.
Avoid executing raw model-generated commands without whitelisting or templates.
Sanitize user input and block directory traversal or command injection attempts.

####Monitoring and Recovery
Log important actions but redact any sensitive information.
Add resource limits and timeouts to prevent runaway tasks.
Maintain backups and a clear plan for revoking keys or rolling back if something goes wrong.

###Future Improvements
As mentioned before, L.U.C.Y’s current capabilities are restricted to strictly file operations and conversation. However, some future improvements I would like to implement are:

####Directory Navigation
Right now, L.U.C.Y can only make files in her own directory, which is where everything is housed. This, however, can quickly get messy and L.U.C.Y needs a way to change directories given a path by the user. 

####Screen Capture
A major struggle I have is that L.U.C.Y can’t see what’s on my screen. I plan to solve this with a screen capture feature where L.U.C.Y screenshots my screen, processes it, and answers whatever I asked her about the screen. Then, she deletes it. 

###Contributing
Contributions to L.U.C.Y are welcome, but please follow these guidelines to keep the project stable, safe, and easy to maintain.
1. Fork the repository and never commit directly to the main branch.
2. Create a branch for new features if you want to add one (ex. features/screencapture.py or docs/updated-readme.md)
3. Keep changes focused and submit concise pull requests instead of large, unrelated changes.
4. Follow the project structure and avoid modifying systems like ai.py, speech.py, and commands.py. If there’s a change you would like to propose, please open an issue first to discuss it.
5. Maintain safety standards. As discussed in the Security Considerations section, any feature that touches the filesystem or interacts with commands needs to follow best security practices (requesting user permission before destructive actions, using limited permissions, etc.).
6. Document your changes. If you add a new feature or need to change L.U.C.Y’s base code, document those changes.
7. Open an issue for questions. If you are unsure how to implement something or want to propose a large feature, open an issue before starting work.
8. Be respectful and considerate. The goal is to have fun and learn. Keep your feedback helpful and collaborative.

##License
L.U.C.Y is released under the GNU General Public License v3.0 (GPLv3). This license allows you to use, study, modify, and share the software freely, as long as any distributed versions or derivative works remain licensed under GPLv3 as well. This ensures that improvements and modifications to L.U.C.Y stay open and benefit the community.
For complete terms and conditions, please refer to the full GPLv3 license included in the LICENSE file in this repository.

##Contact
If you have questions, want to report a bug, or would like to contribute to L.U.C.Y, the best place to reach out is through the project’s GitHub repository. You can open an issue for support, feature requests, or general discussion. All project communication and updates will be handled through GitHub.
