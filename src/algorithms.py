from floyd_warshall import FloydWarshall
from bellman_ford import BellmanFord
from dijkstra import Dijkstra
from johnson import Johnson
from dispatch import Dispatch
from tarjan import Tarjan
from dispatchability import Dispatchability
from dc_checking import cairo_et_al_2018


__all__ = ['floyd_warshall', 'bellman_ford',
           'dijkstra', 'johnson', 'dispatch', 'tarjan', 'dc_cairo_et_al_2018']


def floyd_warshall(network):
    return FloydWarshall.floyd_warshall(network)


def bellman_ford(network, src=-1):
    return BellmanFord.bellman_ford_wrapper(network, src)


def dijkstra(network, src, succ_direction=True, potential_function=False):
    return Dijkstra.dijkstra_wrapper(network, src, succ_direction, potential_function)


def johnson(network):
    return Johnson.johnson(network)


def dispatch(network):
    return Dispatch.fast_dispatch(network)


def slow_dispatch(network):
    return Dispatch.slow_dispatch(network)


def luke_dispatch(network):
    return Dispatch.luke_dispatch(network)


def dc_cairo_et_al_2018(network):
    return cairo_et_al_2018(network)


def tarjan(network):
    t = Tarjan(network)
    return t.tarjan()


def greedy_execute(network):
    potential_function = bellman_ford(network)
    return Dispatchability.greedy_execute(network, potential_function)
