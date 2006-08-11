# **********************************************************************
#
# Copyright (c) 2003-2006 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

productName = "IceE"

blocking = " --Ice.Blocking "

testDefinitions = [
	(productName, "latency twoway", "latency", [
		("tpc", "twoway", ""),
		("tpc blocking", "twoway" + blocking, ""),
		]
	    ),
	(productName, "latency oneway", "latency", [
		("tpc", "oneway", ""),
		("tpc blocking", "oneway" + blocking, ""),
		]
	    ),
	(productName, "latency oneway batch", "latency", [
		("tpc (batch)", "batch", ""),
		("tpc blocking (batch)", "batch" + blocking, ""),
		]
	    ),
	(productName, "latency twoway with 2k payload", "latency", [
		("tpc", "twoway", "", [("payload", "2000")]),
		("tpc blocking", "twoway" + blocking, "", [("payload", "2000")]),
		]
	    ),
	(productName, "latency oneway with 2k payload", "latency", [
		("tpc", "oneway", "", [("payload", "2000")]),
		("tpc blocking", "oneway" + blocking, "", [("payload", "2000")]),
		]
	    ),
	(productName, "latency twoway with 10k payload", "latency", [
		("tpc", "twoway", "", [("payload", "10000")]),
		("tpc blocking", "twoway" + blocking, "", [("payload", "10000")]),
		]
	    ),
	(productName, "latency oneway with 10k payload", "latency", [
		("tpc", "oneway", "", [("payload", "10000")]),
		("tpc blocking", "oneway" + blocking, "", [("payload", "10000")]),
		]
	    ),
	(productName, "throughput byte", "throughput", [
		("tpc", "byte", ""),
		("tpc blocking", "byte" + blocking, ""),
		("tpc (w/o zero copy)", "byte noZeroCopy", ""),
		("tpc blocking (w/o zero copy)", "byte noZeroCopy" + blocking, ""),
		]
	    ),
	(productName, "throughput string sequence", "throughput", [
		("tpc", "stringSeq", ""),
		("tpc blocking", "stringSeq" + blocking, ""),
		]
	    ),
	(productName, "throughput long string sequence", "throughput", [
		("tpc", "longStringSeq", ""),
		("tpc blocking", "longStringSeq" + blocking, ""),
		]
	    ),
	(productName, "throughput struct sequence", "throughput", [
		("tpc", "structSeq", ""),
		("tpc blocking", "structSeq" + blocking, ""),
		]
	    ),
	]

#
# These tests have been removed from the main run because there is no
# corresponding equivalent in TAO.
#
unusedTests = [
	(productName, "latency oneway batch with 2k payload", "latency", [
		("tpc", "batch", "", [("payload", "2000")]),
		("tpc blocking", "batch" + blocking, "", [("payload", "2000")]),
		]
	    ),
	(productName, "latency oneway batch with 10k payload", "latency", [
		("tpc", "batch", "", [("payload", "10000")]),
		("tpc blocking", "batch" + blocking, "", [("payload", "10000")]),
		]
	    ),
	]

def getDefinitions():
    return testDefinitions
