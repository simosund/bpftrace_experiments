# bpftrace Experiments
This repo contains various bpftrace tools I've implemented while reading through the [BPF-performance tools book](http://www.brendangregg.com/bpf-performance-tools-book.html).
Most of the tools are simply manually copy pasted from the book, with some possible minor modification to better suit my system or to avoid bpftrace issue [#1305](https://github.com/iovisor/bpftrace/issues/1305).
The original implementation of these tools including some more documentation of them can be found at [BPF Performance Tool github repository](https://github.com/brendangregg/bpf-perf-tools-book).

The only noteworthy tools I've implemented myself so far are a couple of pping versions that can found in the network directory.

Most of the tools in here should work with bpftrace version 0.9.4 which is what I've used (as packed for Ubuntu 20.04).
