# IMPORT LIBRARIES
import pandas as pd
import networkx as nx

# BUILD GRAPH FUNCTION
def build_graph():
    df = pd.read_csv('top_1000_by_liquidity.csv')
    #G = nx.from_pandas_edgelist(df, source='token0.symbol', target='token1.symbol', edge_attr='reserveUSD', create_using=nx.Graph().to_undirected())
    edges = pd.DataFrame(
    {
        "source": df["token0.symbol"],
        "target": df["token1.symbol"],
        "weight": df["reserveUSD"],
    }
    )
    G = nx.from_pandas_edgelist(edges, edge_attr=True, create_using=nx.Graph().to_undirected())
    return G

# COMPUTE CENTRALITY MEASURES
def compute_centrality(G):
    """ Compute Centrality

    This function computes different centrality measures for the input graph. The following centrality measures are comptued:
        Degree centrality, betweenness centrality, closeness centrality, eigenvector centrality,

    :param G: the input graph
    :return: centrality measures of the graph
    """
    degree_centrality = nx.degree_centrality(G)
    between_centrality = nx.betweenness_centrality(G)
    close_centrality = nx.closeness_centrality(G)
    eigen_centrality = nx.eigenvector_centrality_numpy(G)

    max_degree_centrality = max(degree_centrality, key=degree_centrality.get)
    return degree_centrality, between_centrality, close_centrality, eigen_centrality, max_degree_centrality

def centrality_properties():
    """Centrality Properties

    This function creates a pandas DataFrame from the centrality measures computed in Compute Centrality function, and sorts them by the degree centrality

    :return: pandas DataFrame containing the centrality metrics of the input graph
    """

    G = build_graph()

    (
        degree_centrality,
        between_centrality,
        close_centrality,
        eigen_centrality,
        _,
    ) = compute_centrality(G)

    centrality_list = pd.DataFrame(
        {
            "deg_cent": degree_centrality,
            "betw_cent": between_centrality,
            "closeness_cent": close_centrality,
            "eigen_cent": eigen_centrality,
        }
    )

    sorted_centrality_list = centrality_list.sort_values(
        by=["deg_cent"], ascending=False
    )

    return sorted_centrality_list