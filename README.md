# cli-bob

cli-bob uses AI to generate command line code in case you can't remember the exact syntax.

![](docs/screenshot1.png)

Under the hood, it uses the [claude](https://anthropic.com/api/) API to generate commands.

## Installation

```bash
pip install cli-bob
```

You also need to set an environment variable named `ANTHROPIC_API_KEY` as `cli-bob` uses the claude LLM for generating commands.

## Usage

On the termal start typing `bob` and afterwards specify what you want to do. 
`cli-bob` will then generate a command proposal for you and you can hit ENTER to run it.
You can also modify the command before running it.
Hit ESC to cancel execution.

## Acknowledgements

We acknowledge the financial support by the Federal Ministry of Education and Research of Germany and by Sächsische Staatsministerium für Wissenschaft, Kultur und Tourismus in the programme Center of Excellence for AI-research „Center for Scalable Data Analytics and Artificial Intelligence Dresden/Leipzig", project identification number: ScaDS.AI
