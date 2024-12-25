def gerenciar_tarefas():
    arquivo="tarefas.txt"
    
    while True:
        with open(arquivo, 'r') as f:
            tarefas = f.readlines()

        print("Tarefas:")
        
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa.strip()}")

        try:
            tarefa_concluida = int(input("Digite o número da tarefa concluída (0 para sair): "))
            if tarefa_concluida == 0:
                break
            elif tarefa_concluida < 1 or tarefa_concluida > len(tarefas):
                print("Número de tarefa inválido.")
                continue

            tarefas[tarefa_concluida - 1] = f"V: {tarefas[tarefa_concluida - 1]}\n"

            with open(arquivo, 'w') as f:
                f.writelines(tarefas)
            print("Tarefa marcada como concluída!")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

gerenciar_tarefas()