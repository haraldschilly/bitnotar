#!/usr/bin/env python
# -*- coding: utf8 -*-
# This is a scipt to run this notary system locally

def _clargs():
  '''
  Reads the commandline arguments and returns the desired settings and activities.
  '''
  from notary import verify_services
  from optparse import OptionParser
  parser = OptionParser(description = """This is a notary service, that either verifys the existance at 
  a given point in time using the Bitcoin blockchain, or it generates a Bitcoin address, where a small amount
  needs to be sent to in order to testify the existance of such a document.""",
  epilog = "Source: http://github.com/bitcoinaustria/bitnotar/")
  parser.add_option('-c', '--verify',  dest = "verify",  help = "verify this file", metavar = "FILE")
  parser.add_option('-t', '--testify', dest = "testify", help = "create a proof to testify that this file exists", metavar = "FILE")
  parser.add_option('-s', '--service', dest = "service", 
    help=("use given service for verification. known: %s" % verify_services) + ". (default: %default)",
    default = verify_services[0])
  parser.add_option('-v', dest = "verbose", action = "store_true", help = "verbose")
  config, _ = parser.parse_args()

  if config.verify is None and config.testify is None:
    parser.print_help()
    import sys; sys.exit(1)

  if config.service not in verify_services:
    print "ERROR: given service '%s' is not known" % config.service
    import sys; sys.exit(1)

  return config

if __name__ == "__main__":
  config = _clargs()
  if config.verbose: print config
  import notary
  if config.testify:
    notary.testify(config.testify)
  if config.verify:
    notary.verify(config.verify)
