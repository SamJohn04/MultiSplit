# MultiSplit

Python micromodule to split and flatten a string using a list of delimiters. Option to include empty strings and/or delimiter strings.

## Methods

> `multisplit(string: str, delims: list[str], keep_delims: bool = False, keep_empty: bool = False)`
> Split the string by each of the of delimiters.
> - `string`: String to be split.
> - `delims`: List of delimiter strings.
> - `keep_delims`: Insert delimiter strings in the list. Not inserted by default.
> - `keep_empty`: Keep empty strings in the list. Filters them out by default.

> `split(string: str, delim: str, keep_delims: bool = False, keep_empty: bool = False)`
> Split the string by one delimiter.
> - `string`: String to be split.
> - `delim`: Delimiter string.
> - `keep_delims`: Insert delimiter strings in the list. Not inserted by default.
> - `keep_empty`: Keep empty strings in the list. Filters them out by default.


