package main

import (
	"flag"
	"fmt"
	"os"
	"os/exec"
	"regexp"
	"strconv"
	"strings"
)

func main() {
	var path string
	var smallgif string
	var maxedge int
	var maxsize int

	flag.StringVar(&path, "path", "", "path to the animated gif")
	flag.StringVar(&smallgif, "smallgif", "resize.gif", "path to smaller animated gif")
	flag.IntVar(&maxedge, "maxedge", 128, "Maximum edge length allowed")
	flag.IntVar(&maxsize, "maxsize", 65536, "Max file size allowed")
	flag.Parse()

	gi := NewGifInfo(path)
	gi.cons = ImgCon{128, 1024 * 64}
	err := gi.GetInfo()
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	curEdge := gi.cons.MaxEdge
	for ; curEdge >= 0; curEdge -= 4 {
		newgi, err := gi.Resize(curEdge)
		if err != nil {
			fmt.Println(err)
			os.Exit(1)
		}

		if newgi.width < gi.cons.MaxEdge &&
			newgi.height < gi.cons.MaxEdge &&
			newgi.fileInfo.Size() < int64(gi.cons.MaxSize) {
			err := os.Rename(newgi.path, smallgif)
			if err != nil {
				fmt.Println(err)
				os.Exit(1)
			}

			fmt.Println("Winner")
			break
		} else {
		}
		curEdge = curEdge - 1
	}

	os.Exit(0)
}

type ImgCon struct {
	MaxEdge int
	MaxSize int
}

type GifInfo struct {
	width    int
	height   int
	path     string
	fileInfo os.FileInfo
	resizeOn string
	cons     ImgCon
}

func NewGifInfo(path string) *GifInfo {
	gi := &GifInfo{}
	gi.path = path
	return gi
}

func (gi *GifInfo) Resize(edgeLen int) (*GifInfo, error) {
	resizeTmpFile := fmt.Sprintf("%s-resize-temp", gi.path)
	// fmt.Println(resizeTmpFile)

	cmdArr := []string{"-o", resizeTmpFile, gi.resizeOn, strconv.Itoa(edgeLen), gi.path}
	cmd := exec.Command("gifsicle", cmdArr...)
	out, err := cmd.CombinedOutput()

	if err != nil {
		fmt.Println(string(out))
		return &GifInfo{}, err
	}

	newgi := NewGifInfo(resizeTmpFile)
	err = newgi.GetInfo()
	if err != nil {
		return &GifInfo{}, err
	}

	return newgi, nil
}

func (gi *GifInfo) GetInfo() error {
	if fi, err := os.Stat(gi.path); os.IsNotExist(err) {
		return err
	} else {
		gi.fileInfo = fi
	}
	cmd := exec.Command("gifsicle", "-I", gi.path)

	out, err := cmd.CombinedOutput()
	if err != nil {
		return err
	}

	outs := strings.Split(string(out), "\n")
	sizere := regexp.MustCompile("([0-9]+)x([0-9]+)")

	for _, line := range outs {
		matches := sizere.FindStringSubmatch(line)
		if len(matches) == 3 {
			gi.width, err = strconv.Atoi(matches[1])
			gi.height, err = strconv.Atoi(matches[2])
			break
		}
	}

	if gi.width > gi.height {
		gi.resizeOn = "--resize-width"
	} else {
		gi.resizeOn = "--resize-height"
	}

	return nil
}
