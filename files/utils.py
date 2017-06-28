import os
import time


def get_human_time(filepath):
    return time.strftime(
        '%Y-%m-%d',
        time.gmtime(int(os.stat(filepath).st_ctime))
    )


def get_newest_files(root, n):
    files = [os.path.join(root, f) for f in os.listdir(root)
             if not f.startswith('.')]
    files.sort(key=lambda f: os.stat(f).st_ctime, reverse=True)
    return files[:n]
