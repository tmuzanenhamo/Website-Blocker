# Website-Blocker

This python scripy can be used to block certain websites which can be distracting when you want to work.

## How To Run

change the times you want to block in the if statement

The default times are between 8am and 11pm(2300)

# Windows

change the host_path path to the path with your host file which is usually in the "C:\Windows\System32\drivers\etc\hosts"

change the extension of the python file to .pyw | you can read further on the extension on the documentation [here](https://filext.com/file-extension/PYW)

# To schedule the script

Open task scheduler
create a task
check the box for run with highest privilledges
Select on startup in triggers (or any time you prefer)
Select actions and select start a program
choose option to run when on battery in conditions
Press ok

## MAC OS and LINUX (ubuntu)

change the hots_path in the script to /etc/hosts

# Using Cron

open the crontab file with an e Flag 
    command -> sudo crontab -e

add the following line in the crontab
    @reboot python3 "Path to your script" witha .py


# Good luck and Happy Working :)






