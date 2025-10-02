from dataclasses import field
from numbers import Number

from nicegui import binding
from sqlalchemy import String


@binding.bindable_dataclass
class State:
    """A bindable dataclass to hold the application state."""

    FV: Number = Number
    FV_latex: str = str

    PV: Number = Number
    PV_latex: str = str

    R: Number = Number
    R_latex: str = str

    StockReturn_PriceReturn: Number = Number
    StockReturn_PriceReturn_latex: str = str

    StockReturn_TotalReturn: Number = Number
    StockReturn_TotalReturn_latex: str = str

    main_page_toggle_status: bool = True
    main_page_active_blocks_rows: list = field(default_factory=list)
