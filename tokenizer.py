import json

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_token = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, token):
        node = self.root
        for ch in token:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_token = True

    def longest_match(self, text, start):
        node = self.root
        longest = -1
        curr = start
        while curr < len(text):
            ch = text[curr]
            if ch not in node.children:
                break
            node = node.children[ch]
            if node.is_token:
                longest = curr
            curr += 1
        return longest

# Global tokenizer state
_trie = None
_token_to_id = {}

def load_tokenizer(json_path):
    global _trie, _token_to_id
    try:
        _trie = Trie()
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Handle different tokenizer file formats
        if isinstance(data, dict):
            if "model" in data and "vocab" in data["model"]:
                # HuggingFace tokenizer format
                _token_to_id = data["model"]["vocab"]
            elif "vocab" in data:
                # Simple vocab format
                _token_to_id = data["vocab"]
            else:
                # Assume the whole dict is the vocab
                _token_to_id = data
        else:
            # Assume it's a simple vocab dict
            _token_to_id = data

        for token in _token_to_id:
            _trie.insert(token)
        print(f"Loaded {len(_token_to_id)} tokens from {json_path}")
    except Exception as e:
        print(f"Error loading tokenizer from {json_path}: {e}")
        # Fallback to empty tokenizer
        _trie = Trie()
        _token_to_id = {}

def simple_word_tokenizer(text, max_tokens=70000):
    """
    Simple word-based tokenizer that splits on whitespace and common punctuation.
    This is a fallback when the main tokenizer produces character-level output.
    """
    import re
    # Split on whitespace and common punctuation, but keep the delimiters
    tokens = re.findall(r'\w+|[^\w\s]', text)
    if len(tokens) > max_tokens:
        return tokens[:max_tokens]
    return tokens

def tokenizer(text):
    if _trie is None or len(_token_to_id) == 0:
        print(F"Tokenizer not loaded. Call load_tokenizer(json_path) first.")
        load_tokenizer('qc.json')
        print("Tokenizer loaded.")

        # If still empty after loading, use simple tokenizer
        if len(_token_to_id) == 0:
            print("Tokenizer vocab is empty, falling back to simple word tokenizer")
            return simple_word_tokenizer(text)

    tokens = []
    i = 0
    while i < len(text):
        j = _trie.longest_match(text, i)
        if j != -1:
            tokens.append(text[i:j+1])
            i = j + 1
        else:
            tokens.append(text[i])
            i += 1
    return tokens  # or return [ _token_to_id[t] for t in tokens ] for encoded IDs







# EXAMPLE USAGE:
# load_tokenizer("ENTER_PATH_TO_TOKENIZER")
# tokenized_content = tokenizer("ENTER_TEXT_TO_TOKENIZE")
# tokens = len(tokenized_content)



def count_total_tokens(text):
    return len(tokenizer(text))


def count_tokens(text):
    """
    Count the estimated number of tokens in text.
    Returns just the count, not the tokens themselves.
    """
    tokenized_content = tokenizer(text)

    # Check if we got character-level tokenization
    single_char_count = sum(1 for token in tokenized_content[:100] if len(token) == 1)
    if single_char_count > 80:  # If more than 80% are single characters
        # Use simple word tokenizer for counting
        tokenized_content = simple_word_tokenizer(text)

    return len(tokenized_content)


def truncate_text_by_tokens(text, max_tokens=70000):
    """
    Truncate raw text based on estimated token count.
    Returns clean raw text, not token arrays.
    """
    print("Estimating tokens and truncating content...")

    # First, check if the full text fits
    total_tokens = count_tokens(text)
    print(f"Estimated tokens: {total_tokens}")

    if total_tokens <= max_tokens:
        print("Content fits within token limit")
        return text

    print(f"Content too long ({total_tokens} tokens), truncating to ~{max_tokens} tokens...")

    # Estimate characters per token (rough approximation)
    chars_per_token = len(text) / total_tokens
    estimated_chars = int(max_tokens * chars_per_token * 0.9)  # 90% safety margin

    # Truncate by characters, but try to end at word boundary
    if estimated_chars >= len(text):
        return text

    truncated = text[:estimated_chars]

    # Try to end at a word boundary (find last space)
    last_space = truncated.rfind(' ')
    if last_space > estimated_chars * 0.8:  # If space is reasonably close
        truncated = truncated[:last_space]

    print(f"Truncated to {len(truncated)} characters")
    return truncated


# Legacy function for backward compatibility
def truncated_tokenizer_content(text, max_tokens=70000):
    """
    DEPRECATED: Use truncate_text_by_tokens() instead.
    This function now returns raw text instead of token arrays.
    """
    print("WARNING: truncated_tokenizer_content is deprecated. Use truncate_text_by_tokens() instead.")
    return truncate_text_by_tokens(text, max_tokens)