# Impact of central tokens in the structure and properties of a DeFi exchange network

The UniSwap liquidity pool network is a decentralized platform that enables users to trade Ethereum-based tokens without the need for a centralized exchange. By collecting the top 1000 token liquidity pools on UniSwap for a span of two years we construct a DeFi exchange network and analyze it. Our study answers four questions: (i) what are the main properties of the network and which tokens are more “important”, (ii) what is the structure of the network, (iii) is the network nested and how much, and (iv) how much disruption will the removal of “important” tokens cause to the DeFi ecosystem? Our results show that, the DeFi exchange network is a not nested scale-free network that breaks apart dramatically if the most central token, \emph{WETH}, goes out of the market. Overall, our analysis demonstrates that the UniSwap liquidity pool network is a complex and dynamic system that exhibits a range of network properties that contribute to its connectivity and low level of resilience.

## Authors
Georgia Lazaridou, Tanmay Chimurkar, Prakhar Bhandari, Kartikey Sharma

## Usage
* [exploratory_data_analysis.ipynb](exploratory_data_analysis.ipynb): Construction of the network and analysis of the components
* [centrality.py](centrality.py): Calculation of centrality measures
* [properties.ipynb](properties.ipynb): Calculation of other properties of the network
* [nestedness.ipynb](nestedness.ipynb): Calculation of the nestedness
* [robustness.ipynb](robustness.ipynb): Checking how robust the network is


## Dependencies
The code has been written in *Python 3.8* and uses the following packages:
* [NumPy](http://www.numpy.org/)
* [NetworkX](https://networkx.org/)
* [Pandas](https://pandas.pydata.org/)
* [cpnet](https://pypi.org/project/cpnet/)
* [powerlaw](https://pypi.org/project/powerlaw/)
* [matplotlib](https://matplotlib.org/)
* [datetime](https://docs.python.org/3/library/datetime.html)
* [seaborn](https://seaborn.pydata.org/)
* [random](https://docs.python.org/3/library/random.html)
* [heapq](https://docs.python.org/3/library/heapq.html)
* [tqdm](https://tqdm.github.io/)

It also uses the following implemented class:
* [NestednessCalculator](https://github.com/tsakim/nestedness/blob/master/nestedness_calculator.py)