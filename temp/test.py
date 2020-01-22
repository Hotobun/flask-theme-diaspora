import os

import markdown, markdown

with open("temp/test.md",'r', encoding = 'utf-8') as f:
    data = f.read()


a = markdown.markdown(data, extensions=['markdown.extensions.toc','markdown.extensions.fenced_code'] )


with open("temp/a.html", 'w', encoding = 'utf-8') as f:
    f.write(a)



print("hello world!")

