FROM gcr.io/distroless/python3

ENV PYTHONUNBUFFERED=x

WORKDIR /

COPY . .

ENTRYPOINT [ "python3", "-u", "./driver.py" ]