GO_PKG                  = command
GO_BUILD_RECIPE         = GOOS=linux go build

all: build run clean
.PHONY: all


build:
	go fmt
	$(GO_BUILD_RECIPE)
.PHONY: build

run:
	$(shell echo "############### 开始执行go命令 ###################")
	./${GO_PKG}
	$(shell echo "############### go命令执行完成 ###################")
.PHONY: run


clean:
	rm -rf ${GO_PKG} 
.PHONY: clean
	
