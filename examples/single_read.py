import mlx90614_human_body

mlx = mlx90614_human_body.MLX90614HumanBody()

print("Ambient temperature: %f" % mlx.ambient_temperature)
print("Object temperature: %f" % mlx.object_temperature)
print("Body temperature: %f" % mlx.body_temperature)