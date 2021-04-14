from ..core import ChepyCore as ChepyCore, ChepyDecorators as ChepyDecorators
from typing import Any

RSA: Any
OpenSSL: Any

class Publickey(ChepyCore):
    def __init__(self, *data: Any) -> None: ...
    state: Any = ...
    def parse_x509_pem(self): ...
    def parse_x509_der_hex(self): ...
    def public_from_x509(self): ...
    def pem_to_der_hex(self): ...
    def der_hex_to_pem(self): ...
    def parse_public_pem(self): ...
    def parse_private_pem(self): ...
    def dump_pkcs12_cert(self, password: str) -> Any: ...
