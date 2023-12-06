from .algoritmo_lagrange import lagrange_finite_field


primo = 208351617316091241234326746312124448251235562226470491514186331217050270460481


def get_k(evaluaciones):
    return lagrange_finite_field(primo, evaluaciones, 0)
