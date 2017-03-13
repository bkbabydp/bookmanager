# -*- coding: UTF-8 -*-


from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from barcode import get_barcode_class
from barcode.writer import ImageWriter
import barcode.base

try:
    from StringIO import StringIO
except ImportError:
    from io import BytesIO as StringIO

import traceback


# Create your views here.

def index(request):
    pass


def create_barcode(request, code, name=None):
    """

    :param request:
    :type request: HttpRequest
    :param code:
    :type code: str
    :param name:
    :type name: str
    :return:
    """
    try:
        if name in barcode.PROVIDED_BARCODES:
            w = ImageWriter()
            bc = get_barcode_class(name)(code, writer=w)  # type: barcode.base.Barcode
            s = StringIO()
            bc.write(s)
            image = s.getvalue()
        else:
            image = None
    except Exception:
        traceback.print_exc()
        image = None

    return HttpResponse(image, content_type="image/png")
