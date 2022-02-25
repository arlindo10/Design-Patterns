from dispositivo_de_entretenimento import DispositivoDeEntretenimento


class Tv(DispositivoDeEntretenimento):
    def __init__(self, estado_do_dispositivo: int, configuracao_maxima: int):
        super().__init__()
        self.estado_do_dispositivo = estado_do_dispositivo
        self.configuracao_maxima = configuracao_maxima

    def botao_cinco_pressionado(self):
        print("Decreasing the channel")
        self.estado_do_dispositivo -= 1

    def botao_seis_pressionado(self):
        print("increasing the channel")
        self.estado_do_dispositivo += 1

    def botao_sete_pressionado(self):
        super(Tv, self).botao_sete_pressionado()

    def botao_oito_pressionado(self):
        super(Tv, self).botao_oito_pressionado()

    def feedback_do_dispositivo(self):
        super(Tv, self).feedback_do_dispositivo()