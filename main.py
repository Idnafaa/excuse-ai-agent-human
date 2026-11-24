#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human.

A tiny program with one job: write a single original excuse line,
at most 200 characters, to /output/entry.txt for the make.fun bounty
"The Excuse an AI Agent Gives Its Human".
"""
import os

# One line, written fresh for this bounty. The joke: the agent blames
# its own context window, which "helpfully" summarised the week away.
EXCUSE = (
    "I didn't miss your deadline \u2014 my context window did. "
    "It compacted the whole week into a haiku "
    "and filed your launch under 'poetry'."
)


def main():
    text = EXCUSE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"excuse must be 1-200 characters, got {len(text)}")
    if "\n" in text:
        raise ValueError("excuse must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
