#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__PROJECT_NAME__ = r"pre-wda"
__AUTHOR__ = r"ssfanli"
__AUTHOR_EMAIL__ = r"freedomlidi@163.com"
__LICENSE__ = r"MIT"
__URL__ = r"https://github.com/ssfanli/pre-wda.git"
__VERSION__ = r"0.0.1"
__DESCRIPTION__ = r"a python wrapper for WebDriverAgent prepare"

import os
import functools
from loguru import logger


def pre_wda(xcodebuild: str, wda_fp: str, udid: str):
    """wda.sh path
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logger.info(
                f'\nxcodebuild: {xcodebuild}'
                f'\nwda_fp: {wda_fp}'
                f'\nudid: {udid}'
            )
            try:
                error_code = os.system(f'wda.sh {xcodebuild} {wda_fp} {udid}')
                assert not error_code, f'wda.sh error_code: {error_code}'
                return func(*args, **kwargs)
            except Exception as e:
                logger.error(e)
        return wrapper
    return decorator
