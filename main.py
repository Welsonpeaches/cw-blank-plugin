from .ClassWidgets.base import PluginBase, SettingsBase, PluginConfig  # 导入CW的基类

from PyQt5 import uic
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QScrollArea, QWidget, QVBoxLayout, QScrollBar
from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation, QEasingCurve, pyqtSignal
from loguru import logger
import os
import csv
from datetime import datetime, timedelta
from PyQt5 import uic
from loguru import logger
from datetime import datetime
from qfluentwidgets import ComboBox, PrimaryPushButton, Flyout, InfoBarIcon, \
    FlyoutAnimationType
from qfluentwidgets import isDarkTheme



from PyQt5.QtWidgets import QHBoxLayout
from qfluentwidgets import ImageLabel, LineEdit

import json
from datetime import datetime, timedelta

widget_width = 999



class Settings(SettingsBase):  # 设置类
    def __init__(self, plugin_path, parent=None):  # 初始化
        super().__init__(plugin_path, parent)
        uic.loadUi(f'{self.PATH}/settings.ui', self)

        widget_width = self.nameEdit.text()
        WIDGET_WIDTH = widget_width
        logger.info(widget_width)



    # 其他代码……


WIDGET_CODE = 'blank.ui'  # 插件代号
WIDGET_NAME = '空|Blank'  # 您的插件显示的名称
WIDGET_WIDTH = widget_width


class Plugin(PluginBase, SettingsBase):  # 插件类
    def __init__(self, cw_contexts, method):  # 初始化
        super().__init__(cw_contexts, method)  # 调用父类初始化方法

        self.method = method
        self.method.register_widget(WIDGET_CODE, WIDGET_NAME, WIDGET_WIDTH)
        self.cfg = PluginConfig(self.PATH, 'config.json')  # 实例化配置类

    def update(self, cw_contexts):  # 自动更新部分
        super().update(cw_contexts)  # 调用父类更新方法
        self.cfg.update_config()



    def execute(self):  # 自启动执行部分



        logger.success('空白加载成功！本插件开发者：月下的桃子')
        logger.success('这个插件并没有什么用但是ci有我们也要有')


