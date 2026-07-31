FROM astral/uv:python3.12-bookworm-slim
# FROM python:3.12.11-slim-bookworm

# RUN pip install uv
# COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
ENV PATH="/app/.venv/bin:$PATH"

WORKDIR /app

COPY ".python-version" "uv.lock" "pyproject.toml" ./

RUN uv sync --locked

COPY "predict.py" "model.bin" ./

EXPOSE 9696

ENTRYPOINT ["uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "9696", "--reload"]