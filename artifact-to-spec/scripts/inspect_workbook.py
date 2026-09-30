#!/usr/bin/env python3
"""
Dump structural summary of spreadsheet-like files (.xlsx, .xls, .ods, .csv) so
their domain model can be reverse-engineered without opening each one by hand.

For every sheet/tab it prints: dimensions, header row, a few sample data rows,
and any cell formulas found (these usually encode business rules — interest
calculations, running balances, % splits — worth surfacing explicitly).

Usage:
    python3 inspect_workbook.py <file_or_directory> [--rows N]

Falls back gracefully: if openpyxl/odfpy aren't installed, tells you the pip
install command instead of crashing.
"""
import sys
import os
import csv
import argparse


def inspect_csv(path, n_rows):
    print(f"\n=== {os.path.basename(path)} (csv) ===")
    with open(path, newline="", encoding="utf-8", errors="replace") as f:
        reader = csv.reader(f)
        rows = list(reader)
    if not rows:
        print("  (empty)")
        return
    print(f"  rows: {len(rows)}, cols: {len(rows[0])}")
    print(f"  header: {rows[0]}")
    for r in rows[1 : 1 + n_rows]:
        print(f"  {r}")


def inspect_xlsx(path, n_rows):
    try:
        import openpyxl
    except ImportError:
        print(f"\n=== {os.path.basename(path)} ===")
        print("  openpyxl not installed. Run: pip3 install openpyxl (or use a venv)")
        return
    wb = openpyxl.load_workbook(path, data_only=True)
    wb_formulas = openpyxl.load_workbook(path, data_only=False)
    print(f"\n=== {os.path.basename(path)} (xlsx, {len(wb.sheetnames)} sheets) ===")
    for name in wb.sheetnames:
        ws = wb[name]
        wsf = wb_formulas[name]
        print(f"\n  --- sheet: {name!r}  dims: {ws.dimensions} ---")
        max_col = ws.max_column
        for r in range(1, min(1 + n_rows, ws.max_row) + 1):
            row = [ws.cell(row=r, column=c).value for c in range(1, max_col + 1)]
            while row and row[-1] is None:
                row.pop()
            print(f"  r{r}: {row}")
        formulas = []
        for row in wsf.iter_rows():
            for cell in row:
                if isinstance(cell.value, str) and cell.value.startswith("="):
                    formulas.append((cell.coordinate, cell.value))
        if formulas:
            print(f"  formulas found ({len(formulas)}), sample:")
            for coord, f in formulas[:8]:
                print(f"    {coord}: {f}")


def inspect_ods(path, n_rows):
    try:
        from odf.opendocument import load
        from odf.table import Table, TableRow, TableCell
        from odf.text import P
    except ImportError:
        print(f"\n=== {os.path.basename(path)} ===")
        print("  odfpy not installed. Run: pip3 install odfpy (or use a venv)")
        return

    def cell_text(cell):
        return "".join(
            str(node)
            for p in cell.getElementsByType(P)
            for node in p.childNodes
            if hasattr(node, "data")
        )

    doc = load(path)
    tables = doc.getElementsByType(Table)
    print(f"\n=== {os.path.basename(path)} (ods, {len(tables)} sheets) ===")
    for table in tables:
        name = table.getAttribute("name")
        rows = table.getElementsByType(TableRow)
        print(f"\n  --- sheet: {name!r}  rows: {len(rows)} ---")
        for i, row in enumerate(rows[: n_rows + 1]):
            cells = row.getElementsByType(TableCell)
            values = [cell_text(c) for c in cells]
            print(f"  r{i+1}: {values}")


def inspect_path(path, n_rows):
    ext = os.path.splitext(path)[1].lower()
    if ext == ".csv":
        inspect_csv(path, n_rows)
    elif ext in (".xlsx", ".xlsm"):
        inspect_xlsx(path, n_rows)
    elif ext == ".ods":
        inspect_ods(path, n_rows)
    else:
        print(f"\n=== {os.path.basename(path)} ===\n  (skipped: unsupported extension {ext})")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("target", help="file or directory to inspect")
    ap.add_argument("--rows", type=int, default=5, help="sample rows per sheet")
    args = ap.parse_args()

    if os.path.isdir(args.target):
        for fname in sorted(os.listdir(args.target)):
            if fname.startswith("."):
                continue
            fpath = os.path.join(args.target, fname)
            if os.path.isfile(fpath):
                inspect_path(fpath, args.rows)
    else:
        inspect_path(args.target, args.rows)


if __name__ == "__main__":
    main()
