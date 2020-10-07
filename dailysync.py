#!/usr/bin/env python
import subprocess
src = "/home/student-00-9db5bbeae0e7/data/prod/"
dest = "/home/student-00-9db5bbeae0e7/data/prod_backup/"
subprocess.call(["rsync", "-arq", src, dest])
