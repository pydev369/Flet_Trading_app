
# * PS E:\ProJECTS\VScode Env> cd "E:\ProJECTS\VScode Env\.vscode\pythoonic_app_dev\Flet\projects\Template"
#*PS E:\ProJECTS\VScode Env\.vscode\pythoonic_app_dev\Flet\projects\Template> flet template.py -d
#


import flet as ft
from flet.container import Container
import datetime
from plotly.subplots import make_subplots
import plotly.graph_objects as go

import plotly.graph_objects as go
from plotly.subplots import make_subplots

# from alert import bs,dlg,dlg_modal,show_bs,open_dlg,open_dlg_modal
from flet import NavigationDestination, NavigationBar, icons
# from markdwn_temp import  row_continer



def main(page: ft.Page):


    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()
    page.theme_mode = "dark"
        
    def theme_select(e):
        page.theme_mode = "dark" if page.theme_mode == "light" else "light"
        switch_theme.label = "Light" if page.theme_mode == "light" else "Dark"
        page.update()


    switch_theme = ft.Switch(label="Light", on_change=theme_select)
      
        # todo ####### ALERTS #########  
    stock_qty = 11
    cash = 29000
    order_msg = f"order placed ~ ICICI Bank-EQ BUY 5 qty @920 @ {datetime.datetime.now().strftime('%d-%b-%Y %a %H:%M:%S')}_ICICI Holding {stock_qty} Nos | cash Avl {cash}"
    scan_alert = f'alert'
    
    # page.overlay.append(bs)    
    def show_snackbar(e):
        page.snack_bar = ft.SnackBar(ft.Text(),
        action_color= "blue",
        bgcolor="green",
        on_action= ft.Text("Check Holdings")
        )
        page.snack_bar.open = True
        page.update()
        
    
          
    notify_1 = '9'
    pnl =  '3000'
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.MENU_OUTLINED),
        leading_width=40,
        title=ft.Text("Trade Wiser"), ##Resilience  Adaptive Serene#
        center_title=False,
        bgcolor=ft.colors.BLACK26 ,
        actions=[
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED,on_click=show_snackbar),
            ft.FilledButton(f"Net PNL {pnl}",icon=ft.icons.CURRENCY_RUPEE,height=30,icon_color="green"),
            ft.TextField(hint_text="Enter symbol", height =300,width=300),
            ft.IconButton(ft.icons.SEARCH_ROUNDED) ,
            ft.IconButton(ft.icons.BALLOT,content=(ft.Text(f'{notify_1}')),icon_color = ft.colors.BLUE_ACCENT_200),
            ft.IconButton(ft.icons.FILTER_3_ROUNDED,icon_color = ft.colors.GREEN_ACCENT_100),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Triggered"),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(text="Checked Trigger", checked=False, on_click=check_item_clicked),
                      
                ]
            ),
            switch_theme,
        ],
    )
    
    
    
    
    row_continer= ft.Row(
                    [
                        ft.Container(
                            content=ft.Text("Non clickable"),
                            margin=10,
                            padding=10,
                            alignment=ft.alignment.center,
                            bgcolor=ft.colors.AMBER,
                            width=150,
                            height=150,
                            border_radius=10,
                        ),
                        ft.Container(
                            content=ft.Text("Clickable without Ink"),
                            margin=10,
                            padding=10,
                            alignment=ft.alignment.center,
                            bgcolor=ft.colors.GREEN_200,
                            width=150,
                            height=150,
                            border_radius=10,
                            on_click=lambda e: print("Clickable without Ink clicked!"),
                        ),
                        ft.Container(
                            content=ft.Text("Clickable with Ink"),
                            margin=10,
                            padding=10,
                            alignment=ft.alignment.center,
                            bgcolor=ft.colors.CYAN_200,
                            width=150,
                            height=150,
                            border_radius=10,
                            ink=True,
                            on_click=lambda e: print("Clickable with Ink clicked!"),
                        ),
                        ft.Container(
                            content=ft.Text("Clickable transparent with Ink"),
                            margin=10,
                            padding=10,
                            alignment=ft.alignment.center,
                            width=150,
                            height=150,
                            border_radius=10,
                            ink=True,
                            on_click=lambda e: print("Clickable transparent with Ink clicked!"),
                        ),
                    ],
                    alignment="center",
                )
        

