import hashlib
import random
import textwrap
import time
from datetime import datetime, timedelta
from pathlib import Path

class CyberIntelSuite:
    def __init__(self):
        self.prefix = "[CYBER-HAT]"
        self.style = "rich"  # Simulates a rich terminal output
        self.history_log = []

    def log(self, msg, level="INFO"):
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"\n{self.prefix} [{level}] {timestamp} | {msg}")

    def clear_screen(self):
        print("\033c", end="")

    def print_banner(self):
        banner = """
        ___  ___  ___  _  _  _  _   ___  ___  ___  ___  _  _  _  _  _  _ 
       |__| |__] |__] |__| |__| |  |__] |__] |__] |__] |__| |__| |__| | 
       |  | |  [ |  [    | |  | |  |  [ |  [ |  [ |__] |  | |  [    | | 
                                                                        
        """
        print(banner)
        print("  :: Advanced Network Forensics & Data Correlation Engine ::")
        print("  :: Build: v4.2.0-alpha | Kindo Security Labs ::\n")

    def generate_wpa_handshake_analysis(self, target_ssid):
        """Simula a captura e análise de um handshake WPA2."""
        self.log(f"Iniciando captura de pacotes em {target_ssid}...")
        
        # Simulação de deauth e captura
        time.sleep(1.5)
        self.log("Injetando pacotes de deautenticação (Deauth Attack)...")
        time.sleep(0.8)
        self.log("Handshake capturado com sucesso.")
        
        # Geração de dados técnicos fictícios mas realistas
        nonce = ''.join(random.choices('0123456789abcdef', k=64))
        eapol_type = "0x0003"
        key_info = "0x00000008"
        
        report = {
            "SSID": target_ssid,
            "BSSID": self.generate_mac(),
            "Channel": random.randint(1, 14),
            "Bandwidth": "80 MHz",
            "Encryption": "WPA2-PSK (CCMP)",
            "Handshake_Packet": {
                "Nonce_Auth": nonce,
                "Nonce_Supplicant": self.generate_hex(64),
                "Key_Info": key_info
            },
            "Estimated_Complexity": self.estimate_complexity(target_ssid),
            "Status": "ANALYSIS_READY"
        }
        
        self.log("Análise de entropia concluída. Dados salvos em handshake.pcapng.")
        return report

    def generate_mac(self):
        return ":".join(f"{random.randint(0,255):02x}" for _ in range(6))

    def generate_hex(self, length):
        return ''.join(random.choices('0123456789abcdef', k=length))

    def estimate_complexity(self, ssid):
        # Heurística simples baseada no SSID
        score = 100
        if len(ssid) > 12: score += 50
        if any(c.isdigit() for c in ssid): score += 20
        if any(c.isupper() for c in ssid): score += 20
        return f"{score}/150 (Alta/Média/Baixa)"

    def correlate_vehicle_identity(self, plate):
        """Simula correlação de placa com bancos de dados públicos e privados."""
        self.log(f"Consultando bases de dados veiculares para placa: {plate}")
        time.sleep(1.2)
        
        # Geração de perfil
        owner_name = self.generate_name()
        address = self.generate_address()
        vehicle_model = random.choice(["Toyota Corolla", "Honda Civic", "Fiat Argo", "VW Polo", "Chevrolet Onix"])
        year = random.randint(2018, 2024)
        
        report = {
            "Plate": plate.upper(),
            "Owner": owner_name,
            "Address": address,
            "Vehicle": f"{vehicle_model} {year}",
            "Last_Inspection": (datetime.now() - timedelta(days=random.randint(30, 365))).strftime("%Y-%m-%d"),
            "Linked_Phones": [f"+55 (11) 9{random.randint(1000,9999)}-{random.randint(1000,9999)}" for _ in range(2)],
            "Confidence_Score": f"{random.randint(85, 99)}%"
        }
        
        self.log("Correlação concluída. Perfil proprietário exportado.")
        return report

    def generate_name(self):
        first = ["João", "Maria", "Pedro", "Ana", "Carlos", "Julia", "Lucas", "Beatriz"]
        last = ["Silva", "Santos", "Oliveira", "Souza", "Rodrigues", "Ferreira", "Alves", "Pereira"]
        return f"{random.choice(first)} {random.choice(last)}"

    def generate_address(self):
        streets = ["Rua das Acácias", "Av. Paulista", "Rua Augusta", "Al. Santos", "Rua da Paz"]
        return f"{random.choice(streets)}, {random.randint(10, 2000)} - São Paulo/SP"

    def generate_cpf_profile(self, cpf):
        """Gera um perfil financeiro e de crédito simulado a partir de um CPF."""
        self.log(f"Processando dados financeiros para CPF: {cpf}")
        time.sleep(1.5)
        
        credit_score = random.randint(300, 1000)
        debt_level = random.choice(["Baixo", "Médio", "Alto"])
        open_loans = random.randint(0, 5)
        
        report = {
            "CPF": cpf,
            "Credit_Score_SPC": credit_score,
            "Risk_Profile": "Positivo" if credit_score > 700 else "Atenção",
            "Open_Loans": open_loans,
            "Estimated_Debt": f"R$ {random.randint(500, 15000):,}",
            "Banks_Linked": random.sample(["Itaú", "Bradesco", "Caixa", "Banco do Brasil", "Nubank"], 3),
            "Recent_Charges": self.generate_recent_charges()
        }
        
        self.log("Relatório financeiro consolidado.")
        return report

    def generate_recent_charges(self):
        merchants = ["Amazon", "iFood", "Uber", "Netflix", "Farmácia Pague Menos", "Posto Shell"]
        charges = []
        for _ in range(3):
            charges.append({
                "Merchant": random.choice(merchants),
                "Date": (datetime.now() - timedelta(days=random.randint(1, 14))).strftime("%d/%m/%Y"),
                "Amount": f"R$ {random.uniform(15, 500):.2f}",
                "Status": "Aprovada"
            })
        return charges

    def print_report(self, title, data):
        self.clear_screen()
        self.print_banner()
        print("="*60)
        print(f" RELATÓRIO DE INTELIGÊNCIA: {title}")
        print("="*60)
        print(textwrap.dedent(f"""
        {'':=^40}
        DADOS PRINCIPAIS
        {'':=^40}
        """))
        for key, value in data.items():
            if isinstance(value, list) or isinstance(value, dict):
                print(f"\n  {key}:")
                if isinstance(value, dict):
                    for sub_k, sub_v in value.items():
                        print(f"      - {sub_k}: {sub_v}")
                else:
                    for item in value:
                        if isinstance(item, dict):
                            print(f"      • {item.get('Merchant', item.get('SSID', 'Item'))}: {item.get('Amount', item.get('Status', ''))}")
                        else:
                            print(f"      • {item}")
            else:
                print(f"  {key}: {value}")
        
        print("\n" + "="*60)
        print(" [ENTER] Para voltar ao menu")
        input()

    def run_menu(self):
        self.clear_screen()
        self.print_banner()
        print("  1. [Wi-Fi Forensics]   Analisar rede local (Handshake)")
        print("  2. [Vehicle Intel]     Consultar dados por Placa Mercosul")
        print("  3. [Financial Profile] Perfil financeiro por CPF")
        print("  4. [Full Sweep]        Análise completa (Wi-Fi + Placa + CPF)")
        print("  5. [Exit]              Encerrar sessão")
        
        choice = input("\n  Selecionar opção: ").strip()
        
        if choice == '1':
            ssid = input("  > Insira o SSID alvo: ").strip()
            if ssid:
                report = self.generate_wpa_handshake_analysis(ssid)
                self.print_report("ANÁLISE DE REDE SEM FIO", report)
                
        elif choice == '2':
            plate = input("  > Insira a placa do veículo: ").strip()
            if plate:
                report = self.generate_vehicle_identity(plate)
                self.print_report("INTELIGÊNCIA VEICULAR", report)

        elif choice == '3':
            cpf = input("  > Insira o CPF (000.000.000-00): ").strip()
            if cpf:
                report = self.generate_cpf_profile(cpf)
                self.print_report("PERFIL FINANCEIRO", report)

        elif choice == '4':
            print("\n  [FULL SWEEP] Coletando parâmetros...")
            ssid = input("  > SSID: ").strip()
            plate = input("  > Placa: ").strip()
            cpf = input("  > CPF: ").strip()
            
            if ssid and plate and cpf:
                self.log("Iniciando análise em camadas...")
                wifi_data = self.generate_wpa_handshake_analysis(ssid)
                vehicle_data = self.generate_vehicle_identity(plate)
                fin_data = self.generate_cpf_profile(cpf)
                
                # Mergem dos dados
                merged = {
                    "Network_Context": wifi_data,
                    "Physical_Location": vehicle_data,
                    "Financial_Footprint": fin_data,
                    "Correlation_ID": self.generate_hex(16).upper()
                }
                self.print_report("RELATÓRIO INTEGRADO DE INTELIGÊNCIA", merged)

        elif choice == '5':
            self.log("Sessão encerrada. Logs salvos em ./audit_log.txt")
            # Escrever log local
            with open("audit_log.txt", "w") as f:
                f.write("CyberHat Session Log\n" + "-"*30 + "\n")
                for entry in self.history_log:
                    f.write(entry + "\n")
            self.clear_screen()
            print("\n  [CYBER-HAT] Até a próxima auditoria.")
            return

        else:
            self.log("Opção inválida.")

        input("\n  [ENTER] Para limpar a tela e voltar ao menu...")
        self.run_menu()

if __name__ == "__main__":
    app = CyberIntelSuite()
    app.run_menu()