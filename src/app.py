#!/usr/bin/env python3
#!/usr/bin/python3
# -*- coding: iso-8859-1 -*-


"""
/******************************************************************************\
| PROGRAM : qt-coinrate     VERSION : @version 0.1    AUTHOR: @author tuanhace |
| LANGUAGE: Python 3.9      COMPILER: GCC 4.8.5       IDE   : PyCharm CE       |
| FILE    : @file dashboard.py                                                 |
| DATE    : @date 2024-08-11 22:00                                             |
| NOTE    :                                                                    |
|                                                                              |
|------------------------------------------------------------------------------|
| AUTHORISATION AND DISCLAIMER:                                                |
| * @copyright 2024 - 2024 by The Authors. All rights reserved.                |
|                                                                              |
|   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS        |
|   "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT          |
|   LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR      |
|   A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT       |
|   OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,      |
|   SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT           |
|   LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,      |
|   DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY      |
|   THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT        |
|   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE      |
|   OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.       |
|                                                                              |
|------------------------------------------------------------------------------|
| DESIGN REFERENCE:                                                            |
|                                                                              |
|------------------------------------------------------------------------------|
| DESCRIPTION:                                                                 |
| * @brief                                                                     |
|   Qt Coinrate Telegram                                                       |
|                                                                              |
| * @details                                                                   |
|                                                                              |
|------------------------------------------------------------------------------|
| REVISION HISTORY:                                                            |
|   Ver     Date        Author      Reason                                     |
| * 0.1     2024-08-11  tuanhace    Init                                       |
|                                                                              |
\******************************************************************************/
"""


#==============================[ IMPORT ]==============================#
# conda install -n condaenv --update-deps --force-reinstall --yes plotly dash dash_bootstrap_components
# python -m pip install --upgrade-strategy only-if-needed ccxt
#======================================== Import sys
import sys
import time
import threading

#======================================== Import third parties
import warnings
warnings.filterwarnings("ignore")

#import dash
from dash import Dash
#from dash import dcc   # import dash_core_components as dcc
from dash import html  # import dash_html_components as html
from dash import Input, Output, callback, clientside_callback
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeChangerAIO

import requests
import  ccxt

#======================================== Import log


#======================================== Import mine


#==============================[ CONST ]==============================#

# APP_DIR_CWD = os.path.abspath(os.getcwd())



#==============================[ SETTINGS ]==============================#



#==============================[ DEFINE ]==============================#



#==============================[ VAR ]==============================#

dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME, dbc_css])
server = app.server

g_coin_rate = 1
g_old_coin_rate = 1


#==============================[ CLASS ]==============================#



#==============================[ INTERNAL FUNCTION ]==============================#



#==============================[ VIEW ]==============================#

header = html.H4(
    "Dashboard", className="bg-primary text-white p-2 mb-2 text-center"
)

#========================================
span_color_mode_switch = html.Span([
    dbc.Label(className="fa fa-moon", html_for="switch"),
    dbc.Switch(id="switch", value=True, className="d-inline-block ms-1", persistence=True),
    dbc.Label(className="fa fa-sun", html_for="switch"),
])

div_theme_controls = html.Div(
    [ThemeChangerAIO(aio_id="theme"), span_color_mode_switch],
    className="hstack gap-3 mt-2",
    style={"left": "auto", "top": 0, "right": 0},
)

# https://s3-us-west-1.amazonaws.com/plotly-tutorials/logo/new-branding/dash-logo-by-plotly-stripe.png
# https://viettelhightech.com/storage/icon/logo2.svg
img_logo = html.Img(src="https://seeklogo.com/images/V/viettel-high-tech-logo-2D3DB3ECA8-seeklogo.com.png", style={'height': '100px', 'float': 'left'},)
box_logo = dbc.Card(
    children=[],
    body=True,
)

#========================================
button_color_list = [
    "primary",
    "secondary",
    "success",
    "warning",
    "danger",
    "info",
    "light",
    "dark",
    "link",
]
div_color = html.Div(
    [dbc.Button(f"{color}", color=f"{color}", size="sm") for color in button_color_list]
)
div_color = html.Div(["Legend:", div_color], className="mt-2")

