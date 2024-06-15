import scrapy
from scrapy.linkextractors import LinkExtractor

class JobItem(scrapy.Item):
    jobName = scrapy.Field()
    jobUrl = scrapy.Field()
    # last_updated = scrapy.Field(serializer=str)

class basicSpider(scrapy.Spider):
    name="basic"
    # linkCount = None
    start_urls = ["https://tulip.co/careers/engineering/#tulip-job-board_header"]

    link_extractor = LinkExtractor()

    def parse(self, response):
        
        anchors = response.css("div.tulip-job-board_department-content a")
        
        # jobLinks = []

        # linkCount = len(anchors)
        jobCount = len(anchors)
        
        # yield {
        #     "count": jobCount
        # }


        # linkList = link_extractor.extract_links(anchors)
        # yield {
        #     "link": linkList
        # }
        # yield{
        #     "url": linkList
        # }

        for link in anchors:
            
            item = JobItem()
            
            item['jobName'] = link.css("::text").get()
            item['jobUrl'] = link.css("::attr(href)").get()
            
            yield item
            
            # yield {
            #     # "JobCount": jobCount,
            #     "desc": item
            # }
            
            # yield{
            #     "jobName": link.css("::attr(href)").get(),
            #     "jobUrl":  link.css("::text").get()
            # }
        # for anchor in anchors:
        #     href = anchor.css("::href").get()

        
        

        # yield {
        #         "topicCount": linkCount,
        #     }
        

        
