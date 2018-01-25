import os

import wx
import wx.grid

import Main

NUMBER_EXP_CUTOFF = 6
GUI_DIMENSIONS = (600, 700)


def format_number(n, _pow):
    return str(n) if n < 10 ** _pow else "{:.5e}".format(n)


def write_buildings_status(buildings):
    os.system("cls")
    print("{:10}{:10}{:15}{:15}{:10}".format("NAME", "COUNT", "COST", "REWARD", "TIME"))
    for k, v in sorted(buildings.items(), key=lambda b: b[1].id):
        print("{:10}{:<10}{:<15}{:<15}{:<10}".format(k, v.count, format_number(v.cost(), NUMBER_EXP_CUTOFF),
                                                     format_number(v.generate_reward(), NUMBER_EXP_CUTOFF),
                                                     v.base_timer))


def initialise_gui(buildings_dict):
    app = wx.App()
    frm = BuildingsFrame(None, title="Test")
    frm.buildings = buildings_dict
    frm.create_buttons()
    frm.Show()
    app.MainLoop()


# FIX
def initialise_input():
    while True:
        myint = input("Here >")


class BuildingsFrame(wx.Frame):
    REFRESH_RATE = 1000
    SPACING_HOR = 75
    SPACING_VER = 25
    ANCHOR_POS = (25, 25)
    PANEL_SIZE = (400, 400)
    TEXT_SPACING = 5
    SPACING_WIDGET = 15
    SPACING_BUTTONS = 0

    # Needed for now
    initial_resize = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.buildings = dict()
        self.buttons_purchase = []

        self.pnl_display = wx.Panel(self)

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update_buildings, self.timer)
        self.Bind(wx.EVT_TIMER, self.update_buttons, self.timer)
        self.Bind(wx.EVT_TIMER, self.update_status_bar, self.timer)

        # Status bar
        self.CreateStatusBar()

        # Building columns
        self.col_txt_buildings_name = wx.StaticText(self.pnl_display, label="Hello World!", pos=self.ANCHOR_POS)
        self.col_txt_buildings_count = wx.StaticText(self.pnl_display, label="Hello World!",
                                                     pos=(
                                                         self.ANCHOR_POS[0] + self.SPACING_HOR * 1, self.ANCHOR_POS[1]))
        self.col_txt_buildings_cost = wx.StaticText(self.pnl_display, label="Hello World!",
                                                    pos=(self.ANCHOR_POS[0] + self.SPACING_HOR * 2, self.ANCHOR_POS[1]))
        self.col_txt_buildings_reward = wx.StaticText(self.pnl_display, label="Hello World!",
                                                      pos=(self.ANCHOR_POS[0] + self.SPACING_HOR * 3,
                                                           self.ANCHOR_POS[1]))
        self.col_txt_buildings_time = wx.StaticText(self.pnl_display, label="Hello World!",
                                                    pos=(self.ANCHOR_POS[0] + self.SPACING_HOR * 4, self.ANCHOR_POS[1]))

        self.timer.Start(self.REFRESH_RATE)

        # Building column sizer
        sizer_building_cols = wx.BoxSizer(wx.HORIZONTAL)
        sizer_building_cols.Add(self.col_txt_buildings_name, 0, wx.ALL, self.SPACING_WIDGET)
        sizer_building_cols.Add(self.col_txt_buildings_count, 0, wx.ALL, self.SPACING_WIDGET)
        sizer_building_cols.Add(self.col_txt_buildings_cost, 0, wx.ALL, self.SPACING_WIDGET)
        sizer_building_cols.Add(self.col_txt_buildings_reward, 0, wx.ALL, self.SPACING_WIDGET)
        sizer_building_cols.Add(self.col_txt_buildings_time, 0, wx.ALL, self.SPACING_WIDGET)

        # Frame sizer
        self.sizer_top = wx.BoxSizer(wx.VERTICAL)
        self.sizer_top.Add(sizer_building_cols)
        self.pnl_display.SetSizer(self.sizer_top)
        self.sizer_top.Fit(self)

    def create_buttons(self):
        sizer_purchase_buttons = wx.BoxSizer(wx.VERTICAL)

        i = 0
        for k, v in sorted(self.buildings.items(), key=lambda b: b[1].id):
            btn = wx.Button(self.pnl_display, label=k, name=k,
                            pos=(self.ANCHOR_POS[0], self.ANCHOR_POS[1] + self.SPACING_VER * i))
            btn.Bind(wx.EVT_BUTTON, lambda evt, btn_name=k: self.purchase_building(evt, btn_name))
            sizer_purchase_buttons.Add(btn, 0, wx.ALL, self.SPACING_BUTTONS)
            self.buttons_purchase.append(btn)

            i += 1

        self.sizer_top.Add(sizer_purchase_buttons, 0, wx.ALL, self.SPACING_WIDGET)

    def purchase_building(self, event, button):
        self.buildings[button].count += 1
        Main.reduce_money(self.buildings[button].cost())
        print(Main.get_money())

        self.update_buttons(event)
        self.update_buildings(event)
        self.update_status_bar(event)

    def update_buttons(self, event):
        for b in self.buttons_purchase:
            if self.buildings[b.Name].cost() > Main.get_money():
                b.Disable()
            else:
                b.Enable()

        event.Skip()

    def update_buildings(self, event):
        content_name = "NAME\n"
        content_count = "COUNT\n"
        content_cost = "COST\n"
        content_reward = "REWARD\n"
        content_time = "TIME\n"

        for k, v in sorted(self.buildings.items(), key=lambda b: b[1].id):
            content_name += k + "\n"
            content_count += str(v.count) + "\n"
            content_cost += format_number(v.cost(), NUMBER_EXP_CUTOFF) + "\n"
            content_reward += format_number(v.generate_reward(), NUMBER_EXP_CUTOFF) + "\n"
            content_time += str(v.base_timer) + "\n"

        self.col_txt_buildings_name.SetLabelText(content_name)
        self.col_txt_buildings_count.SetLabelText(content_count)
        self.col_txt_buildings_cost.SetLabelText(content_cost)
        self.col_txt_buildings_reward.SetLabelText(content_reward)
        self.col_txt_buildings_time.SetLabelText(content_time)

        if self.initial_resize:
            self.sizer_top.Fit(self)
            self.initial_resize = False

        event.Skip()

    def update_status_bar(self, event):
        self.SetStatusText("Money: ${}".format(Main.get_money()))

        event.Skip()
