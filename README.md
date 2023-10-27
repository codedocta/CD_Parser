
# RegexParser

A utility class for commonly used regex operations in Python.

## Features

- **Replace**: Easily replace occurrences of a regex pattern with a new string.
- **Find All**: Retrieve all occurrences of a regex pattern in a string.
- **Find First**: Get the first occurrence of a regex pattern in a string.
- **Find Before**: Extract the portion of text immediately before a given substring.
- **Find After**: Fetch the portion of text immediately after a given substring.
- **Find Between**: Find text between two specified substrings.
- **Is Match**: Check if the input text matches a given regex pattern from the start.
- **Split**: Divide the input text using a provided regex pattern.

## Usage

Here are some example usages of the `RegexParser` class:

```python
# Replace text
modified_text = RegexParser.replace("old", "new", "This is an old text.")
print(modified_text)  # Output: "This is a new text."

# Find all matches
matches = RegexParser.find_all("[A-Za-z]+", "123 apple 456 banana")
print(matches)  # Output: ['apple', 'banana']

# ... [You can add more examples for other methods]
```

## Installation

No installation is required. Simply include the `RegexParser` class in your project and import it to use.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)



License

MIT License

More documentation at:
[Code Docta](https://codedocta.com "Code Docta")
