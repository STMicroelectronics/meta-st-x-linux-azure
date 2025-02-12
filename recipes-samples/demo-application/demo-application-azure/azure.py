#!/usr/bin/python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import Pango
import os
from time import time
import subprocess

# -------------------------------------------------------------------
# -------------------------------------------------------------------
ICON_SIZE_1080 = 260
ICON_SIZE_720 = 160
ICON_SIZE_480 = 160
ICON_SIZE_272 = 48

# return format:
# [ icon_size, font_size ]
SIZES_ID_ICON_SIZE = 0
SIZES_ID_FONT_SIZE = 1
def get_sizes_from_screen_size(width, height):
    minsize =  min(width, height)
    icon_size = None
    font_size = None
    if minsize == 720:
        icon_size = ICON_SIZE_720
        font_size = 25
    elif minsize == 480:
        icon_size = ICON_SIZE_480
        font_size = 20
    elif minsize == 272:
        icon_size = ICON_SIZE_272
        font_size = 10
    elif minsize == 600:
        icon_size = ICON_SIZE_720
        font_size = 15
    elif minsize >= 1080:
        icon_size = ICON_SIZE_1080
        font_size = 32
    return [icon_size, font_size]

def get_icon_size_from_screen_size(width, height):
    minsize =  min(width, height)
    if minsize == 720:
        return ICON_SIZE_720
    elif minsize == 480:
        return ICON_SIZE_480
    elif minsize == 272:
        return ICON_SIZE_272
    elif minsize == 600:
        return ICON_SIZE_1080
    elif minsize >= 1080:
        return ICON_SIZE_1080

class NetworkPage(Gtk.VBox):
    def __init__(self):
        Gtk.VBox.__init__(self, homogeneous=False, spacing=0)
        self.set_border_width(5)

        self.scrolled_network = Gtk.ScrolledWindow()
        self.scrolled_network.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self.scrolled_network.set_vexpand(True)

        self.button_refresh_ip = Gtk.Button.new_with_label("Refresh")
        self.button_refresh_ip.connect("clicked", self._on_refresh_button_clicked)

        self.network_info_grid = Gtk.Grid()
        self.network_info_grid.set_column_spacing(2)
        self.network_info_grid.set_row_spacing(2)

        self.network_interfaces = []
        network_interface_names = self._get_network_interface_names("end") + self._get_network_interface_names("wlan")

        position_in_grid = 1
        for network_interface_name in network_interface_names:
            label = Gtk.Label()
            label.set_max_width_chars(20)
            label.set_xalign (0.0)
            label.set_hexpand(True)
            label.set_line_wrap(True)
            self.network_interfaces.append((network_interface_name, label))
            self.network_info_grid.attach(label, 0, position_in_grid, 1, 1)
            position_in_grid = position_in_grid + 1

        self.scrolled_network.add(self.network_info_grid)

        self.network_grid = Gtk.Grid()
        self.network_grid.set_column_spacing(2)
        self.network_grid.set_row_spacing(2)

        self.network_grid.attach(self.scrolled_network, 0, 1, 2, 1)
        self.network_grid.attach(self.button_refresh_ip,  0, 2, 1, 1)

        self.add(self.network_grid)

        self.refresh()

    def _get_network_interface_names(self, name):
        network_interface = []
        command = f'ip a | grep -o {name}[0-9]'
        ret = subprocess.run(command, shell=True, capture_output=True)
        if ret.returncode == 0:
            network_interface = list(dict.fromkeys(ret.stdout.decode('utf-8').splitlines()))
        return network_interface

    def _on_refresh_button_clicked(self, button):
        print('"Refresh ip" button was clicked')
        self.refresh()

    def refresh(self):
        for network_interface in self.network_interfaces:
            name, label = network_interface

            ip = os.popen(f"ip -4 addr show {name} | grep -oP '(?<=inet\s)\d+(\.\d+){{3}}'").read().strip()
            label.set_text(f"{name}: " + ip)

class ConfigPage(Gtk.VBox):
    def __init__(self):
        Gtk.VBox.__init__(self, homogeneous=False, spacing=0)
        self.set_border_width(5)

        self.scrolled_window = Gtk.ScrolledWindow()
        self.scrolled_window.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self.scrolled_window.set_vexpand(True)

        self.button_refresh = Gtk.Button.new_with_label("Refresh")
        self.button_refresh.connect("clicked", self._on_refresh_button_clicked)

        self.label_config = Gtk.Label()
        self.label_config.set_max_width_chars(20)
        self.label_config.set_xalign (0.0)
        self.label_config.set_hexpand(True)
        self.label_config.set_ellipsize(Pango.EllipsizeMode.END)
        self.label_config.set_line_wrap(True)
        self.label_config.set_line_wrap_mode(Pango.WrapMode.WORD_CHAR)
        self.scrolled_window.add(self.label_config)

        self.grid = Gtk.Grid()
        self.grid.set_column_spacing(2)
        self.grid.set_row_spacing(2)

        self.grid.attach(self.scrolled_window, 0, 1, 2, 1)
        self.grid.attach(self.button_refresh,  0, 2, 1, 1)

        self.add(self.grid)

        self.refresh()

    def _on_refresh_button_clicked(self, button):
        print('"Refresh config" button was clicked')
        self.refresh()

    def refresh(self):
        file = "/etc/aziot/config.toml"
        try:
            f = open(file, 'r')
            config = f"File: {file}\n\n" + str(f.read())
            self.label_config.set_text(config)
        except:
            config = f"Error reading file: {file}\n\n"
            self.label_config.set_text(config)
                

