import time
from random import randrange
from essential_generators import DocumentGenerator

def main():
 a = 1
 gen = DocumentGenerator()
 while a <= 10:
  with open(r'C:\Spark3\datafolder\random_log{}{}.txt'.format(a,randrange(100)),'w') as writefile:
   #writefile.write(gen.paragraph())
   writefile.write(gen.sentence())
   print('creating file random_log{}{}.txt'.format(a,randrange(100)))
   a += 1
   time.sleep(randrange(10))


if __name__ == '__main__':
    main()