### * ###################
    
     
    # todo  container
       
    container_col = ft.Container(
    
                                # content=ft.PopupMenuItem(text="Features", checked=False, on_click=check_item_clicked),        
                                # ft.Stack(
                                #     [
                                #         ft.Container(width=20, height=20, bgcolor=ft.colors.RED, border_radius=5),
                                #         ft.Container(
                                #             width=20,
                                #             height=20,
                                #             bgcolor=ft.colors.YELLOW,
                                #             border_radius=5,
                                #             right=0,    # * location param
                                #         ),
                                #         ft.Container(
                                #             width=20,
                                #             height=20,
                                #             bgcolor=ft.colors.BLUE,
                                #             border_radius=5,
                                #             right=0,    # * location param
                                #             bottom=0,   # * location param
                                #         ),
                                #         ft.Container(
                                #             width=20,
                                #             height=20,
                                #             bgcolor=ft.colors.GREEN,
                                #             border_radius=5,
                                #             left=0,
                                #             bottom=0,
                                #         ),
                                #         ft.Column(
                                #             [
                                #                 ft.Container(
                                #                     width=20,
                                #                     height=20,
                                #                     bgcolor=ft.colors.PURPLE,
                                #                     border_radius=5,
                                #                 )
                                #             ],
                                #             left=35,
                                #             top=35,
                                #         ),
                                #     ]
                                # ),
                                content=row_continer,
                                border_radius=8,
                                padding=5,
                                width=800,
                                height=1200,
                                bgcolor=ft.colors.BLACK)
                                # ,content = ft.PopupMenuItem(text="Features", checked=False, on_click=check_item_clicked),]
                   
                        
    
    
   # todo
    # card_container =
    
    
    
    ## todo TAB_with_card

    row_card = ft.Row(scroll=True)  
    tab_bar_content = []
    row_card.controls.append(
        ft.Card(
                elevation=30,
                content=ft.Container(
                width=160,
                height=160,
                padding=15,
                border_radius= 10,#ft.border_radius.symmetric(vertical=border.BorderSide(5,"Orange")),
                bgcolor='white',
                    content=ft.Text("Charts",color="black")
                )
        
        
        )
    
    )
    
    
    tab_item = ft.Tabs(
        selected_index=1,
        animation_duration=300,
        tabs= [
            ft.Tab(
                text="OPTION SCANNER",
                content=ft.Container(
                    content=container_col, alignment= ft.alignment.center
                ),
            ),
            ft.Tab(
                text="INDEX OPTION",                
                content=ft.Container(
                    content=container_col, alignment=ft.alignment.center
                ),
            ),
            ft.Tab(
                text="Major Indices",
                content=ft.Container(
                    content=container_col, alignment= ft.alignment.center
                ),
            ),
            ft.Tab(
                text="CASH",
                content=ft.Container(
                    content=container_col, alignment=ft.alignment.center
                ),
            ),
            ft.Tab(
                text="MCX",
                content=ft.Container(
                    content=container_col, alignment=ft.alignment.center
                ),
            ),
            ft.Tab(
                text="GLOBAL WATCHLIST",
                # tab_content=ft.Icon(name = ft.icons.ARROW_FORWARD_IOS),
                content=ft.Container(
                    content=container_col, alignment=ft.alignment.center
                ),
            ),
        ],
        col=6,width=800,expand=3,
    )
    
    
    page.navigation_bar = NavigationBar(
        destinations=[
            NavigationDestination(icon=icons.HOME, label="HOME"),
            NavigationDestination(icon=icons.MONETIZATION_ON, label="POSITION"),
            NavigationDestination(icon=icons.HAIL_SHARP, label="SENTIMENT"),
            NavigationDestination(icon=icons.CHARGING_STATION_ROUNDED, label="PNL"),
            NavigationDestination(
                icon=icons.BOOKMARK_BORDER,
                selected_icon=icons.BOOKMARK,
                label="PROFILE",
            ),
        ]
    )