class ModulePage(Gtk.VBox):
    def __init__(self):
        Gtk.VBox.__init__(self, homogeneous=False, spacing=0)
        self.set_border_width(5)

        self.scrolled_window = Gtk.ScrolledWindow()
        self.scrolled_window.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self.scrolled_window.set_vexpand(True)

        self.button_refresh = Gtk.Button.new_with_label("Refresh")
        self.button_refresh.connect("clicked", self._on_refresh_button_clicked)

        self.button_restart = Gtk.Button.new_with_label("Restart")
        self.button_restart.connect("clicked", self._on_restart_button_clicked)

        self.label_modules = Gtk.Label()
        self.label_modules.set_max_width_chars(20)
        self.label_modules.set_xalign (0.0)
        self.label_modules.set_max_width_chars(20)
        self.label_modules.set_hexpand(True)
        self.label_modules.set_ellipsize(Pango.EllipsizeMode.END)
        self.label_modules.set_line_wrap(True)
        self.label_modules.set_line_wrap_mode(Pango.WrapMode.WORD_CHAR)

        # Select a monospaced font
        pango_font = Pango.FontDescription("Menlo")
        self.label_modules.modify_font(pango_font)

        self.scrolled_window.add(self.label_modules)

        self.grid = Gtk.Grid()
        self.grid.set_column_spacing(2)
        self.grid.set_row_spacing(2)

        self.grid.attach(self.scrolled_window, 0, 1, 2, 1)
        self.grid.attach(self.button_refresh,  0, 2, 1, 1)
        self.grid.attach(self.button_restart,  1, 2, 1, 1)

        self.add(self.grid)

        self.refresh()

    def _on_refresh_button_clicked(self, button):
        print('"Refresh modules" button was clicked')
        self.refresh()

    def _on_restart_button_clicked(self, button):
        print('"Restart modules" button was clicked')
        self.restart()

    def refresh(self):
        modules = os.popen("sudo iotedge list").read()
        self.label_modules.set_text(modules)

    def restart(self):
        self.refresh()
        os.popen("sudo iotedge system restart").read()
        self.refresh()

class AzureIotEdge(Gtk.Dialog):
    def __init__(self, parent, log=0):
        Gtk.Dialog.__init__(self, "AzureIotEdge", parent, 0, title="Simple Notebook Example")
        self.log = log

        self.maximize()
        try:
            display = Gdk.Display.get_default()
            monitor = display.get_primary_monitor()
            geometry = monitor.get_geometry()
            scale_factor = monitor.get_scale_factor()
            self.screen_width = scale_factor * geometry.width
            self.screen_height = scale_factor * geometry.height
        except:
            self.screen_width = self.get_screen().get_width()
            self.screen_height = self.get_screen().get_height()

        self.icon_size = get_icon_size_from_screen_size(self.screen_width, self.screen_height)
        sizes = get_sizes_from_screen_size(self.screen_width, self.screen_height)
        self.font_size = sizes[SIZES_ID_FONT_SIZE]

        self.set_decorated(False)
        rgba = Gdk.RGBA(0.31, 0.32, 0.31, 0.8)
        self.override_background_color(0,rgba)

        mainvbox = self.get_content_area()

        # Enable double click to close page

        self.previous_click_time=0
        self.connect("button-release-event", self.on_page_press_event)

        # Create Notebook with tabs
        self.notebook = Gtk.Notebook()

        self.page_config = ConfigPage()
        self.notebook.append_page(self.page_config, Gtk.Label(label="Config"))

        self.page_modules = ModulePage()
        self.notebook.append_page(self.page_modules, Gtk.Label(label="Modules"))

        self.page_network = NetworkPage()
        self.notebook.append_page(self.page_network, Gtk.Label(label="LAN"))

        # Display title

        self.title = Gtk.Label()
        self.title.set_markup(f"<span font='{self.font_size + 5}' color='#FFFFFFFF'><b>Azure Iot Edge</b></span>")

        # Create main grid

        self.main_grid = Gtk.Grid()
        self.main_grid.attach(self.title,  0, 1, 1, 1)
        self.main_grid.attach(self.notebook,  0, 2, 1, 1)

        mainvbox.pack_start(self.main_grid, False, True, 3)
        self.show_all()

    def on_page_press_event(self, widget, event):
        self.click_time = time()
        #print(self.click_time - self.previous_click_time)
        # TODO : a fake click is observed, workaround hereafter
        if (self.click_time - self.previous_click_time) < 0.01:
            self.previous_click_time = self.click_time
        elif (self.click_time - self.previous_click_time) < 0.3:
            print ("double click : exit")
            self.destroy()
        else:
            #print ("simple click")
            self.previous_click_time = self.click_time

def create_subdialogwindow(parent, log=0):
    _window = AzureIotEdge(parent, log=log)
    _window.show_all()
    response = _window.run()
    _window.destroy()
