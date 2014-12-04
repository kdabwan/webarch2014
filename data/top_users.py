

from mrjob.job import MRJob
from combine_user_visits import csv_readline

class TopPages(MRJob):

    def mapper(self, line_no, line):
        """Extracts the Vroot that was visited"""
        cell = csv_readline(line)
        if cell[0] == 'V':
            yield cell[2],1

    def reducer(self, user, visit_counts):
        total = sum(visit_counts)
        if total > 20:
            yield user , total
        
if __name__ == '__main__':
    TopPages.run()
