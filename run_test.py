#!/usr/bin/env python3
import pathlib
import subprocess
import shutil

if __name__ == '__main__':
    test_results = pathlib.Path('test_results')
    test_results.mkdir(exist_ok=True)
    inps = pathlib.Path('test_cases/').glob('*.md')
    for inp in inps:
        subprocess.run(
            [
                'pandoc',
                '-s',
                str(inp),
                '--filter',
                shutil.which('pandoc-static-katex'),
                '--css',
                'https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.8.3/katex.min.css',
                '-o',
                str(test_results / f'{inp.stem}.html'),
            ],
            check=True,
        )
