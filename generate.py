"""This program generates Quine.rickroll"""

import string


def declare_var(name):
    return f"Never gonna let {name} down"


def set_var(name, val):
    return f"Never gonna give {name} {val}"


def define_var(name, val):
    return declare_var(name) + "\n" + set_var(name, val)


def call_fn(fn, args, rtn):
    return f"(Ooh give you {rtn}) Never gonna run {fn} and desert {', '.join(args)}"


SPECIAL_CHARS = {" ": "space", "\n": "newline", "'": "quote", "\\": "backslash"}


def letter_var(letter):
    if letter in SPECIAL_CHARS:
        return SPECIAL_CHARS[letter]
    else:
        return letter


def letter_literal(letter):
    if letter == "\n":
        inner = "\\n"
    elif letter == "'":
        inner = "\\'"
    elif letter == "\\":
        inner = "\\\\"
    else:
        inner = letter
    return f"'{inner}'"


def define_letter(letter):
    return define_var(letter_var(letter), letter_literal(letter))


chars = string.ascii_letters + "".join(SPECIAL_CHARS)

define_chars = "\n".join(map(define_letter, chars))

SRC_VAR = "src"
ARRAY_OF = "ArrayOf"

program = f"""[Chorus]
{define_chars}
{declare_var(SRC_VAR)}
{call_fn(ARRAY_OF,[letter_var('a'),letter_var(chr(10)),letter_var('d'),letter_var('c')],SRC_VAR)}
Never gonna say {SRC_VAR}
"""

print(program)
