#!/usr/bin/env python
"""
A pandoc filter that renders math at build time using KaTeX.

KaTeX is assumed to be installed with npm and the command

```
npx katex
```

is assumed to exist in the PATH.
"""

__version__ = '0.1.2'

import subprocess
import html

import pandocfilters


def katex(key, value, format, meta):
    if key != "Math":
        return None
    fmt, code = value
    if not isinstance(fmt, dict) and 't' not in fmt:
        return None
    display = fmt['t'] == 'DisplayMath'
    call = subprocess.run(
        ['npx', 'katex', '--no-throw-on-error', '--display-mode' if display else ''],
        input=code,
        text=True,
        capture_output=True,
        check=True,
    )
    return pandocfilters.RawInline(
        'html',
        f'<span class="math {"display" if display else "inline"}" '
        f'data-latex-input="{html.escape(code)}">{call.stdout}</span>',
    )


def main():
    pandocfilters.toJSONFilter(katex)


if __name__ == '__main__':
    main()
