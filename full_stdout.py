import fcntl
import os
import subprocess

# 1. Create pipes for stderr and stdout
r_out, w_out = os.pipe()
r_out_stream = os.fdopen(r_out, 'r')
w_out_stream = os.fdopen(w_out, 'w')

r_err,w_err = os.pipe()
r_err_stream = os.fdopen(r_err, "r")
w_err_stream = os.fdopen(w_err, "w")

# 2. Set the size of the stdout pipe
fcntl.fcntl(w_out, fcntl.F_SETPIPE_SZ, 2**10)

# 3. Full up stdout pipe with garbage
for i in range(2**10 * 4):
    w_out_stream.write('`')
    w_out_stream.flush()

# 4. Run command with the full pipe
print("<python> Starting cpp tsk...")
p = subprocess.Popen("./build/pipes.tsk", stderr=w_err, stdout=w_out)

# 5. Read from buffers
print("<python> Starting to read from buffers...")
print(r_err_stream.readline())
print(r_err_stream.readline())

line_in_pipe = r_out_stream.readline()
print("<python> Size of stdout pipe: ", fcntl.fcntl(w_out, fcntl.F_GETPIPE_SZ))
print("<python> Len of line in stdout pipe:", len(line_in_pipe))
print(line_in_pipe[line_in_pipe.rindex("```````")+7:]) # Only print non garbage
