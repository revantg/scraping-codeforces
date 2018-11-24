# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from codeforces.items import SubmissionData, SubmissionsList
import os
import json

# replace this with your path where you want your submissions to be placed
path = "/home/revant/Desktop/all_programs/"
#-------------------------------------------------------------------------------------

class CodeforcesPipeline(object):
    
    def gen_prog_file(self, program, submitted_time, time_taken, memory, username, problemname, language, problem_id):
        program_headers = '''/* \n\t{problem_id} {problemname} \n\tauthor : {username} | submitted at : {submitted_time}\n\ttime taken : {time_taken} | memory consumed : {memory}\n*/\n'''.format(
                                                problem_id = problem_id,
                                                problemname = problemname,
                                                username = username,
                                                submitted_time = submitted_time,
                                                time_taken = time_taken[0],
                                                memory = memory,
                                            )

        print(program_headers, program[0])
        if 'C++' in language:
            full_prog_text = program_headers + program[0]
            file_name = problemname + '.cpp'
        else:
            full_prog_text = program[0]
            file_name = problemname + '.py'
        
        global path
        path += problem_id + problemname 
        if not os.path.exists(path):
            os.mkdir(path)
            os.chdir(path)
            with open(file_name, 'w') as file:
                file.write(full_prog_text)
        return path
    def process_item(self, item, spider):
        # return item
        if isinstance(item, SubmissionsList):
            return self.process_submission_list(item, spider)
        elif isinstance(item, SubmissionData):
            return self.process_submission_data(item, spider) 

    def process_submission_list(self, item, spider):
        try :
            with open("submission_list.json") as file:
                data = json.load(file)
        except:
            data = {}

        data.update(item)

        with open("submission_list.json", 'w') as file:
            json.dump(data, file)

        return item

    def process_submission_data(self, item, spider):
        submission_stats = item['submission_stats']
        submissionid = item['submissionid']
        problemname = item['problemname']
        language = item['language']
        verdict = item['verdict']
        time_taken = item['time_taken']
        memory = item['memory']
        submitted_time = item['submitted_time']
        judged_time = item['judged_time']
        program = item['program']
        try : 
            username = item['username']
        except :
            username = 'ltra_golu'
        problem_id = item['submission_stats'][0]['problem_id']
        problem_id = str(problem_id[0]) + ' ' + str(problem_id[1])

        if "C++" in language:
            path = self.gen_prog_file(program, submitted_time, time_taken, memory, username, problemname, language, problem_id[0])
            os.chdir(path)

        try : 
            with open("submission_data.json") as f:
                data = json.load(f)
        except:
            data = {}    
            
        data.update(item)

        with open("submssion_data.json", 'w') as f:
            json.dump(data, f)
        


