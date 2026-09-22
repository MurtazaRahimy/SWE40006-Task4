FROM python:3.12-slim
WORKDIR /app
COPY wordstat.py .
RUN useradd -m appuser && mkdir /data && chown appuser /data
USER appuser
VOLUME /data
ENTRYPOINT ["python", "wordstat.py"]
