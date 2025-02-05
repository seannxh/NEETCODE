# generate_reference_pdf.py

from fpdf import FPDF

CONTENT = """
PYTHON REFERENCE FOR STR, LIST, TUPLE, DICT, SET, ETC.

===========================================
1) STRINGS (str)
===========================================
Common Methods
-------------
• Formatting & Case:
  - str.capitalize()
  - str.casefold()
  - str.lower()
  - str.upper()
  - str.swapcase()
  - str.title()
  - str.center(width[, fillchar])
  - str.ljust(width[, fillchar])
  - str.rjust(width[, fillchar])
  - str.zfill(width)

• Searching & Checking:
  - str.count(sub[, start[, end]])
  - str.endswith(suffix[, start[, end]])
  - str.startswith(prefix[, start[, end]])
  - str.find(sub[, start[, end]])
  - str.rfind(sub[, start[, end]])
  - str.index(sub[, start[, end]])
  - str.rindex(sub[, start[, end]])
  - str.isalnum()
  - str.isalpha()
  - str.isdigit()
  - str.isnumeric()
  - str.isdecimal()
  - str.islower()
  - str.isupper()
  - str.isspace()
  - str.istitle()
  - str.isidentifier()
  - str.isprintable()
  - str.isascii()

• Splitting & Joining:
  - str.split(sep=None, maxsplit=-1)
  - str.rsplit(sep=None, maxsplit=-1)
  - str.splitlines(keepends=False)
  - str.join(iterable)

• Replacing & Stripping:
  - str.strip([chars])
  - str.lstrip([chars])
  - str.rstrip([chars])
  - str.replace(old, new[, count])
  - str.removeprefix(prefix)  (Python 3.9+)
  - str.removesuffix(suffix)  (Python 3.9+)

• Partition & Translation:
  - str.partition(sep)
  - str.rpartition(sep)
  - str.maketrans(x[, y[, z]])
  - str.translate(table)

• Encoding:
  - str.encode(encoding='utf-8', errors='strict')

• Formatting (Old & New Styles):
  - str.format(*args, **kwargs)
  - str.format_map(mapping)
  - f-Strings (Python 3.6+): f"text {variable}"

===========================================
2) LISTS (list)
===========================================
Methods
-------
- list.append(x)
- list.extend(iterable)
- list.insert(i, x)
- list.remove(x)
- list.pop([i])
- list.clear()
- list.index(x[, start[, end]])
- list.count(x)
- list.sort(*, key=None, reverse=False)
- list.reverse()
- list.copy()

===========================================
3) TUPLES (tuple)
===========================================
Immutable sequence. Limited methods:
- tuple.count(x)
- tuple.index(x[, start[, end]])

===========================================
4) DICTIONARIES (dict)
===========================================
Methods
-------
- dict.clear()
- dict.copy()
- dict.get(key[, default])
- dict.items()
- dict.keys()
- dict.values()
- dict.pop(key[, default])
- dict.popitem()
- dict.setdefault(key[, default])
- dict.update([other])
- dict.fromkeys(iterable[, value])

(Python 3.9+ Operators)
- merged_dict = dict1 | dict2
- dict1 |= dict2

===========================================
5) SETS (set) and FROZEN SETS (frozenset)
===========================================
• set
-----
- set.add(elem)
- set.clear()
- set.copy()
- set.discard(elem)
- set.remove(elem)
- set.pop()
- set.update(*others)
- set.intersection_update(*others)
- set.difference_update(*others)
- set.symmetric_difference_update(other)
- set.union(*others)
- set.intersection(*others)
- set.difference(*others)
- set.symmetric_difference(other)
- set.isdisjoint(other)
- set.issubset(other)
- set.issuperset(other)

• frozenset
-----------
(Immutable; no methods that change the set)
- frozenset.union(*others)
- frozenset.intersection(*others)
- frozenset.difference(*others)
- frozenset.symmetric_difference(other)
- frozenset.isdisjoint(other)
- frozenset.issubset(other)
- frozenset.issuperset(other)

===========================================
6) LINKED LISTS IN PYTHON?
===========================================
- Not a built-in type.
- Often implemented via custom classes or by using collections.deque (a double-ended queue).

• collections.deque
-------------------
from collections import deque

Methods:
- deque.append(x)
- deque.appendleft(x)
- deque.pop()
- deque.popleft()
- deque.clear()
- deque.copy()        (Python 3.9+)
- deque.count(x)
- deque.extend(iterable)
- deque.extendleft(iterable)
- deque.remove(value)
- deque.rotate(n=1)

===========================================
END OF REFERENCE
"""

class PDF(FPDF):
    def header(self):
        # Add a bold title at the top
        self.set_font("Arial", style="B", size=14)
        self.cell(0, 10, "Python Reference for Built-in Collections", border=False, ln=True, align="C")
        self.ln(5)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        self.set_font("Arial", size=8)
        # Page number
        page_num = f"Page {self.page_no()}"
        self.cell(0, 10, page_num, 0, 0, "C")


def main():
    # Create PDF object
    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.set_font("Arial", size=11)

    # Split the content by lines and output each line
    lines = CONTENT.strip().split("\n")
    for line in lines:
        pdf.multi_cell(0, 6, line)
    
    # Save the PDF
    pdf.output("python_reference.pdf")
    print("PDF generated: python_reference.pdf")

if __name__ == "__main__":
    main()
