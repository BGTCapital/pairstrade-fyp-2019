## Yuri Updates

The authors added helpful instructions how to run the code [here](https://github.com/ScrapeWithYuri/pairstrade-fyp-2019/blob/master/model/README.md). I ran the [rl_train](https://github.com/ScrapeWithYuri/pairstrade-fyp-2019/blob/master/model/rl_train.py) code by using these parameters: **--job_name train_0_1_2_test_3 --run_mode "train" --train_indices 0 1 2 --test_indices 3**

I added datasets used by the authors [here](https://github.com/ScrapeWithYuri/pairstrade-fyp-2019/tree/master/model/dataset/nyse-daily-transformed-old). However, when I proccessed the [raw data](https://github.com/ScrapeWithYuri/pairstrade-fyp-2019/tree/master/model/dataset/nyse-daily-trimmed-same-length) into the transformed data via the [process_data.py script](https://github.com/ScrapeWithYuri/pairstrade-fyp-2019/blob/master/process_data/process_data.py), the [resulting log prices](https://github.com/ScrapeWithYuri/pairstrade-fyp-2019/tree/master/model/dataset/nyse-daily-transformed) were different than the data used by the authors. After training and testing the reinforcement code with my processed raw data, my results were marginally positive. I believe the authors' dataset may have had look ahead bias when they originally transformed the data. My results are [here](https://github.com/ScrapeWithYuri/pairstrade-fyp-2019/tree/master/model/logging/train_0_1_2_test_3/plots) (slightly positive but not large enough to warrant trading), while the results I was able to achieve using the authors' dataset is located [here](https://github.com/ScrapeWithYuri/pairstrade-fyp-2019/tree/master/model/logging/train_0_1_2_test_3/plots_old) (40%+ as mentioned in their paper).

I made one adjustment to the code, and believe another is warranted.

- The [incur_commission](https://github.com/ScrapeWithYuri/pairstrade-fyp-2019/blob/master/model/trading_env.py#L112) script added 10%+ cost over the course of a year. Since the strategy generally executed few trades, I expected this to be lower. Based on my knowledge, this should be 0.25% - 0.50%, so I divided the cost by 50.
- I believe the [compute reward](https://github.com/ScrapeWithYuri/pairstrade-fyp-2019/blob/master/model/trading_env.py#L175) should include the shorted value to `self.port_val_minus_com[i]` when the shorted value goes below zero by adding `spv_nex`. In a real-world environment, shorted values can go "below zero" (i.e. you owe money to cover the short). I did not make this change to the code though.

## pairstrade-fyp-2019
Final year project at HKUST. We tested 3 main approaches for performing Pairs Trading: 
- distance method
- cointegration method (rolling OLS, Kalman Filter)
- reinforcement learning agent (proposed)

Final report can be found [here](https://github.com/wywongbd/statistical-arbitrage-18-19/blob/master/reports/FYP_Final_Report_LZ2.pdf).
Presentation slides can be found [here](https://github.com/wywongbd/statistical-arbitrage-18-19/blob/master/reports/FYP_Final_Presentation.pdf).

FYP members: [myself](https://github.com/wywongbd), [Gordon](https://github.com/GordonCW), [Brendan](https://github.com/thambrendan)

### How to get started?
- Run `./setup.sh` to install all dependencies

### Note
- In our experiments, we used financial data taken from the Interactive Brokers platform, which is not free. Due to their regulations, we cannot release the financial data used in our experiments to the public. Feel free to use your own price data to perform experiments. 

### Disclaimer
- The strategies we implemented have not been proven to be profitable in a live trading account
- The reported returns are purely from backtesting procedures, and they may be susceptible to lookahead bias that we are not aware of
