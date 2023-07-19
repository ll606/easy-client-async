# 🐍Python: Easy Client Async 

1. 🎆Client Development Framework with python async programming. 
2. 🎆Easy to Use and High Extensibility.

## How to use!
1. create a folder in the folder of **views**, named: **start**
![READMEGIF1](readme_gif1.gif)

2. create a python Script, named **view.py** with the following code in the file:
![READMEGIF2](readme_gif2.gif)

```python
from core.view import ViewBase
from pywebio.output import put_markdown

class View(ViewBase):
    
    async def render(self):
        put_markdown(
            '# Hello, World'
        )
```

![README1](README1.png)
![README2](README2.png)