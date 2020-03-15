import os, sys

def iterateProcess(arr):
  if not isinstance(arr, list):
    raise TypeError
  for cmd in arr:
    print(cmd)
    os.system(cmd)

message = sys.argv[1]

processes = [
  "git add .",
  "git commit -m '%s'" % message,
  "git push origin HEAD"
]

iterateProcess(processes)

# os.system('git add .')
