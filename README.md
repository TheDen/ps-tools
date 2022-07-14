# 	ps-tools

Various \*nix process tools

# signals.py

Tool to test out [signals](https://en.wikipedia.org/wiki/Signal_(IPC)). Program will capture signals and print out the received signal.

For example, 

```bash
$ ./signals.py
Interpreter: /opt/homebrew/opt/python@3.9/bin/python3.9

Keyboard combinations for signal inputs:
     CTRL + c (^C) for SIGINT
     CTRL + \ (^\) for SIGQUIT
     CTRL + z (^z) for SIGTSTP

To kill this process run: kill -9 74974

List of signals:
1: SIGHUP
2: SIGINT
3: SIGQUIT
4: SIGILL
5: SIGTRAP
6: SIGABRT
7: SIGEMT
8: SIGFPE
9: SIGKILL
10 SIGBUS
11 SIGSEGV
12 SIGSYS
13 SIGPIPE
14 SIGALRM
15 SIGTERM
16 SIGURG
17 SIGSTOP
18 SIGTSTP
19 SIGCONT
20 SIGCHLD
21 SIGTTIN
22 SIGTTOU
23 SIGIO
24 SIGXCPU
25 SIGXFSZ
26 SIGVTALRM
27 SIGPROF
28 SIGWINCH
29 SIGINFO
30 SIGUSR1
31 SIGUSR2
```


Note that `SIGSTOP` and `SIGKILL` cannot be captured


# pid_watch.py

Tool to watch processes until they die. Takes one or more PIDs as arguments, and will exit when the processes end. 

```bash
$ ./pid_watch.py -h
usage: pid_watch.py [-h] Process ID [Process ID ...]

Watch process IDs

positional arguments:
  Process ID  Process IDs

optional arguments:
  -h, --help  show this help message and exit
```

For example, 

```bash
$ ./pid_watch.py 94352 95133
watching PID: 94352
watching PID: 95133
PID ended: 94352
PID ended: 95133
```