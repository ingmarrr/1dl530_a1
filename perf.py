
import os
import sys
import subprocess as sp

def main():

    os.system("echo '' > output/perf.txt")
    counter = 1
    for nr_threads in [1, 2, 4, 8, 16, 32]:
        for mb in [1, 2, 4, 8, 16, 32]:
            p = sp.Popen(['./bin/performance', F"{nr_threads}", F"{mb}"], stdout=sp.PIPE, stderr=sp.PIPE, stdin=sp.PIPE)
            stdout = p.stdout
            if stdout is None:
                print("Could not get stdout pipe.")
                return

            output = str(stdout.read())
            time = float(output.split(" ")[2])
            os.system(f"echo 'Iteration {counter} [Threads: {nr_threads}, Mb: {mb}]: {time}' >> output/perf.txt")
            counter += 1
            # os.system(f"./bin/performance {nr_threads} {mb} >> output/perf.txt")

if __name__ == '__main__':
    main()