#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: AM_receive
# Generated: Mon May 11 13:08:54 2020
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import zeromq
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import sip
import sys


class am_receive(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "AM_receive")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("AM_receive")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "am_receive")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.volume = volume = 300e-3
        self.samp_rate = samp_rate = 1e6
        self.decim = decim = 8

        ##################################################
        # Blocks
        ##################################################
        self._volume_range = Range(0, 1, 50e-3, 300e-3, 200)
        self._volume_win = RangeWidget(self._volume_range, self.set_volume, "volume", "counter_slider", float)
        self.top_layout.addWidget(self._volume_win)
        self.zeromq_sub_source_0 = zeromq.sub_source(gr.sizeof_float, 1, "tcp://127.0.0.1:50001", 100, False, -1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	256, #size
        	int(samp_rate/decim), #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_fcf(decim, (firdes.low_pass(1,samp_rate, (samp_rate/(2*decim)), 2000)), 48e3, samp_rate)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((volume, ))
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        self.band_pass_filter_0 = filter.fir_filter_fff(1, firdes.band_pass(
        	1, samp_rate/decim, 500, 6000, 400, firdes.WIN_HAMMING, 6.76))
        self.audio_sink_0 = audio.sink(48000, "", True)
        self.analog_agc_xx_0 = analog.agc_cc(625e-6, 1.0, 1.0)
        self.analog_agc_xx_0.set_max_gain(65536)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc_xx_0, 0), (self.blocks_complex_to_mag_0, 0))    
        self.connect((self.band_pass_filter_0, 0), (self.audio_sink_0, 0))    
        self.connect((self.band_pass_filter_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_complex_to_mag_0, 0), (self.band_pass_filter_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.analog_agc_xx_0, 0))    
        self.connect((self.zeromq_sub_source_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "am_receive")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume
        self.blocks_multiply_const_vxx_0.set_k((self.volume, ))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate/self.decim, 500, 6000, 400, firdes.WIN_HAMMING, 6.76))
        self.freq_xlating_fir_filter_xxx_0.set_taps((firdes.low_pass(1,self.samp_rate, (self.samp_rate/(2*self.decim)), 2000)))
        self.qtgui_time_sink_x_0.set_samp_rate(int(self.samp_rate/self.decim))

    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate/self.decim, 500, 6000, 400, firdes.WIN_HAMMING, 6.76))
        self.freq_xlating_fir_filter_xxx_0.set_taps((firdes.low_pass(1,self.samp_rate, (self.samp_rate/(2*self.decim)), 2000)))
        self.qtgui_time_sink_x_0.set_samp_rate(int(self.samp_rate/self.decim))


def main(top_block_cls=am_receive, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
