A quine is "a computer program that takes no input and produces a copy of its own source code as its only output."[^1]

The program `Quine.rickroll` is a quine written in [Rickroll](https://github.com/BattleMage0231/rickroll):
```bash
rickroll Quine.rickroll > output
diff Quine.rickroll output  # the output is identical to the program's source code
```

[^1]: https://en.wikipedia.org/wiki/Quine_(computing)