#======================================== Tab 1

#--------------------
div_cm_checkbox = html.Div(children=[
    dbc.Label("Input rate:"),
    dbc.Input(
        id="txt_number",
        type="number",
        placeholder="0.0",
    ),
], className="mb-4",)

#--------------------
div_cm_calc = html.Div(children=[
    dbc.Button("Send", id="btn_cm_calc", color='primary', size='md'),
], className="mb-4", style={
    'textAlign': 'center',
},)

#--------------------
box_cm_controls = dbc.Card(
    #html.Div(id='btn_cm_calc_dummy'),
    children=[div_cm_checkbox, div_cm_calc],
    body=True,
    style={'width': '25%', 'border-radius': '5%', 'background': 'PowderBlue'},
)

#--------------------
box_cm_tmp = dbc.Card(
    children=[html.Img(id='img_tmp', style={'width': '100%', 'height': '100%'}),],
    body=True,
    style={'width': '70%'},
)

#======================================== Tab 2



#======================================== Tab
tab1 = dbc.Tab([
    dbc.Row([
        box_cm_controls,
        box_cm_tmp,
    ], justify="center",),
], label="Main")

tab2 = dbc.Tab([
    dbc.Row([
    ], justify="left",),
], label="Help")

box_tab = dbc.Card(dbc.Tabs([tab1, tab2]))

#========================================

app.layout = dbc.Container(
    [
        header,
        dbc.Row([
            div_theme_controls,
        ], justify="right",),
        dbc.Row([
            dbc.Col([
                box_logo,
            ], width=2),
            dbc.Col([
                box_tab,
                div_color,
            ], width=10),
        ]),
        #dcc.Markdown(''' --- '''),
    ],
    fluid=True,
    className="dbc dbc-ag-grid",
)


#==============================[ CONTROL ]==============================#

# Update Bootstrap global theme light/dark mode
clientside_callback(
    """
    switchOn => {
       switchOn
         ? document.documentElement.setAttribute('data-bs-theme', 'light')
         : document.documentElement.setAttribute('data-bs-theme', 'dark')
       return window.dash_clientside.no_update
    }
    """,
    Output("switch", "id"),
    Input("switch", "value"),
)


@callback(
    Output('img_tmp', 'src'),
    Input('btn_cm_calc', 'n_clicks'),
    Input('txt_number', 'value'),
    prevent_initial_call=True
)
def on_btn_cm_calc_clicked(n_clicks, txt_number):
    #logger.info("on_btn_cm_calc_clicked(n_clicks={}, txt_number={})".format(n_clicks, txt_number))

    global g_coin_rate
    g_coin_rate = float(txt_number)


#==============================[ API FUNCTION ]==============================#

def sua_mang(mang):
    return [x.replace("/", "") for x in mang]
def kiem_tra_USDT(chuoi):
    return True if "USDT" in chuoi else False
def kiem_tra_KRW(chuoi):
    return True if "/KRW" in chuoi else False
def kiem_tra_JPY(chuoi):
    return True if "JPY" in chuoi else False
def kiem_tra_taiwan(chuoi):
    return True if "TWD" in chuoi else False
def replace_krw_with_usdt(string_list):
    modified_strings = []
    for string in string_list:
        modified_string = string.replace("KRW", "USDT")
        modified_strings.append(modified_string)
    return modified_strings

def sendTelegram(text, chat_id, bot_token):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": text,
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("Tin nhắn đã được gửi")
    else:
        print("Lỗi khi gửi tin nhắn")

binance1 = ccxt.binance()
upbit = ccxt.upbit()
bithump = ccxt.bithumb()
token_tele = "6806723301:AAENvRJUZZTHa7QxJXKGEYbbBHRY_gkmYNw"
chat_id =  "7027766704"
token_tele2 = "7089214198:AAGXxt_878avqWDna3j3V2MbDTstaFYq3qE"
chat_id2 =  "7027766704"

