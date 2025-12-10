import re

with open('task2.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

matches = re.findall(r'font-(family|size|style|weight|display)\s*:\s*([^;\'"]+)', html_content, re.IGNORECASE)
matches += re.findall(r'(face|size)\s*=\s*[\'"]([^\'"]+)[\'"]', html_content, re.IGNORECASE)

for param, value in set(matches):
    print(f"{param} = {value.strip()}")