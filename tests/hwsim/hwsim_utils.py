#!/usr/bin/python
#
# hwsim testing utilities
# Copyright (c) 2013, Jouni Malinen <j@w1.fi>
#
# This software may be distributed under the terms of the BSD license.
# See README for more details.

import subprocess
import logging
logger = logging.getLogger(__name__)

def test_connectivity(ifname1, ifname2):
    cmd = ["sudo",
           "../../mac80211_hwsim/tools/hwsim_test",
           ifname1,
           ifname2]
    try:
        s = subprocess.check_output(cmd)
        logger.debug(s)
    except subprocess.CalledProcessError, e:
        print "hwsim failed: " + str(e.returncode)
        print e.output
        raise

def test_connectivity_p2p(dev1, dev2):
    ifname1 = dev1.group_ifname if dev1.group_ifname else dev1.ifname
    ifname2 = dev2.group_ifname if dev2.group_ifname else dev2.ifname
    test_connectivity(ifname1, ifname2)

def test_connectivity_sta(dev1, dev2):
    ifname1 = dev1.ifname
    ifname2 = dev2.ifname
    test_connectivity(ifname1, ifname2)
