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


def print_signals(signals):
    print("List of signals:")
    for sig in set(signals):
        print(f"{sig::<2} {sig.name}")
    print("")


if __name__ == "__main__":
    pid = os.getpid()
    print_info(pid)
    signals = signal.Signals
    print_signals(signals)
    while True:
        catchable_sigs = set(signals) - {signal.SIGKILL, signal.SIGSTOP}
        for sig in catchable_sigs:
            signal.signal(sig, signal_handler)
