"""A tiny string-utilities library used to demonstrate a second test target."""


def reverse(s):
    return s[::-1]


def is_palindrome(s):
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]


def shout(s):
    return s.upper() + "!"
