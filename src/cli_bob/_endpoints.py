"""
This module provides helper functions to interact with different language models.
"""

def prompt_anthropic(message: str, model="claude-3-5-sonnet-20241022"):
    """
    A prompt helper function that sends a message to anthropic
    and returns only the text response.

    Example models: claude-3-5-sonnet-20240620 or claude-3-opus-20240229
    """
    from anthropic import Anthropic

    # convert message in the right format if necessary
    message = [{"role": "user", "content": message}]

    # setup connection to the LLM
    client = Anthropic()

    model = model.replace("anthropic:", "")

    message = client.messages.create(
        max_tokens=4096,
        messages=message,
        model=model
    )

    # extract answer
    return message.content[0].text



def prompt_openai(message: str, model="gpt-4o-2024-08-06", max_response_tokens=1024, base_url=None, api_key=None):
    """A prompt helper function that sends a message to openAI
    and returns only the text response.
    """
    # convert message in the right format if necessary
    import openai

    message = [{"role": "user", "content": message}]

    model = model.replace("openai:", "")

    # setup connection to the LLM
    if base_url is not None and api_key is not None:
        client = openai.OpenAI(base_url=base_url, api_key=api_key)
    else:
        client = openai.OpenAI()
    # submit prompt
    response = client.chat.completions.create(
        model=model,
        messages=message,
        max_tokens=max_response_tokens,
    )

    return response.choices[0].message.content


def prompt_kisski(message: str, model=None, max_response_tokens=1024, base_url=None, api_key=None):
    import os
    if base_url is None:
        base_url = "https://chat-ai.academiccloud.de/v1"
    if api_key is None:
        api_key = os.environ.get("KISSKI_API_KEY")
    model = model.replace("kisski:", "")
    return prompt_openai(message, model=model, max_response_tokens=max_response_tokens, base_url=base_url, api_key=api_key)


def prompt_blablador(message: str, model=None, max_response_tokens=1024, base_url=None, api_key=None):
    import os
    if base_url is None:
        base_url = "https://helmholtz-blablador.fz-juelich.de:8000/v1"
    if api_key is None:
        api_key = os.environ.get("BLABLADOR_API_KEY")
    model = model.replace("blablador:", "")
    return prompt_openai(message, model=model, max_response_tokens=max_response_tokens, base_url=base_url, api_key=api_key)


def prompt_deepseek(message: str, model="deepseek-chat", max_response_tokens=1024, base_url=None, api_key=None):
    import os
    if base_url is None:
        base_url = "https://api.deepseek.com"
    if api_key is None:
        api_key = os.environ.get("DEEPSEEK_API_KEY")
    model = model.replace("deepseek:", "")
    return prompt_openai(message, model=model, max_response_tokens=max_response_tokens, base_url=base_url, api_key=api_key)


def prompt_gh_models(message: str, model="gpt-4o", max_response_tokens=1024, base_url=None, api_key=None):
    import os
    if base_url is None:
        base_url = "https://models.inference.ai.azure.com"
    if api_key is None:
        api_key = os.environ["GH_MODELS_API_KEY"]
    model = model.replace("github_models:", "")
    model = model.replace("gh_models:", "")
    return prompt_openai(message, model=model, max_response_tokens=max_response_tokens, base_url=base_url, api_key=api_key)


def prompt_ollama(message: str, model="phi4", max_response_tokens=8192, base_url=None, api_key=None):
    if base_url is None:
        base_url = "http://localhost:11434/v1"
    if api_key is None:
        api_key = "none"
    model = model.replace("ollama:", "")
    return prompt_openai(message, model=model, max_response_tokens=max_response_tokens, base_url=base_url, api_key=api_key)
