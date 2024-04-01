import os 
from django.http import FileResponse
from django.shortcuts import render 
from op import language 
from django.conf import settings 

# Create your views here.

BACK_URL = settings.ESSENTIALS + "bbcodetemp/" 

trantext ={
    "en": {
        "bbcodetemp": "BBCode tamplates",
        "description": "You can choose a template to fill in, click Add Paragraph to add a paragraph and fill it in. After completing the filling, click Convert and copy the generated content to copy it in the early forum. All forums that support\nBBCode can be used (including Discuz forums such as MCBBS and Creeper forums, etc.)",
        "temp1": "Template 1",
        "temp1d1": "Good choice for articles", 
        "temp1d2": "Bold borders", 
        "temp1d3": "No borders between subparagraphs", 
        "temp1d4": "Template from KLPBBS@Cinder", 
        "temp2": "Template 2",
        "temp2d1": "Suitable for pictures", 
        "temp2d2": "Easy to use", 
        "temp2d3": "No subparagraphs", 
        "temp2d4": "Template from FDS@XiaoYan", 
        "temp3": "Template 3",
        "temp3d1": "Suitable for informative texts", 
        "temp3d2": "Have Subtitles/Subparagraphs", 
        "temp3d3": "Multi textfields", 
        "temp3d4": "Template from FDS@Redstone", 
        "use": "Use", 
        "return": "Return", 
        "title": "Title", 
        "subtitle": "Subtitle", 
        "innertitle": "Inner Title", 
        "innersubtitle": "Inner Subtitle", 
        "headpicture": "Header", 
        "honmo": "Main body", 
        "emoji": "Emoji", 
        "notes": "Inscription", 
        "viewtemplate": "View Template", 
        "decoratecolour": "Decorate Colour", 
        "maincolour": "Colour", 
        "innersize": "Inner Size", 
        "size": "Size", 
        "insertimage": "Insert Image", 
        "insertpara": "Insert Paragraph", 
        "insertsubpara": "Insert Subparagraph", 
        "deletepara": "Delete", 
        "compile": "Convert", 
        "compileandcopy": "Convert and copy", 
        "spxx":{ 
            "title": "苦力怕论坛 SPXX", 
            "klpspxxd1": "只适合翻译 Minecraft 资讯使用", 
            "klpspxxd2": "符合苦力怕论坛版规", 
            "klpspxxd3": "使用油猴脚本编写", 
            "klpspxxd4": "制作：@我是redstone @Cinder", 
            "desc": "这是一个特别为苦力怕论坛制作的 SPXX 版本。SPXX 原本是可以自动在 Minecraft 官网中复制粘贴新闻的符合 MCBBS 排版的 BBCode，方便译者在论坛更加便捷的发帖。由于 MCBBS 发生了一些事情，我和 @Cinder 决定将其进行一些改动，以更加适应苦力怕论坛的排版，方便苦力怕论坛的用户使用。我们注意到原软件使用的是 CC0 协议，因此我们对其进行更改是符合其版权协议的。感谢 SPXFellow 对 SPXX 的开发乃至 Minecraft 资讯翻译的巨大贡献", 
            "orilink": "原版链接", 
            "howtouse": "下载之后，请先安装 Tamper Monkey 插件。下载之后将进入插件主页，选择添加插件（如下图所示），之后再新建的插件中粘贴下载的文本。下载之后需要启用插件，启用之后即可在 Minecraft 新闻之中直接拷贝 BBCode ", 
            "download": "下载", 
            "github": "Github" 
        } 
    },
    "zh-hans": {
        "bbcodetemp": "BBCode 模板",
        "description": "您可以选择模板进行填写，点击添加段落添加段落后填写，填写完成之后点击 Convert 之后复制生成的内容即可复制早论坛之中。所有支持\nBBCode 的论坛均可使用（包括 Discuz 论坛，例如 MCBBS 和苦力怕论坛等） ",
        "temp1": "模板一", 
        "temp1d1": "适合文字类内容使用", 
        "temp1d2": "加粗边框", 
        "temp1d3": "段落标题无边框", 
        "temp1d4": "排版来自：KLPBBS@Cinder", 
        "temp2": "模板二",
        "temp2d1": "适合图片、展示类内容使用", 
        "temp2d2": "排版简单干净", 
        "temp2d3": "无二级标题", 
        "temp2d4": "排版来自：FDS@小研Y", 
        "temp3": "模板三",
        "temp3d1": "适合需要多级标题内容使用", 
        "temp3d2": "有英语标题/副标题/提示", 
        "temp3d3": "排版相对困难", 
        "temp3d4": "排版来自：FDS@我是redstone", 
        "use": "使用", 
        "return": "返回", 
        "title": "标题", 
        "subtitle": "副标题", 
        "innertitle": "内部标题", 
        "innersubtitle": "内部副标题", 
        "headpicture": "头图", 
        "honmo": "正文", 
        "emoji": "Emoji", 
        "notes": "题记", 
        "viewtemplate": "查看模板", 
        "decoratecolour": "装饰颜色", 
        "maincolour": "主题颜色", 
        "innersize": "内部大小", 
        "size": "大小", 
        "insertimage": "插入图片", 
        "insertpara": "插入段落", 
        "insertsubpara": "插入第二段落", 
        "deletepara": "删除", 
        "compile": "编译", 
        "compileandcopy": "拷贝并编译", 
        "spxx":{ 
            "title": "苦力怕论坛 SPXX", 
            "klpspxxd1": "只适合翻译 Minecraft 资讯使用", 
            "klpspxxd2": "符合苦力怕论坛版规", 
            "klpspxxd3": "使用油猴脚本编写", 
            "klpspxxd4": "制作：@我是redstone @Cinder", 
            "desc": "这是一个特别为苦力怕论坛制作的 SPXX 版本。SPXX 原本是可以自动在 Minecraft 官网中复制粘贴新闻的符合 MCBBS 排版的 BBCode，方便译者在论坛更加便捷的发帖。由于 MCBBS 发生了一些事情，我和 @Cinder 决定将其进行一些改动，以更加适应苦力怕论坛的排版，方便苦力怕论坛的用户使用。我们注意到原软件使用的是 CC0 协议，因此我们对其进行更改是符合其版权协议的。感谢 SPXFellow 对 SPXX 的开发乃至 Minecraft 资讯翻译的巨大贡献", 
            "orilink": "原版链接", 
            "howtouse": "下载之后，请先安装 Tamper Monkey 插件。下载之后将进入插件主页，选择添加插件（如下图所示），之后再新建的插件中粘贴下载的文本。下载之后需要启用插件，启用之后即可在 Minecraft 新闻之中直接拷贝 BBCode ", 
            "download": "下载", 
            "github": "Github" 
        } 
    },
    "ja": {
        "bbcodetemp": "BBCode tamplate",
        "description": "You can choose a template to fill in, click Add Paragraph to add a paragraph and fill it in. After completing the filling, click Convert and copy the generated content to copy it in the early forum. All forums that support\nBBCode can be used (including Discuz forums such as MCBBS and Creeper forums, etc.)",
        "temp1": "Template 1",
        "temp1d1": "Good choice for articles", 
        "temp1d2": "Bold borders", 
        "temp1d3": "No borders between subparagraphs", 
        "temp1d4": "Template from KLPBBS@Cinder", 
        "temp2": "Template 2",
        "temp2d1": "Suitable for pictures", 
        "temp2d2": "Easy to use", 
        "temp2d3": "No subparagraphs", 
        "temp2d4": "Template from FDS@XiaoYan", 
        "temp3": "Template 3",
        "temp3d1": "Suitable for informative texts", 
        "temp3d2": "Have Subtitles/Subparagraphs", 
        "temp3d3": "Multi textfields", 
        "temp3d4": "Template from FDS@Redstone", 
        "use": "Use", 
        "return": "Return", 
        "title": "Title", 
        "subtitle": "Subtitle", 
        "innertitle": "Inner Title", 
        "innersubtitle": "Inner Subtitle", 
        "headpicture": "Header", 
        "honmo": "Main body", 
        "emoji": "Emoji", 
        "notes": "Inscription", 
        "viewtemplate": "View template", 
        "decoratecolour": "Decorate Colour", 
        "maincolour": "Colour", 
        "innersize": "Inner Size", 
        "size": "Size", 
        "insertimage": "Insert Image", 
        "insertpara": "Insert Paragraph", 
        "insertsubpara": "Insert Subparagraph", 
        "deletepara": "Delete", 
        "compile": "Convert", 
        "compileandcopy": "Convert and copy", 
        "spxx":{ 
            "title": "苦力怕论坛 SPXX", 
            "klpspxxd1": "只适合翻译 Minecraft 资讯使用", 
            "klpspxxd2": "符合苦力怕论坛版规", 
            "klpspxxd3": "使用油猴脚本编写", 
            "klpspxxd4": "制作：@我是redstone @Cinder", 
            "desc": "这是一个特别为苦力怕论坛制作的 SPXX 版本。SPXX 原本是可以自动在 Minecraft 官网中复制粘贴新闻的符合 MCBBS 排版的 BBCode，方便译者在论坛更加便捷的发帖。由于 MCBBS 发生了一些事情，我和 @Cinder 决定将其进行一些改动，以更加适应苦力怕论坛的排版，方便苦力怕论坛的用户使用。我们注意到原软件使用的是 CC0 协议，因此我们对其进行更改是符合其版权协议的。感谢 SPXFellow 对 SPXX 的开发乃至 Minecraft 资讯翻译的巨大贡献", 
            "orilink": "原版链接", 
            "howtouse": "下载之后，请先安装 Tamper Monkey 插件。下载之后将进入插件主页，选择添加插件（如下图所示），之后再新建的插件中粘贴下载的文本。下载之后需要启用插件，启用之后即可在 Minecraft 新闻之中直接拷贝 BBCode ", 
            "download": "下载", 
            "github": "Github" 
        }
    }
} 

