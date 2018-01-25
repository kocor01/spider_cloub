# spider_cloub
python爬虫，Scrapy爬取豆瓣电影《芳华》电影短评，分词生成云图。


Python版本为3.6

爬虫爬取最近比较火的电影《芳华》分词后生成词云图
使用了 jieba分词，云图用wordcloud生成
用了朋友的2B姿势的自拍照片简单的P了下（为了不暴露，P成全黑的），作为生成词云图的底图模板

在生成词云图的过程中，发现一个问题，词云图底图模板有PNG格式的图片生成出来的效果很差，例如用下图PNG格式去生成，生成出来的词语图根本不成人形。本例是用JPG格式的图片去生成，生成出来的效果还是相当不错的。建议底图用JPG去生成。其他格式的图片没试验，不知生成的效果如何。


***  
云图底图模板：
![云图底图模板](http://img.blog.csdn.net/20180125173350651?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQveWdjMTIzMTg5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)  

***  
生成的云图效果：
![生成的云图效果](http://img.blog.csdn.net/20180125173433271?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQveWdjMTIzMTg5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)  
