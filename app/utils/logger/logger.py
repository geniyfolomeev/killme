import json
import logging.config
from contextvars import ContextVar


LOG_LEVEL = "INFO"


REQUEST_ID_CTX = "request_id"

_request_id_ctx_var: ContextVar[str] = ContextVar(REQUEST_ID_CTX, default="")


def get_request_id() -> str:
    return _request_id_ctx_var.get()


class RequestIdFilter(logging.Filter):
    def filter(self, record):
        record.request_id = get_request_id()
        return True


class RequestIdFormatter(logging.Formatter):
    def format(self, record):
        record.message = record.getMessage()
        record.asctime = self.formatTime(record, self.datefmt)
        if request_id := get_request_id():
            record.message = f"[{request_id}] {record.message}"
        return json.dumps(
            {
                "ts": record.asctime,
                "level": record.levelname,
                "message": record.message,
            }
        )


LOGGING_CONFIG: dict = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "add_request_id": {
            "()": RequestIdFilter,
        },
    },
    "formatters": {
        "standart": {
            "()": RequestIdFormatter,
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "standart",
            "stream": "ext://sys.stdout",
            "level": LOG_LEVEL,
            "filters": ["add_request_id"],
        },
    },
    "loggers": {
        "uvicorn": {
            "level": LOG_LEVEL,
            "handlers": ["console"],
            "propagate": True,
        },
    },
}

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger("uvicorn")
