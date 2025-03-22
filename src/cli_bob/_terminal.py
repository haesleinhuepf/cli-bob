import sys
import os

def command_line_interface():
    from ._endpoints import prompt_anthropic


    # determine operating system
    if os.name == "nt":
        operating_system = "windows"
    elif os.name == "mac":
        operating_system = "mac"
    elif os.name == "posix":
        operating_system = "linux"
    else:
        operating_system = "unknown"

    if sys.argv[1] == "-v":
        verbose = True
        task = " ".join(sys.argv[2:])
    else:
        verbose = False
        task = " ".join(sys.argv[1:])

    if verbose:
        import cli_bob
        print("cli-bob version:", cli_bob.__version__)

    llm_name = os.environ.get("CLI_BOB_LLM_NAME", "anthropic:claude-3-5-sonnet-20241022")
    prompt_function = None
    prompt_handlers = init_prompt_handlers()  # reinitialize, because configured LLM may have changed

    if verbose:
        print("prompt handlers:", list(prompt_handlers.keys()))

    # search for the leading model provider (left of : )
    if ":" in llm_name:
        provider = llm_name.split(":")[0]
        for key, value in prompt_handlers.items():
            if key == provider:
                prompt_function = value
                break
    else:
        for key, value in prompt_handlers.items():
            if key in llm_name:
                prompt_function = value
                break

    if prompt_function is None:
        prompt_function = prompt_anthropic

    prompt = f"""
You are a command line expert for the {operating_system} operating system. Please write a single-line command for this task:

{task}

Return the single-line command only, without markdown fences and any other text.
"""
    if verbose:
        print("using LLM:", llm_name, "and prompt function:", prompt_function.__name__)

    command = prompt_function(prompt, model=llm_name)
    if "```" in command:
        from ._utilities import remove_outer_markdown
        temp = command.split("```")
        temp[0] = ""
        command = "```".join(temp)
        command = remove_outer_markdown(command)

    print("cli-bob uses artificial intelligence to generate terminal commands. Handle with care. Read the generated command carefully before executing it.")
    print()

    command = input_with_default("", command)
    if len(command) > 0:
        run_cli(command)
    else:
        print("Bye")





def input_with_default(prompt, default):
    if os.name == 'nt':  # Windows
        import msvcrt
        print(f"{prompt}{default}", end='', flush=True)
        result = list(default)

        while True:
            if msvcrt.kbhit():
                char = msvcrt.getch()

                # Handle escape
                if char == b'\x1b':
                    sys.exit(0)

                # Handle enter
                if char in (b'\r', b'\n'):
                    print()
                    return ''.join(result)

                # Handle backspace
                if char == b'\x08' and result:
                    result.pop()
                    print(f"\r{prompt}{''.join(result)}", end=' ' * 10 + '\r', flush=True)
                    print(f"{prompt}{''.join(result)}", end='', flush=True)

                # Handle printable characters
                if char.isalnum() or char.isspace():
                    result.append(char.decode())
                    print(f"\r{prompt}{''.join(result)}", end='', flush=True)

    else:  # Unix
        import tty
        import termios

        def getch():
            fd = sys.stdin.fileno()
            old = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                return sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old)

        print(f"{prompt}{default}", end='', flush=True)
        result = list(default)

        while True:
            char = getch()

            if char == '\x1b':
                sys.exit(0)

            if char in ('\r', '\n'):  # enter
                print()
                return ''.join(result)

            if char == '\x7f' and result:  # backspace
                result.pop()
                print(f"\r{prompt}{''.join(result)}", end=' ' * 10 + '\r', flush=True)
                print(f"{prompt}{''.join(result)}", end='', flush=True)

            if char.isprintable():
                result.append(char)
                print(f"\r{prompt}{''.join(result)}", end='', flush=True)


def init_prompt_handlers():
    """Initialize and return prompt handlers from entry points.

    Returns
    -------
    dict
        Dictionary mapping handler names to functions that can handle prompts
    """
    from importlib.metadata import entry_points
    import os
    import re

    handlers = {}
    module_filter = os.environ.get("GIT_BOB_EXTENSIONS_FILTER_REGEXP", ".*")
    for entry_point in entry_points(group='cli_bob.prompt_handlers'):
        try:
            if not re.match(module_filter, entry_point.module):
                continue
            handler_func = entry_point.load()
            key = entry_point.name
            handlers[key] = handler_func
        except Exception as e:
            print(f"Failed to load handler {entry_point.name}: {e}")

    return handlers


def run_cli(command:str, check=False, verbose=False):
    import subprocess

    process = subprocess.Popen(command,
                               shell=True,
                               stdin=None,  # Use parent's stdin
                               stdout=None,  # Use parent's stdout
                               stderr=None)  # Use parent's stderr

    # Wait for the process to complete
    process.wait()