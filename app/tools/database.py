import ZODB, ZODB.FileStorage
import transaction

class BaseManager:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.storage = None
        self.db = None

    def _connect(self):
        if not self.storage:
            self.storage = ZODB.FileStorage.FileStorage(self.db_path)
        if not self.db:
            self.db = ZODB.DB(self.storage)
        return self.db.open()

    def write(self, key: str, obj):
        conn = self._connect()
        try:
            root = conn.root()
            root[key] = obj
            transaction.commit()
        finally:
            conn.close()

    def read(self, key: str):
        conn = self._connect()
        try:
            root = conn.root()
            return root.get(key)
        finally:
            conn.close()

    def remove(self, key: str):
        conn = self._connect()
        try:
            root = conn.root()
            if key in root:
                del root[key]
                transaction.commit()
        except Exception as e:
            transaction.abort()
            raise e
        finally:
            conn.close()

    def get_root(self):
        conn = self._connect()
        try:
            root = conn.root()
            return dict(root)
        finally:
            conn.close()

    def exists(self, key: str) -> bool:
        conn = self._connect()
        try:
            root = conn.root()
            return key in root
        finally:
            conn.close()

    def clear(self):
        conn = self._connect()
        try:
            root = conn.root()
            root.clear()
            transaction.commit()
        finally:
            conn.close()

    def count(self) -> int:
        conn = self._connect()
        try:
            root = conn.root()
            return len(root)
        finally:
            conn.close()

    def list_keys(self):
        conn = self._connect()
        try:
            root = conn.root()
            return list(root.keys())
        finally:
            conn.close()

    def close(self):
        if self.db:
            self.db.close()
            self.db = None
        if self.storage:
            self.storage.close()
            self.storage = None