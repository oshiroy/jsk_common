#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

from nose.tools import assert_equal
from freezegun import freeze_time

from jsk_data.util import filename_with_timestamp


@freeze_time('1999-01-01 23:59:59')
def test_filename_with_timestamp():
    stamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    # originally no stamp
    filename = 'pr2-test-1.bag'
    expected = '_'.join([stamp, filename])
    assert_equal(expected, filename_with_timestamp(filename))
    # stamped
    filename = '2015-01-01-23-59-59-pr2-test-999.bag'
    assert_equal(filename, filename_with_timestamp(filename))
    # wrong formated stamp
    filename = '2015-01-01_23-59-59-pr2-test-999.bag'
    expected = '_'.join([stamp, filename])
    assert_equal(expected, filename_with_timestamp(filename))
