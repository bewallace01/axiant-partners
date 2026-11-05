# -*- coding: utf-8 -*-
"""Small helper for the v2 table markup used by cluster modules."""


def table(heads, rows):
    head = "".join(f"<th>{h}</th>" for h in heads)
    body = "".join(
        "<tr>" + "".join(f'<td data-label="{h}">{c}</td>' for h, c in zip(heads, r)) + "</tr>"
        for r in rows)
    return (f'<div class="table-wrap"><table style="width:100%"><thead><tr>{head}</tr></thead>'
            f"<tbody>{body}</tbody></table></div>")
