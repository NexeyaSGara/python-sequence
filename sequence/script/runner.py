# -*- coding: utf-8 -*-

""" Main module for the block sequence editor """

#-------------------------------------------------------------------------------
# Name:        BlockSequenceEditor
# Purpose:     Main module for the sequence diagram editor
#
# Author:      michel.vincent
#
# Created:     21/10/2013
# Copyright:   (c) michel.vincent 2013
# Licence:     GPL
#-------------------------------------------------------------------------------

import os, sys
from PyQt4 import QtGui, QtCore
from sequence.widget.runner.runner import RunnerWidget


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ui = RunnerWidget()
    if len(sys.argv)>1 :
        filename = sys.argv[1]
        ui.set_filename(filename)
    ui.setWindowTitle("PySequence Runner")
    ui.show()
    sys.exit(app.exec_())
