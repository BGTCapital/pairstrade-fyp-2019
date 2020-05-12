import sys

sys.path.append('./log_helper')
sys.path.append('./model')

from rl_train import run_rl_backtest

#df1, df2 = run_rl_backtest('HHS', 'LXFT', 3)
df1, df2 = run_rl_backtest('LEAF', 'XRX', 3)