def index(request): 
    return render(request, "bbcodetemp/index.html", { 
        'lang': language.get_language(request), 
        'trans': trantext[f"{language.get_language(request)}"], 
        'url': BACK_URL, 
        'temp': "index", 
    }) 

def templates(request, temp): 
    return render(request, f"bbcodetemp/{temp}/index.html", { 
        'lang': language.get_language(request), 
        'trans': trantext[f"{language.get_language(request)}"], 
        'url': BACK_URL, 
        'temp': temp, 
    }) 

def viewtemp(request, temp): 
    return render(request, f"bbcodetemp/{temp}/temp.html", { 
        'lang': language.get_language(request), 
        'trans': trantext[f"{language.get_language(request)}"], 
        'url': BACK_URL, 
        'temp': temp, 
    }) 

def spxxklp(request): 
    return render(request, f"bbcodetemp/spxxforklp/index.html", { 
        'lang': language.get_language(request), 
        'trans': trantext[f"{language.get_language(request)}"], 
        'url': BACK_URL 
    }) 

def spxxklpdown(request): 
    file_path = os.path.join(os.path.dirname(__file__), './templates/bbcodetemp/spxxforklp/spxxklp.js')
    response = FileResponse(open(file_path, 'rb'), as_attachment=True) 
    response['Content-Disposition'] = 'attachment; filename="spxxklp.js"' 
    return response 
