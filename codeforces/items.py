# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, Join, TakeFirst

class SubmissionsList(scrapy.Item):
    date_time = scrapy.Field(
        output_processor = TakeFirst()
    )
    submission_id = scrapy.Field(
        output_processor = TakeFirst()
    )
    problem_name = scrapy.Field(
        output_processor = TakeFirst()
    )
    submission_link = scrapy.Field(
        output_processor = TakeFirst()
    )
    participant_id = scrapy.Field(
        output_processor = TakeFirst()
    )
    contest_url = scrapy.Field(
        output_processor = TakeFirst()
    )
    submission_lang = scrapy.Field(
        output_processor = TakeFirst()
    )
    time_consumed = scrapy.Field(
        output_processor = TakeFirst()
    )
    memory_consumed = scrapy.Field(
        output_processor = TakeFirst()
    )
    submission_verdict = scrapy.Field(
        output_processor = TakeFirst()
    )
    submission_verdict_text = scrapy.Field(
        output_processor = TakeFirst()
    )
    problem_id = scrapy.Field(
        # output_processor = TakeFirst()
    )


class SubmissionData(scrapy.Item):
    submission_stats = scrapy.Field()
    submissionid = scrapy.Field(
        # input_processor = MapCompose(lambda x : x[0].strip()),
        output_processor=TakeFirst()
    )
    problemname = scrapy.Field(
        # input_processor=MapCompose(lambda x: x[0].strip()),
        output_processor=TakeFirst()
    )
    language = scrapy.Field(
        # input_processor=MapCompose(lambda x: x[0].strip()),
        output_processor=TakeFirst()
    )
    verdict = scrapy.Field(
        # input_processor=MapCompose(lambda x: x[0].strip()),
        output_processor=TakeFirst()
    )
    time_taken = scrapy.Field(
        output_processsor=TakeFirst()
    )
    memory = scrapy.Field(
        # input_processor=MapCompose(lambda x: x[0].strip()),
        output_processor=TakeFirst()
    )
    submitted_time = scrapy.Field(
        # input_processor=MapCompose(lambda x: x[0].strip()),
        output_processor=TakeFirst()
    )
    judged_time = scrapy.Field(
        # input_processor=MapCompose(lambda x: x[0].strip()),
        output_processor=TakeFirst()
    )
    username = scrapy.Field(
        output_processor = TakeFirst()
    )
    program = scrapy.Field()
    testcases_data = scrapy.Field()
