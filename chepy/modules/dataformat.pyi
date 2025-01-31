from ..core import ChepyCore as ChepyCore, ChepyDecorators as ChepyDecorators
from chepy.modules.internal.constants import Encoding as Encoding
from typing import Any, Union

yaml: Any

class DataFormat(ChepyCore):
    def __init__(self, *data: Any) -> None: ...
    state: Any = ...
    def eval_state(self): ...
    def bytes_to_ascii(self): ...
    def list_to_str(self, join_by: Union[str, bytes]=...) -> Any: ...
    def str_list_to_list(self): ...
    def join_list(self, by: Union[str, bytes]=...) -> Any: ...
    def json_to_dict(self): ...
    def dict_to_json(self): ...
    def yaml_to_json(self): ...
    def json_to_yaml(self): ...
    def base58_encode(self): ...
    def base58_decode(self): ...
    def base85_encode(self): ...
    def base85_decode(self): ...
    def base16_encode(self): ...
    def base16_decode(self): ...
    def base32_encode(self): ...
    def base32_decode(self): ...
    def to_int(self): ...
    def to_bytes(self): ...
    def from_bytes(self): ...
    def base64_encode(self, custom: str=...) -> Any: ...
    def base64_decode(self, custom: str=..., fix_padding: bool=...) -> Any: ...
    def decode_bytes(self, errors: str=...) -> Any: ...
    def to_hex(self): ...
    def from_hex(self): ...
    def hex_to_int(self): ...
    def hex_to_binary(self): ...
    def hex_to_str(self, ignore: bool=...) -> Any: ...
    def str_to_hex(self): ...
    def int_to_hex(self): ...
    def int_to_str(self): ...
    def binary_to_hex(self): ...
    def normalize_hex(self, is_bytearray: bool = ...): ...
    def str_from_hexdump(self): ...
    def to_hexdump(self): ...
    def from_hexdump(self): ...
    def url_encode(self, safe: str=...) -> Any: ...
    def url_decode(self): ...
    def bytearray_to_str(self, encoding: str=..., errors: str=...) -> Any: ...
    def str_to_list(self): ...
    def str_to_dict(self): ...
    def to_charcode(self, escape_char: str=...) -> Any: ...
    def from_charcode(self, prefix: str=...) -> Any: ...
    def to_decimal(self): ...
    def from_decimal(self): ...
    def to_binary(self): ...
    def from_binary(self): ...
    def to_octal(self): ...
    def from_octal(self): ...
    def to_html_entity(self): ...
    def from_html_entity(self): ...
    def to_punycode(self): ...
    def from_punycode(self): ...
    def encode_bruteforce(self): ...
    def decode_bruteforce(self): ...
    def to_braille(self): ...
    def from_braille(self): ...
    def trim(self): ...
