import board
import adafruit_mlx90614

class MLX90614HumanBody:
    A_FACTOR = 0.001081
    B_FACTOR = -0.2318
    C_FACTOR = 12.454

    def __init__(self):
        self._i2c = board.I2C()
        self._mlx90614 = adafruit_mlx90614.MLX90614(self._i2c)

    @property
    def ambient_temperature(self):
        return self._mlx90614.ambient_temperature

    @property
    def object_temperature(self):
        return self._mlx90614.object_temperature

    '''
    Human body temperature estimation, https://www.robotshop.com/community/forum/t/medical-tricorder/13546
    US Patent: US6299347B1, https://patents.google.com/patent/US6299347
    '''
    @property
    def body_temperature(self):
        # temperatures in F
        atF = self.ambient_temperature * 1.8 + 32
        otF = self.object_temperature * 1.8 + 32

        # estimated core body temperature
        ctF = (self.A_FACTOR*otF*otF + self.B_FACTOR*otF + self.C_FACTOR) * (otF-atF) + otF

        # return temperature in Celsius
        return (ctF - 32) * 0.5556

        