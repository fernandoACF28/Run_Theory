# Identificação de Seca (Run-Theory)
A seca é um fenômeno complexo e cumulativo que ameaça a disponibilidade hídrica local [(Amin Zargar et al., 2011)](https://cdnsciencepub.com/doi/10.1139/a11-013).
A seca pode ser pode ter impactos meteorológico, agrícolas e hidrológicos [(Liu, C et al., 2021)](https://www.nature.com/articles/s41598-020-80527-3).

## Run Theory
A Run Theory é utilizada para classificações de eventos, porém, pode trazer as características de fenômenos de seca [(V. Yevjevich, 1969)](https://api.mountainscholar.org/server/api/core/bitstreams/5f26da05-d712-49bc-acc0-397ec0f70fef/content), eventos e seca tem como características severidade, duração,
intensidade e intervalo entre eventos. Na figura (1) podemos identificar visualmente algumas destas características, a intensidade é a razão da severidade pela duração como pode ser visto na equação 1. 

$$intensity = \frac{severity}{duration} \ \ \ \ \ \ \ \  \  \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  (1)$$ 

Na figura (1), temos a duração, severidade e intervalo entre eventos.

<p align="center">
  <img src="./src/Run_theory.png" style="width: 80%; height: 80%" />
</p>

*Figure 1. Características dos eventos de seca por meio de uma função de um índice arbitrário*

## Drought characteristics
O SPI foi calculado através do método de função gamma [(James Adams, 2017)](https://github.com/monocongo/climate_indices), e depois foi obtido os valores de severidade, duração e intensidade por meio da Run-Theory figura (2).
<p align="center">
  <img src="./src/run_theory_spi.png" style="width: 80%; height: 80%" />
</p>

*Figure 2. Características dos eventos de seca obtidas do SPI*
