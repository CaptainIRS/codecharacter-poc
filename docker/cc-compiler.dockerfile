FROM alpine:latest

RUN apk add --update --no-cache gcc

ENTRYPOINT [ "gcc" ]