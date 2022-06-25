import re

text_1 = "crypto-bot that is trading Bitcoin and other currencies"
text_2 = "cryptographic encryption methods that can be cracked easily with quantum computers"

pattern = re.compile("crypto(.{1,30})coin")

print(pattern.match(text_1))
print(pattern.match(text_2))