dias_alugados = int(input("Quantos dias você alugou?"))
km_percorridos = float(input("Quantos Kms você percorreu?"))
total_pagar = ((dias_alugados * 60) + (km_percorridos * 0.15))
print("Você alugou o carro por {} dias , percorreu {} Kms e o total em pagamento será : R$ {:.2f}"
      .format(dias_alugados, km_percorridos, total_pagar))