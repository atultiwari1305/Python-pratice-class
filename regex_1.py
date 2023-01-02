import re

value = "This is a string"
output = re.search("^This.*string$", value)

print(output)

pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+=-])(?=.{8,})"

#     "." (dot) matches any single character (except a newline)
#     "^" matches the start of a string
#     "$" matches the end of a string
#     "*" matches zero or more occurrences of the preceding character or pattern
#     "+" matches one or more occurrences of the preceding character or pattern
#     "?" matches zero or one occurrence of the preceding character or pattern
#     "{n}" matches exactly n occurrences of the preceding character or pattern
#     "{n,}" matches n or more occurrences of the preceding character or pattern
#     "{n,m}" matches at least n and at most m occurrences of the preceding character or pattern
#     "[...]" matches any single character contained within the brackets
#     "[^...]" matches any single character not contained within the brackets
#     "|" denotes a choice between the preceding and following pattern (e.g. a|b matches either a or b)
#     "\" is used to escape metacharacters and treat them as literal characters