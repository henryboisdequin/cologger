# cologger

[![PyPI version shields.io](https://img.shields.io/pypi/v/cologger.svg)](https://pypi.python.org/pypi/cologger/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Make your endless print statements with color, different formats, and more!

## Installation

Windows:

```
pip install cologger
```

Mac or Linux:

```
pip3 install cologger
```

## Usage

Cologger allows for colors, background colors, and formats. Let's have a look at a basic example:

```python
from cologger import Cologger

cologger = Cologger()
cologger.set_color("red")
cologger.colog("Hello Cologger!")
```

This code will print out a red "Hello Cologger!" message. To set the background we use the `set_bg` method.

```python
from cologger import Cologger

cologger = Cologger()
cologger.set_color("red")
cologger.set_bg("white")
cologger.colog("Hello Cologger!")
```

To set the format of a string, use the `set_fmt` method.

```python
from cologger import Cologger

cologger = Cologger()
cologger.set_color("red")
cologger.set_bg("white")
cologger.set_fmt("bold")
cologger.colog("Hello Cologger!")
```

What separates Cologger from other Python color logging libraries is custom colors and backgrounds. Cologger allows for you to add a custom RGB color into the `set_color` and `set_bg` methods. Let's have a look at an example.

Custom Color:

```python
from cologger import Cologger

cologger = Cologger()
cologger.set_color("custom", [255, 0, 0])  # red rgb code
cologger.colog("Hello Cologger!")
```

Custom Background:

```python
from cologger import Cologger

cologger = Cologger()
cologger.set_bg("custom", [255, 255, 255])  # white rgb code
cologger.colog("Hello Cologger!")
```

Here are all the supported colors for the `set_color` method:

- "black"
- "red"
- "green"
- "yellow"
- "blue"
- "violet"
- "cyan"
- "white"

Here are all the supported colors for the `set_bg` method:

- "black"
- "red"
- "green"
- "yellow"
- "blue"
- "violet"
- "cyan"
- "white"

Here are all the supported formats for the `set_fmt` method:

- "bold"
- "italic"
- "underline"
- "selected"
- "strikethrough"
