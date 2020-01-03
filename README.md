# cut-ze-bullshit

Program to extract the essence from long videos.

cut-ze-bullshit takes a configuration file that specifies an input file
and a list of time segments.

It makes little video segments from the original video based on the 
time segments and then splices them all together. 
All the segments and the final video are created in the same directory
as the input file.

 
## Requirements

cut-ze-bullshit depends on [ffmpeg](https://ffmpeg.org) for all the heavy lifting. 
It uses a Docker image of ffmpeg, so there ino need to install ffmpeg. But, it
requires [Docker](https://www.docker.com)


## Configuration file

The first line of the configuration must contain the path to the source video.
Time segments are comma-separated pairs of <start time>,<end time>.

You can sprinkle comments freely by starting a line with #.

Empty lines are ignored.
 
Here is a sample configuration file:

```
/Users/gigi.sayfan/Videos/my-awesome-video.mp4

# the awsesome stuff
12:34,12:39
14:50,16:33
20:00,56:22
```
 
## Usage 

`python cut-ze-bullshit.py <config file>`

## Trivia

"Cut ze bullshit" is named after the famous Chinese phrase as quoted by Miri Regev:

[![Cut Ze Bullshit](http://img.youtube.com/vi/SNg5v8BqTdw/0.jpg)](http://www.youtube.com/watch?v=SNg5v8BqTdw "Cut Ze Bullshit")
