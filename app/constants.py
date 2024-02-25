from fastapi.templating import Jinja2Templates

templates = Jinja2Templates("templates")

APP_NAME = "ls-srt-qa-metrics-api"
WARDEN_HOST_TEMPLATE = "warden.platform.{env}.s.o3.ru:82"
