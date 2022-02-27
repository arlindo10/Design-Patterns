# Object Pool Design Pattern

## Propósito

O **Object Pool** é um **padrão de design  criacional**  que usa um conjunto de [objetos](https://en.wikipedia.org/wiki/Object_(computer_science)) inicializados mantidos prontos para uso - um " [pool](https://en.wikipedia.org/wiki/Pool_(computer_science)) " - em vez de alocá-los e destruí-los sob demanda. Um cliente do pool solicitará um objeto do pool e executará operações no objeto retornado. Quando o cliente termina,  ele é devolvido ao pool para ser reutilizado. 

### Recomendação

Para mais informações sobre esse padrão, recomendo a leitura no site [sourcemaking](https://sourcemaking.com/design_patterns/object_pool)