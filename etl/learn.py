import re
with open('sample_text.txt', 'r') as fp:
    text = fp.read()

pattern = re.compile(r'(?:href=\")(.*)(?:\"sclass)')
urls = pattern.findall(text)
print urls
