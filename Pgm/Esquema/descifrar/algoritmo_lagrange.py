def lagrange_finite_field(prime, puntos, x):
    ans = 0
    for i in range(len(puntos)):
        term = puntos[i][1]  # y_i

        for j in range(len(puntos)):
            if j != i:
                numerador = (x - puntos[j][0]) % prime
                denominador = (puntos[i][0] - puntos[j][0]) % prime
                
                if denominador == 0:
                    raise ValueError("Denominador es cero")

                inverso_denominador = pow(denominador, -1, prime)

                term = (term * numerador * inverso_denominador) % prime

        ans = (ans + term) % prime

    return ans  

