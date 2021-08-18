# coding=utf-8
""""Wrapper fo Data Plotly plot_layout_item module.

.. note:: This program is free software; you can redistribute it and/or modify
    it under the terms of the Mozilla Public License 2.0.

"""

__author__ = 'lorenzetti@gis3w.it'
__date__ = '2021-08-18'
__copyright__ = 'Copyright 2015 - 2021, Gis3w'

from qdjango.apps import QGS_APPLICATION
from qplotly.vendor.DataPlotly.layouts.plot_layout_item import PlotLayoutItemMetadata

class QplotlyLayoutItemMetadata(PlotLayoutItemMetadata):
    pass


QGS_APPLICATION.layoutItemRegistry().addLayoutItemType(QplotlyLayoutItemMetadata())