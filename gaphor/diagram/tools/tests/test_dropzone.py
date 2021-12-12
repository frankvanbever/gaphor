from gaphas.item import NW, SE

from gaphor import UML
from gaphor.diagram.tools.dropzone import drop_zone_tool, grow_parent, on_motion
from gaphor.UML.components import ComponentItem, NodeItem


def test_hover_over_drop_zone(diagram, element_factory, view):
    node_item = diagram.create(NodeItem, subject=element_factory.create(UML.Node))
    node_item.width = node_item.height = 200
    comp_item = diagram.create(
        ComponentItem, subject=element_factory.create(UML.Component)
    )

    view.request_update((node_item, comp_item))

    tool = drop_zone_tool(view, ComponentItem)
    view.add_controller(tool)
    on_motion(tool, 100, 100, ComponentItem)

    selection = view.selection
    assert selection.dropzone_item is node_item


def test_grow_parent(diagram, element_factory):
    node_item = diagram.create(NodeItem, subject=element_factory.create(UML.Node))
    node_item.width = node_item.height = 200
    comp_item = diagram.create(
        ComponentItem, subject=element_factory.create(UML.Component)
    )
    comp_item.matrix.translate(200, 200)

    grow_parent(node_item, comp_item)

    assert node_item.handles()[NW].pos.tuple() == (0, 0)
    assert node_item.handles()[SE].pos.tuple() == (320, 270)
