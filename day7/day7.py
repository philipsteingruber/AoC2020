import re
from collections import defaultdict

EMPTY_BAG = 'no other bags.'


def create_graph_part1(lines):
    graph = defaultdict(set)

    for line in lines:
        outer_bag, inner_bags = re.split(r'contain', line)
        outer_bag = get_bag_type(fix_bag(outer_bag))

        if EMPTY_BAG in inner_bags:
            graph[outer_bag].add(None)
        else:
            inner_bags = list(map(fix_bag, inner_bags.split(', ')))
            for inner_bag in inner_bags:
                graph[outer_bag].add(get_bag_type(inner_bag))
    return graph


def get_bag_type(bag):
    return re.match(r'[\d ]*([\w ]+) bag', bag).group(1)


def fix_bag(bag):
    bag = bag.strip()
    if bag[-1] == '.':
        bag = bag[:len(bag)-1]
    return bag


def number_of_paths_containing_endpoint(graph, endpoint):
    paths = 0

    for node in graph:
        if node == endpoint:
            continue
        if connected_to_endpoint(graph, node, endpoint):
            paths += 1

    return paths


def connected_to_endpoint(graph, start, end):
    while True:
        if start == end:
            return True
        elif start == None:
            return False
        else:
            for node in graph[start]:
                if connected_to_endpoint(graph, node, end):
                    return True
            return False


def get_bag_type_and_amount(bag):
    return re.match(r'([\d ]*[\w ]+) bag', bag).group(1)


def create_graph_part2(lines):
    graph = defaultdict(set)

    for line in lines:
        outer_bag, inner_bags = re.split(r'contain', line)
        outer_bag = get_bag_type(fix_bag(outer_bag))

        if EMPTY_BAG in inner_bags:
            graph[outer_bag].add(None)
        else:
            graph[outer_bag].update(list(map(get_bag_type_and_amount, map(fix_bag, inner_bags.split(', ')))))
    return graph


def split_count_and_type(bag):
    count, bag_type = re.match(r'(\d+) ([\w ]+)', bag).groups()
    count = int(count)
    return count, bag_type


def bags_in_outer_bag(graph, outer_bag):
    children = graph[outer_bag]

    contained_bags = 0

    for child in children:
        count, bag_type = split_count_and_type(child)
        contained_bags += count + count * bags_in_outer_bag_recursive(graph, bag_type, 0)

    return contained_bags


def bags_in_outer_bag_recursive(graph, outer_bag, rolling_sum):
    children = graph[outer_bag]

    sum = 0
    if None in children:
        return sum
    else:
        for child in children:
            count, bag_type = split_count_and_type(child)
            sum += count
            sum += count * bags_in_outer_bag_recursive(graph, bag_type, rolling_sum)
        return sum


if __name__ == '__main__':
    with open('input.txt') as file:
        lines = file.readlines()

    graph = create_graph_part1(lines)
    print('Part 1:', number_of_paths_containing_endpoint(graph, 'shiny gold'))

    graph = create_graph_part2(lines)
    print('Part 2:', bags_in_outer_bag(graph, 'shiny gold'))
