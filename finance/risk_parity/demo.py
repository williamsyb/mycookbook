# 协方差矩阵和收益率向量
from scipy.optimize import minimize
import pandas as pd
import numpy as np

V = np.matrix('123 37.5 70 30; 37.5 122 72 13.5; 70 72 321 -32; 30 13.5 -32 52') / 100  # covariance
R = np.matrix('14; 12; 15; 7') / 100  # return


# 风险预算优化
def calculate_portfolio_var(w, V):
    # 计算组合风险的函数
    w = np.matrix(w)
    return (w * V * w.T)[0, 0]


def calculate_risk_contribution(w, V):
    # 计算单个资产对总体风险贡献度的函数
    w = np.matrix(w)
    sigma = np.sqrt(calculate_portfolio_var(w, V))
    # 边际风险贡献
    MRC = V * w.T
    # 风险贡献
    RC = np.multiply(MRC, w.T) / sigma
    return RC


# 风险平价投资组合是所有资产中每个资产的RC相等的投资组合。
# 计算风险平价组合的权重，本质上属于一个二次优化问题。
# 让投资组合资产RC的平方误差的总和为(优化问题的目标函数)：
def risk_budget_objective(x, pars):
    # 计算组合风险
    V = pars[0]  # 协方差矩阵
    x_t = pars[1]  # 组合中资产预期风险贡献度的目标向量
    sig_p = np.sqrt(calculate_portfolio_var(x, V))  # portfolio sigma
    risk_target = np.asmatrix(np.multiply(sig_p, x_t))
    asset_RC = calculate_risk_contribution(x, V)
    J = sum(np.square(asset_RC - risk_target.T))[0, 0]  # sum of squared error
    return J


# 约束一
def total_weight_constraint(x):
    return np.sum(x) - 1.0


# 约束二
def long_only_constraint(x):
    return x


def calcu_w(x):
    w0 = [0.2, 0.2, 0.2, 0.6]
    #     x_t = [0.25, 0.25, 0.25, 0.25] # 目标是让四个资产风险贡献度相等，即都为25%
    x_t = x
    cons = ({'type': 'eq', 'fun': total_weight_constraint},
            {'type': 'ineq', 'fun': long_only_constraint})
    res = minimize(risk_budget_objective, w0, args=[V, x_t], method='SLSQP', constraints=cons, options={'disp': True})
    print('res:\n', res)
    w_rb = np.asmatrix(res.x)
    return w_rb


def plot_rc(w):
    rc = calculate_risk_contribution(w, V)
    rc = rc.tolist()
    rc = [i[0] for i in rc]
    rc = pd.DataFrame(rc, columns=['rick contribution'], index=[1, 2, 3, 4])
    plt.plot(rc, chart_type='column', title='Contribution to risk')


if __name__ == '__main__':
    w_rb = calcu_w([0.25, 0.25, 0.25, 0.25])
    print('各资产权重：', w_rb)
    # plot_rc(w_rb)
