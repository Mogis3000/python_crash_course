# This code was used to help me understand how to use f-strings, string capitalization and formatting, along with whitespace stripping.
# Mogis / 10 June 2021

quote = '"Greatness is simple. In fact, to be simple is to be great." '
author = "           ralph waldo emerson"

print(quote)
print(author)


print(f'World-renowned author {author.title().lstrip()} once said, {quote.rstrip()} and I believe it has challenged my perspective and changed parts of my life for the better.')
print("\n\n")

print(quote)
print(f"\t{author.title().strip()}")