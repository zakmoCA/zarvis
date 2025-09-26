import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("missing OPENAI_API_KEY in /.env")

BRAIN_DIR      = os.getenv("BRAIN_DIR", "./data")
EMBED_MODEL    = os.getenv("EMBED_MODEL", "text-embedding-3-small")
EMBED_DIM      = int(os.getenv("EMBED_DIM", "1536"))

CHUNK_SIZE     = int(os.getenv("CHUNK_SIZE", "800"))
CHUNK_OVERLAP  = int(os.getenv("CHUNK_OVERLAP", "120"))

TOP_K          = int(os.getenv("TOP_K", "8")) 