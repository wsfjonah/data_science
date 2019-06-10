import os

with open('d:/rndom.bin', 'wb') as f:
    f.write(os.urandom(10))
    # f.write(123)
