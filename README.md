# cli-bob

cli-bob uses AI to generate command line code in case you can't remember the exact syntax.

![](https://github.com/haesleinhuepf/cli-bob/raw/main/docs/screenshot1.png)

Under the hood, it uses the Large Language Models (LLMs) to generate commands.


## Disclaimer

`cli-bob` is a research project aiming at streamlining command line interaction. Under the hood it uses
artificial intelligence / large language models to generate terminal commands fulfilling the user's requests. 
Users are responsible to verify the generated commands before executing them.

When using `cli-bob` you configure it to use an API key to access the AI models. 
You have to pay for the usage and must be careful in using the generated commands.
Do not use this technology if you are not aware of the costs and consequences.

> [!CAUTION]
> When using the Anthropic, OpenAI, DeepSeek or any other endpoint via cli-bob, you are bound to the terms of service 
> of the respective companies or organizations.
> The text you enter is transferred to their servers and may be processed and stored there. 
> Make sure to not submit any sensitive, confidential or personal data. Also using these services may cost money.


## Installation

```bash
pip install cli-bob
```

## Configuring which LLM to use

`cli-bob` uses the claude LLM for generating commands per default. You can configure other LLM-service providers by setting the environment variable `CLI_BOB_LLM_NAME`. 
Additionally, you need to set the respective API key for the LLM-service provider.

# Table of models and their respective API keys

| Model name                                         | API key                                                                                                         |
|----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| `anthropic:claude-3-5-sonnet-20241022`             | `ANTHROPIC_API_KEY` ([get here](https://anthropic.com/api/))                                                    |
| `openai:gpt-4o-2024-08-06`                         | `OPENAI_API_KEY` ([get here](https://platform.openai.com/api-keys))                                             |
| `github_models:gpt-4o` (openai-compatible models only) | `GH_MODELS_API_KEY` ([get here](https://github.com/marketplace/models))                                         |
| `deepseek:deepseek-chat`                           | `DEEPSEEK_API_KEY` ([get here](https://platform.deepseek.com/api_keys))                                         |
| `kisski:codestral-22b`                             | `KISSKI_API_KEY` ([get here](https://services.kisski.de/services/en/service/?service=2-02-llm-service.json))    |
| `blablador:alias-code`                            | `BLABLADOR_API_KEY` ([get here](https://login.helmholtz.de/oauth2-as/oauth2-authz-web-entry))                    |
| `ollama:deepseek-coder-v2`                         | no API key required, but [model downloaded](https://ollama.com) )                                               |
 |--|--|

For quickly testing the models, you can set an environment variable in your terminal on Windows like this:

![](https://github.com/haesleinhuepf/cli-bob/raw/main/docs/screenshot_set_env.png)

## Usage

On the terminal start typing `bob` and afterwards specify what you want to do. 
`cli-bob` will then generate a command proposal for you and you can hit ENTER to run it.
You can also modify the command before running it.
Hit ESC to cancel execution.

## Debugging

To make sure `cli-bob` uses the right LLM, you can activate the verbose mode by calling `bob -v <your prompt>`. 
It will then print its version, available prompt-handlers and the chosen prompt handler.

![](https://github.com/haesleinhuepf/cli-bob/raw/main/docs/screenshot_verbose_mode.png)

## Acknowledgements

We acknowledge the financial support by the Federal Ministry of Education and Research of Germany and by Sächsische Staatsministerium für Wissenschaft, Kultur und Tourismus in the programme Center of Excellence for AI-research „Center for Scalable Data Analytics and Artificial Intelligence Dresden/Leipzig", project identification number: ScaDS.AI
