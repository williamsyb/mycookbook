###########################
# STEP 1 编译源代码
############################
FROM golang:alpine as builder
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories
RUN apk update && apk add --no-cache git ca-certificates tzdata && update-ca-certificates && apk add tree

RUN adduser -D -g '' appuser
ENV GOPROXY https://goproxy.io,direct
WORKDIR /app

# 先拷贝 go.mod 安装依赖项
# 这样改变源代码时，重新构建镜像，就不用重复拉取依赖项了(use cache)
COPY ./go.mod ./go.mod
RUN GO111MODULE=on go mod download
# 再拷贝源代码
COPY . .
RUN pwd && tree .

# 编译（尽量干掉 GOPATH）
# ENV GOPATH="$(pwd):$GOPATH"
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags="-w -s" -a -installsuffix cgo -o /go/bin/iris

############################
# STEP 2 构建执行镜像
############################
FROM scratch

# 导入 HTTPS 证书等
COPY --from=builder /usr/share/zoneinfo /usr/share/zoneinfo
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=builder /etc/passwd /etc/passwd

# 拷贝二进制
WORKDIR /app
COPY --from=builder /go/bin/iris /go/bin/iris

# 使用普通账户权限，不使用 root
USER appuser

# 服务端口
ENV PORT=8080

# 默认运行 adapter
#ENTRYPOINT ["/bin/bash"]
ENTRYPOINT ["/bin/sh","-c","['/go/bin/iris']"]
