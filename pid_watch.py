#!/usr/bin/env python3

import os
import sys
import errno
import signal
import argparse
import multiprocessing as mp


def pid_exists(pid):
    if pid == 0:
        return True
    try:
        os.kill(pid, 0)
    except OSError as err:
        if err.errno == errno.ESRCH:
            return False
        elif err.errno == errno.EPERM:
            return True
        else:
            raise err
    else:
        return True


def watch_pid(pid):
    if not pid_exists(pid):
        print(f"{pid} does not exist")
        return
    print(f"watching PID: {pid}")
    pid_running = True
    while pid_running:
        pid_running = pid_exists(pid)
    print(f"PID ended: {pid}")


def signal_handler(sig, frame):
    pool.close()
    poo.join()
    sys.exit(0)


def main():
    parser = argparse.ArgumentParser(description="Watch process IDs")
    parser.add_argument(
        "process_ids",
        type=int,
        nargs="+",
        help="Process IDs",
    )

    args = parser.parse_args()
    pool = mp.Pool(mp.cpu_count())
    pool.map(watch_pid, args.process_ids)
    signal.signal(signal.SIGINT, signal_handler, pool)


if __name__ == "__main__":
    main()
