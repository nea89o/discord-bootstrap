from ._bs.config import *


@section('discord')
class Config:
    token = required('token')
    admin = required('admin', int)
