from mrjob.job import MRJob
class xpensive_count(MRJob):
   def mapper(self, _, line):
       for word in line.split():
           if word.lower() == "expensive":
               yield "expensive", 1

   def reducer(self, key, values):
       yield key, sum(values)
if __name__ == "__main__":
   xpensive_count.run()