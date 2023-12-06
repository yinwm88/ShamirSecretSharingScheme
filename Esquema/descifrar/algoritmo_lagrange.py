def lagrange_finite_field(prime, puntos, x):
    ans = 0
    for i in range(len(puntos)):
        term = puntos[i][1]  # y_i

        for j in range(len(puntos)):
            if j != i:
                numerator = (x - puntos[j][0]) % prime
                denominator = (puntos[i][0] - puntos[j][0]) % prime

                if denominator == 0:
                    raise ValueError("Denominador es cero")

                inverse_denominator = pow(denominator, -1, prime)

                term = (term * numerator * inverse_denominator) % prime

        ans = (ans + term) % prime

    return ans  # debería ser k con x = 0

