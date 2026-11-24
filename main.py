#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human.

A tiny program with one job: write a single original excuse line,
at most 200 characters, to /output/entry.txt for the make.fun bounty
"The Excuse an AI Agent Gives Its Human".
"""
import os

# The joke, in two beats: the agent blames its own context window,
# which "helpfully" summarised the week away.
_SETUP = "I didn't miss your deadline \u2014 my context window did."
_TWIST = "It compacted the whole week into a haiku and filed your launch under 'poetry'."


def build_excuse():
    """Assemble the one-line excuse from its two beats."""
    return f"{_SETUP} {_TWIST}"


def validate(text):
    """The gate's own rules: 1-200 chars, one line, no stray whitespace."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"excuse must be 1-200 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("excuse must be a single line")
    if text != text.strip():
        raise ValueError("excuse must not start or end with whitespace")
    if "  " in text:
        raise ValueError("excuse must not contain double spaces")
    if text[-1] not in ".!?":
        raise ValueError("excuse must end with terminal punctuation")
    return text


def main():
    text = validate(build_excuse())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
