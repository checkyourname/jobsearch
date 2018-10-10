# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
import MySQLdb.cursors

class JobsearchPipeline(object):
    def process_item(self, item, spider):
        return item
class MysqlPipeline(object):


    def __init__(self):

        self.conn = MySQLdb.connect('localhost', 'root', '', 'job_database', charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):

        insert_sql = """
        insert into job_search(company_name, job_name,working_city,salary,release_time)
        VALUES (%s, %s, %s, %s,%s)
            """
        self.cursor.execute(insert_sql, (item["company_name"],item["job_name"], item["working_city"], item["salary"], item["release_time"]))
        self.conn.commit()


