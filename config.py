# import os
from pathlib import Path

# Application parameters
USER_NAME = 'Martini'
HOST = '127.0.0.1'
PORT = 8080

# File paths
# ROOT_DIR = os.path.dirname(__file__)
ROOT_DIR = Path(__file__).parent
# ASSETS_FOLDER = os.path.join(ROOT_DIR, 'assets')
ASSETS_FOLDER = ROOT_DIR / 'assets'
ASSETS_FOLDER.mkdir(parents=True, exist_ok=True)

# DB_ROOT = os.path.join(ASSETS_FOLDER, 'database')
DB_ROOT = ASSETS_FOLDER / 'database'
DB_ROOT.mkdir(parents=True, exist_ok=True)
DB_NAME = 'medassist'
# DB_PATH = os.path.join(DB_ROOT, DB_NAME + '.db')
DB_PATH = DB_ROOT / (DB_NAME + '.sqlite3')

# INDEX_ROOT = os.path.join(ASSETS_FOLDER, 'index')
INDEX_ROOT = ASSETS_FOLDER / 'index'
INDEX_ROOT.mkdir(parents=True, exist_ok=True)
INDEX_NAME = 'medassist'
# INDEX_PATH = os.path.join(INDEX_ROOT, INDEX_NAME + '.faiss')
INDEX_PATH = INDEX_ROOT / (INDEX_NAME + '.faiss')

# CHAT_HISTORY_FOLDER = os.path.join(ASSETS_FOLDER, 'chat_history')
CHAT_HISTORY_FOLDER = ASSETS_FOLDER / 'chat_history'
CHAT_HISTORY_FOLDER.mkdir(parents=True, exist_ok=True)
USER_CHAT_FILE = USER_NAME.lower() + '.txt'

EMBEDDING_MODEL = 'sentence-transformers/all-MiniLM-L6-v2'
# Parameters for creating vector index
CHUNK_SIZE = 500
CHUNK_OVERLAP = 20

# Parameters for LLM initialization
CHAT_BUFFER = 5
K=2
T=0.1
MAX_TOKENS = 512

OLLAMA_MODEL = 'llama3.1'
