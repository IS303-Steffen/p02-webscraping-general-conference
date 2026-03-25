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
    # r before a string makes it a string literal, that means the backslashes \
    # aren't used as escape characters, instead they are interpreted as regular
    # expression patterns. Then we also add f so we can stick the std_work in.
    regex_pattern = fr'(?<!\d\s)\b{std_work}\s\d+'

    # re is included in the python standard libary, so no need to download it.
    # it stands for regular expression. .findall will return a list of all the
    # matches. You can find the number of matches using len()
    matches = re.findall(regex_pattern, example_references_section)
    num_of_matches = len(matches)
    print(f"For {std_work}: there are this many valid references using regex: {num_of_matches}")
    num_counts_using_count = example_references_section.count(std_work)
    print(f"For {std_work}: the .count() function found this many: {num_counts_using_count}")


