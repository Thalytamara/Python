import time
import threading

class Cronometro:
    def __init__(self):
        self.tempo_inicial = 0
        self.tempo_passado = 0
        self.rodando = False
        self.thread = None

    def iniciar(self):
        if not self.rodando:
            self.tempo_inicial = time.time() - self.tempo_passado
            self.rodando = True
            self.thread = threading.Thread(target=self._atualizar)
            self.thread.start()

    def pausar(self):
        if self.rodando:
            self.tempo_passado = time.time() - self.tempo_inicial
            self.rodando = False
            if self.thread is not None:
                self.thread.join()

    def reiniciar(self):
        self.tempo_inicial = 0
        self.tempo_passado = 0
        self.rodando = False

    def _atualizar(self):
        while self.rodando:
            tempo_corrente = time.time() - self.tempo_inicial
            self._mostrar_tempo(tempo_corrente)
            time.sleep(0.1)

    def _mostrar_tempo(self, tempo_corrente):
        horas, resto = divmod(tempo_corrente, 3600)
        minutos, segundos = divmod(resto, 60)
        print(f"\r{int(horas):02}:{int(minutos):02}:{int(segundos):02}", end='')

def main():
    cronometro = Cronometro()

    while True:
        print("\nCronômetro")
        print("1. Iniciar")
        print("2. Pausar")
        print("3. Reiniciar")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            cronometro.iniciar()
        elif escolha == '2':
            cronometro.pausar()
        elif escolha == '3':
            cronometro.reiniciar()
        elif escolha == '4':
            cronometro.pausar()
            break
        else:
            print("Escolha inválida!")

if __name__ == "__main__":
    main()
