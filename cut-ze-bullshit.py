import os
import sys
import subprocess


def make_segment(input_file, start_time, duration, segment):
    """ """
    cmd = f"""docker run --rm 
             -v {os.getcwd()}:/data -w /data 
             jrottenberg/ffmpeg -i {input_file}
             -ss {start_time}
             -t  {duration}
             {segment}
             """.split()
    subprocess.check_call(cmd)


def splice_segments(segments, output_file):
    """ """
    files = '\n'.join(f"file '{s}'" for s in segments)
    open('files.txt', 'w').write(files)
    cmd = f"""docker run --rm 
             -v {os.getcwd()}:/data -w /data 
             jrottenberg/ffmpeg -f concat -safe 0
             -i files.txt
             -c copy
             {output_file}""".split()
    subprocess.check_call(cmd)


def read_config(config_filename):
    """Read the config file

    Return the input filename and a list of segments times

    Each time segment is a pair (start_time, duration) in seconds

    The format of the input file is:

    input_filename
    start_time_1,end_time_1
    start_time_2,end_time_2
    .
    .
    .
    start_time_N,end_time_N

    You may comment out lines with #

    """

    def time2seconds(t):
        components = t.split(':')
        seconds = 0
        for i, c in enumerate(components):
            seconds += int(c) * 60 ** (len(components) - i - 1)
        return seconds

    lines = open(config_filename).read().split('\n')
    input_file = lines[0]
    segment_times = []
    for line in lines[1:]:
        if line.startswith('#') or line == '':
            continue
        times = [time2seconds(x) for x in line.split(',')]
        duration = times[1] - times[0]
        if duration <= 0:
            raise RuntimeError('Start time > end time: ', line)
        segment_times.append((times[0], duration))

    return input_file, segment_times


def main():
    """ """
    if len(sys.argv) != 2:
        print('Usage: python cut-ze-bullshit.py <config_file>')
        sys.exit(1)

    input_file, segment_times = read_config(sys.argv[1])
    basedir = os.path.dirname(input_file)
    os.chdir(basedir)
    basename, ext = os.path.splitext(input_file)
    base = basename.split('/')[-1]
    # Now use local filename
    input_file = os.path.split(input_file)[-1]
    segments = []
    for i, segment_time in enumerate(segment_times):
        start_time, duration = segment_time
        print(f'Processing segment {i + 1}/{len(segment_times)}, duration: {duration} seconds...')
        segment = f'{base}-{i + 1}{ext}'
        segments.append(segment)
        if os.path.isfile(segment):
            continue
        make_segment(input_file, start_time, duration, segment)

    output_file = f'{base}.cut-ze-bullshit{ext}'
    splice_segments(segments, output_file)


if __name__ == '__main__':
    main()
