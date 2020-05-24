#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author: Ssfanli
@Time  : 2020/05/24 2:57 下午
@Desc  : demo test
"""

from prepare_wda import prepare
import time
import wda


@prepare('xcodebuild', './WebDriverAgent', '00008020-001D1D900CB9002E')
def open_ysp(_bundle_id):

    cli = wda.Client('http://localhost:8100')
    cli.session(_bundle_id, alert_action='accept')
    if cli(label='跳过').exists:
        cli(label='跳过').click()
    w, h = cli.window_size()
    print(f'width = {w}, height = {h}')
    time.sleep(1)
    cli(label='我的').click()


if __name__ == '__main__':
    bundle_id = 'com.cctv.yangshipin.app.iphone'
    open_ysp(bundle_id)
