from nicegui import ui

from apps.tvm_time_value_of_money.time_value_of_money import TimeValueOfMoney
from database_helper.database_common import create_sqlite_session, cursor_to_list_of_dict
from tvm_state import State

my_database_path = '/home/qxu6895/projects/udemy-business-fin-python/sqlite_db/my_database.sqlite'

with create_sqlite_session(my_database_path) as session:
    rows = cursor_to_list_of_dict(session.execute("select * from investments"))

# Enrich rows
rows = [row |
        {"FV Calc" : True if bool(row["pv"]) else False }
        for row in rows
        ]

ui.table(rows=rows, row_key='name')

# calculation of TVM
ui.separator()

ui.label("Time value of Stock Return")

def calc_TVM():
    tvm = TimeValueOfMoney(present_value=num_pv.value,
                           future_value=num_fv.value,
                           interest=num_rate.value,
                           period=num_period.value)
    State.FV = tvm.fv()
    State.FV_latex = tvm.fv_latex()

    State.PV = tvm.pv()
    State.PV_latex = tvm.pv_latex()

    State.R = tvm.r()
    State.R_latex = tvm.r_latex()



with ui.row(align_items="end") as row_fv:
    num_pv = ui.number("PV", format='%.2f', value=100, on_change=calc_TVM)
    num_fv = ui.number("FV", format='%.2f', value=110, on_change=calc_TVM)
    num_rate = ui.number("R = Rate (p/a)", format='%.2f', value=.1, on_change=calc_TVM)
    num_period = ui.number("P = Period (years)", format='%.2f', value=1, on_change=calc_TVM)

with ui.row(align_items="end").classes("pb-2") as row_tvm:
    ui.markdown(extras=['latex']).bind_content_from(State, "FV_latex")

    ui.space()

    ui.markdown(extras=['latex']).bind_content_from(State, "PV_latex")

    ui.space()

    ui.markdown(extras=['latex']).bind_content_from(State, "R_latex")


with ui.row(align_items="end").classes("pb-2") as row_pv:
    ui.label().bind_text_from(State, 'FV', lambda val: f"R{val:.2f}")

    ui.space()

    ui.label().bind_text_from(State, 'PV', lambda val: f"R{val:.2f}")

    ui.space()

    ui.label().bind_text_from(State, 'R', lambda val: f"{val*100:.2f}%")

# Input calculation Stock Values
ui.separator()

ui.label("Time value of Stock Return")

def calc_TVM_stock():
    tvm = TimeValueOfMoney(stock_price_at_start=num_pt_start.value,
                           stock_price_at_end=num_pt_end.value,
                           dividend_yield=num_yt_end.value,)

    State.StockReturn_PriceReturn = tvm.stock_return_price_return()
    State.StockReturn_PriceReturn_latex = tvm.stock_return_price_return_latex()

    State.StockReturn_TotalReturn = tvm.stock_return_total_return()
    State.StockReturn_TotalReturn_latex = tvm.stock_return_total_return_latex()


with ui.row(align_items="end") as row_stock:
    num_pt_start = ui.number("Price@time Start(Pt)", format='%.2f', value=90, on_change=calc_TVM_stock)
    num_pt_end = ui.number("Price@time End(Pt+1)", format='%.2f', value=93.5, on_change=calc_TVM_stock)
    num_yt_end = ui.number("Yield@time End(Yt+1)", format='%.2f', value=2, on_change=calc_TVM_stock)

with ui.row(align_items="end").classes("pb-2") as row_price_return:
    ui.markdown(extras=['latex']).bind_content_from(State, "StockReturn_PriceReturn_latex")
    ui.space()

    ui.markdown(extras=['latex']).bind_content_from(State, "StockReturn_TotalReturn_latex")

with ui.row(align_items="end").classes("pb-2") as row_total_return:
    ui.label().bind_text_from(State,'StockReturn_PriceReturn', lambda val: f"{val*100:.5f}%")
    ui.space()

    ui.label().bind_text_from(State,'StockReturn_TotalReturn', lambda val: f"{val*100:.5f}%")

# Initial run
calc_TVM()
calc_TVM_stock()

ui.run()