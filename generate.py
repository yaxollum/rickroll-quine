"""This program generates Quine.rickroll"""

import itertools
import string
import sys


def join_lists(lists):
    return list(itertools.chain.from_iterable(lists))


# track variable declarations
_vars = set()


def declare_var(name):
    if name in _vars:
        raise NameError(f"variable '{name}' declared multiple times")
    _vars.add(name)
    return [f"Never gonna let {name} down"]


def set_var(name, val):
    return [f"Never gonna give {name} {val}"]


def define_var(name, val):
    return declare_var(name) + set_var(name, val)


def increment_var(name):
    return set_var(name, f"{name} + 1")


def call_fn(fn, args, rtn):
    args_str = ", ".join(args) if len(args) > 0 else "you"
    return [f"(Ooh give you {rtn}) Never gonna run {fn} and desert {args_str}"]


def call_fn_no_rtn(fn, args):
    assert len(args) > 0
    return [f"Never gonna run {fn} and desert {', '.join(args)}"]


def put_char(name):
    return call_fn_no_rtn(PUT_CHAR, [name])


def put_string(s):
    return join_lists(put_char(letter_var(c)) for c in s)


def array_index(array, index):
    return f"{array} : {index}"


def while_loop(cond, body):
    return (
        [f"Inside we both know {cond}"]
        + body
        + ["We know the game and we're gonna play it"]
    )


def less_than(val1, val2):
    return f"{val1} < {val2}"


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
    ",": "comma",
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
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

define_chars = join_lists(map(define_letter, chars))

SRC_VAR = "src"
ARRAY_OF = "ArrayOf"
ARRAY_LENGTH = "ArrayLength"
PUT_CHAR = "PutChar"
SRC_LEN_VAR = "srclen"
COUNTER_VAR = "counter"
TMP_VAR = "tmp"


def lines_to_str(lines):
    return "\n".join(lines) + "\n"


prog_part1 = (
    ["[Chorus]"]
    + define_chars
    + declare_var(SRC_VAR)
    + declare_var(TMP_VAR)
    + declare_var(COUNTER_VAR)
    + declare_var(SRC_LEN_VAR)
)


loop_body1 = (
    set_var(TMP_VAR, array_index(SRC_VAR, COUNTER_VAR))
    + put_char(TMP_VAR)
    + increment_var(COUNTER_VAR)
)

loop_body2 = (
    set_var(TMP_VAR, array_index(SRC_VAR, COUNTER_VAR))
    + put_char(TMP_VAR)
    + increment_var(COUNTER_VAR)
)

magic_num = len(lines_to_str(prog_part1))
prog_part2 = (
    # print prog_part1:
    set_var(COUNTER_VAR, 0)
    + while_loop(less_than(COUNTER_VAR, magic_num), loop_body1)
    # print build_src:
    + put_string(f"(Ooh give you {SRC_VAR}) Never gonna run {ARRAY_OF} and desert ")
    + set_var(COUNTER_VAR, 0)
    + call_fn(ARRAY_LENGTH, [SRC_VAR], SRC_LEN_VAR)
    + while_loop(less_than(COUNTER_VAR, SRC_LEN_VAR), loop_body2)
)

build_src = call_fn(
    ARRAY_OF,
    list(map(letter_var, lines_to_str(prog_part1 + prog_part2))),
    SRC_VAR,
)


print(lines_to_str(prog_part1 + build_src + prog_part2), end="")
