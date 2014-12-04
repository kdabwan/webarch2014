

from mrjob.job import MRJob
from combine_user_visits import csv_readline



class TopPages(MRJob):

    def mapper(self, line_no, line):
        cell = csv_readline(line)
        yield cell[0],1

    def reducer(self, word, visit_counts):
        total = sum(visit_counts)
        if total >= 10:
            yield word , total
        
if __name__ == '__main__':
    TopPages.run()
