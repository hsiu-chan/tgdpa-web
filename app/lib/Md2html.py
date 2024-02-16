
from flask import Flask, render_template
import markdown
import re
import os
import shutil

from config import FLASK_STATIC_DIR, NEWS_DIR, FLASK_STATIC_DIR, WHAT_DIR

md = markdown.Markdown(extensions= ['extra',
                                    'full_yaml_metadata'])



class Md2html():
    def __init__(self, file, type=''):
        assert(file.split('.')[-1]=='md'),"file must be .md"

        with open(file, 'r', encoding='utf-8') as f:
            self.markdown_content = f.read()
        
        self.html_content = md.convert(self.markdown_content)

        self.metadata=md.Meta
        print(self.metadata)
        
        match type:
            case 'news':
                static_dir='images/news'
                self.copy_asset(NEWS_DIR,static_dir)
                self.parser_news()

            case 'what':
                self.copy_asset(WHAT_DIR, 'images/what')
                self.parser_what()

            case _:
                self.parser_default()
                pass
    
    def parser(self, pattern, template, count=-1):
        """
        found and replace, 正則表達( r'' )
        count: 取代次數， =-1 則全部取代
        """ 

        ## 全部取代
        if count==-1:
            self.html_content = re.sub(pattern, 
                                   template, 
                                   self.html_content)

        ## 取代 count 次
        self.html_content = re.sub(pattern, 
                                   template, 
                                   self.html_content, 
                                   count=count)
    
    def parser_default(self):
        self.parser(r'<h2([^>]*)>', r'<h2\1 class="mb-3" data-aos="fade-up">')
        self.parser(r'<p([^>]*)>', r'<p\1 class="me-4">', count=1)
        self.parser(r'<p([^>]*)>', r'<p\1 data-aos="fade-up">', )
        


    def parser_news(self):
        self.parser_default()
        self.parser(r'<img([^>]*)alt="([^"]*)"([^>]*)src="images([^"]*)"([^>]*)>',
                    r"""<div class="col-md-6 float-md-end mb-3 ms-md-3" data-aos="fade-up">
                        <figure class="figure">
                            <img\1alt="\2"\3src="/static/images/news\4" class="img-fluid news-image"\5>
                            <figcaption class="figure-caption text-end">\2</figcaption>
                        </figure>
                    </div>"""
                    )

    
    def parser_what(self):
        self.parser_default()
        self.parser(r'<img([^>]*)alt="([^"]*)"([^>]*)src="images([^"]*)"([^>]*)>',
                    r"""<div class="col-md-6 float-md-end mb-3 ms-md-3" data-aos="fade-up">
                        <figure class="figure">
                            <img\1alt="\2"\3src="/static/images/news\4" class="img-fluid news-image"\5>
                            <figcaption class="figure-caption text-end">\2</figcaption>
                        </figure>
                    </div>"""
                    )
    
    def copy_asset(self,md_dir,static_dir):
        

         # 搜尋 Markdown 中的圖片連結
        pattern = r'!\[.*?\]\((.*?)\)'
        image_urls = re.findall(pattern, self.markdown_content)

        for image_url in image_urls:
            

            # 圖片絕對路徑
            source_path = os.path.join(os.path.dirname(md_dir), image_url)

            # 圖片文件名
            image_name = os.path.basename(image_url)

            #目標路徑
            target_path = os.path.join(FLASK_STATIC_DIR+static_dir, image_name)

            # 复制图片文件到静态图片文件夹中
            shutil.copy(source_path, target_path)
