import re
# 在字符串前加r，标记为原始字符，不包括转义字符
phoneNumber = re.compile(r'(\d{3,4}[.-]?)+')
mo = phoneNumber.search('my name is 123-232-1234')
print(mo.group())