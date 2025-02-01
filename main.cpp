#include <iostream>

int main() {
    // Write first line to stderr. If program blocks that should be all we see
    fprintf(stderr, "<CPP> Hi from stderr!\n");

    // Write to stdout, which may or may not be full
    int bytesWritten = fprintf(stdout, "<CPP> Hi from stdout!\n");
    int rc = 0;
    // rc = fflush(stdout); // If we try to flush, the program blocks. That is because fprintf has an internal buffer and won't be able to flush if the pipe is full

    // Write to stderr. If program blocked we shouldn't get here
    fprintf(stderr, "<CPP> Hi (again) from stderr!\n");
}