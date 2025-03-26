import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from logger import setup_logger

# Inicializa o logger
logger = setup_logger()

logger.info(
    f"teste 123456",
    extra={"tabela": "teste", "etapa": "extração"},
)