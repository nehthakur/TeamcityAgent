def generate_execution_order(graph):

    order = []
    visited = set()

    def visit(node):

        if node in visited:
            return

        visited.add(node)

        for dep in graph.get(node, []):
            visit(dep)

        order.append(node)

    for node in graph:
        visit(node)

    return order
