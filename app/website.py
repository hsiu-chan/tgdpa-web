from flask import Blueprint,render_template,abort,url_for,redirect, url_for
from jinja2 import TemplateNotFound, Template,Environment, FileSystemLoader
import markdown

from lib.BuildQA import buildQA
from lib.Md2html import Md2html
from config import FILESYSTEM, WEBSITE_INFO, PAGE_TITLE, NEWS_DIR, WHAT_DIR

## Jinja 環境設定
file_loader = FileSystemLoader(FILESYSTEM)
env = Environment(loader=file_loader)

website_pages_blueprint = Blueprint('website_pages_blueprint', __name__)

@website_pages_blueprint.route('/pages/')
@website_pages_blueprint.route('/pages/<page>')
def show(page='index'):

    info=WEBSITE_INFO.copy() ## 網站基本資料

    try:
        tp= env.get_template(f'{page}.html') ## 該頁面的模板

        info['pagetitle']=PAGE_TITLE[page]
    except TemplateNotFound:
        abort(404)



    match page:
        case "index":
            all_qa=buildQA() ## QA 資料
            return tp.render(pagename=page,  
                         info=info,    ## 頁面基本資料
                         allqa=all_qa, ## QA資料
                         url_for=url_for ## Flask 的 url_for 傳遞
                        )
        
        case "news-detail":
            
            news=Md2html(NEWS_DIR+'test.md', type='news')

            return tp.render(pagename=page,  
                         info=info,    ## 頁面基本資料
                         news_content=news.html_content, ##　News 
                         news_info=news.metadata,
                         url_for=url_for, ## Flask 的 url_for 傳遞
                         )
        
        case "what":
            content=Md2html(WHAT_DIR+'test.md', type='what')

            return tp.render(pagename=page,  
                         info=info,    ## 頁面基本資料
                         content=content.html_content, ##　News 
                         url_for=url_for, ## Flask 的 url_for 傳遞
                         )

        case _:
            return tp.render(pagename=page,  
                         info=info,    ## 頁面基本資料
                         url_for=url_for ## Flask 的 url_for 傳遞
                        )







home_blueprint = Blueprint('home_blueprint', __name__)
@home_blueprint.route('/')
def index():
    #return redirect(url_for('/pages/'))
    html = '''
    <!DOCTYPE html>
    <html><head>
    <title>index</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
    <link rel="stylesheet" href="static/css/katex.min.css">
    <link href="static/css/style.css" rel="stylesheet" type="text/css">
    <script src="https://kit.fontawesome.com/849ddf9236.js" crossorigin="anonymous"></script>
    <script src="static/js/jquery-3.4.1.min.js"></script>
    </head>

    <body for="html-export">
    <div class="mume markdown-preview" id="main">
    %s
    </div>
    <script src="static/js/label/main.js"></script>
    </body></html>
  
    '''
    
    readme_file = open("README.md", "r",encoding="utf-8")
    md_template_string = markdown.markdown(
        readme_file.read(), extensions=[
    'markdown.extensions.extra', 'markdown.extensions.codehilite','markdown.extensions.tables','markdown.extensions.toc']
    )
    return html% md_template_string
