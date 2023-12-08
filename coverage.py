def make_coverage(g) -> set:
    s = set()
    for node in g.nodes:
        g.nodes[node]['label'] = 0

    while g.nodes:
        a_n = None

        for node in g.nodes:
            if g.degree(node) == 0 or (
                    g.degree(node) == 1 and g.nodes[node]['label'] == 0):
                a_n = node
                break

        if not a_n:
            for node in g.nodes:
                if g.degree(node) == 1:
                    a_n = list(g[node])[0]
                    break

        s.add(a_n)
        # print(f"s += {a_n}")

        for node in g[a_n]:
            g.nodes[node]['label'] += 1

        g.remove_node(a_n)
        # print(f"removed {a_n}")

        while True:
            acted = False

            nodes = list(g.nodes)
            for node in nodes:
                if g.nodes[node]['label'] > 1 and g.degree(node) in {0, 1}:
                    # print(f"removed {node}")
                    g.remove_node(node)
                    acted = True

            if not acted:
                break
    # print("fineshed algorithm")
    # print(f"{len(s)=} {s=}")
    return s
