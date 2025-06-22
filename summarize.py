   
import ollama

def summarize(
    text: str,
    model: str = 'mistral',
    min_sentences: int = 3,
    max_sentences: int = 5
) -> str:
    """
    Summarize `text` using a local Ollama model.

    Args:
        text: The input string to summarize.
        model: Ollama model name (e.g., 'mistral', 'llama3').
        min_sentences: Minimum number of sentences in the summary.
        max_sentences: Maximum number of sentences in the summary.

    Returns:
        The summary string.
    """
    prompt = (
        f"Summarize the following text in {min_sentences}–{max_sentences} sentences:\n\n"
        f"{text}"
    )
    response = ollama.chat(
        model=model,
        messages=[{'role': 'user', 'content': prompt}]
    )
    return response['message']['content']

