from typing import Optional
from typing_extensions import Literal
import logging

LogLevel = Optional[Literal['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']]
class Logger:
    
    def debug(self, message: str, *args, **kwargs) -> None:...
    def info(self, message: str, *args, **kwargs) -> None:...
    def warning(self, message: str, *args, **kwargs) -> None:...
    def error(self, message: str, exc_info: bool, *args, **kwargs) -> None:...
    def critical(self, message: str, *args, **kwargs) -> None:...
    def add_handler(self, handler: logging.Handler):...
    @classmethod
    def set_level(cls, level: LogLevel):...