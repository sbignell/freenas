#!/usr/local/bin/python2.7
#
# Copyright (c) 2015 iXsystems, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS ``AS IS'' AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.
#
import argparse
import os
import sys

if '/usr/local/www' not in sys.path:
    sys.path.insert(0, '/usr/local/www')

from freenasUI.services.utils import SmartAlert


def event():
    device = os.environ.get('SMARTD_DEVICE')
    if device is None:
        return

    message = os.environ.get('SMARTD_MESSAGE')
    if message is None:
        return

    with SmartAlert() as sa:
        sa.message_add(device, message)


def remove(dev):
    if not dev.startswith('/dev/'):
        dev = '/dev/{0}'.format(dev)
    with SmartAlert() as sa:
        sa.device_delete(dev)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dev')
    parser.add_argument('-s')
    parser.add_argument('email', nargs='*')

    args = parser.parse_args()
    if args.dev:
        remove(args.dev)
    else:
        event()


if __name__ == '__main__':
    main()
