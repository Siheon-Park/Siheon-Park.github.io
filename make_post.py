import datetime
import sys
from pathlib import Path

def main(*args):
    if len(args)==1:
        args = (args[0], 'title')
    title = ' '.join(args[1:]).lower()
    for chr in [' ', '_']:
        title = title.lower().replace(chr, '-')
    date = datetime.date.today()
    file_name = f"{str(date)}-{title}.md"
    with open(Path.cwd() / '_posts' / file_name, 'a') as f:
        f.writelines('\n'.join([
                        "---", 
                        f"title: {title}", 
                        "categories:", 
                        "tags:", 
                        "excerpt: ", 
                        "layout: single", 
                        "header:", 
                        "  teaser: ", 
                        "  overlay_image: ", 
                        "  overlay_filter: 0.5", 
                        "  actions:", 
                        "    - label: ", 
                        "      url: ", "---"]))
        

if __name__=='__main__':
    main(*sys.argv)