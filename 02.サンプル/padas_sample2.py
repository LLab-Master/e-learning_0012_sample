import pandas as pd
import random
t  = [ [random.random() for x in range(4) ]
      for y in range(10)]


df = pd.DataFrame(t , columns=list('ABCD'))
print(df)
