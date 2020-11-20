#!/bin/bash

PID=$(docker inspect -f='{{.State.Pid}}' $1)
NSID=$(stat /proc/$PID/ns/pid -c "%N" | cut -d[ -f2 | cut -d] -f1)

bpftrace ./overlayfs.bt $NSID
