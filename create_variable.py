"""
演示Python如何动态创建变量
"""

pages = {}

for page in range(1, 50):
    """
    这里想创建变量page1 = 1, page2 = 2, page3 = 3,...
    """
    pages[page] = page

print(pages[1])
print(pages[2])
