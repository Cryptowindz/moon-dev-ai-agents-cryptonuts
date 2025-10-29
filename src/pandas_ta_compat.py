"""
pandas-ta compatibility layer for Python 3.10.9
This module provides a compatibility layer for pandas-ta using ta-lib and ta libraries
"""

import pandas as pd
import numpy as np
import talib
import ta

class PandasTACompat:
    """Compatibility layer for pandas-ta functions"""
    
    @staticmethod
    def rsi(data, length=14):
        """RSI indicator"""
        return talib.RSI(data.values, timeperiod=length)
    
    @staticmethod
    def sma(data, length=20):
        """Simple Moving Average"""
        return talib.SMA(data.values, timeperiod=length)
    
    @staticmethod
    def ema(data, length=20):
        """Exponential Moving Average"""
        return talib.EMA(data.values, timeperiod=length)
    
    @staticmethod
    def macd(data, fast=12, slow=26, signal=9):
        """MACD indicator"""
        macd_line, signal_line, histogram = talib.MACD(data.values, fastperiod=fast, slowperiod=slow, signalperiod=signal)
        return macd_line, signal_line, histogram
    
    @staticmethod
    def bbands(data, length=20, std=2):
        """Bollinger Bands"""
        upper, middle, lower = talib.BBANDS(data.values, timeperiod=length, nbdevup=std, nbdevdn=std)
        return upper, middle, lower
    
    @staticmethod
    def atr(high, low, close, length=14):
        """Average True Range"""
        return talib.ATR(high.values, low.values, close.values, timeperiod=length)
    
    @staticmethod
    def stoch(high, low, close, k_period=14, d_period=3):
        """Stochastic Oscillator"""
        slowk, slowd = talib.STOCH(high.values, low.values, close.values, 
                                  fastk_period=k_period, slowk_period=d_period, slowd_period=d_period)
        return slowk, slowd
    
    @staticmethod
    def adx(high, low, close, length=14):
        """Average Directional Index"""
        return talib.ADX(high.values, low.values, close.values, timeperiod=length)
    
    @staticmethod
    def obv(close, volume):
        """On Balance Volume"""
        return talib.OBV(close.values, volume.values)
    
    @staticmethod
    def willr(high, low, close, length=14):
        """Williams %R"""
        return talib.WILLR(high.values, low.values, close.values, timeperiod=length)
    
    @staticmethod
    def cci(high, low, close, length=20):
        """Commodity Channel Index"""
        return talib.CCI(high.values, low.values, close.values, timeperiod=length)
    
    @staticmethod
    def roc(data, length=10):
        """Rate of Change"""
        return talib.ROC(data.values, timeperiod=length)
    
    @staticmethod
    def mom(data, length=10):
        """Momentum"""
        return talib.MOM(data.values, timeperiod=length)

# Create a pandas-ta like module
class pandas_ta:
    """pandas-ta compatibility module"""
    
    @staticmethod
    def rsi(data, length=14):
        """RSI indicator"""
        return pd.Series(PandasTACompat.rsi(data, length), index=data.index)
    
    @staticmethod
    def sma(data, length=20):
        """Simple Moving Average"""
        return pd.Series(PandasTACompat.sma(data, length), index=data.index)
    
    @staticmethod
    def ema(data, length=20):
        """Exponential Moving Average"""
        return pd.Series(PandasTACompat.ema(data, length), index=data.index)
    
    @staticmethod
    def macd(data, fast=12, slow=26, signal=9):
        """MACD indicator"""
        macd_line, signal_line, histogram = PandasTACompat.macd(data, fast, slow, signal)
        return (pd.Series(macd_line, index=data.index),
                pd.Series(signal_line, index=data.index),
                pd.Series(histogram, index=data.index))
    
    @staticmethod
    def bbands(data, length=20, std=2):
        """Bollinger Bands"""
        upper, middle, lower = PandasTACompat.bbands(data, length, std)
        return (pd.Series(upper, index=data.index),
                pd.Series(middle, index=data.index),
                pd.Series(lower, index=data.index))
    
    @staticmethod
    def atr(high, low, close, length=14):
        """Average True Range"""
        return pd.Series(PandasTACompat.atr(high, low, close, length), index=high.index)
    
    @staticmethod
    def stoch(high, low, close, k_period=14, d_period=3):
        """Stochastic Oscillator"""
        slowk, slowd = PandasTACompat.stoch(high, low, close, k_period, d_period)
        return (pd.Series(slowk, index=high.index),
                pd.Series(slowd, index=high.index))
    
    @staticmethod
    def adx(high, low, close, length=14):
        """Average Directional Index"""
        return pd.Series(PandasTACompat.adx(high, low, close, length), index=high.index)
    
    @staticmethod
    def obv(close, volume):
        """On Balance Volume"""
        return pd.Series(PandasTACompat.obv(close, volume), index=close.index)
    
    @staticmethod
    def willr(high, low, close, length=14):
        """Williams %R"""
        return pd.Series(PandasTACompat.willr(high, low, close, length), index=high.index)
    
    @staticmethod
    def cci(high, low, close, length=20):
        """Commodity Channel Index"""
        return pd.Series(PandasTACompat.cci(high, low, close, length), index=high.index)
    
    @staticmethod
    def roc(data, length=10):
        """Rate of Change"""
        return pd.Series(PandasTACompat.roc(data, length), index=data.index)
    
    @staticmethod
    def mom(data, length=10):
        """Momentum"""
        return pd.Series(PandasTACompat.mom(data, length), index=data.index)

# Make it available as pandas_ta
import sys
sys.modules['pandas_ta'] = pandas_ta
