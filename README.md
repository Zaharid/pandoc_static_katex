# pandoc-static-katex

A simple [pandoc](https://pandoc.org/) [filter](https://pandoc.org/filters.html)
that uses [KaTeX](https://katex.org/) to render math equations at build time. It
makes possible to display equations without any JavaScript execution in the
browser.


## Example usage

```bash
$ cat math.md
# A title and whatnot.

This is inline $\log(\frac{1}{2})$ and this is display:

$$
\int_{-\infty}^{+\infty}\LambdaLamda(x)dx
$$

$ pandoc -s  math.md --filter pandoc-static-katex --to html5 --css https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.8.3/katex.min.css -o math.html
```

Note that the `--katex` option of `pandoc` option doesn't add the styles since
`pandoc` doesn't see any math element after the filter pass.

## Installation

The script can be installed by pip:

```
python3 -m pip install pandoc_static_katex
```

The filter runs in Python 3.7+.

When the filter is run, KaTeX needs to be installed with
[nodejs](https://nodejs.org/en/); the command

```bash
npx katex
```

must work on the current path. The filter has been developed with version 0.10.2
of KaTeX.

Additionally, `pandoc` is needed for most usages.

### Development mode

It requires [flit](https://flit.readthedocs.io/en/latest/) to be installed from
source in development mode.

```bash
flit install --symlink
```

## Test script

If `pandoc`, `katex` and the filter have all been installed correctly, the
command:

```
python3 run_test.py
```

should produce rendered results in the `test_results` folder.
