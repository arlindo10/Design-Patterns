from abc import ABC, abstractmethod

class DispositivoDeEntretenimento(ABC):
    def __init__(self):
        self.estado_do_dispositivo = 0
        self.configuracao_maxima = 0
        self.volume = 0

    @abstractmethod
    def botao_cinco_pressionado(self):
        pass

    @abstractmethod
    def botao_seis_pressionado(self):
        pass

    @abstractmethod
    def botao_sete_pressionado(self):
        self.volume += 1
        print(f"Volume em {self.volume}")

    @abstractmethod
    def botao_oito_pressionado(self):
        self.volume -= 1
        print(f"Volume em {self.volume}")

    @abstractmethod
    def feedback_do_dispositivo(self):
        if self.estado_do_dispositivo > self.configuracao_maxima or self.estado_do_dispositivo < 0:
            self.estado_do_dispositivo = 0

        print(f"No canal {self.estado_do_dispositivo}")

class Tv(DispositivoDeEntretenimento):
    def __init__(self, estado_do_dispositivo: int, configuracao_maxima: int):
        super().__init__()
        self.estado_do_dispositivo = estado_do_dispositivo
        self.configuracao_maxima = configuracao_maxima

    def botao_cinco_pressionado(self):
        print("Diminuindo o canal")
        self.estado_do_dispositivo -= 1

    def botao_seis_pressionado(self):
        print("Aumentando o canal")
        self.estado_do_dispositivo += 1

    def botao_sete_pressionado(self):
        super(Tv, self).botao_sete_pressionado()

    def botao_oito_pressionado(self):
        super(Tv, self).botao_oito_pressionado()

    def feedback_do_dispositivo(self):
        super(Tv, self).feedback_do_dispositivo()

class BotaoRemoto(ABC):
    def __init__(self, dispositivo: DispositivoDeEntretenimento):
        self._dispositivo = dispositivo

    @abstractmethod
    def botao_cinco_pressionado(self):
        self._dispositivo.botao_cinco_pressionado()

    @abstractmethod
    def botao_seis_pressionado(self):
        self._dispositivo.botao_seis_pressionado()

    @abstractmethod
    def feedback_do_dispositivo(self):
        self._dispositivo.feedback_do_dispositivo()

    @abstractmethod
    def botao_nove_pressionado(self):
        pass

class TvRemotaMuda(BotaoRemoto):
    def botao_cinco_pressionado(self):
        super(TvRemotaMuda, self).botao_cinco_pressionado()

    def botao_seis_pressionado(self):
        super(TvRemotaMuda, self).botao_seis_pressionado()

    def feedback_do_dispositivo(self):
        super(TvRemotaMuda, self).feedback_do_dispositivo()

    def __init__(self, dispotivo: DispositivoDeEntretenimento):
        super().__init__(dispositivo=dispotivo)

    def botao_nove_pressionado(self):
        print(f"A tv foi mutada")

class TvRemotaPausa(BotaoRemoto):
    def botao_cinco_pressionado(self):
        super(TvRemotaPausa, self).botao_cinco_pressionado()

    def botao_seis_pressionado(self):
        super(TvRemotaPausa, self).botao_seis_pressionado()

    def feedback_do_dispositivo(self):
        super(TvRemotaPausa, self).feedback_do_dispositivo()

    def __init__(self, dispotivo: DispositivoDeEntretenimento):
        super().__init__(dispositivo=dispotivo)

    def botao_nove_pressionado(self):
        print(f"A tv foi pausada")

if __name__ == '__main__':
    botao_remoto_tv_1 = TvRemotaMuda(Tv(1, 200))
    botao_remoto_tv_2 = TvRemotaPausa(Tv(1, 200))

    print("TESTE DA TELEVISÃO MUTADA")
    botao_remoto_tv_1.botao_cinco_pressionado()
    botao_remoto_tv_1.botao_seis_pressionado()
    botao_remoto_tv_1.botao_nove_pressionado()

    print("\nTESTE DA TELEVISÃO PAUSADA")
    botao_remoto_tv_2.botao_cinco_pressionado()
    botao_remoto_tv_2.botao_seis_pressionado()
    botao_remoto_tv_2.botao_seis_pressionado()
    botao_remoto_tv_2.botao_seis_pressionado()
    botao_remoto_tv_2.botao_seis_pressionado()
    botao_remoto_tv_2.botao_nove_pressionado()
    botao_remoto_tv_2.feedback_do_dispositivo()
