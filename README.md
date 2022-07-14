# 	ps-tools

Various *nix process tools

# signals.py

Tool to test out [signals](https://en.wikipedia.org/wiki/Signal_(IPC)). Program will capture signals and print out the received signal.

e.g., 

```bash
$ ./signals.py
Interpreter: /opt/homebrew/opt/python@3.9/bin/python3.9

Keyboard combinations for signal inputs:
     CTRL + c (^C) for SIGINT
     CTRL + \ (^\) for SIGQUIT
     CTRL + z (^z) for SIGTSTP

To kill this process run: kill -9 82505
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

e.g., 

```bash
$ ./pid_watch.py 94352 95133
watching PID: 94352
watching PID: 95133
PID ended: 94352
PID ended: 95133
```