## ? Navigate  Routing
    navigation_rail = ft.NavigationRail(
        selected_index=0,
        label_type="all",
        extended=True,
        height=600,
        min_width=50,
        min_extended_width=100,
        leading=ft.FloatingActionButton(icon=ft.icons.DASHBOARD , text="SNAP"),
        group_alignment=-0.9,
        disabled= True,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.BOOK, selected_icon=ft.icons.BOOK_ONLINE, label="Porfolio",
            ),
                        
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.BOOKMARK),
                selected_icon_content=ft.Icon(ft.icons.BOOKMARK_BORDER),
                label="FNO",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.MANAGE_SEARCH_ROUNDED,
                selected_icon_content=ft.Icon(ft.icons.MANAGE_SEARCH_ROUNDED),
                label_content=ft.Text("SCAN"),
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.CRISIS_ALERT_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.ARROW_FORWARD_IOS),
                label_content=ft.Text("TRIGGER"),
            ),
                        
            ft.NavigationRailDestination(
                icon=ft.icons.CALENDAR_MONTH,
                selected_icon_content=ft.Icon(ft.icons.ARROW_FORWARD_IOS),
                label_content=ft.Text("EVENTS"),
            ),
            
            
            
                     
            ft.NavigationRailDestination(
                icon=ft.icons.UPCOMING_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.ARROW_FORWARD_IOS),
                label_content=ft.Text("UPDATES"),
            ),
            
                        
            ft.NavigationRailDestination(
                icon=ft.icons.TASK_ALT_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.ARROW_FORWARD_IOS),
                label_content=ft.Text("TASK"),
            ),
            
                      
            ft.NavigationRailDestination(
                icon=ft.icons.ERROR_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.ARROW_FORWARD_IOS),
                label_content=ft.Text("ERROR Log"),
            ),
                ft.NavigationRailDestination(
                # icon=ft.icons.BUG_REPORT_OUTLINED,
                # selected_icon_content=ft.Icon(ft.icons.ARROW_FORWARD_IOS),
                label_content=ft.Text(""),
            ),
            
            # ft.Divider(height=0.3,color= ft.colors.AMBER_100,thickness=2), # todo Divider
                                              
            ft.NavigationRailDestination(
                icon=ft.icons.BUG_REPORT_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.ARROW_FORWARD_IOS),
                label_content=ft.Text("AI"),
            ),
            
            # ft.TextField(width=200,bgcolor = 'white', border_radius =10, border_width = 1, border_color= 'white',hint_text="Enter item name"),                     
            ft.NavigationRailDestination(
                icon=ft.icons.BUG_REPORT_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.ARROW_FORWARD_IOS),
                label_content=ft.Text("DEV"),
            ),
                                     
            ft.NavigationRailDestination(
                icon=ft.icons.FIRE_TRUCK_SHARP,
                selected_icon_content=ft.Icon(ft.icons.ARROW_FORWARD_IOS),
                label_content=ft.Text("Backtest"),
            ),           
            
            # ft.Text("Broker Agonistic Customizable Trading System",no_wrap=False),
            
        ],
        on_change=lambda e: print("Selected destination:", e.control.selected_index),
    )
   
    
    
    # todo########
    page.add(ft.Row())
    #     ft.Row(
    #         [
    #             rail,
    #             ft.VerticalDivider(width=1),tab_item
    #         ,],
    #         expand=True,
    #     )
    # )
    
    col = ft.Ref[ft.Column]()
    row = ft.Ref[ft.Column]()
    # ! multi_chart 

#plot title
#value [ltpvs time , oi vs time ]
    
    def plotly_oi_ltp(symbol: list[str]):
        fig = make_subplots(rows=2, cols=2,
                                   specs=[[{"secondary_y": True}, {"secondary_y": True}],
                                   [{"secondary_y": True}, {"secondary_y": True}]],
                                    shared_xaxes=True,
                                    subplot_titles=("Plot 1", "Plot 2", "Plot 3", "Plot 4"),
                                    vertical_spacing=0.08)                         
                                
        
    # Top left
        fig.add_trace(
            go.Scatter(x=[1, 2, 3], y=[2, 52, 62], name="yaxis data"),      #ltp
            row=1, col=1, secondary_y=False)
        
        fig.add_trace(
            go.Scatter(x=[1, 2, 3], y=[40, 50, 60], name="yaxis2 data"),    #oi
            row=1, col=1, secondary_y=True,
        )
        
        # Top right
        fig.add_trace(
            go.Scatter(x=[1, 2, 3], y=[2, 52, 62], name="yaxis3 data"),
            row=1, col=2, secondary_y=False,
        )
        
        fig.add_trace(
            go.Scatter(x=[1, 2, 3], y=[40, 50, 60], name="yaxis4 data"),
            row=1, col=2, secondary_y=True,
        )
        
        # Bottom left
        fig.add_trace(
            go.Scatter(x=[1, 2, 3], y=[2, 52, 62], name="yaxis5 data"),
            row=2, col=1, secondary_y=False,
        )
        
        fig.add_trace(
            go.Scatter(x=[1, 2, 3], y=[40, 50, 60], name="yaxis6 data"),
            row=2, col=1, secondary_y=True,
        )
        
        # Bottom right
        fig.add_trace(
            go.Scatter(x=[1, 2, 3], y=[2, 52, 62], name="yaxis7 data"),
            row=2, col=2, secondary_y=False,
        )
        
        fig.add_trace(
            go.Scatter(x=[1, 2, 3], y=[40, 50, 60], name="yaxis8 data"),
            row=2, col=2, secondary_y=True,
        )
        
        return  fig.show()
        
        
    # todo #######  checkbox & containers  ##########
    tab_col=ft.Column()
    page.add(
        ft.Row(
        [
        navigation_rail,
        ft.VerticalDivider(width=1,color= ft.colors.AMBER_300,thickness=2),
        
        tab_item,
        
        # ft.PopupMenuItem(text="Features", checked=False, on_click=check_item_clicked)]                  
            # ft.Column([ ft.Checkbox(['1m','5m','15m','1H','D','W'])], alignment="start", expand=True),
            # col = ft.Column(),
            # col.current.controls.append(t)
        ],
            expand=True,
        )
    )
    # page.title = "DRONACHARYA"
        
ft.app(name= "TERMINAL",target=main,view=ft.WEB_BROWSER)
