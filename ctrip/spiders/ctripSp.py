# -*-coding:utf-8-*-

import scrapy
from ctrip.items import CtripItem


class TcopspSpider(scrapy.Spider):
    name = 'CtripPy'
    allowed_domains = ['http://you.ctrip.com']
    offset = 1

    url = "http://you.ctrip.com/destinationsite/TTDSecond/SharedView/AsynCommentView?poiID=77653&districtId=175&districtEName=Nanchang&pagenow="
    url2 = "&order=1&star=0.0&tourist=0.0&resourceId=9075&resourcetype=2"
    # 这个是我们最想要的链接
    # 秋水广场
    # http://you.ctrip.com/destinationsite/TTDSecond/SharedView/AsynCommentView?poiID=92374&districtId=175&districtEName=Nanchang&pagenow=2&order=1&star=0.0&tourist=0.0&resourceId=119790&resourcetype=2
    # 八一纪念馆
    # http://you.ctrip.com/destinationsite/TTDSecond/SharedView/AsynCommentView?poiID=77635&districtId=175&districtEName=Nanchang&pagenow=2&order=3.0&star=0.0&tourist=0.0&resourceId=9055&resourcetype=2
    # 南昌万达主题乐园
    # http://you.ctrip.com/destinationsite/TTDSecond/SharedView/AsynCommentView?poiID=24826548&districtId=175&districtEName=XinjianDistrict&pagenow=2&order=3.0&star=0.0&tourist=0.0&resourceId=1836888&resourcetype=2
    # http://you.ctrip.com/destinationsite/TTDSecond/SharedView/AsynCommentView?poiID=24826548&districtId=175&districtEName=XinjianDistrict&pagenow=2&order=1&star=0.0&tourist=0.0&resourceId=1836888&resourcetype=2
    # 滕王阁
    # http://you.ctrip.com/destinationsite/TTDSecond/SharedView/AsynCommentView?poiID=77653&districtId=175&districtEName=Nanchang&pagenow=2&order=1&star=0.0&tourist=0.0&resourceId=9075&resourcetype=2
    start_urls = [url + str(offset) + url2]

    def parse(self, response):
        # with open("123.html", "w") as f:
        #    f.write(response.body)
        data = response.xpath('//div[@class="comment_single"]')
        # data = json.loads(response.text)["data"]
        # print data

        for each in data:
            item = CtripItem()
            # 获取评论
            item["cat_user_comment"] = each.xpath(
                './ul/li[@class="main_con"]/span[@class="heightbox"]/text()').extract()
            # 获取评论时间
            item["cat_comment_time"] = each.xpath(
                './ul/li[@class="from_link"]/span[@class="f_left"]/span[@class="time_line"]/em/text()').extract()
            # 获取评论人姓名
            item["cat_user_name"] = each.xpath(
                './div[@class="userimg"]/span[@class="ellipsis"]/a/text()').extract()

            yield item

        # 被限制了,慎用
        if self.offset < 50:
            self.offset += 1
            # print self.offset
            yield scrapy.Request(self.url + str(self.offset) + self.url2, callback=self.parse, dont_filter=True)
