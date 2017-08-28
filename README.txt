===========
auto SSH
===========

This program reads the ssh server configuration details from configuration 
file ipAddr.txt and automatically logs in after performing all sanity checks
and runs commands provided in the configuration file. For each successful 
login, it creates a file output.txt for each of servers specified in the 
configuration file. The output of the commdands if any are saved in the 
output file. 

This program can be used to run scripts in routers such as to display running 
configuration, system health etc.

Salient Features
================
The program uses primarily paramiko package and has been implemented by using python 2.7

Testing
=======

Configuration file:ipAddr.txt
=============================
127.0.0.1:<login>:<password>:df -h,ps -aux
90.0.24.92:<login>:<password>:ls


Contents of output1.txt

IP Address:127.0.0.1
=====================

df -h
================
Filesystem      Size  Used Avail Use% Mounted on
udev            7.6G     0  7.6G   0% /dev
tmpfs           1.6G  9.5M  1.6G   1% /run
/dev/sdb2       219G  129G   80G  62% /
tmpfs           7.6G  1.1M  7.6G   1% /dev/shm
tmpfs           5.0M  4.0K  5.0M   1% /run/lock
tmpfs           7.6G     0  7.6G   0% /sys/fs/cgroup
/dev/sdb1       511M  3.4M  508M   1% /boot/efi
tmpfs           1.6G   56K  1.6G   1% /run/user/1000

ps -aux
================
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.0 185392  6080 ?        Ss   05:52   0:01 /sbin/init splash
root         2  0.0  0.0      0     0 ?        S    05:52   0:00 [kthreadd]
root         4  0.0  0.0      0     0 ?        S<   05:52   0:00 [kworker/0:0H]
root         6  0.0  0.0      0     0 ?        S    05:52   0:00 [ksoftirqd/0]
root         7  0.0  0.0      0     0 ?        S    05:52   0:22 [rcu_sched]
root         8  0.0  0.0      0     0 ?        S    05:52   0:00 [rcu_bh]
root         9  0.0  0.0      0     0 ?        S    05:52   0:00 [migration/0]
root        10  0.0  0.0      0     0 ?        S<   05:52   0:00 [lru-add-drain]
root        11  0.0  0.0      0     0 ?        S    05:52   0:00 [watchdog/0]
root        12  0.0  0.0      0     0 ?        S    05:52   0:00 [cpuhp/0]
............................................
............................................
............................................
............................................
root     16288  0.0  0.0      0     0 ?        S    18:21   0:00 [kworker/2:1]
root     16291  0.0  0.0      0     0 ?        S    18:21   0:00 [kworker/7:3]
root     16305  0.0  0.0      0     0 ?        S    18:22   0:00 [kworker/3:3]
root     16358  0.0  0.0      0     0 ?        S    18:24   0:00 [kworker/u16:0]
root     16412  0.0  0.0      0     0 ?        S    18:26   0:00 [kworker/5:2]
root     16416  0.0  0.0      0     0 ?        S    18:26   0:00 [kworker/7:0]
root     16457  0.0  0.0      0     0 ?        S    18:27   0:00 [kworker/0:1]
root     16458  0.0  0.0      0     0 ?        S    18:27   0:00 [kworker/0:3]
root     16518  0.0  0.0      0     0 ?        S    18:28   0:00 [kworker/1:1]
root     16586  0.0  0.0      0     0 ?        S    18:30   0:00 [kworker/3:0]
sudip    16594  5.5  0.1 218880 25628 pts/20   Sl+  18:31   0:00 python ./test1.py
root     16599  0.0  0.0  97496  6964 ?        Ss   18:31   0:00 sshd: sudip [priv]
sudip    16627  0.0  0.0  97496  4424 ?        S    18:31   0:00 sshd: sudip@notty
sudip    16629  0.0  0.0  37364  3400 ?        Rs   18:31   0:00 ps -aux


Authors
  - Sudip Midya
