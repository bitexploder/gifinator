mac:
	GOOS=darwin GOARCH=amd64 go build -o bin/gifinator_mac_amd64 gifinator.go
win:
	GOOS=windows GOARCH=amd64 go build -o bin/gifinator_amd64.exe gifinator.go
linux:
	GOOS=linux GOARCH=amd64 go build -o bin/gifinator_lin_amd64 gifinator.go

all: mac win linux
