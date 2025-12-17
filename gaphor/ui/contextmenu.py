#!/usr/bin/env python3

"""
Context menu support for elements.

This module allows for registering context menu actions for specific
element types using a generic function. Plugins and other modules can
register their own handlers.

It supports multiple handlers for the same element type, allowing
different plugins to contribute to the same context menu.
"""

import inspect
from collections import defaultdict

from gi.repository import Gio, GLib

from gaphor import UML

# A dictionary that holds a list of handlers for each type
_handlers = defaultdict(list)


def register(item_type):
    """
    A decorator to register a context menu handler for a given element type.
    """

    def decorator(func):
        _handlers[item_type].append(func)
        return func

    return decorator


def context_menu(element):
    """
    A generator that yields all registered menu items for a given element.

    It walks the Method Resolution Order (MRO) of the element's class,
    so handlers for superclasses are also included.
    """
    for cls in inspect.getmro(element.__class__):
        if cls in _handlers:
            for handler in _handlers[cls]:
                yield from handler(element)


# Imagine this is part of Gaphor's core functionality:
@register(UML.UseCase)
def use_case_context_menu(element):
    """
    A core context menu item for UML.UseCase elements.
    """
    menu_item = Gio.MenuItem.new("Frank was here", "win.franks-action")
    menu_item.set_attribute_value("target", GLib.Variant.new_string(element.id))
    yield menu_item


# Now, imagine this is in a separate plugin file:
@register(UML.UseCase)
def harmony_plugin_use_case_menu(element):
    """
    A plugin-specific menu item for the same UML.UseCase element.
    """
    menu_item = Gio.MenuItem.new("Create Harmony Package", "win.harmony-action")
    menu_item.set_attribute_value("target", GLib.Variant.new_string(element.id))
    yield menu_item


# We can even register a handler for a more general type
@register(UML.NamedElement)
def named_element_menu(element):
    """
    A menu item that will appear for ANY element with a name.
    """
    menu_item = Gio.MenuItem.new(f"Log name: {element.name}", "win.log-name-action")
    menu_item.set_attribute_value("target", GLib.Variant.new_string(element.id))
    yield menu_item
