import sympy as sp #pip3 install sympy



def max_value(plus_value_side, minus_value_side, true_coef):
    """ Подсчет размера ставки с максимальной прибылью
    """
    x = sp.Symbol('x')
    
    coef = 1 / ((x+plus_value_side) / (x+plus_value_side+minus_value_side))
    func = x * coef - x * float(true_coef)
    
    derivative = sp.diff(func)
    so = sp.solveset(derivative, x)
    max_value_vager = max(sp.solveset(derivative, x))
    
    return max_value_vager
 
 
def calc_value(vager, plus_value_side, minus_value_side, true_coef):
    """ Подсчет прибыли от ставки
    """
    diff = (vager * (1 / ((vager + plus_value_side) / 
            (vager + plus_value_side + minus_value_side))) - 
            vager * true_coef)
    return diff
