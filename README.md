From [Wikipedia](https://en.wikipedia.org/wiki/Quine_(computing)):
> A **quine** is a computer program that takes no input and produces a copy of its own source code as its only output.

After learning the basics of how to write a quine, I decided to challenge myself by writing a quine in the ultimate programming language &mdash; [Rickroll](https://github.com/BattleMage0231/rickroll) by Leyang Zou.

Using the Python script `generate.py`, I successfully generated a gigantic 432-line Rickroll quine: [`Quine.rickroll`](Quine.rickroll).

```bash
# Generate the quine:
python generate.py > Quine.rickroll

# Test the quine:
rickroll Quine.rickroll > output.txt
diff Quine.rickroll output.txt  # the output is identical to the program's source code
```

## Explanation
The quine which I created is composed of two parts:
1. An array that holds the program's source code
2. A piece of code that prints the program by looping through the array

The main challenge is that the array itself is part of the program, so it would be impossible to initialize it with the complete source code of the program (otherwise we would have an infinitely recursive definition). The trick is to exclude the definition of the array from the source code that is initially stored in the array. Later, during the execution of the program, we can fill in the missing pieces by doing some string manipulation. See the Java example given at [Quine#Constructive quines](https://en.wikipedia.org/wiki/Quine_(computing)#Constructive_quines) for an implementation of this concept.

After figuring out how to structure my quine, another challenge was that Rickroll does not have a datatype for strings. As a result, I worked with an array of characters, and I output each character individually using the `PutChar` function. I also needed to write some logic to handle special characters such as `\n`, `'`, and `\`.
