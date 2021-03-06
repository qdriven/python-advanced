# encoding: utf-8
import datetime
import os


def update_git():
    cmd_git_add = "git add ."
    cmd_git_commit = 'git commit -m "{date} data update"' \
        .format(date=str(datetime.date.today()))
    cmd_git_push = 'git push -u origin master'

    for item in [cmd_git_add, cmd_git_commit, cmd_git_push]:
        os.system(item)
