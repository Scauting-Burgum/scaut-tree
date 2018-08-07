def node_to_string(node, layer = 0):
    message = '|' * layer + repr(node) + '\n'
    for child in node.children:
        message += node_to_string(child, layer + 1)

    return message
