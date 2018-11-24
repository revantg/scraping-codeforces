# -*- coding: utf-8 -*-

from scrapy import Spider, Request
from scrapy.exceptions import CloseSpider
from scrapy.loader import ItemLoader

from codeforces.items import SubmissionsList, SubmissionData

import pickle 
import datetime 
from time import sleep

main_url = "http://codeforces.com/" 
all_problems = {}

class LtraGoluSpider(Spider):
    name = 'codeforces'
    # allowed_domains = ['codeforces.com/submissions/ltra_golu']
    # start_urls = ['http://codeforces.com/submissions/ltra_golu/page/1']
    last_submission_id = None
    # username = 'ltra_golu'

    def __init__(self, user_name = 'ltra_golu', submission_id = None):
        self.last_submission_id = submission_id
        self.start_urls = [
            'http://codeforces.com/submissions/' + user_name + '/page/1'
        ]
        self.username = user_name

    def parse(self, response):
        for i in range(1, 13):
            url = 'http://codeforces.com/submissions/' + self.username + '/page/' + str(i)

            yield Request(url, callback = self.parse_submission_page)
            # break


    def parse_submission_page(self, response):
        submssions = response.xpath("//*[@data-submission-id]")
        for submission in submssions:
            to_scrape = False
            date_time = submission.xpath('.//*[@class="status-small"]/text()')[0].extract().strip()

            submission_id = submission.xpath('./@data-submission-id').extract_first()
            if submission_id and submission_id == self.last_submission_id:
                raise CloseSpider('Successfully Scraped all files till ' + submission_id)

            problem_name = submission.xpath(".//*[@data-problemid]/a/text()").extract_first().strip()

            submission_link = submission.xpath('.//*[@class = "view-source"]/@href').extract_first()
            if submission_link: submission_link = response.urljoin(submission_link)

            participant_id = submission.xpath('.//*[@data-participantid]/@data-participantid').extract_first()

            contest_url = submission.xpath(".//*[@data-problemid]/a/@href").extract_first()
            if contest_url: contest_url = response.urljoin(contest_url)

            submission_lang = submission.xpath('./td[5]/text()').extract_first().strip()

            time_consumed = submission.xpath('.//*[@class = "time-consumed-cell"]/text()').extract_first().strip()

            memory_consumed = submission.xpath('.//*[@class = "memory-consumed-cell"]/text()').extract_first().strip()

            submission_verdict = submission.xpath('.//*[@submissionverdict]/@submissionverdict').extract_first()

            submission_verdict_text = submission.xpath('.//*[@class = "verdict-rejected"]/text()').extract_first()

            error_on = 'NA'

            problem_id = tuple(contest_url.replace('http://codeforces.com', '').replace('/contest/', '').replace('/problem', '').split('/'))
            

            submission_verdict_text = submission.xpath('.//*[@class = "verdict-accepted"]/text()').extract_first()

            if submission_verdict_text: 
                error_on = submission.xpath('.//*[@class = "verdict-format-judged"]/text()').extract_first()
                if error_on:
                    submission_verdict_text += error_on

            submission_prog_link = response.urljoin(submission_link)
            if submission_verdict_text:
                to_scrape = True
                # yield scrapy.Request(submission_prog_link, callback = self.parse_submission)
            else :
                submission_verdict_text = submission_verdict

            submission_stats = {
                'date_time': date_time,
                'submission_id': submission_id,
                'problem_name': problem_name,
                'submission_link': submission_link,
                'participant_id': participant_id,
                'contest_url': contest_url,
                'submission_lang': submission_lang,
                'time_consumed': time_consumed,
                'memory_consumed': memory_consumed,
                'submission_verdict': submission_verdict,
                'submission_verdict_text': submission_verdict_text,
                'problem_id': problem_id,
            }

            if problem_id[0] not in all_problems.keys():
                all_problems[problem_id[0]] = []
            all_problems[problem_id[0]].append(submission_stats)

            submission_stats_il = ItemLoader(item = SubmissionsList(), response = response)

            submission_stats_il.add_value('date_time', submission_stats['date_time'])
            submission_stats_il.add_value('submission_id', submission_stats['submission_id'])
            submission_stats_il.add_value('problem_name', submission_stats['problem_name'])
            submission_stats_il.add_value('submission_link', submission_stats['submission_link'])
            submission_stats_il.add_value('participant_id', submission_stats['participant_id'])
            submission_stats_il.add_value('contest_url', submission_stats['contest_url'])
            submission_stats_il.add_value('submission_lang', submission_stats['submission_lang'])
            submission_stats_il.add_value('time_consumed', submission_stats['time_consumed'])
            submission_stats_il.add_value('memory_consumed', submission_stats['memory_consumed'])
            submission_stats_il.add_value('submission_verdict', submission_stats['submission_verdict'])
            submission_stats_il.add_value('submission_verdict_text', submission_stats['submission_verdict_text'])
            submission_stats_il.add_value('problem_id', submission_stats['problem_id'])
            # submission_stats_il.add_value('username', self.username)


            yield submission_stats_il.load_item()
            if to_scrape:
                yield Request(submission_prog_link, 
                            callback=self.parse_submission,
                            meta = {
                                    'submission_data': submission_stats,
                                    'to_scrape' : to_scrape,
                                    'dont_redirect': True,
                                    'handle_httpstatus_list': [302]
                                }
                              )            

            # il.add_value('submission_stats', submission_data)
            
            # return il.load_item()
        
    def parse_submission(self, response):
        # pass
        submission_stats = response.meta.get('submission_data')
        # to_scrape = response.meta.get('to_scrape')
        
        # if to_scrape is False:    
        #     return submission_stats_il.load_item()

        # print ('sleeping')
        # sleep(5)

        all_testcase_data = []

        table_data = list(response.xpath("//*[table]//*[@class = '']"))[0]

        submission_id = table_data.xpath("./tr[2]/td[1]/text()").extract_first().strip()
        problem_name = table_data.xpath("./tr[2]/td[3]/a/@title").extract_first().strip()
        language = table_data.xpath("./tr[2]/td[4]/text()").extract_first().strip()
        verdict = table_data.xpath("./tr[2]/td[5]/span/text()").extract_first().strip()
        time_taken = table_data.xpath("./tr[2]/td[6]/text()").extract_first().strip()
        memory = table_data.xpath("./tr[2]/td[7]/text()").extract_first().strip()
        submitted_time = table_data.xpath("./tr[2]/td[8]/text()").extract_first().strip()
        judged_time = table_data.xpath("./tr[2]/td[9]/text()").extract_first().strip()
        program = response.xpath('.//*[@id="program-source-text"]/text()').extract()

        testcases = response.xpath(".//*[@class = 'roundbox ']")[1:]
        for test in testcases:
            test_no = test.xpath("./div[3]/text()").extract_first()

            qty1, qty2 = test.xpath("./div[4]/text()").extract()
            metrics = test.xpath("./div[4]/strong/text()").extract()

            testcase_verdict = test.xpath("./div[5]/div/text()").extract_first()

            input_data = test.xpath(".//*[@class = 'file input-view']/div[2]/pre/text()").extract_first()
            output_data = test.xpath(".//*[@class = 'file output-view']/div[2]/pre/text()").extract_first()
            correct_answer = test.xpath(".//*[@class='file answer-view']/div[2]/pre/text()").extract_first()
            comment = test.xpath(".//*[@class='file checker-comment-view']/div[2]/pre/text()").extract_first()

            testcase_data = {
                "test_no" : test_no,
                "testcase_verdict" : testcase_verdict,
                "input_data" : input_data,
                "output_data" : output_data,
                "correct_answer" : correct_answer,
                "comment" : comment,
                metrics[0] : qty1,
                metrics[1] : qty2,
            }

            # print (testcase_data)
            all_testcase_data.append(testcase_data)

        submission_data_il = ItemLoader(item = SubmissionData(), response = response)

        submission_data_il.add_value("submission_stats", submission_stats)
        submission_data_il.add_value("submissionid", submission_id)
        submission_data_il.add_value("problemname", problem_name)
        submission_data_il.add_value("language", language)
        submission_data_il.add_value("verdict", verdict)
        submission_data_il.add_value("time_taken", time_taken)
        submission_data_il.add_value("memory", memory)
        submission_data_il.add_value("submitted_time", submitted_time,)
        submission_data_il.add_value("judged_time", judged_time)
        submission_data_il.add_value("program", program)
        submission_data_il.add_value("testcases_data", all_testcase_data)
        submission_data_il.add_value("username", self.username)



        return submission_data_il.load_item()

        # all_submission_data = {
            # 'submission_stats' : submission_stats,
            # "submission_id" : submission_id, 
            # "problem_name" : problem_name, 
            # "language" : language, 
            # "verdict" : verdict, 
            # "memory" : memory, 
            # "submitted_time" : submitted_time, 
            # "judged_time" : judged_time, 
            # "program" : program, 
            # "testcases_data" : all_testcase_data,
        # }

    def close(self, reason):
        filename = str(datetime.datetime.now())
        with open(filename + '.pickle', 'wb') as file:
            pickle.dump(all_problems, file)
