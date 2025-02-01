# Blocking pipes

If an application tries to write to a pipe without using an application level buffer, the write will block.

In this program I start `main.cpp` with a full stdout buffer and an empty stderr buffer. Because `fprintf()` automatically buffers writes to stdout, `main.cpp` does not block and the extra data is held within the program. When the pipe is read from python, we can see that a single line for the buffer was larger than the buff size:

```
peter@chronos:~/Documents/personalProjects/pipes$ python3.12 full_stdout.py
<python> Starting cpp tsk...
<python> Starting to read from buffers...
<CPP> Hi from stderr!

<CPP> Hi (again) from stderr!

<python> Size of stdout pipe:  4096
<python> Len of line in stdout pipe: 4118
<CPP> Hi from stdout!
```

If `fprintf()` is prevented from buffering the stdout write, we can see `main.cpp` blocks as the stdout buffer is full. We can prove the application is blocked as the second stderr log is not printed:

```
peter@chronos:~/Documents/personalProjects/pipes$ python3.12 full_stdout.py
<python> Starting cpp tsk...
<python> Starting to read from buffers...
<CPP> Hi from stderr!


```