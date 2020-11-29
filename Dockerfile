FROM python:3-slim
WORKDIR /src
COPY requirements.txt .
RUN python -m pip install -r requirements.txt
COPY setup.py setup.cfg project.toml ./
COPY fad ./fad
RUN python -m pip install .
EXPOSE 5000

CMD ["fad"]
