import re

# Find a, followed by 0 or more b's followed by c
assert re.findall("ab*c", "ac") == ['ac']
assert re.findall("ab*c", "abcd") == ['abc']
assert re.findall("ab*c", "acc") == ['ac']
assert re.findall("ab*c", "abcac") == ['abc', 'ac'] 
assert re.findall("ab*c", "abdc") == []
assert re.findall("ab*c", "ABC") == []


# Find the word 'Hello' between paragraph tags 
assert re.findall("<p>Hello<\/p>", "<body><p>Hello</p></body>") == ['<p>Hello</p>']

# Find one or more of any characters between paragraph tags

# Greedy Quantifier, matches the biggest match it can, so the <p> before Hello and the </p> after World. So matches both <p>Hello</p><p>World</p>
assert re.findall("<p>.+<\/p>", "<body><p>Hello</p><p>World</p></body>") == ['<p>Hello</p><p>World</p>']

# Lazy Quantifier, matches only enough to complete the pattern, so matches both <p>Hello</p> and <p>World</p>
assert re.findall("<p>.+?<\/p>", "<body><p>Hello</p><p>World</p></body>") == ['<p>Hello</p>', '<p>World</p>']

# Extract just the text from paragraphs with a group
assert re.findall("<p>(.+?)<\/p>", "<body><p>A long time ago</p><p>in a land far away</p></body>") == ["A long time ago", "in a land far away"]