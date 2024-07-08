https://docs.python.org/3/library/timeit.html
-n N, --number=N
how many times to execute ‘statement’

-r N, --repeat=N
how many times to repeat the timer (default 5)

-s S, --setup=S
statement to be executed once initially (default pass)

-p, --process



############
import timeit
t= Timer(...)
try:
    t.timit(...)  # t.repeat()
except:
    t.print_exc()