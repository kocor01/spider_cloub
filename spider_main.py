#coding:utf-8

import url_manager,html_parser,html_outputer,html_downloader,word_cloud

class SpiderMain(object):

    def __init__(self):
        # URL管理器
        self.urls = url_manager.UrlManager()
        # 网页下载器
        self.downloader = html_downloader.HtmlDownloader()
        # 数据提取器
        self.parser = html_parser.HtmlParser()
        # 数据处理器
        self.outputer = html_outputer.HtmlOutputer()
        # 云图生成器
        self.cloud = word_cloud.Wordcloud()

    def craw(self, root_url):
        count =1
        # 爬虫入口URL
        self.urls.add_new_url(root_url)
        # 待爬取URL
        wait_url = self.urls.has_new_url()

        if wait_url is not None:
            while wait_url:
               try:
                    # 获取一个待爬取URL
                    new_url = self.urls.get_new_url()
                    print("carw %d : %s" % (count, new_url))
                    # 爬取页面
                    html_cont = self.downloader.download(new_url)
                    # 数据提取
                    new_url, new_datas = self.parser.parser(new_url, html_cont)
                    # 添加新待爬取URL
                    self.urls.add_new_url(new_url)
                    # 数据加工处理
                    self.outputer.collect_data(new_datas)
                    # 爬虫循环控制
                    if count == 10:
                        break

                    count = count + 1
               except:
                   print("craw failed")

        # 数据加工输出
        self.outputer.process_data()
        #print("finish")

        # 分词
        self.outputer.cut_str()

        # 生成云图
        self.cloud.make()
        print("finish")



if __name__ == "__main__":
    # 爬虫入口URL
    root_url = "https://movie.douban.com/subject/26862829/comments?status=P"
    obj_spider = SpiderMain()
    # 启动爬虫
    obj_spider.craw(root_url)



