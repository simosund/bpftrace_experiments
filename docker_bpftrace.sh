#!/bin/bash
docker run -ti -v /usr/src:/usr/src:ro \
       -v /lib/modules/:/lib/modules:ro \
       -v /sys/kernel/debug/:/sys/kernel/debug:rw \
       -v /home/simon/Desktop/bpftrace_experiments:/home/my_scripts:ro \
       -w /home/my_scripts \
       --net=host --pid=host --privileged --name bpftrace\
       quay.io/iovisor/bpftrace:latest
