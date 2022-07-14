#!/usr/bin/env python3

import sys
import os
import signal


def print_pid(pid):
    print(f"\nPID: {pid}")


def print_info(pid):
    info = f"""Interpreter: {sys.executable}\n\nKeyboard combinations for signal inputs:
     CTRL + c (^C) for SIGINT
     CTRL + \ (^\) for SIGQUIT
     CTRL + z (^z) for SIGTSTP\n\nTo kill this process run: kill -9 {pid}\n"""
    print(info)


def signal_handler(signum, frame):
    print(f"\nReceived signal {signal.Signals(signum).name}")


if __name__ == "__main__":
    pid = os.getpid()
    print_info(pid)
    while True:
        catchable_sigs = set(signal.Signals) - {signal.SIGKILL, signal.SIGSTOP}
        for sig in catchable_sigs:
            signal.signal(sig, signal_handler)
