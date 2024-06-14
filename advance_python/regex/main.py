import re

# print(r"Brijesh go\ndaliya")

data = "vcmdhg,fmdnf,znc.,jnh.c nxjhc.k,mnj 23-12-1996 djfgjksdcbn jhfgb,dsn cmnb xzmjnc xcmjbc xchxzb,cmn xzcmnb hdzc 2/08/1995 f mgh ,kjnxf,kdjf.kdjf.dkfj.ckxjhvlkszj;dklnf,ljksdhf"
pattern = r'\b\d{1,2}[-/]\d{1,2}[-/]\d{4}\b'

# res = re.search(pattern, data)
# res = re.findall(pattern, data)
# # print(res.group())
# print(res)

# data = "Tops technology in delhi"
# pattern = r"\bdelhi\b"
# res = re.sub(pattern, "Surat", data)
# print(res)


# A local part, which can include letters, digits, dots, underscores, and hyphens.
# An "@" symbol.
# A domain part, which includes letters, digits, dots, and hyphens, ending with a top-level domain like ".com", ".org", etc.

# data = """
# Hello, please contact us at support@example.com for assistance.
# You can also reach out to John Doe at john.doe123@sub.domain.co.uk or jane_doe-56@example-email.org.
# For feedback, email feedback@example.net. Thanks!
# """

# # Regular expression pattern to match email addresses
# pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

# # Find all matches in the data
# emails = re.findall(pattern, data)

# # Print the list of email addresses found
# print(emails)


data = """
You can reach us at (123) 456-7890, or at 123-456-7890.
Alternative numbers include 123.456.7890 and +1-123-456-7890.
Please call between 9 AM and 5 PM.
"""

# Regular expression pattern to match various phone number formats
pattern = r'\+?\d{1,3}?[-.()\s]*\d{3}[-.()\s]*\d{3}[-.()\s]*\d{4}'

# Find all matches in the data
phone_numbers = re.findall(pattern, data)

# # Print the list of phone numbers found
# print(phone_numbers)


# Example string containing hashtags
data = """
Join the conversation with #OpenAI, #Python, and #MachineLearning.
Don't forget to tag your posts with #DataScience and #AI2024!
"""

# Regular expression pattern to match hashtags
pattern = r'#\w+'

# Find all matches in the data
hashtags = re.findall(pattern, data)

# Print the list of hashtags found
# print(hashtags)

# Example string containing different date formats
data = """
Important dates include the project start date on 2024-06-01, the release on 01/12/2024, and the event on 15-08-2024.
Also, note the anniversary on 2023/12/31 and the fiscal year end on 2024.12.30.
"""

# Regular expression pattern to match various date formats
pattern = r'\b\d{4}[-/.]\d{2}[-/.]\d{2}\b|\b\d{2}[-/.]\d{2}[-/.]\d{4}\b'

# Find all matches in the data
dates = re.findall(pattern, data)

# # Print the list of dates found
# print(dates)


import re

# Example string containing social security numbers
data = """
Here are some SSNs for testing: 123-45-6789, 987-65-4321.
Invalid numbers like 123-45-678 or 123-456-7890 should not be matched.
"""

# Regular expression pattern to match SSNs
pattern = r'\b\d{3}-\d{2}-\d{4}\b'

# Find all matches in the data
ssns = re.findall(pattern, data)

# Print the list of SSNs found
# print(ssns)


import re

# Example string containing hex color codes
data = """
The color scheme includes primary colors #FF5733, #33FF57, and secondary colors #3357FF, #123ABC.
Short hex codes like #FFF and #000 are also common.
Invalid codes like #GGG, #12345, and #1234567 should not be matched.
"""

# Regular expression pattern to match hex color codes
pattern = r'#[A-Fa-f0-9]{6}\b|#[A-Fa-f0-9]{3}\b'

# Find all matches in the data
hex_colors = re.findall(pattern, data)

# Print the list of hex color codes found
# print(hex_colors)

import re

# Example string containing quoted text
data = """
She said, "Hello, how are you?" and he replied, "I'm fine, thank you!"
In another instance, 'They were talking in whispers', and he added, 'Let's keep it a secret'.
"""

# Regular expression pattern to match quoted strings
pattern = r'["\'](.*?)["\']'

# Find all matches in the data
quoted_strings = re.findall(pattern, data)

# Print the list of quoted strings found
print(quoted_strings)
