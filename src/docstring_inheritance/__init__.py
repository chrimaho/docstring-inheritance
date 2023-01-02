# Copyright 2021 Antoine DECHAUME
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from __future__ import annotations

from typing import Any

from .class_processor import ClassDocstringsInheritor
from .class_processor import DocstringProcessorType
from .docstring_processors.google import GoogleDocstringProcessor
from .docstring_processors.numpy import NumpyDocstringProcessor

process_numpy_docstring = NumpyDocstringProcessor()
process_google_docstring = GoogleDocstringProcessor()


class _BaseDocstringInheritanceMeta(type):
    """Metaclass for inheriting class docstrings with a docstring processor."""

    def __init__(
        cls,
        class_name: str,
        class_bases: tuple[type],
        class_dict: dict[str, Any],
        docstring_processor: DocstringProcessorType,
    ) -> None:
        super().__init__(class_name, class_bases, class_dict)
        if class_bases:
            inheritor = ClassDocstringsInheritor(cls, docstring_processor)
            inheritor.inherit_class_docstring()
            inheritor.inherit_attrs_docstrings()


class GoogleDocstringInheritanceMeta(_BaseDocstringInheritanceMeta):
    """Metaclass for inheriting docstrings in Google format."""

    def __init__(
        self,
        class_name: str,
        class_bases: tuple[type],
        class_dict: dict[str, Any],
    ) -> None:
        super().__init__(class_name, class_bases, class_dict, process_google_docstring)


class NumpyDocstringInheritanceMeta(_BaseDocstringInheritanceMeta):
    """Metaclass for inheriting docstrings in Numpy format."""

    def __init__(
        self,
        class_name: str,
        class_bases: tuple[type],
        class_dict: dict[str, Any],
    ) -> None:
        super().__init__(class_name, class_bases, class_dict, process_numpy_docstring)
