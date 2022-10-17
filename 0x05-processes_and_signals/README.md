## 0x05. Processes and signals

> This repository contains the tasks for `Processes and signals` project and a description of what each script or function does:

### Tasks

#### Task: 0-what-is-my-pid
Write a Bash script that displays its own PID.

#### Task: 1-list_your_processes
Write a Bash script that displays a list of currently running processes.
* Must show all processes, for all users, including those which might not have a TTY. Display in a user-oriented format. Show process hierarchy

#### Task: 2-show_your_bash_pid
Using your previous exercise command, write a Bash script that displays lines containing the `bash` word, thus allowing you to easily get the PID of your Bash process.

#### Task: 3-show_your_bash_pid_made_easy
Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word `bash`.

#### Task: 4-to_infinity_and_beyond
Write a Bash script that displays `To infinity and beyond` indefinitely.

#### Task: 5-dont_stop_me_now
Write a Bash script that stops `4-to_infinity_and_beyond process`. You must use `kill`

#### Task: 6-stop_me_if_you_can
Write a Bash script that stops `4-to_infinity_and_beyond process`. You cannot use `kill` or `killall`

#### Task: 7-highlander
Write a Bash script that displays:
* `To infinity and beyond` indefinitely. With a `sleep 2` in between each iteration. `I am invincible!!!` when receiving a `SIGTERM` signal

#### Task: 8-beheaded_process
Write a Bash script that kills the process `7-highlander`.

#### Task: 100-process_and_pid_file
Write a Bash script that:
* Creates the file `/var/run/myscript.pid` containing its PID
* Displays `To infinity and beyond` indefinitely
* Displays `I hate the kill command` when receiving a SIGTERM signal
* Displays `Y U no love me?!` when receiving a SIGINT signal
* Deletes the file `/var/run/myscript.pid` and terminates itself when receiving a SIGQUIT or SIGTERM signal

#### Task: 101-manage_my_process, manage_my_process
Write a `manage_my_process` Bash script that:
* Indefinitely writes `I am alive!` to the file `/tmp/my_process`
* In between every `I am alive!` message, the program should pause for 2 seconds
Write Bash (init) script `101-manage_my_process` that manages `manage_my_process`

#### Task: 102-zombie.c
Write a C program that creates 5 zombie processes.
* For every zombie process created, it displays `Zombie process created, PID: ZOMBIE_PID`
* When your code is done creating the parent process and the zombies, use the function bellow
```
int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}
```
___

#### Files:

* [test_files](https://github.com/jonyamagiri/alx-system_engineering-devops/tree/master/0x05-processes_and_signals/test_files)


