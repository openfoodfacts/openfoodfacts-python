import pytest

from openfoodfacts.taxonomy import TaxonomyNode


def make_node(identifier):
    return TaxonomyNode(identifier, names={}, synonyms={})


def connect(parent, child):
    parent.children.append(child)
    child.parents.append(parent)


@pytest.mark.parametrize("direction", ["children", "parents"])
def test_deep_hierarchy(direction):
    nodes = [make_node(str(i)) for i in range(1500)]
    for parent, child in zip(nodes, nodes[1:], strict=False):
        connect(parent, child)

    if direction == "children":
        assert nodes[0].get_children_hierarchy() == nodes[1:]
    else:
        assert nodes[-1].get_parents_hierarchy() == nodes[-2::-1]


def test_deep_ancestry():
    nodes = [make_node(str(i)) for i in range(1500)]
    for parent, child in zip(nodes, nodes[1:], strict=False):
        connect(parent, child)

    assert nodes[-1].is_child_of(nodes[0])
    assert nodes[0].is_parent_of(nodes[-1])
    assert not nodes[-1].is_child_of(make_node("unrelated"))


def test_shared_ancestor_preserves_depth_first_order():
    root, left, right, leaf = [
        make_node(name) for name in ("root", "left", "right", "leaf")
    ]
    connect(root, left)
    connect(root, right)
    connect(left, leaf)
    connect(right, leaf)

    assert root.get_children_hierarchy() == [left, leaf, right]
    assert leaf.get_parents_hierarchy() == [left, root, right]
    assert leaf.is_child_of(root)
    assert not root.is_child_of(leaf)


def test_cycle_does_not_revisit_nodes():
    first, second, third = [make_node(str(i)) for i in range(3)]
    connect(first, second)
    connect(second, third)
    connect(third, first)

    assert first.get_children_hierarchy() == [second, third]
    assert first.get_parents_hierarchy() == [third, second]
    assert first.is_child_of(third)
    assert not first.is_child_of(make_node("unrelated"))


def test_shared_subtrees_are_traversed_once():
    class CountingList(list):
        traversals = 0

        def __iter__(self):
            self.traversals += 1
            return super().__iter__()

        def __reversed__(self):
            self.traversals += 1
            return super().__reversed__()

    levels = [[make_node(f"{depth}-{side}") for side in range(2)] for depth in range(8)]
    root = make_node("root")
    for child in levels[0]:
        connect(root, child)
    for parents, children in zip(levels, levels[1:], strict=False):
        for parent in parents:
            for child in children:
                connect(parent, child)
    nodes = [root] + [node for level in levels for node in level]
    for node in nodes:
        node.children = CountingList(node.children)
        node.parents = CountingList(node.parents)

    assert len(root.get_children_hierarchy()) == len(nodes) - 1
    assert all(node.children.traversals <= 1 for node in nodes)
    assert not levels[-1][-1].is_child_of(make_node("unrelated"))
    assert all(node.parents.traversals <= 1 for node in nodes)
