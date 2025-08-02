import os
from PIL import Image 

if not os.path.exists('_'):
    os.mkdir('_')

img = Image.new('RGBA', (1, 1), (0, 0, 0, 0))

readme = '''
## This repository temporarily bans your IP address from GitHub, if you're reading this on your browser.

The README.md file references [1000 images](./_/), that are loaded automatically in the background,
which leads to your browser making too many requests in a short period of time.

The ban time is usually around 5 minutes.
'''

for i in range(1000):
    img.save(f'_/{i}.png')
    readme += f'<img src="./_/{i}.png" width=0 height=0 />'

open('README.md', 'w+').write(readme)
