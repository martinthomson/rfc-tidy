# rfc-tidy

A simple tool that cleans up RFC XML.

This reads from stdin and writes to stdout.  It will also accept the input file
as the first argument.

## Usage

Install from pypi with:

```sh
pip install --user rfc-tidy
```

Like `black`, `rfc-tidy` cannot be tuned.  Feed XML into `stdin`, get XML
from `stdout` (it also accepts the input file as the first argument).

```sh
rfc-tidy < draft-blah-blah-blah.xml > draft-tidied.xml
```

## Features

Adds `<bcp14>` tags for your "MUST", "SHOULD", and "MAY" statements in text.

Removes extraneous XML, comments, and whitespace.

Indents elements consistently.

Replaces non-ASCII characters in text with XML numeric entities so that you
don't miss them.
