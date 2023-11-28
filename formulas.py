class Formula:
    G: float = 6.6743 * 10**-11  # Gravitation constant
    Em: float = 6 * 10**24  # Earth mass (kg)
    R: float = 6400000  # Earth radius (m)

    def gravitylaw(self, m1, m2, r):
        "Newton's law of universal gravitation"
        F = (m1 * m2 * self.G) / r**2
        return F
