# Embeddings Module

This module provides asynchronous functions to generate text embeddings either locally or via a cloud service. It also maintains legacy compatibility through a class-based interface.

## Functions

### `generate_embeddings_local(batch: bool, texts: Union[str, list[str]]) -> Union[list[float], list[list[float]]]`

Generate embeddings using a local Ollama server.

- **Parameters:**
  - `batch` (bool): Whether to process texts in batch mode.
  - `texts` (Union[str, list[str]]): A single text string or a list of text strings to embed.

- **Returns:**
  - A list of floats representing the embedding for a single text, or a list of such lists for multiple texts.

- **Usage:**
```python
embeddings = await generate_embeddings_local(batch=True, texts=["text1", "text2"])
```

### `generate_embeddings_cloud(batch: bool, texts: Union[str, list[str]]) -> Union[list[float], list[list[float]]]`

Generate embeddings using a cloud service.

- **Parameters:**
  - `batch` (bool): Whether to process texts in batch mode.
  - `texts` (Union[str, list[str]]): A single text string or a list of text strings to embed.

- **Returns:**
  - A list of floats representing the embedding for a single text, or a list of such lists for multiple texts.

- **Usage:**
```python
embeddings = await generate_embeddings_cloud(batch=False, texts="single text")
```

## Legacy Compatibility

The `Embeddings` class preserves the original class structure for backward compatibility.

### `Embeddings.generate.local(batch: bool, texts: Union[str, list[str]])`

Static async method wrapping `generate_embeddings_local`.

### `Embeddings.generate.cloud(batch: bool, texts: Union[str, list[str]])`

Static async method wrapping `generate_embeddings_cloud`.

## Optimization Notes

- The code uses `@logger.catch()` decorator to automatically log exceptions.
- The legacy class structure is preserved but simplified by directly calling the optimized async functions.
- Type hints ensure clarity on input and output types.
- The code is asynchronous to support non-blocking embedding generation.

## Example Usage

```python
from embeddings_module import generate_embeddings_local, Embeddings

# Using the new function directly
embeddings = await generate_embeddings_local(batch=True, texts=["Hello", "World"])

# Using legacy class interface
embeddings_legacy = await Embeddings.generate.local(batch=True, texts=["Hello", "World"])