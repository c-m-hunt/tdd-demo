





















































# def format_money(val: int) -> str:
#     return f"£{val:.2f}"

# def format_money(val: int, curr: str = "GBP") -> str:
#     curr_symbols = {
#         "GBP": "£",
#         "USD": "$",
#         "EUR": "€",
#     }
#     return f"{curr_symbols[curr]}{val:.2f}"

# def format_money(val: int, curr: str = "GBP") -> str:
#     if len(curr) != 3:
#         raise ValueError("Currency must be a three letter code")
#     curr_symbols = {
#         "GBP": "£",
#         "USD": "$",
#         "EUR": "€",
#     }
#     return f"{curr_symbols[curr]}{val:.2f}"

# def format_money(val: int, curr: str = "GBP") -> str:
#     if len(curr) != 3:
#         raise ValueError("Currency must be a three letter code")
#     curr_symbols = {
#         "GBP": "£",
#         "USD": "$",
#         "EUR": "€",
#     }
#     if curr not in curr_symbols:
#         raise ValueError("Currency does not exist")
#     return f"{curr_symbols[curr]}{val:.2f}"

# def format_money(val: int, curr: str = "GBP") -> str:
#     if len(curr) != 3:
#         raise ValueError("Currency must be a three letter code")
#     curr_symbols = {
#         "GBP": "£",
#         "USD": "$",
#         "EUR": "€",
#     }
#     if curr not in curr_symbols:
#         raise ValueError("Currency does not exist")

#     if val < 0:
#         raise ValueError("Value must be greater than zero")
#     return f"{curr_symbols[curr]}{val:.2f}"

# def format_money(val: int, curr: str = "GBP") -> str:
#     if len(curr) != 3:
#         raise ValueError("Currency must be a three letter code")
#     curr_symbols = {
#         "GBP": "£",
#         "USD": "$",
#         "EUR": "€",
#     }
#     if curr not in curr_symbols:
#         raise ValueError("Currency does not exist")

#     if val < 0 and curr != "EUR":
#         raise ValueError("Value must be greater than zero")
#     return f"{curr_symbols[curr]}{val:.2f}"
