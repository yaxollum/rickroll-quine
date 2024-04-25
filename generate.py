"""This program generates Quine.rickroll"""

import itertools
import string
import sys


def declare_var(name):
    return [f"Never gonna let {name} down"]


def set_var(name, val):
    return [f"Never gonna give {name} {val}"]


def define_var(name, val):
    return declare_var(name) + set_var(name, val)


def call_fn(fn, args, rtn):
    args_str = ", ".join(args) if len(args) > 0 else "you"
    return [f"(Ooh give you {rtn}) Never gonna run {fn} and desert {args_str}"]


def call_fn_no_rtn(fn, args):
    assert len(args) > 0
    return [f"Never gonna run {fn} and desert {', '.join(args)}"]


def array_index(array, index):
    return f"{array} : {index}"


def while_loop(cond, body):
    return (
        [f"Inside we both know {cond}"]
        + body
        + ["We know the game and we're gonna play it"]
    )


SPECIAL_CHARS = {
    " ": "space",
    "\n": "newline",
    "'": "quote",
    "\\": "backslash",
    "[": "lbracket",
    "]": "rbracket",
    "(": "lparen",
    ")": "rparen",
    "<": "lt",
    ":": "colon",
    "+": "plus",
    "_": "underscore",
    "0": "zero",
    "1": "one",
}


def letter_var(letter):
    if letter in SPECIAL_CHARS:
        return SPECIAL_CHARS[letter]
    else:
        assert letter in string.ascii_letters
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

define_chars = list(itertools.chain.from_iterable(map(define_letter, chars)))

SRC_VAR = "src"
ARRAY_OF = "ArrayOf"
ARRAY_PUSH = "ArrayPush"
ARRAY_LENGTH = "ArrayLength"
PUT_CHAR = "PutChar"
SRC_LEN_VAR = "src_len"
COUNTER_VAR = "counter"
TMP_VAR = "tmp"


def lines_to_str(lines):
    return "\n".join(lines)


program = ["[Chorus]"] + define_chars + declare_var(SRC_VAR)

loop_body = (
    define_var(TMP_VAR, array_index(SRC_VAR, COUNTER_VAR))
    + call_fn_no_rtn(PUT_CHAR, [TMP_VAR])
    + set_var(COUNTER_VAR, f"{COUNTER_VAR} + 1")
)

print_src = (
    declare_var(SRC_LEN_VAR)
    + call_fn(ARRAY_LENGTH, [SRC_VAR], SRC_LEN_VAR)
    + define_var(COUNTER_VAR, 0)
    + while_loop(f"{COUNTER_VAR} < {SRC_LEN_VAR}", loop_body)
)

build_src = call_fn(
    ARRAY_OF, list(map(letter_var, lines_to_str(program + print_src) + "\n")), SRC_VAR
)


print(lines_to_str(program + build_src + print_src))
