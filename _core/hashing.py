from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():

    def bcrypt(password: str) -> str:
        return pwd_cxt.hash(password)

    def verify(password: str, hash: str) -> bool:
        return pwd_cxt.verify(hash, password)