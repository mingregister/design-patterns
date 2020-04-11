PKG_NAME = simple-factory

all: build run clean
.PHONY: all


build:
	go fmt
	go build
.PHONY: build

run:
	$(shell echo "############### 开始执行go命令 ###################")
	./${PKG_NAME}
	$(shell echo "############### go命令执行完成 ###################")
.PHONY: run


clean:
	rm -rf ${PKG_NAME} 
.PHONY: clean
	
