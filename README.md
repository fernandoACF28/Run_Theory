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

# References

Amin Zargar, Rehan Sadiq, Bahman Naser, Faisal I. Khan, 2011. A review of drought indices. Environmental reviews 19, 333–349. https://doi.org/10.1139/a11-013

Adams, J., 2017. climate_indices, an open source Python library providing reference implementations of commonly used climate indices, URL: https://github.com/monocongo/climate_indices.

Liu, C, Yang, C, Yang, Q, 2021. Spatiotemporal drought analysis by the standardized precipitation index (SPI) and standardized precipitation evapotranspiration index (SPEI) in Sichuan Province, China | Scientific Reports [WWW Document]. URL https://www.nature.com/articles/s41598-020-80527-3 (accessed 9.2.22).

V. Yevjevich, 1969. An objective approach to definitions and investigations of continental hydrologic droughts. VUJICA YEVJEVICH: Fort Collins, Colorado State University, 1967, 19 p. (Hydrology paper no. 23). Journal of Hydrology 7, 353–353. https://doi.org/10.1016/0022-1694(69)90110-3

