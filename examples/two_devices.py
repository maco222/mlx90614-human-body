import mlx90614_human_body

mlx1 = mlx90614_human_body.MLX90614HumanBody(0x5A)
mlx2 = mlx90614_human_body.MLX90614HumanBody(0x5B)

print("Ambient temperature 1: %f" % mlx1.ambient_temperature)
print("Object temperature 1: %f" % mlx1.object_temperature)
print("Body temperature 1: %f" % mlx1.body_temperature)

print("Ambient temperature 2: %f" % mlx2.ambient_temperature)
print("Object temperature 2: %f" % mlx2.object_temperature)
print("Body temperature 2: %f" % mlx2.body_temperature)
