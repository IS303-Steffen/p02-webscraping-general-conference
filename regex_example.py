import re
std_works_short_example = {
    'Matthew': 0,
    'John': 0,
    '1 John': 0,
}
example_references_section = (
    "John 10:6-8, 10-12 "  # should count for John but not 1 John
    "John 3:16 " # should count for John but not 1 John
    "One of my favorite names is John " # shouldn't count for anything
    "1 John 2:3 is another scripture " # count for 1 John but not John
    "Matthew 5:3 " # counts for Matthew
    "I really like the name Matthew and like to use it" # shouldn't count
    )
# We also don't want to count John (don't count) if we use it in passing or in
# someone's name like John Smith (don't count) but we always want to count it
# if it is a scripture reference like John 3:16. (yes count). Then
# we want that to count for other references like Matthew 5:1
# '''


for std_work in std_works_short_example:
    # see the explanation at the end of this file for what eac part of this pattern means.
    regex_pattern = fr'(?<!\d\s)\b{std_work}\s\d+'

    # re is included in the python standard libary, so no need to download it.
    # it stands for regular expression. .findall will return a list of all the
    # matches. You can find the number of matches using len()
    matches = re.findall(regex_pattern, example_references_section)
    num_of_matches = len(matches)
    print(f"For {std_work}: there are this many valid references using regex: {num_of_matches}")

    # notice how the counts are off from when we use .count()
    num_counts_using_count = example_references_section.count(std_work)
    print(f"For {std_work}: the .count() function found this many: {num_counts_using_count}")

# ================================
# EXPLANAITON OF THE REGEX PATTERN
# ================================

# This regex pattern is used to match a specific phrase followed by a number,
# with some conditions about what can come before it.
#
# fr'(?<!\d\s)\b{std_work}\s\d+'
#
# Breakdown:
#
# fr'' 
# - This is a formatted raw string:
#   - 'f' allows {std_work} to be dynamically inserted into the pattern.
#   - 'r' ensures backslashes are treated literally (important for regex).
#
# (?<!\d\s)
# - Negative lookbehind assertion:
# - Ensures that the match is NOT immediately preceded by:
#   - a digit (\d)
#   - followed by a space (\s)
# - In other words, it prevents matches like "3 <your pattern>"
#
# \b
# - Word boundary:
# - Ensures the match starts at the beginning of a word
#   (prevents partial matches inside larger words).
#
# {std_work}
# - A variable inserted into the regex (via the f-string).
# - This represents the specific word or phrase you want to match.
#
# \s
# - Matches a single whitespace character (usually a space).
#
# \d+
# - Matches one or more digits.
# - This means the pattern expects a number after the space.
#
# Overall:
# - Matches: "<std_work> <number>"
# - Example: "Matthew 5"
#
# - But will NOT match if it's immediately preceded by something like:
#   "5 Matthew 5"
# - The purpose of that is so that something like "1 John 5:10" only counts for
#   the "1 John" standard work, but not the "John" standard work.
#
# So this pattern finds standalone occurrences of a word/phrase followed by a number,
# while excluding cases where it looks like part of a numbered list or similar format.
