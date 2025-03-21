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

    task = " ".join(sys.argv[1:])

    prompt = f"""
You are a command line expert for the {operating_system} operating system. Please write a single-line command for this task:

{task}

Return the single-line command only, without markdown fences and any other text.
"""

    command = prompt_anthropic(prompt)

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


def run_cli(command:str, check=False, verbose=False):
    import subprocess

    process = subprocess.Popen(command,
                               shell=True,
                               stdin=None,  # Use parent's stdin
                               stdout=None,  # Use parent's stdout
                               stderr=None)  # Use parent's stderr

    # Wait for the process to complete
    process.wait()