FROM gcr.io/distroless/python3

ENV PYTHONUNBUFFERED=x

ENTRYPOINT [ "python3", "-u" ]