markets = binance1.load_markets()
market_upbit = upbit.load_markets()
market_bithump = bithump.load_markets()
dataUSDT_binance = []
dataKRW_bithump = []
dataUSDT_bybit = []
dataUSDT_kraken = []
dataUpbit = []
dataUpbit_USDT = []
# print(market_coincheck)
dataCoincheck = []

for pair in markets :
    if kiem_tra_USDT(pair):
        dataUSDT_binance.append(pair)
for pair in market_bithump :
    if kiem_tra_KRW(pair):
        dataKRW_bithump.append(pair)
dataKRW_bithump_USDT = replace_krw_with_usdt(dataKRW_bithump)
mang_trung_lap = set(dataUSDT_binance) & set(dataKRW_bithump_USDT)
isDem = 0
isCoin = ""
chuoiUSDT_KRW = "USDT/KRW"


#==============================[ MAIN ]==============================#

def mainloop():
    global g_coin_rate, g_old_coin_rate
    while True:
        for str_input in mang_trung_lap:
            try:
                print(str_input)
                str_input_in_bitHump = str_input.replace("USDT", "KRW")
                gia_coin_san_binance = binance1.fetch_ticker(str_input)['last']
                gia_coin_san_bithump_kwr = bithump.fetch_ticker(str_input_in_bitHump)['last']
                tigiaUSDTandBinance = g_coin_rate
                gia_coin_san_bithump = gia_coin_san_bithump_kwr/tigiaUSDTandBinance
                data_gia_list = []  # Empty list
                data_gia_list.append(("binance", gia_coin_san_binance))
                data_gia_list.append(("bithump", gia_coin_san_bithump))
                chenhlechgiaCoin = 0
                min_value = 0
                max_value = 0
                chenhlenhpercent = 0
                try:
                    filtered_data = [item for item in data_gia_list if item[1] is not None]
                    min_value = min(filtered_data, key=lambda item: item[1])
                    max_value = max(filtered_data, key=lambda item: item[1])
                    chenhlechgiaCoin = max_value[1] - min_value[1]
                    chenhlenhpercent = chenhlechgiaCoin / min_value[1]
                finally:
                    print("")
                if chenhlenhpercent > 0.015:
                    chuoi_format = "{:.2f}".format(chenhlenhpercent * 100)
                    data_input_check = f"Code: {str_input}\nPrice: {gia_coin_san_bithump_kwr} KRW tương đương {gia_coin_san_bithump} USDT ở bithump \nPrice: {gia_coin_san_binance} USDT ở binance\nChênh lệch: {chuoi_format}%"
                    text = f"{data_input_check}\nBuy from {min_value[0]}, and Sell in {max_value[0]}\nKhoảng mua từ {min_value[1]} tới {min_value[1]*1.02} ở {min_value[0]}\nProfit: {chenhlenhpercent *1000 - 12} USDT\nPhần trăm: {chuoi_format}%\n"
                    if g_coin_rate != g_old_coin_rate:
                        g_old_coin_rate = g_coin_rate
                        sendTelegram(text, chat_id, token_tele)
                    print(text)
            except Exception as err:
                #logger.error(err)
                print(err)
        time.sleep(5)


def mainloop2():
    global g_coin_rate, g_old_coin_rate
    while True:
        if g_coin_rate != g_old_coin_rate:
            g_old_coin_rate = g_coin_rate
            with open("./coin_rate_tmp.txt", 'w') as f:
                f.write(str(g_coin_rate))
        time.sleep(5)


"""*****************************************************************************
FUNCTION NAME
    main
DESCRIPTION
    Main
PARAMETERS
    :param str[] argv:          List of arguments
RETURNS
    :return:                    None
GLOBAL DATA REFERENCED
CALLED ROUTINES
NOTES
    Usage:
*****************************************************************************"""
def main(argv=None):
    if argv is None:
        argv = sys.argv
    #print("[DEBUG] main({})".format(argv))

    t = threading.Thread(target=mainloop)
    t.start()
    app.run_server(debug=True, port=8050)


if __name__ == '__main__':
    ret_val = main(sys.argv)
    sys.exit(ret_val)
