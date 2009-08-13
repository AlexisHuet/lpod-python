# -*- coding: UTF-8 -*-
# Copyright (C) 2009 Itaapy, ArsAperta, Pierlis, Talend

# Import from lpod
from xmlpart import odf_create_element


def odf_create_frame(name, size=('1cm', '1cm'), anchor_type='paragraph',
                     page_number=None, position=None, style=None):
    """Create a frame element of the given size. If positioned by page, give
    the page number and the x, y position.

    Size is a 2-tuple (width, height) and position is a 2-tuple (left,
    top); both are strings including the unit, e.g. ('10cm', '15cm').

    Frames are not useful by themselves. You may consider calling
    odf_create_image_frame or odf_create_text_frame directly.

    Arguments:

        name -- unicode

        size -- (str, str)

        anchor_type -- 'page', 'frame', 'paragraph', 'char' or 'as-char'

        page -- int (when anchor_type == 'page')

        position -- (str, str)

        style -- unicode

    Return: odf_element
    """
    data = (u'<draw:frame draw:name="%s" svg:width="%s" svg:height="%s" '
            u'text:anchor-type="%s"/>')
    element = odf_create_element(data % (name, size[0],
                                         size[1], anchor_type))

    if page_number is not None:
        element.set_attribute('text:anchor-page-number', str(page_number))

    if position is not None:
        x, y = position
        element.set_attribute('svg:x', x)
        element.set_attribute('svg:y', y)

    if style is not None:
        element.set_attribute('draw:style-name', style)

    return element



def odf_create_image_frame(uri, size, position=None, style=None):
    """Create a ready-to-use image image, since it must be embedded in a
    frame. Size is a 2-tuple (width, height) and position is a 2-tuple (left,
    top); both are strings including the unit, e.g. ('21cm', '29.7cm'). Images
    are supposed to be embedded by default; if they remain outside the
    packaging, set link to True.

    Arguments:

        uri -- str

        size -- (str, str)

        position -- (str, str)

        style -- unicode

    Return: odf_element
    """
    raise NotImplementedError



def odf_create_text_frame(text_or_element, size, position=None, style=None):
    """Create a ready-to-use image image, since it must be embedded in a
    frame. Size is a 2-tuple (width, height) and position is a 2-tuple (left,
    top); both are strings including the unit, e.g. ('21cm', '29.7cm'). Images
    are supposed to be embedded by default; if they remain outside the
    packaging, set link to True.

    Arguments:

        uri -- str

        size -- (str, str)

        position -- (str, str)

        style -- unicode

    Return: odf_element
    """
    raise NotImplementedError
