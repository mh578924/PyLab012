from solar_system import SolarSystem


class Simulation:
    def __init__(self, solar_system: SolarSystem, width: int, height: int, num_periods: int):
        self._solar_system = solar_system
        self._width = width
        self._height = height
        self._num_periods = num_periods

    def run(self):
        self._solar_system.show_planets()
        for _ in range(self._num_periods):
            self._solar_system.move_planets()
            self._solar_system.show_planets()


def main():
    sol_sys = SolarSystem()
    sim = Simulation(sol_sys, 500, 500, 2000)
    from sun import Sun
    from planet import Planet
    sol_sys.add_sun(Sun("sol", 696340, 10e10, 273, 0, 0))
    sol_sys.add_planet(Planet('Earth', 6371, 5.972e24, 1.496e8, 0, 0, 29.78e3))
    sim.run()

if __name__ == '__main__':
    main()