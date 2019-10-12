# cut-ze-bullshit

Program to extract the essence from long videos.

cut-ze-bullshit takes a configuration file that specifies an input file
and a list of time segments.

It makes little video segments from the original video based on the 
time segments and then splices them all together. 
All the segments and the final video are created in the same directory
as the input file.

Here is a sample configuration file:

```
/Users/gigi.sayfan/Videos/my-awesome-video.mp4
12:34,12:39
14:50,16:33
20:00,56:22
```
 
## Usage 

`python cut-ze-bullshit.py <config file>`
