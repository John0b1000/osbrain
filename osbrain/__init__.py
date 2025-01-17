import os
from pathlib import Path

import Pyro4

Pyro4.config.SERIALIZERS_ACCEPTED.add('pickle')
Pyro4.config.SERIALIZERS_ACCEPTED.add('cloudpickle')
Pyro4.config.SERIALIZERS_ACCEPTED.add('dill')
Pyro4.config.SERIALIZER = 'cloudpickle'
Pyro4.config.THREADPOOL_SIZE = 16
Pyro4.config.SERVERTYPE = 'thread'
Pyro4.config.REQUIRE_EXPOSE = False
Pyro4.config.COMMTIMEOUT = 0.0
Pyro4.config.DETAILED_TRACEBACK = True

config = {}
config['SAFE'] = os.environ.get('OSBRAIN_DEFAULT_SAFE', 'true') != 'false'
config['SERIALIZER'] = os.environ.get('OSBRAIN_DEFAULT_SERIALIZER', 'pickle')
config['LINGER'] = float(os.environ.get('OSBRAIN_DEFAULT_LINGER', '1'))
# Set IPC by default only for POSIX systems
if os.name != 'posix':
    config['TRANSPORT'] = os.environ.get('OSBRAIN_DEFAULT_TRANSPORT', 'tcp')
    config['IPC_DIR'] = Path('')
else:
    config['TRANSPORT'] = os.environ.get('OSBRAIN_DEFAULT_TRANSPORT', 'ipc')
    # Set storage folder for IPC socket files
    config['IPC_DIR'] = (
        Path(os.environ.get('XDG_RUNTIME_DIR', Path.home())) / '.osbrain_ipc'
    )
    config['IPC_DIR'].mkdir(exist_ok=True, parents=True)


__version__ = '0.6.6'

from .address import AgentAddress  # isort:skip
from .address import SocketAddress  # isort:skip
from .agent import Agent  # isort:skip
from .agent import AgentProcess  # isort:skip
from .agent import run_agent  # isort:skip
from .logging import Logger  # isort:skip
from .logging import run_logger  # isort:skip
from .nameserver import NameServer  # isort:skip
from .nameserver import run_nameserver  # isort:skip
from .proxy import NSProxy  # isort:skip
from .proxy import Proxy  # isort:skip
