import tkinter as tk
 
def desmarcar_checkbox():
    var_checkbox.set(0)  # Desmarca a checkbox
 
# Configuração da janela
janela = tk.Tk()
janela.title("Exemplo Checkbox")
 
# Variável associada ao checkbox
var_checkbox = tk.IntVar()
 
# Criando o checkbox
checkbox = tk.Checkbutton(janela, text="Opção", variable=var_checkbox)
checkbox.pack(pady=10)
 
# Botão para desmarcar
botao = tk.Button(janela, text="Desmarcar", command=desmarcar_checkbox)
botao.pack(pady=10)
 
janela.mainloop()
 