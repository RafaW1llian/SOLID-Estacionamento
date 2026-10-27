"""
Aplicação SOLID: Sistema de estacionamento.

SOLID são 5 princípios para escrever código mais fácil de entender,
manter e estender:

    S - Responsabilidade Única   (Single Responsibility)
    O - Aberto/Fechado           (Open/Closed)
    L - Substituição de Liskov   (Liskov Substitution)
    I - Segregação de Interfaces (Interface Segregation)
    D - Inversão de Dependência  (Dependency Inversion)
"""

# S
class Ticket:
    """Guarda a placa e quantas horas o veiculo ficou no estacionamento"""
    def __init__ (self, placa, horas):
        """Cria um ticket com as informações"""
        self.placa = placa
        self.horas = horas

# O
# L
class TarifaCarro:
    """Carro: 5 reais"""
    def Calcular(self, horas):
        """Da o valor a cobrar pelas horas"""
        return max(0, horas) * 5.00

class TarifaMoto:
    """Moto: 3 reais"""
    def Calcular(self, horas):
        return max(0, horas) * 3.00

class TarifaPromocional:
    """Uma promoção em que as duas primeiras horas são gratis"""
    def calcular(self, horas):
        """desconta duas horas gratis e cobra o restante"""
        return max(0, horas - 2) * 5.00

# I
class ComprovanteImpresso:
    """comprovante em papel"""
    def emitir(self, placa, total):
        """emite o comprovante impresso (chamaria uma impressora real)"""
        print(f"[IMPRESSO] Placa {placa} - Total: {total}")
class ComprovanteWhatsapp:
    """Comprovante por Whatsapp"""
    def emitir(self, placa, total):
        """emite o comprovante por mensagem no whatsapp (chamaria uma API de mensagens)"""
        print(f"[WHATSAPP] Placa {placa} - Total: {total}")

# D
class Cancela:
    """Calcula o valor e emite o comprovante"""
    def __init__(self, emissor):
        """Recebe o emissor de comprovante de fora"""
        self.emissor = emissor
    def liberar(self, ticket, tarifa):
        """Calcula o valor da saida e emite o comprovante"""
        #Pede para a tarifa o valor total
        total = tarifa.calcular(ticket.horas)
        #Pede ao emissor para entregar o comprovante
        self.emissor.emitir(ticket.placa, total)

#================================================================

Cancela(ComprovanteImpresso()).liberar(Ticket("YUN-K237", 3), TarifaCarro())
Cancela(ComprovanteImpresso()).liberar(Ticket("RAF-A777", 2), TarifaMoto())
Cancela(ComprovanteImpresso()).liberar(Ticket("ABC-1234", 1), TarifaPromocional())