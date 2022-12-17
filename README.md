# Network of token liquidity pools on UniSwap

The UniSwap liquidity pool network is a decentralized platform that enables users to trade Ethereum-based tokens without the need for a centralized exchange. By collecting the top 1000 token liquidity pools on UniSwap for a span of two years we construct a DeFi exchange network and analyze it. Our study answers four questions: (i) what are the main properties of the network and which tokens are more “important”, (ii) what is the structure of the network, (iii) is the network nested and how much, and (iv) how much disruption will the removal of “important” tokens cause to the DeFi ecosystem? Our results show that, the DeFi exchange network is a not nested scale-free network that breaks apart dramatically if the most central token, \emph{WETH}, goes out of the market. Overall, our analysis demonstrates that the UniSwap liquidity pool network is a complex and dynamic system that exhibits a range of network properties that contribute to its connectivity and low level of resilience.

## Authors
Georgia Lazaridou, Tanmay Chimurkar, Prakhar Bhandari, Kartikey Sharma

## Usage
[exploratory_data_analysis.ipynb](exploratory_data_analysis.ipynb): 
[centrality.py](centrality.py):
[properties.ipynb](properties.ipynb):
[nestedness.ipynb](nestedness.ipynb):


## Dependencies
The module has been written in *Python 3.8* and uses the following packages:
* [NumPy](http://www.numpy.org/)
* [NetworkX](https://networkx.org/)

## References
