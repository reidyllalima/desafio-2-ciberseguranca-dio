# Simulações Seguras: Ransomware & Keylogger (Educational)

> Projeto pedagógico que **simula** comportamentos de malware sem causar dano. Uso exclusivo em ambiente controlado e legal.

## Conteúdo
- `create_test_files.py` — gera arquivos de teste.
- `simulate_ransom.py` — simulação não destrutiva de "encrypt" (marca/copias).
- `fake_keystrokes_generator.py` — cria um arquivo com keystrokes simulados.
- `simulate_keylogger.py` — processa o arquivo simulado em vez de capturar teclas reais.
- `defense.md` — medidas de prevenção e detecção.

## Requisitos
- Python 3.8+
- Executar somente em VMs isoladas com snapshot.

## Como usar (modo seguro)
1. Crie snapshot da VM.  
2. `python3 create_test_files.py` — gera pasta `test_files/` com arquivos de exemplo.  
3. `python3 simulate_ransom.py --target test_files/` — simula encriptação **não destrutiva**.  
4. `python3 fake_keystrokes_generator.py` — gera `fake_keystrokes.log`.  
5. `python3 simulate_keylogger.py --input fake_keystrokes.log` — processa o arquivo simulado.  

## Observações éticas e legais
Este repositório não deve ser usado para atividade maliciosa. Use apenas para aprendizado autorizado.
