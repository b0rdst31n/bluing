#!/usr/bin/env python

from xpycommon.log import INFO, DEBUG

from .. import PKG_NAME as PARENT_PKG_NAME, LOG_LEVEL as PARENT_LOG_LEVEL


PKG_NAME = '.'.join([PARENT_PKG_NAME, 'spoof']) 
LOG_LEVEL = PARENT_LOG_LEVEL
# LOG_LEVEL = DEBUG


from .__main__ import main

__all__ = ['main']