largura = float(input('Qual a largura de sua parede? '))
altura = float(input('Qual a altura da sua parede? '))
area = largura * altura
tinta = area / 2
print('Largura: {}m\nAltura: {}m'.format(largura, altura))
print('Sua parede tem a dimensão de {}x{}, e sua área é de {}m².'.format(largura, altura, area))
print('Você precisará de {}l de tinta.'.format(tinta))


