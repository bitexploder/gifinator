# Gifinator

Ever wanted to turn an animated Gif into a Slack emoji? 

This tool is for you. Automate the tedious process of resizing an animated gif and tweaking things in tools like [ezgif](http://ezgif.com)

Note: There are several other gifinators out there. This one is mine.

Copyright notice: I have no idea who owns the copyright on the gifs in test-img. They aren't mine. If they are yours and you don't want them in this repo, let me know. 

# Installation

You will need `gifsicle` available on your `PATH`

On Apt-based systems: `apt-get install gifsicle` 

On Mac: `brew install gifsicle`

On Windows: Find a windows binary release of gifsicle and make sure they are on your path.

For Go developers:

`go get -u github.com/bitexploder/gifinator` and do the usual `go install`

For everyone else: [Binary Releases](https://github.com/bitexploder/gifinator/releases)

# Example

[![asciicast](https://asciinema.org/a/108664)](https://asciinema.org/a/108664)

# Usage 

`gifinator -url http://example.com/animated.gif` -> outputs `/tmp/resize.gif`
`gifinator -path /some/animated/image.gif` -> outputs `/tmp/resize.gif`
`gifinator -url http://example.com/animated.gif -smallgif /some/other/path/file.gif` -> outputs `/some/other/path/file.gif`

Use path or url, but not both. Path is for local file system. Url is for an HTTP URL.

The default constraints are designed to make gifs suitable for uploading to [Slack](https://slack.com). 

Other constraints can be specified (`-maxedge` and `-maxsize`)

The gif will be resized until it matches both constraints. It will be resized on its longest edge. 

Example: if the gif is 400x200 (WxH) it will be resized by width, maintaining aspect ratio. 


**Command Usage**

~~~~~
Usage of gifinator:
  -maxedge int
        Maximum edge length allowed (default 128)
  -maxsize int
        Max file size allowed (default 65536)
  -path string
        path to the animated gif
  -smallgif string
        path to smaller animated gif (default "/tmp/resize.gif")
  -url string
        url for animated gif
~~~~~
