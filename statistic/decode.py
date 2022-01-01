import os, sys
from subprocess import Popen, PIPE

if __name__ == '__main__':
    decode_folder = sys.argv[1]
    for file in os.listdir(decode_folder):
        path_file = os.path.join("/root/src/data/train", os.path.join(decode_folder, file))
        inference_cmd = """mpirun -n 3 --allow-run-as-root ./fl_asr_decode --flagsfile=%s --logtostderr 1 --minloglevel 0""" % path_file
        process = Popen([inference_cmd],
                        stdin=PIPE, stdout=PIPE, stderr=PIPE,
                        shell=True, preexec_fn=os.setsid)