# ***********************************************************
# ******* WARNING: AUTOGENERATED! ALL EDITS WILL BE LOST ******
# *************************************************************
from __future__ import annotations

from typing import TYPE_CHECKING, Callable, ContextManager

from ._ki import LOCALS_KEY_KI_PROTECTION_ENABLED
from ._run import GLOBAL_RUN_CONTEXT

if TYPE_CHECKING:
    import select

    from .. import _core
    from .._file_io import _HasFileNo
    from ._traps import Abort, RaiseCancelT
import sys

assert not TYPE_CHECKING or sys.platform == "darwin"


def current_kqueue() -> select.kqueue:
    locals()[LOCALS_KEY_KI_PROTECTION_ENABLED] = True
    try:
        return GLOBAL_RUN_CONTEXT.runner.io_manager.current_kqueue()
    except AttributeError:
        raise RuntimeError("must be called from async context") from None


def monitor_kevent(
    ident: int, filter: int
) -> ContextManager[_core.UnboundedQueue[select.kevent]]:
    locals()[LOCALS_KEY_KI_PROTECTION_ENABLED] = True
    try:
        return GLOBAL_RUN_CONTEXT.runner.io_manager.monitor_kevent(ident, filter)
    except AttributeError:
        raise RuntimeError("must be called from async context") from None


async def wait_kevent(
    ident: int, filter: int, abort_func: Callable[[RaiseCancelT], Abort]
) -> Abort:
    locals()[LOCALS_KEY_KI_PROTECTION_ENABLED] = True
    try:
        return await GLOBAL_RUN_CONTEXT.runner.io_manager.wait_kevent(
            ident, filter, abort_func
        )
    except AttributeError:
        raise RuntimeError("must be called from async context") from None


async def wait_readable(fd: int | _HasFileNo) -> None:
    locals()[LOCALS_KEY_KI_PROTECTION_ENABLED] = True
    try:
        return await GLOBAL_RUN_CONTEXT.runner.io_manager.wait_readable(fd)
    except AttributeError:
        raise RuntimeError("must be called from async context") from None


async def wait_writable(fd: int | _HasFileNo) -> None:
    locals()[LOCALS_KEY_KI_PROTECTION_ENABLED] = True
    try:
        return await GLOBAL_RUN_CONTEXT.runner.io_manager.wait_writable(fd)
    except AttributeError:
        raise RuntimeError("must be called from async context") from None


def notify_closing(fd: int | _HasFileNo) -> None:
    locals()[LOCALS_KEY_KI_PROTECTION_ENABLED] = True
    try:
        return GLOBAL_RUN_CONTEXT.runner.io_manager.notify_closing(fd)
    except AttributeError:
        raise RuntimeError("must be called from async context") from None
