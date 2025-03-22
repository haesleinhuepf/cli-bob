POSSBILE_MARKDOWN_FENCES = ["```python", "```Python", "```nextflow", "```java", "```javascript", "```macro", "```groovy", "```cmd",
                           "```jython", "```md", "```markdown", "```plaintext", "```tex", "```latex",
                           "```txt", "```csv", "```yml", "```yaml", "```json", "```JSON", "```py", "```svg", "```xml", "<FILE>", "```"]

def remove_outer_markdown(text):
    """
    Remove outer markdown syntax from the given text.

    Parameters
    ----------
    text : str
        The input text with potential markdown syntax.

    Returns
    -------
    str
        The text with outer markdown syntax removed and stripped.
    """
    text = text.strip("\n").strip(" ")

    possible_beginnings = POSSBILE_MARKDOWN_FENCES

    possible_endings = ["```", "</FILE>"]

    if any([text.startswith(beginning) for beginning in possible_beginnings]) and any([text.endswith(ending) for ending in possible_endings]):

        for beginning in possible_beginnings:
            if text.startswith(beginning):
                text = text[len(beginning):]
                break

        for ending in possible_endings:
            if text.endswith(ending):
                text = text[:-len(ending)]
                break

    text = text.strip("\n")

    return text