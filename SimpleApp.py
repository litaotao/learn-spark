"""SimpleApp.py"""

from pyspark import SparkContext

logFile = 'README-SPARK.md'
sc = SparkContext('local', 'Simple App')
logData = sc.textFile(logFile).cache()

numAs = logData.filter(lambda s: 'a' in s).count()
numBs = logData.filter(lambda s: 'b' in s).count()

print 'lines with a: %i, \nlines with b: %i' % (numAs, numBs)


