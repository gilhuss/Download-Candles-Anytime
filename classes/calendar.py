import datetime

from tkcalendar import Calendar

from classes.button import Button
from classes.window import Window
from colors import *


class Calendar_(Window):
    def __init__(
        self, parent, title, command, min=(2019, 9, 8), pad=(20, 20), today=False
    ):
        super().__init__(parent, title=title)

        today_str = str(datetime.date.today())
        today_val = today_str.split("-")

        bg_color = background_color[self.theme]
        hd_color = header_color[self.theme]
        pr_color = primary_color[self.theme]
        t_color = font_color[self.theme]
        dis_color = button_color[self.theme]
        print(self.theme)

        self.cal = Calendar(
            self,
            year=min[0] if today is False else int(today_val[0]),
            month=min[1] if today is False else int(today_val[1]),
            day=min[2] if today is False else int(today_val[2]),
            selectmode="day",
            mindate=datetime.date(min[0], min[1], min[2]),
            maxdate=datetime.date.today(),
            date_pattern="dd-mm-yyyy",
            showweeknumbers=False,
            showothermonthdays=False,
            font=main_font,
            foreground=t_color,
            background=hd_color,
            normalforeground=t_color,
            normalbackground=bg_color,
            selectbackground=hd_color,
            selectforeground=pr_color,
            weekendforeground=t_color,
            weekendbackground=bg_color,
            headersforeground=t_color,
            headersbackground=bg_color,
            borderwidth=0,
            bordercolor=bg_color,
            disableddaybackground=bg_color,
            disableddayforeground=dis_color,
        )
        self.cal.config(background=bg_color)
        self.cal.pack(pady=pad, padx=pad)

        Button(self, text="Confirm", command=command)

        # self.current = Calendar(
        #     self,
        #     selectmode="day",
        #     date_pattern="dd-mm-yyyy",
        #     showweeknumbers=False,
        #     showothermonthdays=False,
        #     font=main_font,
        #     mindate=datetime.date(min[0], min[1], min[2]),
        #     maxdate=datetime.date.today(),
        #     foreground=background_color,
        #     headersforeground=background_color,
        #     normalforeground=font_color,
        #     weekendforeground=font_color,
        # )
        # self.current.pack(padx=pad, pady=pad)
        #
        # Button(self, text="Confirm", command=command)
