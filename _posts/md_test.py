import mistletoe
from mistletoe.latex_renderer import LaTeXRenderer
from mistletoe import Document, HTMLRenderer

with open("_posts/chip_problem.md", 'r', encoding = 'utf-8') as fin:
    with HTMLRenderer() as renderer:
        rendered = renderer.render(Document(fin))

with open("test.txt", 'w', encoding='utf-8') as f:
    f.write(rendered)

print("done")